# kpi-engine

Calculation engine for the product-sustainability KPI workbook. It reads the workbook
(`data/KPI List.xlsx`), computes every score bottom-up, and prints a per-domain breakdown
plus the composite **Sustainability** score.

## How a company uses it

1. Open `data/KPI List.xlsx` in Excel and fill the right-hand **input block** on the five
   domain sheets:
   - **Value** — the measured number for each grey `Data? = x` leaf row.
   - **Target Min / Target Max** — the normalization bounds for each normalized score.
   - **Reference Value** — the previous-version / industry comparator for the few ratios
     that compare against one (EN12, EN13, EN31, EN42, R32).
   - **Weight** — already seeded with equal defaults; override to change emphasis.
2. Run the engine.

Nothing is entered outside Excel.

## Running

```bash
# from the repo root
uv run --project tools/kpi-engine kpi-engine compute "data/KPI List.xlsx"
uv run --project tools/kpi-engine kpi-engine compute "data/KPI List.xlsx" --json out.json
uv run --project tools/kpi-engine kpi-engine validate "data/KPI List.xlsx"   # structural checks
uv run --project tools/kpi-engine kpi-engine catalog "data/KPI List.xlsx" --json catalog.json
```

## Catalog export (for a frontend)

`catalog --json` emits the **descriptive** KPI catalogue — what each KPI *is*, how it relates
to the others (parent/child id links), its formula, unit, lifecycle stages, and resolved
literature references. It is the read-only projection a web frontend consumes to display the
KPIs instead of the spreadsheet. It carries **no** company inputs or computed scores (no
Value/Weight/Target/status) — that is the `compute` command's job.

Shape: a flat, normalized `id -> kpi` map plus a `label -> reference` bibliography, with
camelCase keys for direct JS use. The frontend builds whatever tree/view it wants and resolves
each `references` code against the `references` map. Archived (intentionally-dormant) rows are
included with `"archived": true` so the UI can show or hide them. Master workbook only.

```jsonc
{
  "meta":   { "source": "KPI List.xlsx", "kpiCount": 266, "referenceCount": 101 },
  "domains":[ { "id": "EN", "name": "Environmental Impact", "scoreId": "EN0" } ],
  "kpis":   { "EN11": { "id": "EN11", "domain": "EN", "level": 3, "name": "...",
                        "underlying": ["EN1-4","EN1-5"], "parents": ["EN1"],
                        "formula": "...", "references": ["..."],
                        "isRawDataPoint": false, "archived": false } },
  "references": { "IFRS S2": { "title": "...", "description": "...",
                               "type": "Industry Standard", "link": "https://..." } }
}
```

## How it computes

| Strategy | Computation |
|---|---|
| `RAW_VALUE_STRATEGY` | the **Value** cell, taken as-is |
| `NORMALIZED_RATIO_STRATEGY` | an encoded intermediate (`src/kpi_engine/formulas.py`) over child values / Reference Value, then `clamp((x − Min)/(Max − Min), 0, 1)` |
| `WEIGHTED_AVERAGE_STRATEGY` | `Σ(wᵢ·sᵢ)/Σ(wᵢ)` over children that have a score (missing children drop out and the present weights renormalize) |
| `WEIGHTED_RATIO_STRATEGY` | same weighted form |
| `SUM_AGGREGATE_STRATEGY` | total of child values (a cost/quantity roll-up, e.g. total Repair Cost = sum of its line items) |

Each KPI resolves to **OK** (a value), **MISSING** (an input/parameter was absent — e.g. a
leaf has no Value, or a normalized row has no Min/Max), or **ERROR** (structurally broken,
e.g. Max == Min). A score derived from an uncertain formula encoding is flagged
`(unverified)`; those are the deferred one-by-one review worklist (`needs_review` in
`formulas.py`).

## Known limitations

- ~11 phase-emission / water-phase ratios (e.g. `EN131`, `EN441`) and `C231` are encoded
  best-effort and flagged `needs_review`.
- The engine computes faithfully per the workbook's declared strategy. A few impact/index
  scores still average raw units instead of normalizing (`EN6`, `EN7`, `EN8`, `EN9`, `C4`,
  `C5`, `S34`) and so produce out-of-range numbers — deferred to the formula review; the
  engine surfaces these rather than hides them.
- Read-only: it does not write scores back into the `.xlsx`.

## Development

```bash
cd tools/kpi-engine
uv run --extra dev pytest      # tests
uv run --extra dev mypy src    # strict type check
```
