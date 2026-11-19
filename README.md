# LTA DataMall API User Guide — Markdown

This repo keeps a Markdown copy of the official
[LTA DataMall API User Guide](https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf)
so the API docs are easy to read, diff, and feed to tooling.

The converted document lives in
[LTA_DataMall_API_User_Guide.md](LTA_DataMall_API_User_Guide.md).

## How it works

- `scripts/convert.py` downloads the PDF, converts it with
  [pymupdf4llm](https://pypi.org/project/pymupdf4llm/), and cleans up
  extraction artifacts: repeated page headers, page separators, stray page
  numbers, mangled superscripts, broken emphasis markers, and mid-sentence
  line wraps. Bordered tables come out as GitHub-flavored Markdown tables.
- `scripts/check.py` verifies the output against the source PDF — word and
  URL coverage, section ordering, table well-formedness, and absence of
  known artifacts. It fails loudly so a bad conversion can't land.
- A [GitHub Action](.github/workflows/update.yml) runs weekly, and when the
  upstream PDF changes it opens a pull request with the regenerated
  Markdown.

## Usage

```sh
pip install -r requirements.txt

# Re-fetch the PDF and regenerate the markdown (also saves guide.pdf)
python scripts/convert.py --pdf-out guide.pdf

# Verify the result
python scripts/check.py --pdf guide.pdf --md LTA_DataMall_API_User_Guide.md
```

To convert an existing PDF without downloading:

```sh
python scripts/convert.py --pdf path/to/guide.pdf
```

## Notes

- Attribute lists whose tables have no borders in the PDF are kept as plain
  text lines rather than guessed into tables — this keeps the output
  faithful to the source.
- Content belongs to the Land Transport Authority of Singapore; see the
  [DataMall portal](https://datamall.lta.gov.sg/) for terms of use.
