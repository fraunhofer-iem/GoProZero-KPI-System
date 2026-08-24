# Version-controlled KPI workbook

The [Sustainability KPI List](./data/KPI%20List.xlsx) is manually curated by us from
literature reviews and input from the project partners. The purpose of this repository
however is to make **every change to that workbook reviewable like code** and the defined
AI agents is to help with verification, consistency checks, manual generation, and
tailoring the KPI system.

The visual manual is deployed at
https://fraunhofer-iem.github.io/GoProZero-KPI-System/ while the [data/README.md](data/README.md)
covers the KPI list itself and the literature behind it.

## Design

The workbook is structured as follows:

- Row fill colour encodes the hierarchy level (Level 1 = pale green through Level 4 =
  bright green, Level-5 raw metrics = grey).
- The Metrics List sheet uses `=HYPERLINK(...)` formulas in the *Parent Metrics* column for
  in-file navigation.

The repository model is:

1. **The `.xlsx` is canonical.** It lives at `data/KPI List.xlsx`, and git tracks it as a
   binary file. All edits happen in the workbook.
2. **A deterministic text snapshot is generated:** one tab-separated file per sheet
   under `snapshot/`. A pre-commit hook regenerates it on every commit. These are normal
   diff-able text files and GitHub PRs show cell-level changes here. This is the primary
   review surface.
3. **A git `textconv` diff driver** covers `*.xlsx`, so `git diff` and `git log -p` on the
   workbook render readable text on the command line.

The snapshot captures cell values and formulas, so hyperlink-target changes show up. Fill
colours are the exception. A change to a row's hierarchy level still shows, because the
`Level` column holds that value as text. If you rely on colour without updating the Level
column, that change will not appear in the diff.

## Setup

To reproduce on a fresh clone:

```powershell
# Point git at the versioned hook and register the textconv diff driver.
git config core.hooksPath .githooks
git config diff.xlsx.textconv "uv run tools/scripts/xlsx_to_text.py"
git config diff.xlsx.binary true

# Generate the snapshot (uv fetches openpyxl on first run).
uv run tools/scripts/export_snapshot.py
```

> `.git/config` holds `core.hooksPath`, `diff.xlsx.textconv` and `diff.xlsx.binary`. Git
> does **not** commit that file, so each clone must run the `git config` lines above once.

[UV](https://docs.astral.sh/uv/) runs the Python. Every script under `tools/scripts/`
declares its dependencies in a PEP 723 header, so `uv run` provisions them on first use.
The repo carries no `requirements.txt` and no virtual environment to activate.

## Daily workflow

1. Edit `data/KPI List.xlsx` in Excel, or through `tools/scripts/xlsx_edit.py`. Do *not*
   edit the workbook with a plain openpyxl `load`/`save`: it drops the anchored Top-Level
   diagram and rewrites every package part. See [docs/TOOLING.md](docs/TOOLING.md).
2. Stage and commit. The pre-commit hook regenerates `snapshot/` and adds it to the commit,
   so the review surface never drifts from the workbook.
3. Review the change in your editor. The `snapshot/*.tsv` diffs show exactly which cells
   changed. Install extensions such as `rainbow-csv` & `gc-excelviewer` as helper tools.
4. For a terminal view of the workbook itself, run `git diff -- "data/KPI List.xlsx"`. The
   textconv driver renders it as text.

## Do not

- Do not convert the workbook to CSV as the source of truth, and do not regenerate the
  `.xlsx` from text. Either one drops the level colours and hyperlinks.
- Do not edit files under `snapshot/` by hand. The tooling generates them.
- Do not hand-edit the Metrics List sheet. `sync_metrics_list.py` regenerates it from the
  domain sheets.

## Where to look next

| Document | What it covers |
|---|---|
| [AGENTS.md](AGENTS.md) | The conventions that prevent silent data loss, plus the common command list. Written for humans and coding agents alike. |
| [docs/TOOLING.md](docs/TOOLING.md) | The scripts: programmatic editing, the Metrics List sync, the site and visualization builds, company-specific workbooks. |
| [docs/USER_MANUAL.md](docs/USER_MANUAL.md) | Part A for practitioners filling the system in for a product, Part B for editors changing KPI definitions in Excel. |
| [docs/KPI_System_Understanding.md](docs/KPI_System_Understanding.md) | System-understanding notes: the model, the conventions and the known issues. |
| [data/README.md](data/README.md) | The literature corpus behind the KPI definitions, and why git does not track it. |

`tools/scripts/build_manual_pdf.py` renders the user manual to `output/USER_MANUAL.pdf`,
the distribution format.

## Layout

```
.
├── data/
│   ├── KPI List.xlsx        # canonical workbook (tracked as binary)
│   ├── literature/          # curated source PDFs (local only, gitignored)
│   └── others/              # per-company scope files (local only, gitignored)
├── snapshot/                # generated, committed: the review surface
│   ├── _sheets.txt
│   └── <one .tsv per sheet>
├── output/                  # derived workbooks, catalog JSON, manual PDF (gitignored);
│                            #   the master visualization HTML is committed as an example
├── reviews/                 # literature cross-check and description-audit reports
├── docs/                    # user manual, tooling reference, system-understanding notes
├── tools/
│   ├── scripts/             # workbook and build utilities (self-contained uv run scripts)
│   ├── templates/           # HTML templates for the manual and the visualization
│   └── kpi-engine/          # KPI calculation engine (Python package, carries its own tests)
├── AGENTS.md                # conventions brief for humans and coding agents
├── .claude/agents/          # the three review briefs, packaged for Claude Code
├── SETUP_INSTRUCTION.md     # the original bootstrap brief (superseded, kept as history)
├── .github/workflows/       # builds and publishes the site on every push to main
├── .githooks/pre-commit
├── .vscode/extensions.json
├── .gitattributes
└── .gitignore
```
