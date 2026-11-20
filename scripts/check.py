#!/usr/bin/env python3
"""Deterministic checks of LTA_DataMall_API_User_Guide.md against the PDF.

The Markdown is rendered to HTML with markdown-it (CommonMark + GFM tables)
and compared with what PyMuPDF reads from the PDF. The PDF side is extracted
independently of scripts/convert.py, so a converter bug is not mirrored here.

Checks:
  text       every PDF word appears in the Markdown, and nothing extra
  lines      every PDF text line appears contiguously, in page order
  headings   every PDF bookmark is a heading of the right level, in order
  bold       bold PDF text is bold in the Markdown, and only that text
  italic     same for italic
  sup        superscripts are <sup>
  lists      bullet and numbered items are <li>, with the same nesting
  tables     each PDF table cell is one Markdown cell, rows stay rows,
             and tables continuing on the next page are joined
  images     every content image is extracted, referenced and intact
  links      every PDF hyperlink target is a Markdown link
  code       JSON samples are fenced code blocks and parse as JSON
  syntax     no unrendered Markdown markers or raw tags leak into text
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

import pymupdf
from markdown_it import MarkdownIt

WORD_RE = re.compile(r"\w+")
HEADER_RE = re.compile(r"LTA DataMall|API User Guide|^Version\s+\d", re.I)
BULLETS = {"•", "▪", "◦", "○", "", "", "§", "-", "–"}
ENUM_RE = re.compile(r"^(?:\d{1,2}|[a-z])\.$", re.I)
MIN_IMAGE_H = 25  # smaller images are inline icons; still checked


# --------------------------------------------------------------------------
# Character streams with formatting flags
# --------------------------------------------------------------------------


@dataclass
class Stream:
    chars: list[str] = field(default_factory=list)
    flags: list[frozenset] = field(default_factory=list)

    def add(self, text: str, flags: frozenset = frozenset()):
        for ch in text:
            self.chars.append(ch)
            self.flags.append(flags)

    def sep(self):
        if self.chars and self.chars[-1] != " ":
            self.add(" ")

    def tokens(self) -> list[tuple[str, frozenset]]:
        """Words with the flags shared by all of their characters."""
        text = "".join(self.chars)
        out = []
        for m in WORD_RE.finditer(text):
            fl = frozenset.intersection(*self.flags[m.start() : m.end()])
            out.append((m.group(0), fl))
        return out


def is_bullet(span: dict) -> bool:
    t = span["text"].strip()
    return t in BULLETS or (t == "o" and "courier" in span["font"].lower())


def words(s: str) -> list[str]:
    return WORD_RE.findall(s)


# --------------------------------------------------------------------------
# Markdown side
# --------------------------------------------------------------------------


@dataclass
class MdItem:
    depth: int
    words: list[str]


class HtmlModel(HTMLParser):
    BLOCK = {"p", "li", "td", "th", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
             "pre", "br", "ul", "ol", "table", "img", "blockquote"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.s = Stream()
        self.stack: list[tuple[str, dict]] = []
        self.headings: list[tuple[int, str]] = []
        self.items: list[MdItem] = []
        self.item_stack: list[int] = []
        self.item_start: list[int] = []
        self.ol_counters: list[int | None] = []
        self.images: list[str] = []
        self.links: list[str] = []
        self.codeblocks: list[str] = []
        self.tables: list[list[list[str]]] = []  # table -> row -> cell text
        self.cell_buf: list[str] | None = None
        self.heading_buf: list[str] | None = None
        self.code_buf: list[str] | None = None
        self.raw_text: list[str] = []
        self.anchors: set[str] = set()

    def flags(self) -> frozenset:
        tags = {t for t, _ in self.stack}
        f = set()
        if tags & {"strong", "b", "h1", "h2", "h3", "h4", "h5", "h6"}:
            f.add("bold")
        if tags & {"em", "i"}:
            f.add("italic")
        if "sup" in tags:
            f.add("sup")
        if "pre" in tags:
            f.add("code")
        if tags & {"td", "th"}:
            f.add("cell")
        return frozenset(f)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.BLOCK:
            self.s.sep()
            if self.cell_buf is not None:
                self.cell_buf.append(" ")
        if tag == "br":
            return
        if tag == "img":
            self.images.append(a.get("src", ""))
            return
        self.stack.append((tag, a))
        if tag == "a":
            self.links.append(a.get("href", ""))
        elif tag in ("ul", "ol"):
            self.ol_counters.append(int(a.get("start", 1)) if tag == "ol" else None)
        elif tag == "li":
            self.items.append(MdItem(len(self.ol_counters), []))
            self.item_stack.append(len(self.items) - 1)
            self.item_start.append(len(self.s.chars))
            n = self.ol_counters[-1] if self.ol_counters else None
            if n is not None:
                # The number is rendered by the list, so it has no formatting.
                self.s.add(f"{n}. ", frozenset({"marker"}))
                self.ol_counters[-1] = n + 1
        elif tag == "table":
            self.tables.append([])
        elif tag == "tr":
            self.tables[-1].append([])
        elif tag in ("td", "th"):
            self.cell_buf = []
        elif re.fullmatch(r"h[1-6]", tag):
            self.heading_buf = []
        elif tag == "pre":
            self.code_buf = []

    def handle_endtag(self, tag):
        if tag in ("br", "img"):
            return
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break
        if tag in self.BLOCK:
            self.s.sep()
            if self.cell_buf is not None:
                self.cell_buf.append(" ")
        if tag in ("ul", "ol") and self.ol_counters:
            self.ol_counters.pop()
        elif tag == "li" and self.item_stack:
            i = self.item_stack.pop()
            self.items[i].words = words("".join(self.s.chars[self.item_start.pop():]))
        elif tag in ("td", "th") and self.cell_buf is not None:
            self.tables[-1][-1].append("".join(self.cell_buf))
            self.cell_buf = None
        elif re.fullmatch(r"h[1-6]", tag) and self.heading_buf is not None:
            text = re.sub(r"\s+", " ", "".join(self.heading_buf)).strip()
            self.headings.append((int(tag[1]), text))
            self.anchors.add(github_slug(text))
            self.heading_buf = None
        elif tag == "pre" and self.code_buf is not None:
            self.codeblocks.append("".join(self.code_buf))
            self.code_buf = None

    def handle_data(self, data):
        self.raw_text.append(data)
        if "pre" not in {t for t, _ in self.stack}:
            data = re.sub(r"\s+", " ", data)
        self.text(data)

    def text(self, data):
        self.s.add(data, self.flags())
        if self.cell_buf is not None:
            self.cell_buf.append(data)
        if self.heading_buf is not None:
            self.heading_buf.append(data)
        if self.code_buf is not None:
            self.code_buf.append(data)


def github_slug(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


JSON_LINE = re.compile(r'^\s*"[^"]+"\s*:')


def render(md: str) -> str:
    return MarkdownIt("commonmark").enable("table").render(md)


# --------------------------------------------------------------------------
# PDF side
# --------------------------------------------------------------------------


@dataclass
class PdfLine:
    page: int
    text: str
    bbox: pymupdf.Rect
    spans: list[dict]


@dataclass
class PdfItem:
    page: int
    x: float
    y: float
    words: list[str]


class PdfModel:
    def __init__(self, path: str):
        self.doc = pymupdf.open(path)
        self.toc = self.doc.get_toc()
        counts = Counter()
        for page in self.doc:
            for x in {i["xref"] for i in page.get_image_info(xrefs=True)}:
                counts[x] += 1
        self.furniture = {x for x, n in counts.items() if n >= len(self.doc) / 2}
        self.lines: list[PdfLine] = []
        self.images: list[tuple[int, int, pymupdf.Rect]] = []
        self.uris: set[str] = set()
        self.goto_pages: list[int] = []
        self.cells: dict[int, list[pymupdf.Rect]] = {}
        for page in self.doc:
            self._page(page)

    def _page(self, page: pymupdf.Page):
        pno = page.number + 1
        h = page.rect.height
        screens = []
        for info in page.get_image_info(xrefs=True):
            if info["xref"] in self.furniture or not info["xref"]:
                continue
            r = pymupdf.Rect(info["bbox"]) & page.rect
            if r.is_empty:
                continue
            self.images.append((pno, info["xref"], r))
            if r.height >= MIN_IMAGE_H:
                screens.append(r)
        for link in page.get_links():
            if link.get("uri"):
                self.uris.add(link["uri"].strip())
            elif link.get("kind") == pymupdf.LINK_GOTO:
                self.goto_pages.append(link["page"] + 1)
        d = page.get_text("dict", flags=pymupdf.TEXT_PRESERVE_WHITESPACE)
        footer_y = max(
            (l["bbox"][1] for b in d["blocks"] for l in b.get("lines", [])
             if "".join(s["text"] for s in l["spans"]).strip().isdigit()),
            default=h,
        )
        self.cells[pno] = [
            pymupdf.Rect(c)
            for t in page.find_tables(strategy="lines_strict").tables
            for r in t.rows for c in r.cells if c
        ]
        for block in d["blocks"]:
            for line in block.get("lines", []):
                if line["dir"][0] < 0.9:
                    continue
                spans = [s for s in line["spans"] if s["text"].strip()]
                if not spans:
                    continue
                text = "".join(s["text"] for s in line["spans"])
                bbox = pymupdf.Rect(line["bbox"])
                if bbox.y1 < h * 0.16 and HEADER_RE.search(text):
                    continue
                if bbox.y0 > h * 0.85 and text.strip().isdigit() and bbox.y0 >= footer_y - 1:
                    continue
                c = pymupdf.Point((bbox.x0 + bbox.x1) / 2, (bbox.y0 + bbox.y1) / 2)
                if any(r.contains(c) for r in screens):
                    continue
                self.lines.append(PdfLine(pno, text, bbox, line["spans"]))

    def stream(self) -> Stream:
        """Words with their PDF formatting; JSON sample lines are tagged as code."""
        s = Stream()
        for l in self.lines:
            for sp in l.spans:
                t = sp["text"]
                if is_bullet(sp):
                    s.add(" ")
                    continue
                f = set()
                font = sp["font"].lower()
                if sp["flags"] & 16 or "bold" in font:
                    f.add("bold")
                if sp["flags"] & 2 or "italic" in font:
                    f.add("italic")
                if sp["flags"] & 1:
                    f.add("sup")
                if JSON_LINE.match(l.text) or l.text.strip() in ("{", "}", "[", "]", "},", "],"):
                    f.add("code")
                s.add(t, frozenset(f))
            s.sep()
        return s

    def list_items(self) -> list[PdfItem]:
        """Lines that start with a bullet glyph or an enumeration marker."""
        out = []
        by_page: dict[int, list[PdfLine]] = {}
        for l in self.lines:
            by_page.setdefault(l.page, []).append(l)
        for pno, lines in by_page.items():
            for l in lines:
                first = next(s for s in l.spans if s["text"].strip())
                marker = first["text"].strip()
                tok = marker.split(None, 1)[0]
                bullet = is_bullet(first) or tok in BULLETS
                if not (bullet or ENUM_RE.match(tok)):
                    continue
                mcell = self.cell_of(pno, pymupdf.Rect(first["bbox"]))
                rest = "".join(
                    s["text"] for s in l.spans
                    if s is first or self.cell_of(pno, pymupdf.Rect(s["bbox"])) == mcell
                ).strip()[len(tok):]
                if not words(rest):
                    # Marker on its own: the text is a separate line to the right.
                    right = [
                        m for m in lines
                        if m is not l and abs((m.bbox.y0 + m.bbox.y1) / 2 - (l.bbox.y0 + l.bbox.y1) / 2) < 3
                        and m.bbox.x0 >= l.bbox.x1 - 1 and m.bbox.x0 - l.bbox.x1 < 40
                    ]
                    if not right:
                        continue
                    nxt = min(right, key=lambda m: m.bbox.x0)
                    if self.cell_of(pno, l.bbox) != self.cell_of(pno, nxt.bbox):
                        continue  # e.g. "a." in a "#" column
                    rest = nxt.text
                elif tok in ("-", "–") and not first["text"].startswith(tok + " "):
                    continue
                if not words(rest):
                    continue
                if bullet:
                    w = words(rest)
                else:
                    w = words(tok) + words(rest)
                out.append(PdfItem(pno, l.bbox.x0, l.bbox.y0, w))
        return out

    def cell_of(self, pno: int, r: pymupdf.Rect):
        c = pymupdf.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
        return next((i for i, x in enumerate(self.cells.get(pno, [])) if x.contains(c)), None)

    def tables(self):
        out = []
        for page in self.doc:
            for t in page.find_tables(strategy="lines_strict").tables:
                rows = []
                for r in t.rows:
                    cells = []
                    for c in r.cells:
                        if not c:
                            continue
                        rect = pymupdf.Rect(c)
                        page_lines = sorted(
                            (l for l in self.lines if l.page == page.number + 1),
                            key=lambda l: (round(l.bbox.y0 / 3), l.bbox.x0),
                        )
                        parts = []
                        for l in page_lines:
                            texts = [
                                " " if is_bullet(sp) or not sp["text"].strip() else sp["text"]
                                for sp in l.spans
                                if not sp["text"].strip()
                                or rect.contains(pymupdf.Point((sp["bbox"][0] + sp["bbox"][2]) / 2,
                                                                (sp["bbox"][1] + sp["bbox"][3]) / 2))
                            ]
                            if "".join(texts).strip():
                                parts.append("".join(texts))
                        cells.append(words(" ".join(parts)))
                    rows.append(cells)
                out.append((page.number + 1, pymupdf.Rect(t.bbox), rows))
        return out


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


class Report:
    def __init__(self):
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str = ""):
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail else ""))
        if not ok:
            self.failed += 1


def contains_seq(hay: list[str], needle: list[str]) -> bool:
    return f" {' '.join(needle)} " in f" {' '.join(hay)} "


def fmt(c: Counter, n: int = 8) -> str:
    return ", ".join(f"{w}×{k}" for w, k in c.most_common(n))


def run(pdf_path: str, md_path: str) -> int:
    rep = Report()
    md = Path(md_path).read_text(encoding="utf-8")
    base = Path(md_path).parent
    html = render(md)
    m = HtmlModel()
    m.feed(html)
    p = PdfModel(pdf_path)

    md_tokens = m.s.tokens()
    pdf_tokens = p.stream().tokens()
    md_words = [w for w, _ in md_tokens]
    pdf_words = [w for w, _ in pdf_tokens]

    # text: same multiset of words
    missing = Counter(pdf_words) - Counter(md_words)
    extra = Counter(md_words) - Counter(pdf_words)
    rep.check("text: every PDF word is in the Markdown", not missing,
              f"{sum(missing.values())} missing: {fmt(missing)}")
    rep.check("text: no words that are not in the PDF (no duplicates)", not extra,
              f"{sum(extra.values())} extra: {fmt(extra)}")

    # lines: each PDF line appears contiguously; pages appear in order
    hay = " " + " ".join(md_words) + " "
    broken = []
    page_pos: dict[int, list[int]] = {}
    cursor = 0
    for l in p.lines:
        w = words(l.text.replace("•", " ").replace("▪", " "))
        if len(w) < 3:
            continue
        needle = " " + " ".join(w) + " "
        if l.page - 1 in page_pos:
            v = sorted(page_pos[l.page - 1])
            cursor = max(cursor, v[len(v) // 2] if v else 0)
        pos = hay.find(needle, cursor)
        if pos < 0:
            pos = hay.find(needle)
        if pos < 0:
            broken.append(f"p{l.page}: {l.text.strip()[:60]!r}")
        else:
            page_pos.setdefault(l.page, []).append(pos)
    rep.check("lines: every PDF line (3+ words) is contiguous in the Markdown",
              not broken, f"{len(broken)} broken: {broken[:5]}")
    medians = [(pg, sorted(v)[len(v) // 2]) for pg, v in sorted(page_pos.items())]
    order_bad = [f"p{a[0]}>p{b[0]}" for a, b in zip(medians, medians[1:]) if a[1] > b[1]]
    rep.check("lines: pages appear in order", not order_bad, ", ".join(order_bad[:5]))

    # headings
    expected = [(lvl + 1, re.sub(r"\s+", " ", t).strip()) for lvl, t, _ in p.toc]
    got = [h for h in m.headings if h[0] > 1]
    rep.check("headings: every bookmark is a heading of the right level, in order",
              got == expected,
              f"expected {len(expected)}, got {len(got)}; first difference: "
              + next((f"{e} vs {g}" for e, g in zip(expected, got) if e != g), "length"))

    # inline formatting
    md_markers = Counter(w for w, f in md_tokens if "marker" in f)
    for flag in ("bold", "italic", "sup"):
        pdf_f = Counter(w for w, f in pdf_tokens if flag in f and "code" not in f)
        md_f = Counter(w for w, f in md_tokens if flag in f and "code" not in f)
        lost = pdf_f - md_f
        lost_outside_code = lost - md_markers
        added = md_f - pdf_f
        rep.check(f"{flag}: PDF {flag} text is {flag} in the Markdown",
                  not lost_outside_code,
                  f"{sum(pdf_f.values())} {flag} words; lost: {fmt(lost_outside_code)}")
        rep.check(f"{flag}: no {flag} text that is not {flag} in the PDF", not added,
                  f"added: {fmt(added)}")
    def sup_runs(st: Stream) -> Counter:
        text = "".join(c if "sup" in f else "\0" for c, f in zip(st.chars, st.flags))
        return Counter(x.strip() for x in text.split("\0") if x.strip())

    pdf_sup, md_sup = sup_runs(p.stream()), sup_runs(m.s)
    rep.check("sup: superscript runs match the PDF", pdf_sup == md_sup,
              f"{sum(pdf_sup.values())} runs; missing {fmt(pdf_sup - md_sup)}; extra {fmt(md_sup - pdf_sup)}")
    # emphasis must also cover the same runs, not just the same words
    runs_bad = []
    md_flagged = {
        f: [w if (f in fl or "marker" in fl) else "\0" for w, fl in md_tokens]
        for f in ("bold", "italic")
    }
    code_words = [w for w, f in md_tokens if "code" in f]
    for flag in ("bold", "italic"):
        for line in p.lines:
            ls = Stream()
            for sp in line.spans:
                font = sp["font"].lower()
                on = (sp["flags"] & 16 or "bold" in font) if flag == "bold" else (sp["flags"] & 2 or "italic" in font)
                ls.add(" " if is_bullet(sp) else sp["text"], frozenset({flag}) if on else frozenset())
            cur: list[str] = []
            for w, fl in ls.tokens() + [("", frozenset())]:
                if flag in fl:
                    cur.append(w)
                    continue
                if len(cur) >= 2 and not contains_seq(md_flagged[flag], cur) and not contains_seq(code_words, cur):
                    runs_bad.append(f"{flag} p{line.page}: {' '.join(cur)[:50]!r}")
                cur = []
    rep.check("bold/italic: multi-word runs stay one run", not runs_bad,
              f"{len(runs_bad)}: {runs_bad[:5]}")

    # lists
    items = p.list_items()
    li_heads = [it.words for it in m.items]
    matched: list[int | None] = []
    j = 0
    unmatched = []
    for it in items:
        head = it.words[: min(6, len(it.words))]
        k = next((k for k in range(j, len(li_heads)) if li_heads[k][: len(head)] == head), None)
        if k is None:
            k = next((k for k in range(len(li_heads)) if li_heads[k][: len(head)] == head), None)
        if k is None:
            unmatched.append(f"p{it.page}: {' '.join(head)}")
        else:
            j = k + 1
        matched.append(k)
    rep.check("lists: every PDF bullet/numbered line is a list item",
              not unmatched, f"{len(items)} items; {len(unmatched)} not lists: {unmatched[:5]}")
    nest_bad = []
    for (a, ka), (b, kb) in zip(zip(items, matched), list(zip(items, matched))[1:]):
        if ka is None or kb is None or a.page != b.page or not (0 < b.y - a.y < 60):
            continue
        dx = b.x - a.x
        da = m.items[ka].depth
        db = m.items[kb].depth
        want = 0 if abs(dx) <= 4 else (1 if dx > 0 else -1)
        have = (db > da) - (db < da)
        if want != have:
            nest_bad.append(f"p{b.page}: {' '.join(b.words[:5])}")
    rep.check("lists: nesting follows marker indentation", not nest_bad,
              f"{len(nest_bad)}: {nest_bad[:5]}")

    # tables
    md_cells = [c for t in m.tables for r in t for c in r]
    md_cell_words = [words(c) for c in md_cells]
    md_cell_index = {}
    for ti, t in enumerate(m.tables):
        for ri, r in enumerate(t):
            for c in r:
                md_cell_index.setdefault(" ".join(words(c)), (ti, ri))
    pdf_tables = p.tables()
    cell_bad, row_bad, join_bad = [], [], []
    ncells = 0

    flat = [(ti, ri, words(c)) for ti, t in enumerate(m.tables) for ri, r in enumerate(t) for c in r]
    cur = [0]

    def locate(cw: list[str], move: bool = True):
        """First Markdown cell containing the words, searching from the last hit."""
        n = len(flat)
        order = list(range(cur[0], n)) + list(range(0, cur[0]))
        for match in (lambda c: c == cw, lambda c: contains_seq(c, cw)):
            for k in order:
                if match(flat[k][2]):
                    if move:
                        cur[0] = k
                    return flat[k][:2]
        return None

    for pno, bbox, rows in pdf_tables:
        for r in rows:
            nonempty = [c for c in r if c]
            if len(nonempty) == len(r) == 1 and len(rows) > 1:
                continue  # full-width banner row, rendered as a paragraph
            locs = []
            for c in nonempty:
                ncells += 1
                loc = locate(c)
                if loc is None:
                    if len(rows) > 1 or len(r) > 1:
                        cell_bad.append(f"p{pno}: {' '.join(c)[:50]}")
                else:
                    locs.append(loc)
            if len(set(locs)) > 1:
                row_bad.append(f"p{pno}: {' '.join(nonempty[0])[:40]}")
    rep.check("tables: every PDF table cell is a single Markdown cell", not cell_bad,
              f"{ncells} cells; {len(cell_bad)} bad: {cell_bad[:4]}")
    rep.check("tables: cells of a PDF row share a Markdown row", not row_bad,
              f"{len(row_bad)} split: {row_bad[:4]}")
    cur[0] = 0
    for (pa, ba, ra), (pb, bb, rb) in zip(pdf_tables, pdf_tables[1:]):
        if pb != pa + 1 or abs(ba.x0 - bb.x0) > 4 or abs(ba.x1 - bb.x1) > 4:
            continue
        # Only a table that ends a page and one that starts the next continue.
        if any(l.page == pa and l.bbox.y0 > ba.y1 for l in p.lines):
            continue
        if any(l.page == pb and l.bbox.y1 < bb.y0 for l in p.lines):
            continue
        last = next((c for r in reversed(ra) for c in r if c), None)
        first_row = next((r for r in rb if any(r)), None)
        if not last or not first_row:
            continue
        first = next(c for c in first_row if c)
        la = locate(last)
        lb = locate(first)
        is_header = all(
            w in [x for x, f in pdf_tokens if "bold" in f] for c in first_row for w in c
        )
        if la and lb and la[0] != lb[0] and not is_header and not (len(first_row) == 1):
            join_bad.append(f"p{pa}-p{pb}")
    rep.check("tables: tables continuing on the next page are joined", not join_bad,
              ", ".join(join_bad))

    # images
    p.images.sort(key=lambda t: (t[0], round(t[2].y0), t[2].x0))
    srcs = m.images
    missing_files = [s for s in srcs if not (base / s).is_file()]
    rep.check("images: every PDF content image is referenced", len(srcs) == len(p.images),
              f"PDF {len(p.images)}, Markdown {len(srcs)}")
    rep.check("images: referenced files exist", not missing_files, str(missing_files[:5]))
    dims_bad = []
    xref_src: dict[int, str] = {}
    for (pno, xref, r), src in zip(p.images, srcs):
        if xref in xref_src and xref_src[xref] != src:
            dims_bad.append(f"p{pno}: xref {xref} saved twice")
        xref_src[xref] = src
        if (base / src).is_file():
            try:
                pix = pymupdf.Pixmap(str(base / src))
            except Exception as e:  # noqa: BLE001
                dims_bad.append(f"{src}: {e}")
                continue
            info = p.doc.extract_image(xref)
            if (pix.width, pix.height) != (info["width"], info["height"]):
                dims_bad.append(f"{src}: {pix.width}x{pix.height} != {info['width']}x{info['height']}")
    rep.check("images: files decode and match the PDF image size", not dims_bad, str(dims_bad[:5]))
    img_dir = base / "images"
    on_disk = {f"images/{f.name}" for f in img_dir.iterdir()} if img_dir.is_dir() else set()
    orphans = on_disk - set(srcs)
    rep.check("images: no unreferenced files in images/", not orphans, str(sorted(orphans)[:5]))

    # links
    hrefs = set(m.links)
    lost_uris = sorted(u for u in p.uris if u not in hrefs)
    rep.check("links: every PDF hyperlink is a Markdown link", not lost_uris, str(lost_uris[:5]))
    bad_anchors = sorted(h for h in hrefs if h.startswith("#") and h[1:] not in m.anchors)
    rep.check("links: internal links point to headings", not bad_anchors, str(bad_anchors[:5]))

    # code
    json_lines = [l for l in p.lines if JSON_LINE.match(l.text)]
    code_text = "\n".join(m.codeblocks)
    lost_json = [l.text.strip() for l in json_lines if l.text.strip() not in code_text]
    rep.check("code: JSON sample lines are inside code blocks", not lost_json,
              f"{len(json_lines)} lines; {len(lost_json)} outside: {lost_json[:3]}")
    bad_json = []
    for block in m.codeblocks:
        if block.lstrip()[:1] in "{[":
            try:
                json.loads(block)
            except json.JSONDecodeError as e:
                bad_json.append(f"{block.strip()[:40]!r}: {e.msg} line {e.lineno}")
    rep.check("code: JSON code blocks parse", not bad_json, f"{len(bad_json)}: {bad_json[:3]}")

    # syntax: Markdown that failed to render
    text = "".join(m.raw_text)
    leaks = sorted(set(re.findall(r"\*\*|__|\]\(|\\\||</?(?:br|strong|em|sup|ul|ol|li|a|img|code)\b", text)))
    rep.check("syntax: no unrendered Markdown or HTML in the text", not leaks, str(leaks))
    if "\n|" in md:
        bad_rows = [l for l in md.splitlines() if l.startswith("|") and not l.rstrip().endswith("|")]
        rep.check("syntax: table rows are closed", not bad_rows, str(bad_rows[:2]))

    print(f"\n{rep.failed} check(s) failed" if rep.failed else "\nAll checks passed")
    return 1 if rep.failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--md", default="LTA_DataMall_API_User_Guide.md")
    args = ap.parse_args()
    return run(args.pdf, args.md)


if __name__ == "__main__":
    sys.exit(main())
