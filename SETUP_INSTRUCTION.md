# Setup brief: the original bootstrap task

> **Status: superseded. Historical record, not instructions.**
>
> This brief created the repository. It records why the design looks the way it
> does, which is why it stays here. Do not follow it as a setup guide. The
> repository has moved on since then, and [README.md](README.md) plus
> [AGENTS.md](AGENTS.md) describe how it actually works now.
>
> What changed since then:
>
> - Scripts live in `tools/scripts/`, not `scripts/`.
> - The repository has no `requirements.txt` and no virtual environment. Each
>   script is a self-contained PEP 723 file that provisions its own dependencies
>   under `uv run`.
> - The textconv driver runs `uv run tools/scripts/xlsx_to_text.py`. The
>   pre-commit hook runs `uv run tools/scripts/export_snapshot.py`.
> - The workbook is `data/KPI List.xlsx`, with a space in the name.
> - Later work added parts this brief never mentions: the `kpi-engine` package,
>   the surgical `xlsx_edit.py` editor, the per-company workbook builder, and the
>   HTML and PDF builders.
>
> Section 2 still holds. The commands and the folder layout do not.

---

## 1. Goal

Set up a git repository in this folder so that **every change to the KPI Excel
workbook is reviewable in VS Code** (Source Control panel and pull-request diffs),
without losing the information the workbook encodes in formatting.

## 2. Design (do not change without asking)

The workbook is **not** plain tabular data. Two things carry meaning beyond cell
text and must be preserved:

- **Row fill colour encodes the hierarchy level** (Level 1 = pale green … Level 4 =
  bright green, Level-5 raw metrics = grey).
- The **Metrics List** sheet uses `=HYPERLINK(...)` formulas in the
  *Underlying Metrics* column for in-file navigation.

A plain CSV-as-source-of-truth setup would drop both. So the chosen model is:

1. **The `.xlsx` is canonical.** It is committed to git as a binary file. All edits
   happen in the workbook.
2. **A deterministic text snapshot is committed alongside it** — one tab-separated
   file per sheet under `snapshot/`. This is regenerated automatically on every
   commit. Because these are normal text files, **VS Code's diff editor and GitHub
   PRs show line-by-line, cell-level changes** here. This is the primary review
   surface.
3. **A git `textconv` diff driver** is configured for `*.xlsx`, so `git diff` /
   `git log -p` on the workbook itself render readable text **on the command line**.
   (VS Code's built-in diff editor does not run textconv drivers — that is exactly
   why the committed snapshot in step 2 exists.)

Snapshot scope and limits: the snapshot captures **cell values and formulas**
(so hyperlink-target changes are visible). It does **not** capture fill colours; a
change of a row's hierarchy level is still visible because the *Level* column holds
that value as text. Note this limitation in the README.

## 3. Target folder layout

Create exactly this structure (move the existing workbook into `data/`):

```
.
├── data/
│   └── KPI_List.xlsx          # canonical workbook (rename to match the real file)
├── snapshot/                  # generated, committed — the review surface
│   ├── _sheets.txt
│   └── <one .tsv per sheet>
├── scripts/
│   ├── export_snapshot.py     # workbook -> snapshot/*.tsv
│   └── xlsx_to_text.py        # workbook -> stdout (git textconv driver)
├── .githooks/
│   └── pre-commit
├── .vscode/
│   └── extensions.json
├── .gitattributes
├── .gitignore
├── requirements.txt
└── README.md
```

If the workbook in the folder has a different filename, keep its name but place it
under `data/` and update every reference below accordingly.

## 4. Files to create

### `scripts/export_snapshot.py`

```python
#!/usr/bin/env python3
"""Export each worksheet of the KPI workbook to a stable TSV snapshot for git diffing.

One spreadsheet row == one text line, so git produces clean line-level diffs.
Captures cell values and formulas (e.g. =HYPERLINK targets). Does not capture
cell fill colour; hierarchy level is tracked via the workbook's own 'Level' column.
"""
import os
from openpyxl import load_workbook

WORKBOOK = os.environ.get("KPI_WORKBOOK", "data/KPI_List.xlsx")
OUT_DIR = "snapshot"


def cell_text(v):
    if v is None:
        return ""
    s = str(v)
    # Keep every spreadsheet row on a single line and keep whitespace stable.
    return (
        s.replace("\\", "\\\\")
        .replace("\t", "\\t")
        .replace("\r\n", "\\n")
        .replace("\n", "\\n")
        .replace("\r", "\\n")
    )


def safe_name(name):
    return "".join(c if (c.isalnum() or c in " -_") else "_" for c in name).strip()


def main():
    wb = load_workbook(WORKBOOK, data_only=False)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "_sheets.txt"), "w", encoding="utf-8", newline="\n") as idx:
        idx.write("\n".join(wb.sheetnames) + "\n")
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        path = os.path.join(OUT_DIR, f"{safe_name(sheet)}.tsv")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            for row in ws.iter_rows():
                line = "\t".join(cell_text(c.value) for c in row).rstrip("\t")
                f.write(line + "\n")
    print(f"Snapshot written to {OUT_DIR}/ for {len(wb.sheetnames)} sheet(s).")


if __name__ == "__main__":
    main()
```

### `scripts/xlsx_to_text.py`

```python
#!/usr/bin/env python3
"""Print all sheets of an xlsx to stdout as text. Used as a git textconv diff driver
so that `git diff` on the workbook is readable on the command line."""
import sys
from openpyxl import load_workbook


def cell_text(v):
    if v is None:
        return ""
    return (
        str(v)
        .replace("\t", "\\t")
        .replace("\r\n", "\\n")
        .replace("\n", "\\n")
        .replace("\r", "\\n")
    )


def main(path):
    wb = load_workbook(path, data_only=False)
    for sheet in wb.sheetnames:
        print(f"## {sheet}")
        for row in wb[sheet].iter_rows():
            print("\t".join(cell_text(c.value) for c in row).rstrip("\t"))
        print()


if __name__ == "__main__":
    main(sys.argv[1])
```

### `.githooks/pre-commit`

```sh
#!/bin/sh
# Regenerate the committed text snapshot whenever the workbook is part of the commit,
# so the review surface never drifts from the canonical .xlsx.
set -e

# Only act if an .xlsx under data/ is staged.
if git diff --cached --name-only | grep -q '^data/.*\.xlsx$'; then
    if [ -f ".venv/bin/activate" ]; then
        . .venv/bin/activate
    fi
    python scripts/export_snapshot.py
    git add snapshot/
fi
```

Make it executable: `chmod +x .githooks/pre-commit`.

### `.gitattributes`

```
# Treat the workbook as binary (no EOL conversion, not mergeable) but give it a
# readable textconv diff on the command line.
*.xlsx -text -merge diff=xlsx

# Snapshot files are text with stable LF endings.
snapshot/*  text eol=lf
*.tsv       text eol=lf
```

### `.gitignore`

```
.venv/
__pycache__/
*.pyc
~$*.xlsx
.DS_Store
```

### `requirements.txt`

```
openpyxl>=3.1
```

### `.vscode/extensions.json`

```json
{
  "recommendations": [
    "mechatroner.rainbow-csv",
    "GrapeCity.gc-excelviewer"
  ]
}
```

(`rainbow-csv` renders the `snapshot/*.tsv` files as readable tables; the Excel
viewer lets you open the `.xlsx` itself. Confirm the current extension IDs in the
VS Code Marketplace before relying on them.)

### `README.md`

Write a short README that contains: the design summary from section 2, the setup
commands from section 5, the daily workflow from section 6, and the snapshot
limitation (colours not captured; level tracked via the *Level* column).

## 5. Commands to run (in order)

```bash
# 1. Move the workbook into data/ (use the real filename if different)
mkdir -p data && git mv KPI_List.xlsx data/ 2>/dev/null || mv KPI_List.xlsx data/

# 2. Python environment
python3 -m venv .venv
. .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Initialise git and the hook path
git init
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit

# 4. Register the textconv driver for readable CLI diffs of the workbook
git config diff.xlsx.textconv "python scripts/xlsx_to_text.py"
git config diff.xlsx.binary true

# 5. Generate the first snapshot and make the initial commit
python scripts/export_snapshot.py
git add .
git commit -m "Initialise version-controlled KPI workbook environment"
```

## 6. Daily workflow (document this in the README)

1. Edit `data/KPI_List.xlsx` (manually in Excel, or via openpyxl scripts).
2. Stage and commit. The pre-commit hook regenerates `snapshot/` automatically.
3. Review changes in the **VS Code Source Control panel** — the `snapshot/*.tsv`
   diffs show exactly which cells changed.
4. For a quick terminal view of the workbook itself: `git diff -- data/KPI_List.xlsx`
   (rendered via the textconv driver).

## 7. Acceptance checklist (verify before reporting done)

- [ ] `data/KPI_List.xlsx` exists; no `.xlsx` remains in the repo root.
- [ ] `python scripts/export_snapshot.py` runs clean and writes one `.tsv` per sheet
      plus `_sheets.txt`, with the same number of sheets as the workbook.
- [ ] `git config --get core.hooksPath` returns `.githooks`.
- [ ] Make a trivial test edit to one cell, commit, and confirm the matching
      `snapshot/*.tsv` shows that single-line change in `git show` / the VS Code diff.
      Then revert the test edit and commit.
- [ ] `git diff` against a prior commit renders the workbook as readable text on the
      command line (textconv working).
- [ ] `README.md` documents the design, setup, daily workflow, and the snapshot
      colour limitation.
- [ ] `.venv/` and caches are gitignored and not tracked.

## 8. Do not

- Do not convert the workbook to CSV as the source of truth, or regenerate the
  `.xlsx` from text — that would drop the level colours and hyperlinks.
- Do not edit files under `snapshot/` by hand; they are generated artifacts.
- Do not commit the virtual environment.
