# Min/Max sourcing guide for normalized KPIs

*Companion to `reviews/KPI-system-gaps.md` T1.2. Written 2026-06-25.*

Every `NORMALIZED_RATIO_STRATEGY` row turns a raw intermediate into a 0–1 score with

```
score = clamp( (intermediate − Target Min) / (Target Max − Target Min) , 0, 1 )
```

so a row cannot produce a score until its **Target Min** and **Target Max** (columns S and T
of each domain sheet) are set. The workbook shipped all of them blank with no guidance — the
"deepest usability gap". This guide says, for every one of the **81 normalized rows**, what Min
and Max mean and where the numbers come from.

## Two buckets

| Bucket | Count | Min/Max | Status |
|---|---|---|---|
| **Bounded ratio** — intermediate is already a 0–1 fraction, higher = better | 37 | **seeded to 0 / 1** | computes out of the box |
| **Benchmark** — intensity, financial ratio, rating scale, prior-period or LCIA factor | 44 | company-supplied | guidance below |

The 37 bounded-ratio rows were seeded `Min=0, Max=1` (round 7, `apply_review_round7.py`): for a
share like `renewable / total` or a complement like `1 − hazardous / total`, the ratio *is* the
0–1 score, so 0/1 is the correct identity default. A company may still override with a tighter
target band (e.g. score 0 below 50 % renewable, 1 at 90 %). The 44 benchmark rows below stay
blank because there is no safe universal default.

> **Direction of goodness.** The engine has **no direction flag** — every row runs the same
> `score = (value − Min)/(Max − Min)`. Direction is set entirely by *which of Min/Max you make
> larger*, so a *lower-is-better* row scores correctly only with an **inverted band (Min > Max)**.
> See **Setting the band direction** below before filling any benchmark row. (Bounded
> lower-is-better leaves dodge this by being written as a complement `1 − bad/total`; R12 and EN43
> used to lack that and now have it — "End-of-Life Recoverability" (2026-06-26) and "Water
> Independence Ratio" (2026-06-28).)

---

## Benchmark rows by source

### Setting the band direction

The engine normalizes every row identically and has **no "lower is better" flag**:

```text
score = clamp( (value − Min) / (Max − Min) , 0, 1 )
```

`Min` is simply *the raw value that should score 0*; `Max` is *the raw value that should score 1*.
Direction is decided entirely by **which one you make larger**:

| Metric direction | Band | Min (→ score 0) | Max (→ score 1) |
|---|---|---|---|
| **Higher is better** (shares, ratings, ROI, counts) | ascending, `Min < Max` | worst (low) value | best (high) value |
| **Lower is better** (intensities, times, costs, reductions) | **inverted, `Min > Max`** | worst (high) value | best (low) value |

For a lower-is-better row the span `(Max − Min)` is negative and the engine flips the score for
you — there is no other mechanism, so **Min must be the larger number.**

> **Worked example — `R222` Energy Intensity Performance (kWh/unit, lower is better).**
> Worst-acceptable = 25, best-in-class = 0. Set **Min = 25** (worst → 0), **Max = 0** (best → 1):
>
> - 5 kWh/unit (efficient): `(5 − 25) / (0 − 25) = 0.80`
> - 20 kWh/unit (wasteful): `(20 − 25) / (0 − 25) = 0.20`
>
> The efficient product scores higher, on the system's uniform **1 = good** scale. Set the band
> the *other* way (Min = 0, Max = 25) and it silently inverts — the wasteful product would score
> 0.80. The engine will **not** catch this: `validate` rejects only `Min == Max`, not a backwards
> direction. On a lower-is-better row, double-check that **Min > Max**.

(The 14 PEF / LCIA leaves below are a different construct — they normalize a characterised impact
against a per-capita factor rather than a worst/best band; see their section and
`reviews/PEF-factors.md`.)

### LCIA / PEF normalization factors (14 rows)

Each PEF impact leaf holds a **characterised result in its own unit**; normalize it against the
**EF (Environmental Footprint) per-capita normalization factor** for that impact category. Set
**Min = 0** and **Max = the EF normalization factor** (so the score is the share of one
person-equivalent). The factors are **not** in the workbook — they live in the JRC EF reference
package (Rec. (EU) 2021/2279 delegates them). See `reviews/PEF-factors.md`. EN6/EN7/EN8 then
weight-average these by the EF weighting factors (seeded as each leaf's Weight).

| ID | Name | Intermediate | Unit |
|---|---|---|---|
| `EN6-1` | Ozone depletion | `own` | kg CFC-11 eq |
| `EN6-2` | Respiratory inorganics | `own` | disease inc. / kg PM2.5 |
| `EN6-3` | Photochemical ozone formation | `own` | kg NMVOC eq. |
| `EN6-4` | Eutrophication: Terrestrial | `own` | mol N eq. |
| `EN6-5` | Eutrophication: Marine | `own` | kg N eq. |
| `EN6-6` | Eutrophication: Freshwater | `own` | kg P eq. |
| `EN6-7` | Acidification | `own` | mol H+ eq. |
| `EN6-8` | Ionizing radiation | `own` | kBq U-235 eq. |
| `EN7-1` | Human toxicity: cancer | `own` | CTUh |
| `EN7-2` | Human toxicity: non-cancer | `own` | CTUh |
| `EN7-3` | Ecotoxicity: freshwater | `own` | CTUe |
| `EN8-1` | Water Use Scarcity | `own` | m³ (AWARE-weighted) |
| `EN8-2` | Resource Use: Minerals & Metals | `own` | kg Sb eq. |
| `EN8-3` | Resource Use: Fossil | `own` | MJ |

### Intensity benchmarks — industry / sector data (5 rows)

These are physical or monetary **intensities** (per functional unit / per produced unit) — all
**lower is better**, so use the **inverted band** (see *Setting the band direction* above):
**Min = a sector benchmark or worst-acceptable intensity** (→ 0), **Max = best-in-class, often 0**
(→ 1). Note `Min > Max`. Sources: sector LCA databases (ecoinvent, GaBi), industry association
benchmarks, EPDs of comparable products, or an internal best-product baseline.

| ID | Name | Intermediate | Unit |
|---|---|---|---|
| `EN41` | Water Footprint Intensity | `water / units` | m³ / unit |
| `EN5` | Biodiversity Impact Score | `quality * landuse` | — |
| `EC5` | CO2 Cost Performance | `co2cost * (pcf / units)` | € / unit |
| `R222` | Energy Intensity Performance | `energy / units` | kWh / unit |
| `R223` | Logistics Energy Performance | `logistics / inflow` | ratio |

### Financial target bands — company targets (8 rows)

Profitability ratios that can exceed 1 — **higher is better**, ascending band (`Min < Max`). Set
**Min = the hurdle below which the activity scores 0** (often break-even, ratio = 1, or 0) and
**Max = the target ratio that scores 1**. Sources:
the company's investment hurdle rate / required margin / circular-service business case.

| ID | Name | Intermediate | Unit |
|---|---|---|---|
| `EC1` | Return On Investment (ROI) | `profit / cost` | ratio |
| `EC41` | Repair Viability | `profit / cost` | ratio |
| `EC42` | Refurbishment Viability | `profit / cost` | ratio |
| `EC43` | Repurpose Viability | `profit / cost` | ratio |
| `EC44` | Recycling Viability | `savings / cost` | ratio |
| `EC45` | Recovery Viability | `savings / cost` | ratio |
| `EC46` | Remanufacturing Viability | `profit / cost` | ratio |
| `EC47` | Circular Material Viability | `nonvirgin / virgin` | ratio |

### Rating scales — the survey/test scale (5 rows)

These average a rating or score; Min/Max are the **bounds of the rating scale** used (e.g. a
1–5 satisfaction survey → Min = 1, Max = 5; a 0–100 quality test → Min = 0, Max = 100). Source:
the instrument the company uses to collect the feedback / test result.

| ID | Name | Intermediate | Unit |
|---|---|---|---|
| `S21` | Customer Satisfaction Score | `feedback / surveyed` | scale |
| `S23` | Customer Service Timeliness | `response / inquiries` | scale |
| `S24` | Customer Service Satisfaction Score | `feedback / inquiries` | scale |
| `S31` | Employment Satisfaction Score | `feedback / employees` | scale |
| `C212` | Quality of Refurbished Products | `refurbished / new` | scale |

### Company targets — internal goal (8 rows)

A value compared against a company-defined target; **direction varies by row** (see *Setting the
band direction* above):

- **Lower is better — the time rows `C213`, `C223`, `C3-6`:** inverted band, **Min =
  worst-acceptable time** (→ 0), **Max = best-acceptable time, often 0** (→ 1), so `Min > Max`.
- **Higher is better — `C233`, `C3-5`, `S3-6`, `S3-7`:** ascending band, **Min = the floor that
  scores 0**, **Max = the target that scores 1**.

(`S3-5` Average Cost of Living is the reference denominator for the `S3-6` living-wage comparison,
not scored on its own.) Source: internal targets / living-wage benchmark (S3-5/6).

| ID | Name | Intermediate | Unit |
|---|---|---|---|
| `C213` | Timeliness of Refurbishment | `time` | time |
| `C223` | Timeliness of Repair | `time` | time |
| `C233` | Remanufacture Success Rate | `count` | count |
| `C3-5` | Instructions Availability | `own` | % |
| `C3-6` | Disassembly Time | `own` | time |
| `S3-5` | Average Cost of Living | `own` | € |
| `S3-6` | Average Employee Salary | `own` | € |
| `S3-7` | Job Creation | `own` | # |

### Prior period — the company's own records (2 rows)

`current / previous` reduction ratios — **lower is better**, so use the **inverted band** (see
*Setting the band direction* above): **Min = 1.0** (no reduction → 0), **Max = the stretch-target
reduction**, e.g. 0.7 (→ 1). Note `Min > Max`. Source: the previous reporting period's value from
the company's own data.

| ID | Name | Intermediate | Unit |
|---|---|---|---|
| `R224` | Energy Inflow Improvement | `current / previous` | ratio |
| `R32` | Water Consumption Reduction | `current / previous` | ratio |

### Performance / direction — read the note (2 rows)

> Two rows used to be here but had the *intermediate itself* pointing the wrong way (a "lower is
> better" ratio that was never complemented, which an ascending Min/Max band cannot repair). Both
> were reformulated as complements and moved into the bounded bucket:
>
> - `R12` → `1 − (mass − cyclable)/mass = cyclable/mass`, **End-of-Life Recoverability** (2026-06-26,
>   `tools/scripts/flip_r12_recoverability.py`).
> - `EN43` → `1 − blue/absolute = (green+gray)/absolute`, **Water Independence Ratio** (2026-06-28,
>   `tools/scripts/flip_en43_independence.py`).
>
> The two rows below are **not** direction bugs — they are already higher = better and only need a
> company-supplied band (do *not* complement them).

| ID | Name | Intermediate | Note |
|---|---|---|---|
| `C222` | Longevity of repaired product | `repaired / original` | Lifespan ratio that can exceed 1 (repaired outlasts original). Set Max = the longevity target. |
| `R221` | End User Energy Efficiency | `output / input` | Efficiency ratio; set Min/Max to the efficiency band you score. |

---

## Filling it in

1. Enter Target Min / Target Max (columns S / T) on the domain sheet for the benchmark rows you
   want to score; the bounded-ratio rows already carry 0/1 (override only if you want a band).
2. Re-run the engine: `kpi-engine compute "data/KPI List.xlsx"`. Rows still missing a band report
   `Target Min/Max not set`; everything else scores.
3. `kpi-engine validate` checks for degenerate ranges (Min == Max) and weight integrity.

The classification lives in `tools/scripts/apply_review_round7.py` (`SEED_01` and `BENCHMARK`),
so this guide and the seeder stay in sync.
