# KPI System — Understanding & Crosscheck

> **Purpose of this document.** This is *not* the user manual. It is my (Claude's)
> structured understanding of the KPI workbook (`data/KPI List.xlsx`), written so you can
> verify or correct it **before** the manual is drafted. Please mark anything wrong,
> incomplete, or imprecise. The manual will be built from whatever this document settles on.
>
> **Confirmed scope decisions** (driving the eventual manual): two audiences in separated
> sections (practitioners *using* the system + maintainers *editing* it); the **Excel
> workbook only** (no external calculation engine); the workbook treated as a blank
> **master template/catalog**; authored in Markdown, distributed as PDF.

---

## 1. What the system is

A catalogue/specification of **product-focused** sustainability KPIs — explicitly *not*
organization-wide. It defines, for each indicator: a description, objective, formula, unit,
aggregation strategy, lifecycle stages, and the standards it is based on. The system rolls
individual data points bottom-up into sub-scores, then domain scores, then one composite
**Sustainability** score for a single product line.

The workbook is a **master template**: the structural definitions are filled in, but the
per-company inputs — raw data values, **Weight**s, and most **min/max reference values** —
are intentionally left blank. A company supplies those for its own product (in the planned
company-specific system); the master itself stays generic.

---

## 2. The five domains and the ID scheme

| Domain sheet | Prefix | Level-1 score |
|---|---|---|
| Environmental Impact | `EN` | `EN0` Environmental Impact Score |
| Economic Viability | `EC` | `EC0` Economic Viability Score |
| Circular Efforts | `C` | `C0` Circular Efforts Score |
| Resource Efficiency | `R` | `R0` Resource Efficiency Score |
| Social Impact | `S` | `S0` Social Impact Score |

Above all five sits the **Sustainability** composite (defined in the *Top-Level* sheet).

**ID pattern within a domain** (using Environmental as the example):
- `EN0` — domain score (Level 1)
- `EN1`, `EN2`, … — sub-scores (Level 2)
- `EN11`, `EN12`, … — sub-sub-scores (Level 3)
- `EN131`, `EN132`, … — Level 4
- `EN1-1`, `EN1-2`, … — **raw data points (Level 5)** — the leaf inputs a user must supply

> ⚠️ **Naming-collision note for the manual:** the Resource Efficiency IDs `R0`–`R9` look
> identical to the **R-principles** `R0`–`R9` (Refuse, Rethink, Reduce…) defined in the
> Overview. They are *different namespaces*. The manual should call this out so users don't
> confuse "R2 = Reduce (a circular-economy principle)" with "R2 = a Resource Efficiency
> sub-score."

---

## 3. The hierarchy (levels) and how scores aggregate

Each domain sheet holds the full tree. The **`Level`** column (1–5) records the depth, and
the **row fill colour** encodes the same thing visually (Level 1 = pale green … Level 4 =
bright green; **Level-5 raw metrics = grey**).

```
Sustainability  (Top-Level sheet, composite of the 5 domains)
└─ EN0  Environmental Impact Score             Level 1   (domain score)
   └─ EN1 Product Carbon Footprint Score        Level 2   (sub-score)
      └─ EN14 Lifecycle Phase Emission           Level 3
         └─ EN131 Sourcing Emission Ratio         Level 4
            └─ EN1-1 Scope 1 – Direct Emissions    Level 5  ← raw data point (Data? = x, grey)
```

- **Aggregation is bottom-up.** Raw data points (Level 5) feed the score that lists them in
  its **Underlying Metrics**; that score feeds its parent (its **Parent Metrics**), and so
  on up to the domain score and finally the Sustainability composite.
- **Underlying Metrics** = the children that feed *into* this row. **Parent Metrics** = the
  rows this one feeds *up into* (note: in *Metrics List* this same column carries a navigation
  hyperlink instead of a plain ID — see §6).
- Most scores are normalized to a **0–1** range (1 = best). Raw data points carry real-world
  units (kg CO₂ eq., kWh, m³, €, #, etc.).

### The four Calculation Strategies (counts across the workbook)

| Strategy | Count | Meaning |
|---|---|---|
| `RAW_VALUE_STRATEGY` | 294 | A leaf data point; the value is taken as-is (the user-supplied input). |
| `NORMALIZED_RATIO_STRATEGY` | 67 | Compute a ratio/performance, then min-max normalize to 0–1 using the row's reference Min/Max. |
| `WEIGHTED_AVERAGE_STRATEGY` | 50 | Weighted average of the children's (already-normalized) scores. |
| `WEIGHTED_RATIO_STRATEGY` | 3 | A weighted ratio variant. |

*(Counts are across all sheets including Metrics List, so the raw-value count is inflated by
the mirror; the relative picture holds.)*

### Weights (what they are, and the sum-to-1 rule)

In every `WEIGHTED_AVERAGE`/`WEIGHTED_RATIO` score, each child contributes proportionally to
its **Weight**. **No default weights are shipped** — the column is blank on purpose; the
company sets its own. The manual must therefore (a) *explain to a reader who may not know
what a weight is* that it controls how much each sub-metric counts toward its parent score,
and (b) state the rule that **the weights of all children under one parent should sum to 1**
(so the parent stays on the same 0–1 scale).

### Missing-data behaviour (from the Overview's "How It Works")

The system is designed to score on **whatever data is available**: if a branch has no usable
data (e.g. no Social Impact metrics could be calculated), its **weight is effectively set
to 0** so it drops out of the average rather than dragging the parent toward zero. Weights
therefore have a *planned* value (set in advance) and an *actual* value (re-derived when data
is missing). *(Stated descriptively only — the calculation engine itself is out of scope.)*

---

## 4. The nine sheets

| # | Sheet | Role |
|---|---|---|
| 1 | **Overview** | Orientation: Goal, Structure, "How It Works"; the R0–R9 R-principles table; a Glossary (EPD, DPP, ESRS, SASB, GRI, LCA, LCC, PLC, Normalized, Inflow, Outflow). |
| 2 | **Top-Level** | Prose definitions (KPI / Description / Purpose) of the **Sustainability** composite and the five domain KPIs. No hierarchy columns. |
| 3 | **Environmental Impact** | Domain sheet — full `EN` hierarchy. |
| 4 | **Economic Viability** | Domain sheet — full `EC` hierarchy. |
| 5 | **Circular Efforts** | Domain sheet — full `C` hierarchy. |
| 6 | **Resource Efficiency** | Domain sheet — full `R` hierarchy. |
| 7 | **Social Impact** | Domain sheet — full `S` hierarchy. |
| 8 | **Metrics List** | **Generated** flat mirror of only the Level-5 raw data points, with hyperlink navigation back to the domain sheets. Do not hand-edit. |
| 9 | **References** | Bibliography. The **Label** column is the citation code used by the `Reference` column on every KPI row. |

---

## 5. Domain-sheet columns (18)

| Column | Meaning |
|---|---|
| **#** | The KPI/metric ID (e.g. `EN1-4`). |
| **Indicator Name** | Human-readable name. |
| **Description** | What it measures. |
| **Objective / Goal** | Why it matters / what decision it supports (`None` on raw rows). |
| **Underlying Metrics** | Child IDs that feed into this row (`None` on leaves). |
| **Parent Metrics** | Parent IDs this row feeds up into. *(On Metrics List this column holds a navigation hyperlink instead of a plain ID.)* |
| **Potential Reference Values** | What benchmark inputs the formula needs (e.g. "Target Value: Min, Max", "Industry Average"). Mostly the *labels*, not filled-in numbers. |
| **Unit** | Unit of the value (`%` for normalized scores; real units on raw rows). |
| **Formula** | How the value is computed. |
| **Reference** | Standards code(s) → resolve against References **Label**. |
| **Level** | Hierarchy depth 1–5. |
| **Data?** | `x` marks a **raw data point the user must supply** (Level 5). |
| **Data Source** | Where the raw value comes from (commonly `LCA`). |
| **Product Life Cycle Stages** | Stage codes `P/S/M/D/U/E` (see §8), or `All`. |
| **Calculation Strategy** | One of the four strategies (§3). |
| **Example Value** | Sample value for illustration (sparsely populated). *(Header is "Example Values" on some sheets.)* |
| **Weight** | Planned aggregation weight — **currently empty everywhere** (user-supplied per company). |
| **Comment** | Notes / threaded-comment anchors. |

---

## 6. Domain sheets vs. Metrics List (the data model)

- **Domain sheets are the source of truth.** They hold the full hierarchy — both the
  aggregate scores *and* the Level-5 raw data points.
- **Metrics List is a generated flat mirror** of only the raw data points (`Data? = x`). It
  exists as a convenient single list of "everything a user must measure."
- Its **Parent Metrics** column uses `=HYPERLINK("#'<Domain>'!…", "…")` formulas for
  click-through navigation back into the domain hierarchy.
- **Rule:** edit a raw metric *only in its domain sheet*, then regenerate Metrics List
  (`tools/scripts/sync_metrics_list.py`). Never hand-edit Metrics List.

> **Maintainer constraint — confirmed by you:** the maintainer audience will **only have
> the Excel file**, *not* this git repository. So the maintainer section must be written
> entirely in terms of editing **inside Excel** — it will **not** mention git, the
> `snapshot/` review surface, `xlsx_edit.py`, or `sync_metrics_list.py`. Two consequences
> the manual must handle:
> 1. **Threaded comments are fragile**, but that risk comes from programmatic openpyxl
>    round-trips — editing directly **in Excel is the safe path**, so the manual simply
>    instructs maintainers to edit in Excel (no tooling caveat needed for them).
> 2. **Keeping Metrics List in sync.** ✅ *Resolved:* the Excel-only maintainer must
>    **manually update the matching Metrics List row by hand** whenever they change a raw
>    (`Data? = x`) metric in a domain sheet. There is no repo-owner regeneration after
>    hand-off, so the manual gives them an explicit "also edit the same row in Metrics List"
>    step (matched by ID), and reminds them the navigation hyperlink column is not theirs to
>    touch.

---

## 7. References sheet

Columns: **Title, Description, Label, Type, Link, Comment**. The **Label** (e.g. `IFRS S2`,
`SASB-RT-CP`, `ISO 14067`, `GRI 306-3`, `ESRS E1-6`) is the code that KPI rows cite in their
**Reference** column. `Type` classifies the source (e.g. *Industry Standard*). Curated source
PDFs live under `data/literature/` in per-standard subfolders.

---

## 8. Glossary terms the manual must define

- **R-principles (R0–R9):** Refuse, Rethink, Reduce, Reuse, Repair, Refurbish, Remanufacture,
  Repurpose, Recycle, Recover — the circular-economy hierarchy.
- **Product Life Cycle (PLC) stage codes:** `P` Planning · `S` Sourcing · `M` Manufacturing ·
  `D` Distribution · `U` Use · `E` End of Life · `All` = applies to every stage.
- **Standards/frameworks:** EPD, DPP, ESRS, SASB, GRI, IFRS, ISO 14xxx/59xxx, EN 15804, PSILCA…
- **Methodology terms:** **Normalized** (min-max to 0–1), **Inflow / Outflow**, **LCA**
  (Life Cycle Assessment — common data source), **LCC** (Life Cycle Cost — monetary data).

---

## 9. Intended workflow order (for the practitioner section) — **confirmed**

1. **Overview** — orient (goal, structure, R-principles, glossary).
2. **Top-Level** — understand the composite *Sustainability* score and the five domains.
3. Drill into a **domain sheet** top-down: domain score (L1) → sub-scores (L2) → … →
   raw data points (L5, `Data? = x`).
4. Identify the **raw metrics to supply** — the grey `Data? = x` rows; the flat **Metrics
   List** is the convenient checklist.
5. **Gather the data first**, per metric, using **Unit**, **Data Source**, and
   **Product Life Cycle Stages** for guidance.
6. **Then** set per-company **Weights** (none are provided by default; under each parent the
   children's weights should **sum to 1**) and **min/max reference values**.
7. Consult **References** (`Reference` code → References **Label**) for the standards basis.

---

## 10. Defects / inconsistencies I found (for you to decide / fix)

1. **EPD / DPP columns do not exist.** ✅ *Confirmed by you as a defect to remove.* The
   Overview glossary states indicators complying with EPD/DPP "are marked under the EPD/DPP
   column," but no such columns exist in any sheet (EPD/DPP appear only inside description
   text). This is leftover from a previous version. **Action: you will remove the EPD/DPP
   column references from the Overview glossary.** The manual will be written to the
   corrected state (EPD/DPP described as concepts only).
2. **Column-name drift between domain sheets and Metrics List.** ✅ *Resolved.* Metrics List
   formerly labelled two columns *Superior Metrics* and *Source*; both were renamed to match
   the domain sheets (*Parent Metrics*, *Data Source*), so all nine sheets now use one naming.
   On Metrics List, *Parent Metrics* still holds the navigation hyperlink.
3. **"Example Value" vs "Example Values"** header differs between sheets (Environmental uses
   singular; Circular/Resource use plural). Minor; flagging in case you want it unified.
4. **`R0`–`R9` namespace collision** between Resource Efficiency IDs and the R-principles
   (see §2 note).

---

## 11. Open questions still worth your confirmation

- ~~Metrics List sync for the Excel-only maintainer~~ — resolved: maintainers **manually
  update the matching Metrics List row by hand** (no repo-owner regeneration after hand-off).
- ~~§6 maintainer depth~~ — resolved: maintainers have **Excel only**; no git/tooling content.
- ~~Weights model~~ — resolved: no default weights; explain what weights are and that children
  under a parent should **sum to 1**; describe missing-data behaviour descriptively only.
