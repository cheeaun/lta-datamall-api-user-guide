# LTA DataMall API User Guide, in Markdown

A Markdown copy of the official
[LTA DataMall API User Guide](https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf),
regenerated weekly from the PDF. It is easier to read, search, diff and feed
to tools than the PDF.

Read it here: [LTA_DataMall_API_User_Guide.md](LTA_DataMall_API_User_Guide.md).
Screenshots and figures from the PDF are in [`images/`](images/).

## What the conversion keeps

- Headings that match the PDF bookmarks (sections 1–2.x and the annexes).
- Tables, including merged cells and tables that continue across pages.
- Bold, italic and superscript text.
- Bulleted and numbered lists, nested lists, and lists inside table cells.
- Hyperlinks.
- JSON response samples, as fenced code blocks.
- Content images. The LTA logo repeated on every page is left out.

## How it works

`scripts/convert.py` downloads the PDF and reads it with
[PyMuPDF](https://pymupdf.readthedocs.io/). Rather than flattening each page
to text, it works from the PDF's own primitives: text spans with their fonts,
table borders, bullet glyphs, indentation, link annotations and image blocks.

`scripts/check.py` checks the Markdown against the PDF. It renders the
Markdown to HTML with [markdown-it-py](https://github.com/executablebooks/markdown-it-py)
and extracts the PDF separately from the converter, then compares:

| Check | What must hold |
| --- | --- |
| text | Every PDF word is in the Markdown, and no word appears more often than in the PDF |
| lines | Every PDF line is contiguous in the Markdown, and pages stay in order |
| headings | Every PDF bookmark is a heading at the right level, in order |
| bold, italic, sup | Formatted PDF text is formatted the same way, and nothing else is |
| lists | Every bullet or numbered line is a list item, nested as in the PDF |
| tables | Every PDF cell is one Markdown cell, cells of a row share a row, split tables are joined |
| images | Every content image is referenced, exists, decodes, and has the PDF image's size |
| links | Every PDF hyperlink is a link; internal links point to headings |
| code | JSON samples are in code blocks and parse |
| syntax | No stray Markdown markers or raw HTML in the rendered text |

Any failed check exits non-zero.

A [GitHub Action](.github/workflows/update.yml) runs every Monday. It
regenerates the guide, runs the checks, and opens a pull request if anything
changed.

## Usage

```sh
pip install -r requirements.txt

# Download the PDF, regenerate the Markdown and images, keep a copy of the PDF
python scripts/convert.py --pdf-out guide.pdf

# Check the result against the PDF
python scripts/check.py --pdf guide.pdf
```

To convert a PDF you already have: `python scripts/convert.py --pdf path/to/guide.pdf`.

## License

The guide's content belongs to the Land Transport Authority of Singapore. See
the [DataMall portal](https://datamall.lta.gov.sg/) for terms of use.
