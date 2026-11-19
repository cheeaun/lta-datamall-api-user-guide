# Working in this repo

## What this is

A Markdown mirror of the LTA DataMall API User Guide PDF plus the tooling
that produces it. `LTA_DataMall_API_User_Guide.md` is **generated** — never
edit it by hand; fix `scripts/convert.py` instead and regenerate.

## Commands

```sh
pip install -r requirements.txt
python scripts/convert.py --pdf-out guide.pdf
python scripts/check.py --pdf guide.pdf --md LTA_DataMall_API_User_Guide.md
```

## Rules

- Always run `scripts/check.py` after changing `convert.py`. All checks
  must pass before committing.
- Keep cleanup rules in `clean_markdown()` general and deterministic —
  no content edits, no hard-coded document text beyond the repeated page
  furniture.
- If you add a cleanup rule, add a matching artifact check in `check.py`.
- Pin dependency versions in `requirements.txt`; bump deliberately, then
  re-run convert + check.
- `guide.pdf` is a build artifact — do not commit it.
