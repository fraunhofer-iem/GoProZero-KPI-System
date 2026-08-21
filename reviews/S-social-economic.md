# Social domain cross-check — S34 "Social Economic Contribution Score" and children

Scope: S34 (parent, WEIGHTED_AVERAGE) and its three children S3-5, S3-6, S3-7, read from
`snapshot/Social Impact.tsv`. Context rows S3 (parent), S0 (grandparent) and siblings
S31/S32/S33 read for hierarchy and method comparison. Workbook not edited.

## Summary

| ID | Indicator | Strategy | Cited ref | Verdict | One-line |
|----|-----------|----------|-----------|---------|----------|
| S34 | Social Economic Contribution Score | WEIGHTED_AVERAGE | (none) | NOT-CHECKABLE (composite) → **constructed composite, method defect** | Children are mixed-unit raw values; cannot be weight-averaged until each is normalized to a target. |
| S3-5 | Average Cost of Living (€) | RAW_VALUE | (none) | NOT-CHECKABLE (leaf, no ref) | Maps to PSILCA "Living wage, per month" reference point; no source cited. |
| S3-6 | Average Employee Salary (€) | RAW_VALUE | GRI 202-1 | PARTIAL (adapted) — **mis-cite** | GRI 202-1 is a *ratio to local minimum wage*, not an absolute salary; PSILCA "Sector average wage" / ESRS S1-10/S1-16 are better matches. |
| S3-7 | Job Creation (#) | RAW_VALUE | GRI 401-1 | VERIFIED | GRI 401-1 = "Total number and rate of new employee hires" — direct match. |

Reference-integrity (check A): `PSILCA` (cited by sibling S32) and `ESRS S1` have **no Label
row** in References.tsv. `GRI 202-1` / `GRI 401-1` resolve only to the umbrella `GRI` Label —
sub-locators are not registered as their own Labels. Details in the fixes table.

---

## S34  Social Economic Contribution Score
- Verdict: **NOT-CHECKABLE as cited (no reference) → in practice a constructed composite with a method defect**
- Reference(s): none cited on S34 (blank Reference column). Children cite GRI 202-1 (S3-6),
  GRI 401-1 (S3-7); S3-5 cites nothing.
- Strategy tag: `WEIGHTED_AVERAGE_STRATEGY`; unit `%`; children S3-5 (€), S3-6 (€), S3-7 (#).
- Formula text: "Weighted sum of each underlying metrics compared to a target value or
  comparable product / standard".

### What the children measure (Q1)
From `snapshot/Social Impact.tsv`:
- S3-5 "Average Cost of Living" — "The average cost of living of employees directly linked to
  the product." Unit €, RAW_VALUE.
- S3-6 "Average Employee Salary" — "The average salary of employees directly linked to the
  product." Unit €, RAW_VALUE, ref GRI 202-1.
- S3-7 "Job Creation" — "Number of jobs created directly linked to the product." Unit #,
  RAW_VALUE, ref GRI 401-1.

Mapping to recognised indicators (grounded below): S3-6 ↔ wage/remuneration disclosures
(GRI 201-1 "employee wages and benefits", GRI 202-1 entry-wage ratio, PSILCA "Sector average
wage", ESRS S1-10 "adequate wages" / S1-16 remuneration); S3-5 ↔ PSILCA "Living wage, per
month" (the cost-of-living reference point); S3-7 ↔ GRI 401-1 new-hire count / GRI 203
indirect economic impact (jobs).

### The averaging problem (Q3)
The three children are **two euro amounts and a count** — three different units. A weighted
*average* of €, € and # is dimensionless nonsense; the result has no defensible meaning. The
formula text itself signals the intended fix ("compared to a target value or comparable
product/standard"): each child must first be turned into a **dimensionless score against a
target**, after which a weighted average is legitimate. So S34 is fine as a weighted average
**only once its children are normalized scores** — exactly how its siblings already work
(S31/S32/S33 all carry `NORMALIZED_RATIO_STRATEGY` with explicit min/max targets), while
S34's children are still `RAW_VALUE_STRATEGY` with no targets.

### Do the sources normalize or report absolute? (Q2)
The cited/relevant sources split cleanly:
- **GRI reports absolute disclosures**, not 0–1 composites.
  - GRI 201-1 "Direct economic value generated and distributed … Economic value distributed:
    operating costs, **employee wages and benefits**, payments to providers of capital …"
    — absolute monetary disclosure (data/literature/GRI - Global Reporting Initiative/GRI 201_  Economic Performance 2016.pdf p.8).
  - GRI 401-1 "**Total number and rate of new employee hires** during the reporting period,
    by age group, gender and region." — absolute count/rate
    (data/literature/GRI - Global Reporting Initiative/GRI 401_ Employment 2016.pdf p.8).
  - GRI 202-1 "**Ratios of standard entry level wage by gender compared to local minimum
    wage**" — already a *ratio against a reference*, not an absolute salary
    (data/literature/GRI - Global Reporting Initiative/GRI 202_ Market Presence 2016.pdf p.3, p.8).
- **PSILCA normalizes raw monetary values against a reference before aggregating.** It carries
  a Fair-salary subcategory ("Living wage, per month USD; Minimum wage, per month USD; Sector
  average wage … Ratio salary (sector wage)/living wage")
  (data/literature/PSILCA/PSILCA_manual_v3_1_1_2.pdf p.17), and converts raw values into
  ordinal **risk levels**: "the PSILCA database provides the unassessed indicator values
  (\"raw values\") … as well as the assigned risk levels … and the ordinal risk scales"
  (PSILCA p.21); risk levels then carry characterization factors "Very low risk 0.01 / Low 0.1
  / Medium 1 / High 10 / Very high 100" (PSILCA p.27). The wage normalization is explicit:
  "The minimum wage is assessed in comparison with the living wage … risk levels are defined by
  **calculating the ratio x = Living wage/Minimum wage**" with binned thresholds
  (x<0.5 … x≥1.8) (PSILCA p.36). "Sector average wage … assesses if the salary is enough to
  afford a decent standard of living" (PSILCA p.36).
- **ESRS S1 also frames pay as comparison-to-threshold, not an averaged absolute.** S1-10
  "Adequate wages — The undertaking shall disclose **whether or not its employees are paid an
  adequate wage**, and if they are not all paid an adequate wage, the countries and percentage
  of employees concerned"
  (data/literature/ESRS - European Sustainability Reporting Standards/ESRS S1 Delegated-act-2023-5303-annex-1_en.pdf p.12);
  plus S1-16 "Remuneration metrics (pay gap and total remuneration)" (ESRS S1 p.2).

### Assessment
No source anywhere in the retrieved corpus combines mixed-unit economic-contribution metrics
into a single 0–1/% score. GRI keeps them as separate absolute disclosures; PSILCA and ESRS
S1 express pay as a **ratio/comparison against a target** (living wage, minimum wage, adequate
wage). That is precisely the operation S34's formula text describes but its WEIGHTED_AVERAGE
tag + RAW_VALUE children do not implement. S34 is therefore a **constructed composite with no
standard basis as currently specified** — defensible *only* if each child is first normalized
against a target (the PSILCA living-wage ratio is the closest sourced precedent), then
weight-averaged. The comment ("internal company comparison, e.g. shoes in Germany vs Vietnam")
reinforces that a target/normalization is required, since absolute € differ by geography.

### Issues
- **[blocker]** S34 tagged `WEIGHTED_AVERAGE_STRATEGY` over mixed-unit raw children (€, €, #);
  averaging is dimensionless and meaningless as specified. Conflicts with its own formula text
  ("compared to a target value or comparable product/standard").
- **[major]** Children S3-5/S3-6/S3-7 are `RAW_VALUE_STRATEGY` with **no per-child target /
  normalization**, unlike siblings S31/S32/S33 which all use `NORMALIZED_RATIO_STRATEGY` with
  declared min/max. S34 lists "Target Value: min, max" in its Potential Reference Values column
  but the children carry no such targets.
- **[minor]** S34 has a blank Reference; acceptable for a composite, but the *method* (how
  children are normalized) is undocumented.

### Recommendation
Either (a) keep S34 as a weighted average **but convert each child to a NORMALIZED_RATIO**
first, or (b) re-tag the children. Concretely:
- S3-5 / S3-6 should not feed S34 as raw €. Replace with a **wage-adequacy ratio** — e.g.
  `salary / cost-of-living` (or PSILCA-style `sector wage / living wage`, PSILCA p.36),
  bounded by min/max targets → 0–1. This single ratio arguably supersedes having S3-5 and S3-6
  as separate score inputs (cost of living is the *target* for salary, not a co-equal addend).
- S3-7 (job count) should be normalized against a target jobs figure (min/max) before entering
  the average, or reported separately as an absolute GRI 401-1 / GRI 203 disclosure.
- Document each child's target in the workbook (as S31–S33 already do).
- Once children are 0–1 normalized scores, S34 as a weighted average is sound (composite,
  internal check: children would exist, units compatible, description consistent).

---

## S3-5  Average Cost of Living (€)
- Verdict: **NOT-CHECKABLE** (leaf, no reference cited) — but mappable.
- Reference(s): none cited.
- Evidence (closest sourced concept):
  - PSILCA p.17: "Fair salary — Living wage, per month USD".
  - PSILCA p.36: "Sector average wage … assesses if the salary is enough to afford a decent
    standard of living"; minimum wage "assessed in comparison with the living wage … ratio
    x = Living wage/Minimum wage".
- Assessment: A leaf/raw metric that clearly should trace to a source. It corresponds to
  PSILCA's "Living wage, per month" — but PSILCA uses cost-of-living as the **denominator/
  reference** against which wages are scored, not as a standalone addend in a contribution
  score. As written (raw €, no target, no ref) it cannot be verified or meaningfully averaged.
- Issues: **[major]** leaf metric with no reference; **[major]** raw € cannot feed a
  weighted-average score without normalization.
- Recommendation: cite PSILCA (once that Label exists) and use cost-of-living as the
  normalization target for salary (S3-6) rather than a co-equal score input.

## S3-6  Average Employee Salary (€)
- Verdict: **PARTIAL (adapted) — mis-cite**
- Reference(s): GRI 202-1 [resolves only to umbrella `GRI` Label / data/literature/GRI - Global Reporting Initiative/GRI 202_ Market Presence 2016.pdf]
- Evidence:
  - GRI 202 p.3 / p.8: "Disclosure 202-1 **Ratios of standard entry level wage by gender
    compared to local minimum wage**" — "report the relevant ratio of the entry level wage by
    gender at significant locations of operation to the minimum wage."
  - GRI 201 p.8: "Economic value distributed: … **employee wages and benefits** …" (absolute).
  - PSILCA p.36: "Sector average wage … the mean of monthly earnings of all employees in the
    sector."
  - ESRS S1 p.12: S1-10 "Adequate wages"; p.2: S1-16 "Remuneration metrics (pay gap and total
    remuneration)".
- Assessment: The KPI measures an **absolute average salary (€)**. GRI 202-1 does **not** cover
  that — 202-1 is a *ratio of entry-level wage to the local minimum wage*. The concept of an
  average/mean salary is better matched by PSILCA "Sector average wage" (p.36), GRI 201-1
  "employee wages and benefits" (p.8), or ESRS S1-16 remuneration. So the cited code is the
  wrong locator for what the KPI computes (the source covers a *related but different*
  quantity). Note: 202-1's "compared to minimum wage" framing is itself the normalization
  S34 needs.
- Issues: **[major]** GRI 202-1 mis-cited for an absolute salary; **[major]** raw € input to a
  weighted average without normalization.
- Recommendation: re-cite to PSILCA "Sector average wage" and/or GRI 201-1 / ESRS S1-16; and
  normalize against a target (cost of living / living wage) before feeding S34.

## S3-7  Job Creation (#)
- Verdict: **VERIFIED**
- Reference(s): GRI 401-1 [resolves only to umbrella `GRI` Label / data/literature/GRI - Global Reporting Initiative/GRI 401_ Employment 2016.pdf]
- Evidence:
  - GRI 401 p.3 / p.8: "Disclosure 401-1 New employee hires and employee turnover … **Total
    number and rate of new employee hires** during the reporting period, by age group, gender
    and region."
- Assessment: "Number of jobs created" faithfully reflects GRI 401-1's "total number of new
  employee hires." Direct, supported match. (GRI 203 indirect economic impacts is a secondary
  relevant frame for jobs supported.)
- Issues: **[minor]** as a raw count it still cannot enter a weighted *average* without
  normalization against a target.
- Recommendation: keep the GRI 401-1 citation; normalize against a target jobs figure before
  feeding S34, or report separately as an absolute disclosure.

---

## Recommended actions (S34)
1. **Do not weight-average raw mixed-unit children.** Re-tag S34's pipeline so each child is a
   NORMALIZED_RATIO (0–1) against a declared target before the weighted average — mirroring
   siblings S31/S32/S33. Only then is S34's WEIGHTED_AVERAGE legitimate.
2. **Pair cost-of-living with salary as a ratio.** Use `salary / cost-of-living` (PSILCA-style
   `sector wage / living wage`, PSILCA p.36) as one normalized input, rather than carrying
   S3-5 and S3-6 as two separate raw addends. Cost of living is salary's *target*, not a peer.
3. **Add explicit per-child targets (min/max)** to S3-5/S3-6/S3-7 in the workbook, as S31–S33
   already declare.
4. **Fix the S3-6 citation**: GRI 202-1 is a wage-to-minimum-wage *ratio*, not an absolute
   salary — re-cite to PSILCA "Sector average wage", GRI 201-1, or ESRS S1-16.
5. **Register missing Labels** (`PSILCA`, `ESRS S1`) in References.tsv before citing them.

## Inconsistencies & fixes
| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker | S34 | `WEIGHTED_AVERAGE` over mixed-unit raw children (€, €, #) is dimensionless/meaningless; contradicts S34's own formula text ("compared to a target value or comparable product/standard"). No source aggregates mixed-unit economic metrics into one 0–1 score. | Normalize each child to a 0–1 score vs a target first, then weight-average. Keep S34 as WEIGHTED_AVERAGE only over normalized children. |
| 2 | major | S3-5, S3-6, S3-7 | Children are `RAW_VALUE_STRATEGY` with no per-child target/normalization, unlike siblings S31/S32/S33 (`NORMALIZED_RATIO_STRATEGY`, explicit min/max). | Convert each to NORMALIZED_RATIO with declared min/max targets (e.g. salary/cost-of-living per PSILCA p.36; jobs vs target jobs). |
| 3 | major | S3-6 | `GRI 202-1` cited for "Average Employee Salary (€)", but GRI 202-1 is "Ratios of standard entry level wage … compared to local minimum wage" (GRI 202 p.8) — a ratio, not an absolute salary. | Re-cite to PSILCA "Sector average wage" (p.36), GRI 201-1 "employee wages and benefits" (p.8), or ESRS S1-16 remuneration. |
| 4 | major | S3-5 | Leaf/raw metric "Average Cost of Living" with no Reference; maps to PSILCA "Living wage, per month" (p.17, p.36). | Add PSILCA citation; use cost-of-living as the normalization target for salary, not a separate score addend. |
| 5 | major | References.tsv | `PSILCA` (cited by sibling S32) and `ESRS S1` have no Label row; orphan codes. (`GRI 202-1`/`GRI 401-1` resolve only via the umbrella `GRI` Label — sub-locators unregistered.) | Add `PSILCA` and `ESRS S1` rows to References.tsv. Optionally record GRI/ESRS sub-locators as accepted sub-codes of their umbrella Labels. |
| 6 | minor | S34 | Blank Reference (acceptable for a composite) but the child-normalization method is undocumented. | Document the normalization/target method in the Comment or Formula field. |

### SOURCE-NOT-FOUND codes
None at the file level — every concept was located in a corpus PDF. The gaps are
**reference-registration** gaps (PSILCA, ESRS S1 absent from References.tsv), not missing
files. PSILCA, GRI 201/202/203/401, and ESRS S1 PDFs all exist under `data/literature/`.

### Limits of this run
- Page numbers cited are PDF-search page hits; the PSILCA wage-scale table was confirmed by
  reading the page image (PDF page 37 = printed "36"). GRI/ESRS line numbers were taken from
  search-context snippets, not full-page reads, so exact disclosure paragraph numbering beyond
  the quoted text was not independently re-verified.
- I assessed only S34 and its three children plus sibling context; I did not re-audit
  S31/S32/S33 themselves (used only to establish the in-sheet normalization convention).
- The PSILCA "cost of living ↔ living wage" mapping for S3-5 is an interpretation grounded in
  PSILCA's own "decent standard of living" language (p.36); the workbook does not state which
  source S3-5 derives from, so the mapping is a recommendation, not a confirmed origin.
