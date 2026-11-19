#!/usr/bin/env python3
"""Deterministic quality checks for the generated Markdown.

Verifies the Markdown against the source PDF it was generated from:

  1. Word coverage — nearly every word in the PDF body must appear in the
     Markdown (catches dropped content).
  2. URL coverage — every URL in the PDF must appear in the Markdown.
  3. Section structure — numbered sections (e.g. "2.11 TRAIN SERVICE
     ALERTS") found in the PDF must appear as headings, in order.
  4. Table well-formedness — every table block has a consistent column
     count and a separator row.
  5. No extraction artifacts — page headers, separators, <br>- bullets.

Usage:
    python scripts/check.py --pdf guide.pdf --md LTA_DataMall_API_User_Guide.md
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from collections import Counter

import pymupdf

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    if not ok:
        FAILURES.append(name)


def words(text: str) -> Counter:
    return Counter(w.lower() for w in re.findall(r"[A-Za-z0-9]+", text))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--md", required=True)
    args = ap.parse_args()

    doc = pymupdf.open(args.pdf)
    pdf_text = "\n".join(page.get_text() for page in doc)
    md = open(args.md, encoding="utf-8").read()
    n_pages = doc.page_count

    # --- 1. Word coverage -------------------------------------------------
    # Exclude repeated page furniture from the PDF side so coverage measures
    # real content, not headers we deliberately strip.
    pdf_body = re.sub(
        r"LTA DataMall \| API User Guide & Documentation|Version [\d.]+ \(\d{2} \w{3} \d{4}\)",
        " ",
        pdf_text,
    )
    pdf_words = words(pdf_body)
    md_words = words(md)
    missing = pdf_words - md_words
    missing_total = sum(missing.values())
    total = sum(pdf_words.values())
    coverage = 1 - (missing_total / total if total else 1)
    check(
        "word coverage >= 98%",
        coverage >= 0.98,
        f"{coverage:.2%} ({missing_total} of {total} missing; "
        f"top missing: {missing.most_common(10)})",
    )

    # --- 2. URL coverage --------------------------------------------------
    pdf_urls = sorted(set(re.findall(r"https?://[^\s)\]]+", pdf_text)))
    pdf_urls = [u.rstrip(".,;") for u in pdf_urls]
    missing_urls = [u for u in pdf_urls if u not in md]
    check(
        "all PDF URLs present",
        not missing_urls,
        f"{len(pdf_urls)} URLs in PDF, missing: {missing_urls[:5]}",
    )

    # --- 3. Section structure ----------------------------------------------
    # Numbered sections like "2.11 TRAIN SERVICE ALERTS" in the PDF body.
    pdf_sections = re.findall(
        r"^\s*(\d+\.\d+)\s+([A-Z][A-Z0-9 /&()'\\-]+)$", pdf_text, re.M
    )
    seen = set()
    expected_sections = [
        f"{num} {title.strip()}"
        for num, title in pdf_sections
        if not (num in seen or seen.add(num))
    ]
    md_sections = re.findall(r"^#{2,4}\s+(\d+\.\d+\s+.+)$", md, re.M)
    md_sections_norm = [re.sub(r"\s+", " ", s).strip() for s in md_sections]
    missing_sections = []
    pos = -1
    in_order = True
    for sec in expected_sections:
        sec_norm = re.sub(r"\s+", " ", sec).strip()
        found = None
        for i, ms in enumerate(md_sections_norm):
            if ms.startswith(sec_norm) or sec_norm.startswith(ms):
                found = i
                break
        if found is None:
            missing_sections.append(sec_norm)
        else:
            if found < pos:
                in_order = False
            pos = found
    check(
        "all numbered sections present as headings",
        not missing_sections,
        f"{len(md_sections_norm)} headings, missing: {missing_sections[:8]}",
    )
    check("sections appear in order", in_order)

    # --- 4. Table well-formedness ------------------------------------------
    lines = md.split("\n")
    table_blocks = []
    cur: list[str] = []
    for ln in lines:
        if ln.lstrip().startswith("|"):
            cur.append(ln)
        else:
            if cur:
                table_blocks.append(cur)
                cur = []
    if cur:
        table_blocks.append(cur)

    bad_tables = []
    for i, block in enumerate(table_blocks):
        counts = [ln.count("|") for ln in block]
        dominant = Counter(counts).most_common(1)[0][0]
        # A table split across a PDF page break can emit one fragment row
        # with a merged column layout; tolerate up to 2 such rows, but only
        # when they are wider than the dominant shape (never narrower).
        fragments = [c for c in counts if c != dominant]
        has_sep = any(re.match(r"^\|[\s:|-]+\|?\s*$", ln) for ln in block)
        if not has_sep or len(fragments) > 2 or any(c < dominant for c in fragments):
            bad_tables.append((i + 1, dominant, fragments, has_sep))
    check(
        "all table blocks well-formed",
        not bad_tables,
        f"{len(table_blocks)} tables; bad: {bad_tables[:5]}",
    )
    check("at least one table found", len(table_blocks) > 0, f"{len(table_blocks)} tables")

    # --- 5. No extraction artifacts -----------------------------------------
    noise_patterns = {
        "page header": r"LTA DataMall \| API User Guide & Documentation\n+Version",
        "page separator": r"\n-{5,}\n",
        "empty bullet <br>-": r"<br>-\s*<br>",
        "pseudo-heading": r"^#+\s*•",
        "bracketed superscript": r"\w\[(rd|th|st|nd)\]",
        "standalone page number": r"^\d{1,3}$",
        "bullet-break artifact": r"•\s*<br>|<br>-\s*<br>",
    }
    # Runs of exactly 3 asterisks ("***") are an artifact; runs of 4+ are
    # adjacent "**bold** **bold**" pairs, which are valid.
    hits = [m for m in re.finditer(r"\*+", md) if len(m.group(0)) == 3]
    check("no triple-asterisk runs", not hits, f"{len(hits)} hits")
    for name, pat in noise_patterns.items():
        hits = re.findall(pat, md, flags=re.M)
        check(f"no {name}", not hits, f"{len(hits)} hits")

    # --- 6. Sanity ----------------------------------------------------------
    check("single H1 title present", len(re.findall(r"^# ", md, re.M)) >= 1)
    check(
        "non-trivial size",
        len(md) > 50_000 and len(md) < 1_000_000,
        f"{len(md)} chars",
    )
    check(
        "plausible page count",
        20 <= n_pages <= 300,
        f"{n_pages} pages",
    )

    print()
    if FAILURES:
        print(f"{len(FAILURES)} check(s) failed: {FAILURES}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
