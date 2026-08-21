# Product Sustainability KPI System: user manual

*A guide to the `KPI List` workbook: a product-focused sustainability KPI catalogue.*

---

## Before you start

### What this system is

This workbook is a catalogue of sustainability Key Performance Indicators (KPIs) for a single
product line. It is *product-focused*, not organisation-wide: every indicator describes some aspect
of how sustainable one product is across its life cycle.

The indicators form a tree. One number sits at the very top, the Sustainability score. Five domains
feed it:

| Domain | What it covers |
|---|---|
| Environmental Impact | The product's ecological footprint. |
| Economic Viability | Its financial health and cost-effectiveness. |
| Circular Efforts | How well it supports a circular economy (reuse, repair, recycling, and so on). |
| Resource Efficiency | How efficiently it uses materials and energy. |
| Social Impact | The social value it creates. |

Each domain breaks down into sub-scores, and those break down further. At the bottom sit the raw
data points: the actual measurements that someone must supply, such as kilograms of CO₂, kWh of
energy, or euros. Those numbers flow back up the tree into one composite Sustainability score.

### Who this manual is for

The manual has two separate parts. **Part A, using the KPI system,** is for practitioners. They read
the catalogue to work out what data it needs, then supply that data for their product. Part A
assumes no technical background. **Part B, maintaining the workbook,** is for editors. They add or
change KPI definitions inside the Excel file itself.

If you only need to fill the system in for your product, Part A is all you need.

### This is a master template

The workbook you have is a blank master template, a generic catalogue. The structure is already
there: names, descriptions, formulas, units, and standards. So are neutral default weights, an equal
1/N share under each parent (see A.5). Two kinds of cells stay deliberately empty, and each company
supplies them per product:

| Empty cells | What goes in them |
|---|---|
| Most min/max reference values | The benchmarks a normalised score compares against. |
| Raw data | The actual measured values for your product. |

Empty cells in those areas are **not errors**. They mean "someone must still supply this." The
pre-filled weights likewise expect an override per company. Each company fills these in for its own
product, and the master itself stays generic.

### How to read this manual

Read Part A top to bottom the first time. Its sections follow the order you will actually work in.
After that, use it as a reference. The [Glossary](#a8-glossary) explains the codes and abbreviations
you will meet, and the [Appendix](#appendix) has a one-page column reference.

---

# Part A: using the KPI system (for practitioners)

## A.1 The nine sheets and what each is for

The workbook has nine tabs. Read them roughly in this order:

| # | Sheet | What it is for |
|---|---|---|
| 1 | **Overview** | Orientation. States the goal and the structure, explains "How It Works", lists the R-principles (R0–R9), and gives a glossary of standards and terms. Start here. |
| 2 | **Top-Level** | Plain-language definitions of the composite **Sustainability** score and the five domain scores. Contains only descriptions and purposes. |
| 3 | **Environmental Impact** | Domain sheet: the full `EN` tree. |
| 4 | **Economic Viability** | Domain sheet: the full `EC` tree. |
| 5 | **Circular Efforts** | Domain sheet: the full `C` tree. |
| 6 | **Resource Efficiency** | Domain sheet: the full `R` tree. |
| 7 | **Social Impact** | Domain sheet: the full `S` tree. |
| 8 | **Metrics List** | A single flat **checklist of every raw data point you must supply**, with clickable links back into the domain sheets. |
| 9 | **References** | The bibliography. The **Label** column holds the short citation codes that the KPI rows cite in their **Reference** column. |

The five domain sheets (3–7) are where the real detail lives. Each one contains the complete
hierarchy for its domain: both the aggregate scores and the raw data points beneath them.

## A.2 The hierarchy

### The five levels

Every KPI sits at one of five levels, shown in the Level column (1 to 5). The level tells you how
deep in the tree the row is:

| Level | What it is | Example |
|---|---|---|
| 1 | **Domain score**: the top of one domain | `EN0` Environmental Impact Score |
| 2 | **Sub-score** | `EN1` Product Carbon Footprint Score |
| 3 | **Sub-sub-score** | `EN14` Lifecycle Phase Emission |
| 4 | **Deeper score** | `EN131` Sourcing Emission Ratio |
| 5 | **Raw data point**: a leaf input you must supply | `EN1-1` Scope 1 – Direct Emissions |

Above all five domain scores sits the Sustainability composite, defined in the *Top-Level* sheet.

### Row colours

The rows carry a colour for their level. Higher-level scores run from paler to brighter green as you
go down, and the **Level-5 raw data points are grey**. The grey rows are the ones you supply numbers
for. (In the *Metrics List* sheet the raw rows are *not* greyed, because that whole sheet is raw
data points.)

### The ID scheme

Each domain uses a letter prefix, and the IDs encode the tree:

| Domain | Prefix | Level-1 score |
|---|---|---|
| Environmental Impact | `EN` | `EN0` |
| Economic Viability | `EC` | `EC0` |
| Circular Efforts | `C` | `C0` |
| Resource Efficiency | `R` | `R0` |
| Social Impact | `S` | `S0` |

Within a domain (using Environmental as the example):

| ID pattern | What it is |
|---|---|
| `EN0` | Domain score (Level 1) |
| `EN1`, `EN2`, and so on | Sub-scores (Level 2) |
| `EN11`, `EN12`, and so on | Level 3 |
| `EN131`, `EN132`, and so on | Level 4 |
| `EN1-1`, `EN1-2`, and so on | **Raw data points** (Level 5), written with a hyphen |

> **A naming collision to watch for**. In the Resource Efficiency domain the IDs `R0` to `R9` look
> *identical* to the R-principles `R0` to `R9` defined on the Overview sheet. Take `R2`. As a
> row ID it is a Resource Efficiency sub-score. As an R-principle it is *Reduce*, a
> circular-economy principle. **They are completely different things**. When you see "R2," check
> the context: a row ID in the Resource Efficiency sheet, or a principle in the glossary.

### Aggregation is bottom-up

The system makes numbers flow upward:

```
Sustainability                         (Top-Level: composite of the 5 domains)
└─ EN0   Environmental Impact Score     Level 1   (domain score)
   └─ EN1   Product Carbon Footprint Score   Level 2
      └─ EN14  Lifecycle Phase Emission       Level 3
         └─ EN131 Sourcing Emission Ratio     Level 4
            └─ EN1-1 Scope 1 – Direct Emissions   Level 5  ← raw data point (Data? = x, grey)
```

You supply the raw data points (Level 5). Each score lists the children that feed into it, in its
Underlying Metrics column. Those children combine into the score, the score feeds its parent, and so
on up to the domain score and finally the Sustainability composite. You read the tree top-down to
understand it, but it calculates bottom-up.

> **The domains are not fully separate**. Several domains share a few raw inputs. For example
> *Total produced units* (in Resource Efficiency) also feeds the Economic *CO₂ Cost Performance*
> and the Environmental *Water Footprint Intensity*. So the structure is a network of five trees
> that share leaves: a metric can feed more than one parent, sometimes in another domain. This is
> intentional, because the same measurement legitimately matters to several aspects of
> sustainability. Enter such a shared input once, in its home domain.

## A.3 How to read a domain-sheet row

Each domain sheet (Environmental, Economic, Circular, Resource, Social) has the same 22 columns.
Here is what each one means.

| Column | What it tells you |
|---|---|
| **#** | The KPI/metric ID, e.g. `EN1-4`. This is how rows refer to each other. |
| **Indicator Name** | The human-readable name. |
| **Description** | What the indicator measures. |
| **Objective / Goal** | Why it matters / what decision it supports. Shows `None` on raw data rows. |
| **Underlying Metrics** | The **child** IDs that feed *into* this row. `None` on a leaf (raw) row. |
| **Parent Metrics** | The **parent** IDs this row feeds *up into*. On the *Metrics List* sheet this column holds a clickable navigation link back to the domain row rather than a plain ID. |
| **Potential Reference Values** | What benchmark inputs the formula needs, e.g. "Target Value: Min, Max" or "Industry Average." These are mostly the *labels* of inputs you must provide, not filled-in numbers. |
| **Unit** | The unit of the value. Scores are `%` (a normalised 0–1 fraction shown as a percentage). Raw data rows carry real units, such as kg CO₂ eq., kWh, m³, or €. |
| **Formula** | How the value is computed. |
| **Reference** | The standards code(s) this row is based on. Look the code up in the **References** sheet's **Label** column. |
| **Level** | Hierarchy depth, 1–5 (see A.2). |
| **Data?** | An `x` here marks a **raw data point you must supply** (always a Level-5 row, shown grey). |
| **Data Source** | Where the raw value typically comes from (commonly `LCA`). |
| **Product Life Cycle Stages** | Which life-cycle stage(s) the row applies to: codes `P/S/M/D/U/E`, or `All` (see [Glossary](#a8-glossary)). |
| **Calculation Strategy** | One of six strategies (see A.4). |
| **Example Value** | A sample value for illustration. Sparsely filled. *(Header reads "Example Value" on the Environmental, Economic and Social sheets, and "Example Values" on the Circular and Resource sheets, the same column under a different spelling.)* |
| **Weight** | The aggregation weight (see A.5). **Pre-seeded with equal (1/N) defaults** under each weighted parent; override per company. |
| **Comment** | Notes and clarifications. |
| **Target Min** | The raw value that should score **0** (the worst case). Per-company, **empty by default**. |
| **Target Max** | The raw value that should score **1** (the best case). Per-company, **empty by default**. For a *lower-is-better* metric (an intensity, a time, a cost), the best outcome is the *smaller* number, so you set **Target Min > Target Max**. See the [Glossary](#a8-glossary) "Normalized" note. |
| **Value** | The measured number you supply for a raw data point (the `Data? = x` rows) and for self-normalising leaves. **Empty by default**. |
| **Reference Value** | A benchmark or prior-period figure that some normalised rows compare against (e.g. last reporting period's value). **Empty by default**. |

### A worked example: the carbon-footprint branch

Take the carbon-footprint branch of the Environmental sheet as a concrete read-through.

`EN1` Product Carbon Footprint Score sits at Level 2. Its *Underlying Metrics* are `EN11, EN12,
EN13, EN14`, and its *Parent Metrics* is `EN0`. Strategy: `WEIGHTED_AVERAGE_STRATEGY`.

`EN14` Lifecycle Phase Emission sits at Level 3. *Underlying* `EN131` to `EN135`, *Parent* `EN1`.

`EN131` Sourcing Emission Ratio sits at Level 4. *Underlying* `EN1-1, EN1-2, EN1-3`, *Parent*
`EN14`. Strategy: `NORMALIZED_RATIO_STRATEGY`, applied to life-cycle stage `S` (Sourcing).

<!-- plain-lint-disable en_dash_as_dash -->
`EN1-1` Scope 1 – Direct Emissions sits at Level 5 (grey, Data? = x) and is a raw input. *Unit* kg
CO₂ eq. *Data Source* `LCA`. *References* `ESRS E1-6`, `IFRS S2`, `SASB-RT-CP-110a.1`. This is one
of the numbers you supply.

Read it from the bottom. You measure `EN1-1`, `EN1-2` and `EN1-3`. Those three feed `EN131`, and
`EN131` with its sibling phase ratios feeds `EN14`. `EN14`, together with `EN11` to `EN13`, feeds
`EN1`. `EN1` feeds `EN0`, and `EN0` feeds Sustainability.

## A.4 The six Calculation Strategies

Every row's Calculation Strategy column says how the engine produces its value. Six strategies
exist, and you only need to understand them conceptually:

| Strategy | In plain terms |
|---|---|
| **`RAW_VALUE_STRATEGY`** | A leaf data point. The value is the raw number you supply, taken as-is. These are the `Data? = x` rows. |
| **`NORMALIZED_RATIO_STRATEGY`** | Computes a ratio or performance figure, then *normalises* it onto the 0–1 scale using the row's Min and Max reference values (see "Normalized" in the [Glossary](#a8-glossary)). |
| **`WEIGHTED_AVERAGE_STRATEGY`** | Combines its children's (already-normalised) scores into a weighted average, using each child's **Weight**. A score: the result must land in 0–1. |
| **`WEIGHTED_RATIO_STRATEGY`** | A weighted-ratio variant of the above, used in only a few places. |
| **`SUM_AGGREGATE_STRATEGY`** | Adds up its children's values (it does **not** average or normalise them). Used for quantity/€ summation. E.g. *Total Investment Cost* is the sum of its cost lines. The result is a raw total, not a 0–1 score. |
| **`FORMULA_VALUE_STRATEGY`** | Produces a raw value from a small formula over its children that is not a plain sum. E.g. *Net Profit* = Revenue − (COGS + Operating + Lifecycle + EOL costs). Like a sum, the result is a raw quantity (not normalised), and it usually feeds a ratio higher up (Net Profit ÷ Investment gives ROI). |

The leaf rows are raw values. Above them, a row is either a score or a raw total. A score is a
normalised ratio, or a weighted average or ratio of its children's scores, and it always lands in
0–1. A raw total is a sum, or a formula value such as a difference. It carries real units such as
euros or kilograms, and it does not land in 0–1.

Score rows that combine children must stay within 0–1. The engine flags any that do not as an error.
That check catches a mis-tagged row, such as a raw total accidentally averaged as if it were a
score.

## A.5 Weights and the "sum-to-1" rule

### What a weight is

When a score combines several children, a weight says how much each child counts. A child with a
larger weight pulls the parent score toward its own value more strongly than a child with a smaller
weight. For example, if a domain considers carbon footprint twice as important as water footprint,
carbon gets the larger weight.

### Equal defaults come pre-filled, and you override them

The Weight column is **pre-seeded with equal defaults**. Every child of a weighted parent gets 1/N,
where N is that parent's number of children. So `EN0`'s eight children each get `0.125`, and `R0`'s
three each get `0.3333`. The last sibling absorbs any rounding, so each parent's children sum to
exactly 1. This neutral default means the system produces a score as soon as you open the workbook.
Each company then decides how much each sub-metric matters for its own product and overrides the
cells it cares about.

<!-- plain-lint-disable rule_of_three_phrases -->
Children of a parent that is **not itself a weighted average** (a normalized ratio, a sum, or a
formula) carry no weight. They feed a ratio or a raw total, not an average, so their Weight cell is
intentionally left blank and the engine never reads it.

### The sum-to-1 rule

Under any one parent, the weights of all its direct children **should add up to 1**. This keeps the
parent score on the same 0–1 (0–100%) scale as everything else. Take `EN0`, which has nine children,
`EN1` to `EN9`. Suppose you care only about the first three. Give those three weights that sum to 1,
such as 0.5, 0.3 and 0.2, and give 0 to the rest. Arbitrary numbers that do not add up will skew the
parent score.

### What happens when data is missing (described, not calculated)

The system scores on whatever data is available. Suppose a whole branch has no usable data, because
your product yields no Social Impact metric at all. That branch's weight then counts as 0, so it
drops out of the average instead of dragging the parent toward zero. A weight therefore has two
values. The *planned* value is the one you set in advance. The *actual* value is the one the engine
re-derives when data turns out to be missing.

> This section explains the missing-data behaviour only so you know why an empty branch will not
> unfairly penalise your score. The workbook itself holds the catalogue and the data. It does
> not perform the live computation. A separate calculation engine in the repository can compute
> the scores from a filled-in workbook. It also runs structural checks, including the
> band-direction warning noted under "Normalized". You do **not** need that engine to fill the
> workbook in, and this manual does not cover it.

## A.6 Looking up inputs and standards

### Metrics List: your checklist of inputs

This sheet is a single flat list of only the raw data points (`Data? = x`). That is everything
across all five domains that someone must measure. Use it as the master checklist of "what data do I
need to gather."

Each row in Metrics List mirrors the matching raw row from its domain sheet. Its **Parent Metrics**
column holds clickable hyperlinks back to the matching location in the domain sheet. Follow one to
see the surrounding context for any input.

### References: the standards behind each KPI

Many KPI rows cite a standard in their Reference column, e.g. `IFRS S2`, `ISO 14067`, `GRI 306-3`,
`ESRS E1-6`, `SASB-RT-CP`. To find out what a code means, go to the References sheet and match it
against the Label column. Each reference row gives a Title, Description, Type (e.g. *Industry
Standard*), and a Link.

So the flow starts at a code in a KPI's Reference column. Match that code in the References sheet's
Label column, which gives you the full source.

## A.7 The recommended workflow, step by step

Follow this order the first time you fill the system in for a product:

1. **Read the Overview sheet**. Orient yourself: the goal, the structure, the R-principles, and
   the glossary of standards and terms.
2. **Read the Top-Level sheet**. Understand the composite Sustainability score and what each
   of the five domains means.
3. **Pick a domain and work top-down**. Open a domain sheet. Read from the Level-1 score down
   through the sub-scores to the Level-5 raw data points. This shows you *why* the system needs
   each input and *where it fits*.
4. **Identify the raw inputs you must supply**. They are the grey `Data? = x` rows. The
   Metrics List sheet is the flat checklist of all of them. Use it, and click its hyperlinks
   to jump back to context when needed.
5. **Gather the data first**. For each input, use the Unit, Data Source (often `LCA`),
   and Product Life Cycle Stages columns. They tell you what to measure and where to get it.
   Collect the numbers *before* you worry about weights.
6. **Then set the per-company values**. Once the data is in, fill in the Weights and the
   Target Min / Target Max reference values that the normalised scores need. (None are
   provided, and under each parent the children's weights should **sum to 1**.)
   **Mind the direction**. For *lower-is-better* metrics (intensities, times, costs, reduction
   ratios) set **Target Min > Target Max**, or the score comes out inverted. See the
   [Glossary](#a8-glossary) "Normalized" note.
7. **Consult the References as needed**. To check the basis of any KPI, follow its Reference
   code to the References sheet's Label.

The key sequence to remember: **understand top-down, gather the data first, then set weights and
min/max**.

## A.8 Glossary

### R-principles (R0–R9): the circular-economy hierarchy

| Code | Principle | Meaning |
|---|---|---|
| R0 | Refuse | Avoid unnecessary products and materials. |
| R1 | Rethink | Innovate and redesign products for better sustainability. |
| R2 | Reduce | Minimise resource consumption and waste generation. |
| R3 | Reuse | Re-use a used product with minimal restoration effort. |
| R4 | Repair | Fix broken products to extend their lifespan. |
| R5 | Refurbish | Restore disposed products to good working condition. |
| R6 | Remanufacture | Disassemble and rebuild disposed components into a unit of (at least) original quality. |
| R7 | Repurpose | Use disposed components for a different purpose. |
| R8 | Recycle | Process disposed materials into secondary materials instead of discarding them. |
| R9 | Recover | Extract useful materials or energy from disposed waste. |

> **Namespace-collision warning (repeat)**. These R0–R9 *principle* codes are **not** the same as
> the `R0` to `R9` *row IDs* in the Resource Efficiency sheet. Always read by context.

### Product Life Cycle (PLC) stage codes

Used in the Product Life Cycle Stages column:

| Code | Stage |
|---|---|
| `P` | Planning |
| `S` | Sourcing |
| `M` | Manufacturing |
| `D` | Distribution |
| `U` | Use |
| `E` | End of Life |
| `All` | Applies to every stage |

### Standards and frameworks

| Code | What it is |
|---|---|
| **ESRS** | *European Sustainability Reporting Standards.* Reporting framework aligned with the EU Corporate Sustainability Reporting Directive (CSRD). |
| **SASB** | *Sustainability Accounting Standards Board.* Industry-specific standards for the ESG issues most likely to affect financial outcomes (used alongside IFRS S1). |
| **GRI** | *Global Reporting Initiative.* Reporting standard for economic, environmental and social performance. |
| **IFRS** | *International Financial Reporting Standards*, e.g. IFRS S2 for climate disclosures. |
| **ISO** | International standards, e.g. ISO 14067 (carbon footprint of products), ISO 14046 (water footprint), the ISO 14xxx environmental family, and ISO 59xxx (circular economy). |
| **EN 15804** | European standard for environmental product declarations of construction products. |
| **PSILCA** | A database for social life-cycle assessment. |

### Method terms

#### Normalized

*Min-max normalisation.* It transforms a value linearly onto the 0–1 range using a defined minimum
and maximum: `Normalized = (Value − Minimum) / (Maximum − Minimum)`, clamped to the 0–1 range. The
company sets the Min and Max in the Target Min / Target Max columns.

**Direction matters**. The system has no separate "higher/lower is better" switch. *Which bound is
larger* decides which way a row scores. The whole system reads **1 = good, 0 = bad**, so:

- **Higher-is-better** metrics cover most rows, such as shares, ratings and efficiency. The worst
  value is the Minimum and the best is the Maximum, so **Target Min < Target Max**. That is an
  ordinary ascending band.
- **Lower-is-better** metrics cover intensities, times, costs and reduction ratios. The best
  outcome is the *smaller* number, so you **invert the band**. Set Target Min to the worst (high)
  value and Target Max to the best (low) value, so that **Target Min > Target Max**. For example,
  take energy per unit, where 0 is ideal and 25 kWh/unit is the worst acceptable. Set **Target
  Min = 25, Target Max = 0**. A 5 kWh/unit product then scores 0.8, and a 20 kWh/unit one
  scores 0.2.

Setting an ordinary ascending band on a lower-is-better row scores it **backwards**, so the worst
product gets the highest score. The companion validation tool warns when a band's orientation
contradicts the metric's direction.

#### Other method terms

| Term | Meaning |
|---|---|
| Inflow | All of some quantity *entering* the process scope, e.g. total energy going into manufacturing. |
| Outflow | All of some quantity *leaving* the process scope, e.g. mass leaving the process as waste or by-product. |
| LCA | *Life Cycle Assessment.* A common data source for metric values, often produced with software such as OpenLCA or GaBi. |
| LCC | *Life Cycle Cost(ing).* A data source specifically for monetary data. |

---

# Part B: maintaining the workbook (for Excel editors)

This part is for editors who change the KPI definitions. **It assumes you work directly in the Excel
file**. That is the safe and supported way to edit this workbook.

## B.1 Edit directly in Excel

Make all changes by opening `KPI List.xlsx` in Excel and editing the cells. Editing in Excel
preserves the workbook's comments and structure correctly. No separate tooling or export step
applies. What you save in Excel is the workbook.

## B.2 The data model you edit

**The five domain sheets are the source of truth**. They hold the complete hierarchy for each
domain, both the aggregate scores and the Level-5 raw data points. Add or change a KPI on the domain
sheet.

**The Metrics List sheet is a flat mirror** of only the raw (`Data? = x`) data points. It serves as
a checklist, with navigation hyperlinks back to the domain sheets. Because it is a mirror, you must
**keep it consistent by hand** whenever you change a raw metric (see B.4).

## B.3 Adding or editing a KPI row (on a domain sheet)

When you add a new KPI or edit an existing one, keep the row internally consistent:

1. **ID (`#` column)**. Follow the domain's pattern. `<prefix>0` is the domain score, and
   `<prefix>1`, `<prefix>2` and so on are Level-2 sub-scores. Add another digit per level down
   (`EN11`, `EN131`), and write **raw data points with a hyphen** (`EN1-1`, `EN1-2`). Keep IDs
   unique within the domain.
2. **Level**. Set the Level column (1–5) to match the depth of the ID.
3. **Row colour**. Match the colour of existing rows at the same level. The green runs from paler
   to brighter as the level deepens, and Level-5 raw data points are **grey**. The easiest way is
   to copy the format of an existing row at the same level.
4. **Data? column**. Put an `x` **only** on Level-5 raw data points (the values a user supplies).
   Leave it blank on every score row.
5. **Fill `Underlying Metrics` and `Parent Metrics` consistently**. These two columns must agree
   across rows.
   - In the Underlying Metrics of a parent, list every child ID.
   - In the Parent Metrics of each child, list that parent's ID.
   - A leaf (raw) row has `Underlying Metrics = None`. A top domain score has `Parent Metrics =
     None`.
   - Example: `EN131`'s *Underlying Metrics* are `EN1-1, EN1-2, EN1-3` and its *Parent Metrics* is
     `EN14`. Correspondingly, each of `EN1-1/-2/-3` lists `EN131` among *its* parents, and `EN14`
     lists `EN131` among *its* underlying metrics. If you add or remove a child, update both
     ends.
6. **Fill the descriptive columns** (Indicator Name, Description, Objective/Goal, Unit, Formula,
   Calculation Strategy, Product Life Cycle Stages, Reference) to match the style of similar rows.
7. **Leave the per-company cells blank**. Weight, raw data values, and most min/max reference
   values stay empty in the master template. Each company fills those in, not you.

## B.4 The Metrics List sync rule (manual, by hand)

> **This is the rule most easily forgotten. Read it carefully**.

The Metrics List is a flat copy of the raw (`Data? = x`) rows. It does **not** update itself.
Therefore:

- **Change a raw (`Data? = x`) metric on a domain sheet, and you must update the matching row in
  the Metrics List sheet by hand**. This applies when you add, edit or remove one.
- **Match rows by their ID** (the `#` column). Copy across the same content you changed
  (Indicator Name, Description, Unit, Reference, Data Source, Product Life Cycle Stages, etc.) so
  the two stay identical.
- **Do not touch the navigation hyperlink column** in Metrics List (the Parent Metrics
  column, which there contains `=HYPERLINK(...)` formulas instead of plain parent IDs). That
  column is the click-through navigation back to the domain sheet. Leave it exactly as it is.
- If you add a new raw metric, add a matching row to Metrics List. If you remove one, remove its
  Metrics List row too.
- Score rows (anything *without* `Data? = x`) do **not** appear in Metrics List, so they need no
  mirror.

---

# Appendix

## Quick column reference

The five domain sheets share these 22 columns (left to right). The Metrics List sheet is a raw-row
checklist, so it mirrors only the first 18, under the same column names. It does **not** carry the
four per-company input columns: Target Min, Target Max, Value, and Reference Value.

| Column | Purpose | On the Metrics List sheet |
|---|---|---|
| **#** | Unique KPI/metric ID | *(same)* |
| **Indicator Name** | Human-readable name | *(same)* |
| **Description** | What it measures | *(same)* |
| **Objective / Goal** | Why it matters (`None` on raw rows) | *(same)* |
| **Underlying Metrics** | Child IDs feeding into this row | *(same)* |
| **Parent Metrics** | Parent IDs this row feeds into | holds a nav hyperlink, not a plain ID |
| **Potential Reference Values** | Benchmark inputs the formula needs | *(same)* |
| **Unit** | Unit of the value (`%` for scores, real units on raw rows) | *(same)* |
| **Formula** | How the value is computed | *(same)* |
| **Reference** | Standards code, looked up in References **Label** | *(same)* |
| **Level** | Hierarchy depth 1–5 | *(same)* |
| **Data?** | `x` = a raw data point to supply (Level 5) | *(same)* |
| **Data Source** | Where the raw value comes from (often `LCA`) | *(same)* |
| **Product Life Cycle Stages** | Stage codes `P/S/M/D/U/E` or `All` | *(same)* |
| **Calculation Strategy** | One of the six strategies | *(same)* |
| **Example Value** | Sample value (sparse) | *(same)* |
| **Weight** | Aggregation weight (pre-seeded equal 1/N defaults) | *(same)* |
| **Comment** | Notes | *(same)* |
| **Target Min** | Raw value scoring 0 (worst), empty by default | *(not in Metrics List)* |
| **Target Max** | Raw value scoring 1 (best), empty by default. Lower-is-better means Min > Max | *(not in Metrics List)* |
| **Value** | Measured number you supply (raw and self-normalising rows), empty by default | *(not in Metrics List)* |
| **Reference Value** | Benchmark or prior-period figure some rows compare against, empty by default | *(not in Metrics List)* |

> **Header spelling note**. The Environmental Impact, Economic Viability and Social Impact sheets
> head the sample-value column "Example Value". The Circular Efforts and Resource Efficiency
> sheets head it "Example Values". It is the same column either way.

---

*This manual is a derived document: it describes the `KPI List` workbook as it currently stands. If
the workbook changes, someone must update the manual to match. The distribution format is PDF,
converted from this Markdown source as a separate step.*
