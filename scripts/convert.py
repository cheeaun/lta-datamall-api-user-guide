#!/usr/bin/env python3
"""Fetch the LTA DataMall API User Guide PDF and convert it to Markdown.

Usage:
    python scripts/convert.py [--pdf PATH] [--out PATH]

Downloads the PDF (or uses --pdf), converts it with pymupdf4llm, cleans up
page furniture and extraction artifacts, and writes the Markdown file.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import urllib.request

PDF_URL = (
    "https://datamall.lta.gov.sg/content/dam/datamall/datasets/"
    "LTA_DataMall_API_User_Guide.pdf"
)
OUT_PATH = "LTA_DataMall_API_User_Guide.md"

# Repeated page furniture printed at the top of every PDF page. pymupdf4llm
# emits it as text between "-----" page separators.
PAGE_HEADER_RE = re.compile(
    r"LTA DataMall \| API User Guide & Documentation\n+Version [\d.]+ \([^)]*\)\n*"
)


def fetch_pdf(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Response from {url} is not a PDF")
    return data


def pdf_to_markdown(pdf: bytes) -> str:
    import pymupdf
    import pymupdf4llm

    doc = pymupdf.open(stream=pdf, filetype="pdf")
    return pymupdf4llm.to_markdown(doc, show_progress=False)


def clean_markdown(md: str) -> str:
    """Remove page furniture and tidy extraction artifacts."""
    # Drop the repeated running header (kept once later, via the doc title).
    md = PAGE_HEADER_RE.sub("", md)

    # Drop the "-----" page separators pymupdf4llm emits.
    md = re.sub(r"\n*-{5,}\n*", "\n\n", md)

    # "<br>- " inside table cells renders better as a bullet char.
    md = md.replace("<br>- <br>", "<br>• ")
    md = md.replace("<br>• <br>", "<br>• ")
    # Empty bullet followed by a break: "• <br>text" -> "• text".
    md = re.sub(r"•\s*<br>", "• ", md)

    # Pseudo-headings like "#### • Content" are list items, not headings.
    md = re.sub(r"^#+\s*•\s*", "• ", md, flags=re.M)

    # "***bold-italic***" -> "**bold-italic**" (nothing in the source is
    # genuinely bold-italic; this is an extraction artifact).
    md = md.replace("***", "**")

    # "** text **" -> "**text**" — spaces inside emphasis markers don't
    # render and come from cell-padding artifacts.
    md = re.sub(r"\*\*\s+([^*]*?)\s+\*\*", r"**\1**", md)

    # Restore superscripts mangled into brackets: "3[rd]" -> "3rd",
    # "n[th]" -> "nth", "1[st]" -> "1st".
    md = re.sub(r"(\w)\[(rd|th|st|nd)\]", r"\1\2", md)

    # Rebuild the cover block into a single clean title line.
    md = re.sub(
        r"^#\s*an\s+LTA Open Data Initiative\n+\s*API User Guide & Documentation\n+"
        r"Version\s+([\d.]+)\n+(.*)$",
        r"# LTA DataMall API User Guide\n\n*An LTA Open Data Initiative — "
        r"Version \1, \2*",
        md,
        flags=re.M,
    )

    # Field labels like "**URL **https://..." or "**Description **text"
    # read better as "**URL:** ...".
    md = re.sub(r"\*\*([A-Za-z /&()]{2,25}?)\s+\*\*", r"**\1:**", md)

    # Join lines that were wrapped mid-sentence by the PDF layout back into
    # paragraphs. A line merges into the previous one only when the previous
    # line clearly continues (ends lowercase/comma) or the next starts
    # lowercase — so table-like attribute rows stay on separate lines.
    out: list[str] = []
    for ln in md.split("\n"):
        if (
            out
            and ln
            and not re.match(r"^\s*([|#•\-*_]|\d+\.|\*\*)", ln)
            and out[-1]
            and not re.match(r"^\s*([|#•\-*_]|\d+\.|\*\*)", out[-1])
            and (re.search(r"[a-z,—–-]$", out[-1]) or re.match(r"^[a-z(]", ln))
        ):
            out[-1] += " " + ln.strip()
        else:
            out.append(ln)
    md = "\n".join(out)

    # Insert a space where bold markers abut a letter: "to**Traffic" ->
    # "to **Traffic". Skip inside table rows, where the markers are often
    # real cell boundaries.
    def fix_bold_spacing(line: str) -> str:
        if line.lstrip().startswith("|"):
            return line
        line = re.sub(r"([a-zA-Z0-9,.])\*\*", r"\1 **", line)
        # Closing "**" immediately followed by a letter inside a word pair,
        # e.g. "to**Traffic" handled above; opening "**" glued to text is
        # valid markdown and left alone.
        return line

    md = "\n".join(fix_bold_spacing(ln) for ln in md.split("\n"))

    # Drop standalone page-number lines (a bare 1-3 digit line).
    md = re.sub(r"^\d{1,3}$", "", md, flags=re.M)

    # Collapse runs of blank lines.
    md = re.sub(r"\n{3,}", "\n\n", md)

    # Trim trailing spaces.
    md = re.sub(r"[ \t]+\n", "\n", md)

    return md.strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", help="Local PDF path (skip download)")
    ap.add_argument("--out", default=OUT_PATH)
    ap.add_argument("--pdf-out", help="Also save the fetched PDF to this path")
    args = ap.parse_args()

    if args.pdf:
        pdf = open(args.pdf, "rb").read()
        source = args.pdf
    else:
        pdf = fetch_pdf(PDF_URL)
        source = PDF_URL

    sha = hashlib.sha256(pdf).hexdigest()
    print(f"Source: {source}")
    print(f"SHA256: {sha}")

    if args.pdf_out:
        with open(args.pdf_out, "wb") as f:
            f.write(pdf)

    md = clean_markdown(pdf_to_markdown(pdf))
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Wrote {args.out} ({len(md)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
