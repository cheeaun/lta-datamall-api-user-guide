#!/usr/bin/env python3
"""Fetch the LTA DataMall API User Guide PDF and convert it to Markdown.

The converter reads PDF primitives directly with PyMuPDF: text spans (for
bold, italic, superscript and links), bordered table geometry (for merged
cells and tables that continue across pages), bullet glyphs and indentation
(for nested lists), and embedded images.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf

PDF_URL = (
    "https://datamall.lta.gov.sg/content/dam/datamall/datasets/"
    "LTA_DataMall_API_User_Guide.pdf"
)
OUT_PATH = "LTA_DataMall_API_User_Guide.md"
IMAGE_DIR = "images"

BULLET_GLYPHS = {"•", "▪", "◦", "○", "", "", "§", "-", "–", "o"}
ENUM_RE = re.compile(r"^(?:\d{1,2}|[a-z]|[ivx]{1,4})\.$", re.I)
HEADER_RE = re.compile(r"LTA DataMall|API User Guide|^Version\s+\d", re.I)
JSON_LINE_RE = re.compile(r'^\s*(?:[{}\[\]],?\s*$|[{\[]\s*$|"[^"]*"\s*:)')
URL_RE = re.compile(r"https?://[^\s<>()]+[^\s<>().,;:]")
INLINE_IMAGE_MAX_H = 25
TABLE_X_TOL = 6.0


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------


@dataclass
class Run:
    text: str
    bold: bool = False
    italic: bool = False
    sup: bool = False
    link: str | None = None
    image: str | None = None  # path of an inline image
    hard_break: bool = False


@dataclass
class Line:
    runs: list[Run]
    x0: float
    y0: float
    x1: float
    y1: float
    size: float
    first_word_w: float = 0.0
    boxes: list | None = None  # span bboxes, parallel to runs

    @property
    def text(self) -> str:
        return "".join(r.text for r in self.runs)

    @property
    def h(self) -> float:
        return self.y1 - self.y0


@dataclass
class Heading:
    level: int
    text: str


@dataclass
class Para:
    runs: list[Run]


@dataclass
class Code:
    lines: list[str]


@dataclass
class Image:
    path: str
    alt: str


@dataclass
class ListItem:
    ordered: bool
    marker: str
    runs: list[Run]
    children: list["ListItem"] = field(default_factory=list)


@dataclass
class ListBlock:
    items: list[ListItem]
    # x positions of the markers of the top-level items, used to join lists
    # that continue on the next page.
    x0: float = 0.0


@dataclass
class Cell:
    r0: int
    r1: int
    x0: float
    x1: float
    md: str
    plain: str
    all_bold: bool


@dataclass
class Table:
    cells: list[Cell]
    nrows: int
    x0: float
    x1: float


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------


def fetch_pdf(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Response from {url} is not a PDF")
    return data


# --------------------------------------------------------------------------
# Inline rendering
# --------------------------------------------------------------------------


def escape_text(s: str) -> str:
    out = []
    pos = 0
    for m in URL_RE.finditer(s):
        out.append(_escape_plain(s[pos : m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_escape_plain(s[pos:]))
    return "".join(out)


def _escape_plain(s: str) -> str:
    s = s.replace("\\", "\\\\")
    for ch in "*_`|$~[]":
        s = s.replace(ch, "\\" + ch)
    return s.replace("<", "&lt;").replace(">", "&gt;")


def _style(r: Run) -> tuple:
    return (r.bold, r.italic, r.sup, r.link)


def normalize_runs(runs: list[Run]) -> list[Run]:
    """Collapse whitespace and merge neighbouring runs with the same style."""
    out: list[Run] = []
    for r in runs:
        if r.image or r.hard_break:
            out.append(r)
            continue
        text = re.sub(r"\s+", " ", r.text.replace("\u00a0", " "))
        if not text:
            continue
        if out and out[-1].text.endswith(" ") and text.startswith(" "):
            text = text[1:]
            if not text:
                continue
        if not text.strip():
            # Whitespace takes the style of its left neighbour.
            if out and not out[-1].image and not out[-1].hard_break:
                out[-1] = Run(out[-1].text + text, *_style(out[-1]))
            else:
                out.append(Run(text))
            continue
        out.append(Run(text, r.bold, r.italic, r.sup, r.link))
    merged: list[Run] = []
    for r in out:
        p = merged[-1] if merged else None
        if (
            p
            and not (p.image or p.hard_break or r.image or r.hard_break)
            and _style(p) == _style(r)
        ):
            merged[-1] = Run(p.text + r.text, *_style(r))
        else:
            merged.append(r)
    # Trailing whitespace inside styled runs moves outside the markers.
    while merged and not merged[0].image and not merged[0].text.strip() and not merged[0].hard_break:
        merged.pop(0)
    while merged and not merged[-1].image and not merged[-1].text.strip() and not merged[-1].hard_break:
        merged.pop()
    if merged and not merged[0].image and not merged[0].hard_break:
        merged[0] = Run(merged[0].text.lstrip(), *_style(merged[0]))
    if merged and not merged[-1].image and not merged[-1].hard_break:
        merged[-1] = Run(merged[-1].text.rstrip(), *_style(merged[-1]))
    return merged


def render_runs(runs: list[Run], hard_break: str) -> str:
    runs = normalize_runs(runs)
    parts: list[str] = []
    for i, r in enumerate(runs):
        if r.hard_break:
            parts.append(hard_break)
            continue
        if r.image:
            parts.append(f"![]({r.image})")
            continue
        lead = r.text[: len(r.text) - len(r.text.lstrip())]
        trail = r.text[len(r.text.rstrip()) :]
        core = r.text.strip()
        if not core:
            parts.append(r.text)
            continue
        if r.link and r.link == core:
            inner = f"<{core}>"
        else:
            inner = escape_text(core) if not r.link else _escape_plain(core)
        if r.sup:
            inner = f"<sup>{inner}</sup>"
        prev_ch = runs[i - 1].text[-1:] if i and not runs[i - 1].image else " "
        next_ch = runs[i + 1].text[:1] if i + 1 < len(runs) and not runs[i + 1].image else " "
        if lead:
            prev_ch = " "
        if trail:
            next_ch = " "
        # CommonMark delimiter runs fail next to letters when the emphasised
        # text starts or ends with punctuation; use HTML tags there.
        risky = (prev_ch.isalnum() and not core[0].isalnum()) or (
            next_ch.isalnum() and not core[-1].isalnum()
        )
        if r.italic and not r.sup:
            inner = f"<em>{inner}</em>" if risky else f"*{inner}*"
        if r.bold and not r.sup:
            inner = f"<strong>{inner}</strong>" if risky else f"**{inner}**"
        if r.link and r.link != core:
            inner = f"[{inner}]({r.link})"
        parts.append(lead + inner + trail)
    return "".join(parts)


def runs_all_bold(runs: list[Run]) -> bool:
    texty = [r for r in runs if r.text.strip() and not r.image]
    return bool(texty) and all(r.bold for r in texty)


# --------------------------------------------------------------------------
# Page analysis
# --------------------------------------------------------------------------


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().upper()


class Converter:
    def __init__(self, doc: pymupdf.Document, image_dir: Path | None):
        self.doc = doc
        self.image_dir = image_dir
        self.toc = doc.get_toc()
        self.toc_by_page: dict[int, list[tuple[int, str]]] = {}
        for level, title, page in self.toc:
            self.toc_by_page.setdefault(page, []).append((level, title))
        self.used_headings: set[tuple[int, str]] = set()
        self.saved_images: dict[int, str] = {}
        self.page_anchor: dict[int, str] = {}
        for level, title, page in self.toc:
            self.page_anchor.setdefault(page, slug(title))
        xref_pages = Counter()
        for page in doc:
            for x in {info["xref"] for info in page.get_image_info(xrefs=True)}:
                xref_pages[x] += 1
        # Images on most pages are the running-header logo.
        self.furniture_xrefs = {x for x, n in xref_pages.items() if n >= len(doc) / 2}

    # ---- images ---------------------------------------------------------

    def save_image(self, xref: int, pno: int) -> str:
        if xref in self.saved_images:
            return self.saved_images[xref]
        info = self.doc.extract_image(xref)
        ext = info["ext"]
        data = info["image"]
        if info.get("smask") or ext not in ("png", "jpeg", "jpg", "gif"):
            pix = pymupdf.Pixmap(self.doc, xref)
            if info.get("smask") and not pix.alpha:
                pix = pymupdf.Pixmap(pix, pymupdf.Pixmap(self.doc, info["smask"]))
            if pix.colorspace and pix.colorspace.n > 3:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            data, ext = pix.tobytes("png"), "png"
        n = sum(1 for p in self.saved_images.values() if f"page-{pno:03d}-" in p) + 1
        rel = f"{IMAGE_DIR}/page-{pno:03d}-{n}.{'jpg' if ext == 'jpeg' else ext}"
        if self.image_dir is not None:
            (self.image_dir.parent / rel).write_bytes(data)
        self.saved_images[xref] = rel
        return rel

    # ---- page regions ---------------------------------------------------

    def body_region(self, page: pymupdf.Page, text_lines: list) -> tuple[float, float]:
        h = page.rect.height
        w = page.rect.width
        rules = [
            d["rect"]
            for d in page.get_drawings()
            if d["rect"].width > w * 0.5 and d["rect"].height < 3
        ]
        top = max(
            (y1 for x0, y0, x1, y1, t in text_lines if y1 < h * 0.16 and HEADER_RE.search(t)),
            default=0.0,
        )
        top = max([top] + [r.y1 for r in rules if top <= r.y1 <= top + 15])
        # The footer is the page number, optionally under a full-width rule.
        numbers = [
            y0 for x0, y0, x1, y1, t in text_lines if y0 > h * 0.85 and t.strip().isdigit()
        ]
        bottom = max(numbers, default=h * 0.9) - 1
        bottom = min([bottom] + [r.y0 for r in rules if bottom - 15 <= r.y0 <= bottom])
        for info in page.get_image_info(xrefs=True):
            if info["xref"] in self.furniture_xrefs:
                top = max(top, info["bbox"][3])
        return top, bottom

    # ---- lines ----------------------------------------------------------

    def page_lines(self, page: pymupdf.Page) -> list[Line]:
        links = [l for l in page.get_links() if l.get("uri") or l.get("kind") == pymupdf.LINK_GOTO]
        raw = []
        d = page.get_text("dict", flags=pymupdf.TEXT_PRESERVE_WHITESPACE)
        for block in d["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                if line["dir"][0] < 0.9:  # rotated text
                    continue
                spans = [s for s in line["spans"] if s["text"]]
                if not spans or not "".join(s["text"] for s in spans).strip():
                    continue
                raw.append(spans)
        lines = []
        for spans in raw:
            runs = []
            for s in spans:
                font = s["font"].lower()
                bold = bool(s["flags"] & 16) or "bold" in font or "black" in font
                italic = bool(s["flags"] & 2) or "italic" in font or "oblique" in font
                sup = bool(s["flags"] & 1)
                runs.append(
                    Run(s["text"], bold, italic, sup, self.link_for(pymupdf.Rect(s["bbox"]), links))
                )
            x0 = min(s["bbox"][0] for s in spans)
            y0 = min(s["bbox"][1] for s in spans if s["text"].strip())
            y1 = max(s["bbox"][3] for s in spans if s["text"].strip())
            x1 = max(s["bbox"][2] for s in spans)
            sizes = Counter()
            for s in spans:
                sizes[round(s["size"], 1)] += len(s["text"].strip())
            line = Line(runs, x0, y0, x1, y1, sizes.most_common(1)[0][0],
                        boxes=[pymupdf.Rect(s["bbox"]) for s in spans])
            lines.append((line, spans))
        out = []
        for line, spans in lines:
            # Width of the first word, for detecting soft line wraps.
            for s in spans:
                t = s["text"]
                if t.strip():
                    word = t.lstrip().split(" ")[0]
                    w = s["bbox"][2] - s["bbox"][0]
                    line.first_word_w = w * len(word) / max(len(t), 1)
                    break
            out.append(line)
        return out

    def link_for(self, rect: pymupdf.Rect, links: list) -> str | None:
        area = rect.get_area()
        if not area:
            return None
        for l in links:
            inter = rect & l["from"]
            if inter.is_empty or inter.get_area() < 0.5 * area:
                continue
            if l.get("uri"):
                return l["uri"].strip()
            target = l.get("page")
            if target is not None and (target + 1) in self.page_anchor:
                return "#" + self.page_anchor[target + 1]
        return None

    # ---- tables ---------------------------------------------------------

    def page_tables(self, page: pymupdf.Page, top: float, bottom: float):
        tables = []
        for t in page.find_tables(strategy="lines_strict").tables:
            bbox = pymupdf.Rect(t.bbox)
            if bbox.y1 < top or bbox.y0 > bottom:
                continue
            cells = [pymupdf.Rect(c) for row in t.rows for c in row.cells if c]
            cells = [c & pymupdf.Rect(bbox.x0, top, bbox.x1, bottom) for c in cells]
            cells = [c for c in cells if c.height > 1 and c.width > 1]
            if cells:
                tables.append((bbox, cells))
        return tables

    # ---- block building ---------------------------------------------------

    def merge_baselines(self, lines: list[Line]) -> list[Line]:
        """Join fragments that sit on the same visual line (e.g. a bullet glyph
        and its text), ordered left to right."""
        groups: list[list[Line]] = []
        for l in sorted(lines, key=lambda l: ((l.y0 + l.y1) / 2, l.x0)):
            yc = (l.y0 + l.y1) / 2
            for g in groups[-3:]:
                gy = sum((m.y0 + m.y1) / 2 for m in g) / len(g)
                tol = 0.4 * min(l.h, min(m.h for m in g))
                if abs(yc - gy) <= max(tol, 1.5) and all(
                    l.x0 >= m.x1 - 2 or l.x1 <= m.x0 + 2 for m in g
                ):
                    g.append(l)
                    break
            else:
                groups.append([l])
        out: list[Line] = []
        for g in groups:
            g.sort(key=lambda m: m.x0)
            runs: list[Run] = []
            for k, m in enumerate(g):
                if k and m.x0 - g[k - 1].x1 > 1 and not g[k - 1].text.endswith(" "):
                    runs.append(Run(" "))
                runs += m.runs
            out.append(
                Line(
                    runs,
                    g[0].x0,
                    min(m.y0 for m in g),
                    max(m.x1 for m in g),
                    max(m.y1 for m in g),
                    max(g, key=lambda m: len(m.text.strip())).size,
                    g[0].first_word_w,
                )
            )
        out.sort(key=lambda l: (l.y0, l.x0))
        return out

    def classify(self, line: Line, pno: int, cell: bool):
        text = line.text.strip()
        if not cell:
            for level, title in self.toc_by_page.get(pno, []):
                key = (pno, title)
                if key not in self.used_headings and norm(text) == norm(title):
                    self.used_headings.add(key)
                    return ("heading", level, re.sub(r"\s+", " ", title).strip())
        if JSON_LINE_RE.match(line.text) and not cell:
            return ("code",)
        first = None
        for i, r in enumerate(line.runs):
            if r.text.strip():
                first = i
                break
        if first is not None:
            tok = line.runs[first].text.strip()
            parts = tok.split(None, 1)
            marker = parts[0] if parts else ""
            is_bullet = marker in BULLET_GLYPHS
            is_enum = bool(ENUM_RE.match(marker))
            rest_runs = list(line.runs[first + 1 :])
            if len(parts) > 1:
                r0 = line.runs[first]
                rest_runs.insert(0, Run(parts[1], *_style(r0)))
            has_rest = "".join(r.text for r in rest_runs).strip()
            if (is_bullet or is_enum) and has_rest:
                if is_bullet and marker in "-–o" and len(parts) == 1 and not rest_runs[0].text.startswith((" ", "\t")):
                    pass  # e.g. "o" or "-" glued to a word
                else:
                    return ("item", not is_bullet, marker, rest_runs)
        return ("text",)

    def join_wrapped_headings(self, lines: list[Line], pno: int) -> list[Line]:
        titles = [norm(t) for _, t in self.toc_by_page.get(pno, [])]
        out: list[Line] = []
        for l in lines:
            p = out[-1] if out else None
            if p and l.y0 - p.y1 < p.h:
                joined = norm(p.text + " " + l.text)
                if norm(p.text) not in titles and any(t.startswith(joined) for t in titles):
                    p.runs = p.runs + [Run(" ")] + l.runs
                    p.x1, p.y1 = max(p.x1, l.x1), l.y1
                    continue
            out.append(l)
        return out

    def build_blocks(self, lines: list[Line], pno: int, right: float, cell: bool = False):
        lines = self.merge_baselines(lines)
        if not cell:
            lines = self.join_wrapped_headings(lines, pno)
        blocks: list = []
        i = 0
        cls = [self.classify(l, pno, cell) for l in lines]

        def wraps(prev: Line, nxt: Line) -> bool:
            return prev.x1 + nxt.first_word_w + 0.3 * prev.size > right - 2

        def close(prev: Line, nxt: Line, factor: float) -> bool:
            return nxt.y0 - prev.y1 < factor * max(prev.h, nxt.h) and abs(prev.size - nxt.size) < 1.6

        for k in range(1, len(lines)):
            # "(S/N" + "21) is 1." style wraps are not list items.
            if cls[k][0] == "item" and cls[k][1] and cls[k - 1][0] == "text" \
                    and close(lines[k - 1], lines[k], 0.6) and wraps(lines[k - 1], lines[k]) \
                    and lines[k].x0 < lines[k - 1].x0 + 30:
                cls[k] = ("text",)

        while i < len(lines):
            l, c = lines[i], cls[i]
            if c[0] == "heading":
                blocks.append(Heading(c[1], c[2]))
                i += 1
            elif c[0] == "code":
                code = [l.text.rstrip()]
                i += 1
                while i < len(lines) and (
                    cls[i][0] == "code" or lines[i].text.strip() in ("...", "…")
                ) and close(lines[i - 1], lines[i], 2.0):
                    code.append(lines[i].text.rstrip())
                    i += 1
                blocks.append(Code(code))
            elif c[0] == "item":
                stack: list[tuple[float, float, ListItem]] = []  # (marker x, text x, item)
                top_items: list[ListItem] = []
                while i < len(lines):
                    l, c = lines[i], cls[i]
                    if c[0] == "item":
                        if stack and not close(lines[i - 1], l, 1.6):
                            break
                        item = ListItem(c[1], c[2], list(c[3]))
                        text_x = next(
                            (r for r in c[3] if r.text.strip()), None
                        )
                        tx = l.x0 + 12
                        while stack and l.x0 < stack[-1][0] - 4:
                            stack.pop()
                        if stack and abs(l.x0 - stack[-1][0]) <= 4:
                            stack.pop()
                        if stack:
                            stack[-1][2].children.append(item)
                        else:
                            top_items.append(item)
                        stack.append((l.x0, tx, item))
                        prev = l
                        i += 1
                        continue
                    if c[0] == "text" and stack and close(lines[i - 1], l, 0.8) and l.x0 > stack[-1][0] + 4:
                        # Continuation of the deepest item whose text column matches.
                        it = stack[-1][2]
                        sep = Run(" ") if wraps(lines[i - 1], l) else Run("", hard_break=True)
                        it.runs = it.runs + [sep] + l.runs
                        i += 1
                        continue
                    break
                blocks.append(ListBlock(top_items, stack[0][0] if stack else l.x0))
            else:
                runs = list(l.runs)
                first = l
                i += 1
                while i < len(lines) and cls[i][0] == "text" and close(lines[i - 1], lines[i], 0.6):
                    n = lines[i]
                    if abs(n.x0 - first.x0) > 4 and not (n.x0 < first.x0 + 30 and wraps(lines[i - 1], n)):
                        break
                    sep = Run(" ") if wraps(lines[i - 1], n) else Run("", hard_break=True)
                    runs += [sep] + n.runs
                    i += 1
                blocks.append(Para(runs))
        return blocks

    # ---- page -------------------------------------------------------------

    def convert_page(self, page: pymupdf.Page) -> list:
        pno = page.number + 1
        all_lines = self.page_lines(page)
        top, bottom = self.body_region(
            page, [(l.x0, l.y0, l.x1, l.y1, l.text) for l in all_lines]
        )
        lines = [l for l in all_lines if l.y0 >= top - 1 and l.y1 <= bottom + 1]
        right = page.rect.width - 69

        images = []
        for info in page.get_image_info(xrefs=True):
            if info["xref"] in self.furniture_xrefs or not info["xref"]:
                continue
            r = pymupdf.Rect(info["bbox"]) & page.rect
            if r.is_empty or r.y1 < top or r.y0 > bottom:
                continue
            images.append((r, info["xref"]))
        images.sort(key=lambda t: (t[0].y0, t[0].x0))

        elements = []  # (y, kind, payload)
        block_images = []
        for r, xref in images:
            path = self.save_image(xref, pno)
            if r.height < INLINE_IMAGE_MAX_H:
                cy = (r.y0 + r.y1) / 2
                host = min(
                    (l for l in lines if l.y0 - 2 <= cy <= l.y1 + 2),
                    key=lambda l: abs((l.y0 + l.y1) / 2 - cy),
                    default=None,
                )
                if host is not None:
                    idx = sum(1 for rr in host.runs if True)  # append by default
                    # insert at x position: approximate by appending at end of
                    # the line if the image is right of it, else at the start.
                    img = Run("", image=path)
                    if r.x0 < host.x0:
                        host.runs = [img, Run(" ")] + host.runs
                        host.x0 = r.x0
                    else:
                        host.runs = self._insert_image(host, img, r, page)
                    continue
            block_images.append(r)
            elements.append((r.y0, "image", path, r))

        # Text drawn on top of a screenshot belongs to the screenshot.
        lines = [
            l
            for l in lines
            if not any(
                br.contains(pymupdf.Point((l.x0 + l.x1) / 2, (l.y0 + l.y1) / 2))
                for br in block_images
            )
        ]

        for bbox, cells in self.page_tables(page, top, bottom):
            lines = [piece for l in lines for piece in split_by_cells(l, cells)]
            inside = [
                l
                for l in lines
                if bbox.contains(pymupdf.Point((l.x0 + l.x1) / 2, (l.y0 + l.y1) / 2))
            ]
            lines = [l for l in lines if l not in inside]
            if len(cells) == 1:
                # A single bordered box (e.g. a sample request): plain content.
                elements.append((bbox.y0, "box", inside, cells[0]))
                continue
            elements.append((bbox.y0, "table", self.make_table(bbox, cells, inside, pno)))

        for l in lines:
            elements.append((l.y0, "line", l))
        elements.sort(key=lambda e: e[0])

        blocks = []
        pending: list[Line] = []

        def flush():
            if pending:
                blocks.extend(self.build_blocks(pending, pno, right))
                pending.clear()

        for e in elements:
            if e[1] == "line":
                pending.append(e[2])
                continue
            flush()
            if e[1] == "image":
                blocks.append(Image(e[2], self.caption(e[3], lines) or f"Figure on page {pno}"))
            elif e[1] == "box":
                blocks.extend(self.build_blocks(e[2], pno, e[3].x1 - 3))
            else:
                blocks.append(e[2])
        flush()
        return blocks

    def _insert_image(self, host: Line, img: Run, r: pymupdf.Rect, page) -> list[Run]:
        # Find the character position closest to the image's left edge.
        words = page.get_text("words", clip=pymupdf.Rect(host.x0, host.y0, host.x1, host.y1))
        before = " ".join(w[4] for w in sorted(words, key=lambda w: w[0]) if w[2] <= r.x0 + 1)
        out: list[Run] = []
        consumed = 0
        target = len(re.sub(r"\s+", "", before))
        inserted = False
        for run in host.runs:
            if inserted or run.image:
                out.append(run)
                continue
            n = len(re.sub(r"\s+", "", run.text))
            if consumed + n <= target:
                out.append(run)
                consumed += n
                if consumed == target:
                    out += [Run(" "), img, Run(" ")]
                    inserted = True
                continue
            # split this run
            k, cnt = 0, consumed
            while k < len(run.text) and cnt < target:
                if not run.text[k].isspace():
                    cnt += 1
                k += 1
            out.append(Run(run.text[:k], *_style(run)))
            out += [Run(" "), img, Run(" ")]
            out.append(Run(run.text[k:], *_style(run)))
            inserted = True
        if not inserted:
            out += [Run(" "), img]
        return out

    def caption(self, r: pymupdf.Rect, lines: list[Line]) -> str:
        for l in lines:
            if 0 <= l.y0 - r.y1 < 30 and re.match(r"(Figure|Fig\.|Image)\s*\d", l.text.strip()):
                return re.sub(r"\s+", " ", l.text).strip()
        return ""

    def make_table(self, bbox, rects, lines: list[Line], pno: int) -> Table:
        ys = cluster([v for c in rects for v in (c.y0, c.y1)], 2.0)
        cells = []
        for c in rects:
            r0 = nearest(ys, c.y0)
            r1 = nearest(ys, c.y1)
            if r1 <= r0:
                continue
            inside = [
                l
                for l in lines
                if c.contains(pymupdf.Point((l.x0 + l.x1) / 2, (l.y0 + l.y1) / 2))
            ]
            blocks = self.build_blocks(inside, pno, c.x1 - 3, cell=True)
            md, plain, bold = render_cell(blocks)
            cells.append(Cell(r0, r1, c.x0, c.x1, md, plain, bold))
        return Table(cells, len(ys) - 1, bbox.x0, bbox.x1)

    # ---- document -------------------------------------------------------

    def convert(self) -> str:
        pages = [self.convert_page(p) for p in self.doc]
        blocks: list = []
        for pblocks in pages:
            if blocks and pblocks:
                a, b = blocks[-1], pblocks[0]
                if isinstance(a, Table) and isinstance(b, Table) and abs(a.x0 - b.x0) < 4 and abs(a.x1 - b.x1) < 4:
                    blocks[-1] = join_tables(a, b)
                    pblocks = pblocks[1:]
                elif isinstance(a, Code) and isinstance(b, Code):
                    a.lines += b.lines
                    pblocks = pblocks[1:]
                elif isinstance(a, ListBlock) and isinstance(b, ListBlock) and abs(a.x0 - b.x0) < 4:
                    a.items += b.items
                    pblocks = pblocks[1:]
            blocks.extend(pblocks)
        title = re.sub(r"\s+", " ", self.doc.metadata.get("title") or "").strip()
        out = []
        for b in blocks:
            out.append(render_block(b))
        md = "\n\n".join(x for x in out if x.strip())
        return md.strip() + "\n"


def split_by_cells(line: Line, cells: list[pymupdf.Rect]) -> list[Line]:
    """Split a text line whose spans fall into different table cells."""
    if not line.boxes or len(line.runs) < 2:
        return [line]

    def cell_of(b: pymupdf.Rect):
        c = pymupdf.Point((b.x0 + b.x1) / 2, (b.y0 + b.y1) / 2)
        return next((i for i, r in enumerate(cells) if r.contains(c)), None)

    keys = [cell_of(b) if r.text.strip() else None for r, b in zip(line.runs, line.boxes)]
    real = {k for k in keys if k is not None}
    if len(real) < 2:
        return [line]
    out: list[Line] = []
    cur_runs, cur_boxes, cur_key = [], [], None
    for r, b, k in zip(line.runs, line.boxes, keys):
        if k is not None and cur_key is not None and k != cur_key:
            out.append(_piece(cur_runs, cur_boxes, line))
            cur_runs, cur_boxes = [], []
        if k is not None:
            cur_key = k
        cur_runs.append(r)
        cur_boxes.append(b)
    out.append(_piece(cur_runs, cur_boxes, line))
    return out


def _piece(runs: list[Run], boxes: list, line: Line) -> Line:
    texty = [b for r, b in zip(runs, boxes) if r.text.strip()] or boxes
    first = next((r, b) for r, b in zip(runs, boxes) if r.text.strip()) if any(r.text.strip() for r in runs) else (runs[0], boxes[0])
    word = first[0].text.lstrip().split(" ")[0]
    fw = first[1].width * len(word) / max(len(first[0].text), 1)
    return Line(runs, min(b.x0 for b in texty), line.y0, max(b.x1 for b in texty), line.y1,
                line.size, fw, boxes)


def slug(title: str) -> str:
    s = re.sub(r"\s+", " ", title).strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def cluster(values: list[float], tol: float) -> list[float]:
    out: list[float] = []
    for v in sorted(values):
        if out and v - out[-1] <= tol:
            continue
        out.append(v)
    return out


def nearest(points: list[float], v: float) -> int:
    return min(range(len(points)), key=lambda i: abs(points[i] - v))


def join_tables(a: Table, b: Table) -> Table:
    cells = list(a.cells)
    first_b = [c for c in b.cells if c.r0 == 0]
    first_a = sorted((c for c in a.cells if c.r0 == 0), key=lambda c: c.x0)
    # A repeated header row on the new page is dropped.
    if first_b and [c.plain for c in sorted(first_b, key=lambda c: c.x0)] == [c.plain for c in first_a] and all(c.all_bold for c in first_b if c.plain):
        rest = [Cell(c.r0 - 1, c.r1 - 1, c.x0, c.x1, c.md, c.plain, c.all_bold) for c in b.cells if c.r0 > 0]
        nb = b.nrows - 1
    else:
        rest, nb = b.cells, b.nrows
    # A row split by the page break continues with an empty first column.
    first_rest = [c for c in rest if c.r0 == 0]
    last_a = [c for c in a.cells if c.r1 == a.nrows]
    lead = min(first_rest, key=lambda c: c.x0, default=None)
    if lead is not None and not lead.plain and any(c.plain for c in first_rest) and last_a:
        for c in first_rest:
            if not c.md:
                continue
            target = min(last_a, key=lambda t: abs(t.x0 - c.x0) + abs(t.x1 - c.x1))
            target.md = f"{target.md}<br>{c.md}" if target.md else c.md
            target.plain = f"{target.plain} {c.plain}".strip()
            target.all_bold = target.all_bold and c.all_bold
        for c in a.cells:
            if c.r1 == a.nrows:
                c.r1 += max((x.r1 for x in first_rest), default=1) - 1
        rest = [Cell(c.r0 - 1, c.r1 - 1, c.x0, c.x1, c.md, c.plain, c.all_bold) for c in rest if c.r0 > 0]
        nb -= 1
        # cells of the continued row that spanned further rows keep spanning
    for c in rest:
        cells.append(Cell(c.r0 + a.nrows, c.r1 + a.nrows, c.x0, c.x1, c.md, c.plain, c.all_bold))
    return Table(cells, a.nrows + nb, a.x0, a.x1)


# --------------------------------------------------------------------------
# Block rendering
# --------------------------------------------------------------------------


def escape_block_start(s: str) -> str:
    if re.match(r"(#{1,6}\s|>|[-+*]\s|\d+[.)]\s|=+\s*$|-+\s*$)", s):
        return "\\" + s
    return s


def render_list_md(items: list[ListItem], indent: int = 0) -> list[str]:
    out = []
    n = 0
    for it in items:
        if it.ordered and it.marker[:-1].isdigit():
            marker = f"{it.marker[:-1]}."
        else:
            marker = "-"
        text = render_runs(it.runs, "<br>")
        if it.ordered and marker == "-":
            text = f"{it.marker} {text}"
        else:
            text = escape_block_start(text)
        pad = " " * indent
        out.append(f"{pad}{marker} {text}")
        if it.children:
            out += render_list_md(it.children, indent + len(marker) + 1)
    return out


def render_list_html(items: list[ListItem]) -> str:
    parts = []
    i = 0
    while i < len(items):
        it = items[i]
        ol = it.ordered and it.marker[:-1].isdigit()
        group = [it]
        i += 1
        while i < len(items) and (items[i].ordered and items[i].marker[:-1].isdigit()) == ol:
            group.append(items[i])
            i += 1
        lis = []
        for g in group:
            text = render_runs(g.runs, "<br>")
            if g.ordered and not ol:
                text = f"{g.marker} {text}"
            if g.children:
                text += render_list_html(g.children)
            lis.append(f"<li>{text}</li>")
        if ol:
            start = int(group[0].marker[:-1])
            attr = f' start="{start}"' if start != 1 else ""
            parts.append(f"<ol{attr}>{''.join(lis)}</ol>")
        else:
            parts.append(f"<ul>{''.join(lis)}</ul>")
    return "".join(parts)


def render_block(b) -> str:
    if isinstance(b, Heading):
        return "#" * min(b.level + 1, 6) + " " + b.text
    if isinstance(b, Para):
        return escape_block_start(render_runs(b.runs, "\\\n"))
    if isinstance(b, Code):
        lang = "json" if b.lines and b.lines[0].strip()[:1] in "{[" else ""
        return f"```{lang}\n" + "\n".join(b.lines) + "\n```"
    if isinstance(b, Image):
        return f"![{_escape_plain(b.alt)}]({b.path})"
    if isinstance(b, ListBlock):
        return "\n".join(render_list_md(b.items))
    if isinstance(b, Table):
        return render_table(b)
    raise TypeError(b)


def render_cell(blocks) -> tuple[str, str, bool]:
    parts, plain, bold = [], [], True
    for b in blocks:
        if isinstance(b, Para):
            parts.append(render_runs(b.runs, "<br>"))
            plain.append("".join(r.text for r in b.runs))
            bold = bold and runs_all_bold(b.runs)
        elif isinstance(b, ListBlock):
            parts.append(render_list_html(b.items))
            bold = False
            plain.append(" ".join(flatten_items(b.items)))
        elif isinstance(b, Heading):
            parts.append(f"<strong>{_escape_plain(b.text)}</strong>")
            plain.append(b.text)
        elif isinstance(b, Code):
            parts.append("<br>".join(f"<code>{_escape_plain(x)}</code>" for x in b.lines))
            plain.append(" ".join(b.lines))
            bold = False
    md = "<br>".join(p for p in parts if p)
    # Lists already break the line; avoid an extra blank line around them.
    md = re.sub(r"<br>(<[ou]l)", r"\1", md)
    md = re.sub(r"(</[ou]l>)<br>", r"\1", md)
    md = md.replace("\n", " ")
    plain_s = re.sub(r"\s+", " ", " ".join(plain)).strip()
    return md, plain_s, bold and bool(plain_s)


def flatten_items(items: list[ListItem]) -> list[str]:
    out = []
    for it in items:
        out.append("".join(r.text for r in it.runs))
        out += flatten_items(it.children)
    return out


def render_table(t: Table) -> str:
    xs = cluster([v for c in t.cells for v in (c.x0, c.x1)], TABLE_X_TOL)
    rows: dict[int, list[Cell]] = {}
    for c in t.cells:
        rows.setdefault(c.r0, []).append(c)
    ncols = len(xs) - 1
    out_parts: list[str] = []
    segment: list[list[Cell]] = []
    header: list[Cell] | None = None

    def col(c: Cell) -> int:
        return nearest(xs, c.x0)

    def emit():
        nonlocal segment, header
        rows_ = ([header] if header else []) + segment
        if not rows_:
            return
        starts = sorted({col(c) for r in rows_ for c in r if c.plain or c.md})
        if not starts:
            segment, header = [], None
            return
        idx = {s: i for i, s in enumerate(starts)}

        def line(cells: list[Cell]) -> str:
            vals = [""] * len(starts)
            for c in sorted(cells, key=lambda c: c.x0):
                k = col(c)
                # Cells narrower than the tolerance join their neighbour.
                while k not in idx and k > 0:
                    k -= 1
                if k not in idx:
                    k = starts[0]
                j = idx[k]
                if c.md:
                    vals[j] = (vals[j] + "<br>" + c.md) if vals[j] else c.md
            return "| " + " | ".join(vals) + " |"

        lines = [line(header) if header else "| " + " | ".join([" "] * len(starts)) + " |"]
        lines.append("|" + "|".join(["---"] * len(starts)) + "|")
        lines += [line(r) for r in segment]
        out_parts.append("\n".join(lines))
        segment, header = [], None

    for r in range(t.nrows):
        cells = rows.get(r, [])
        content = [c for c in cells if c.plain or c.md]
        if not content:
            continue
        if len(content) == 1 and len(cells) == 1 and col(cells[0]) == 0 and nearest(xs, cells[0].x1) == ncols and ncols > 1:
            emit()
            out_parts.append(content[0].md)
            continue
        if len(content) >= 2 and all(c.all_bold for c in content):
            emit()
            header = cells
            continue
        segment.append(cells)
    emit()
    return "\n\n".join(out_parts)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def convert_pdf(pdf: bytes, out: Path) -> str:
    doc = pymupdf.open(stream=pdf, filetype="pdf")
    image_dir = out.parent / IMAGE_DIR
    if image_dir.exists():
        shutil.rmtree(image_dir)
    image_dir.mkdir(parents=True)
    md = Converter(doc, image_dir).convert()
    sha = hashlib.sha256(pdf).hexdigest()
    header = (
        f"<!-- Generated by scripts/convert.py from {PDF_URL}\n"
        f"     Source SHA-256: {sha}. Do not edit by hand. -->\n\n"
    )
    return header + md


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf", help="Use a local PDF instead of downloading")
    ap.add_argument("--pdf-out", help="Also save the downloaded PDF here")
    ap.add_argument("--out", default=OUT_PATH)
    args = ap.parse_args()

    if args.pdf:
        pdf = Path(args.pdf).read_bytes()
    else:
        pdf = fetch_pdf(PDF_URL)
        if args.pdf_out:
            Path(args.pdf_out).write_bytes(pdf)
    out = Path(args.out)
    md = convert_pdf(pdf, out)
    out.write_text(md, encoding="utf-8")
    print(f"Wrote {out} ({len(md):,} chars)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
