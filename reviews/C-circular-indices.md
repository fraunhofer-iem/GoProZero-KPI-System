# Circular-economy index cross-check — C4, C5, C231

Scope: `snapshot/Circular Efforts.tsv` rows C4 (Circular Flow Index), C5 (Circular EoL
handling), C231 (Remanufactured Component Share). Grounded against `data/literature/`.
Workbook NOT edited. Every literature claim below is a verbatim quote with file + page.

## Summary

| KPI | Question | Verdict | Headline |
|-----|----------|---------|----------|
| C4 Circular Flow Index | MCI formula; is "1-(virgin+wasted)/2*mass" correct? ratio vs weighted-avg? | CONTRADICTION (formula) + SOURCE-NOT-FOUND (MCI file) | MCI formula PDF absent; the workbook formula is dimensionally broken and not MCI. Should be a NORMALIZED_RATIO, not WEIGHTED_AVERAGE of raw kg. |
| C5 Circular EoL handling | EoL circularity rate = recovered/total mass? ratio vs avg of raw kg? | PARTIAL (adapted) — concept supported by ISO 59020 | ISO 59020 A.3.3/Fig A.2 define circular-outflow share = circular mass / total outflow mass. C5 should be NORMALIZED_RATIO, not WEIGHTED_AVERAGE. |
| C231 Remanufactured Component Share | correct numerator/denominator; which of C2-11/12/13 | CONTRADICTION (internal) — concept supported by DIN SPEC 91472 | Prose formula, description and child-IDs disagree three ways. DIN SPEC 91472 H-quota gives the correct secondary-content ratio. |

Reference-integrity (check A): `MCI+15`, `MCI+16`, `MM+17`, `ISO 59020` are **orphan
codes** — used in Metrics List but absent from `snapshot/References.tsv` as Labels
(verified column-wise). `MCI+25` *is* a Label but its PDF is missing from the corpus.

---

## C4 — Circular Flow Index (WEIGHTED_AVERAGE; children C4-1 virgin kg, C4-2 wasted kg, C4-3 total mass kg)

- Verdict: **CONTRADICTION (formula is dimensionally invalid / not MCI)** + **SOURCE-NOT-FOUND** for the MCI formula text.
- Reference(s) cited: `MCI+15` (on C4 and C4-1), `MCI+16` (on C4-3), `CS+16` (on C4-1).
  - `MCI+15` / `MCI+16` → **orphan**: no matching Label in `snapshot/References.tsv`.
    The bibliography's MCI entry is Label **`MCI+25`** ("An approach to measuring
    circularity / Published 2015, adapted in 2019", DOI 10.13140/RG.2.2.29213.84962).
    Its PDF is **not in `data/literature/`** (no `MCI+*` file in `Papers/`, no
    "approach to measuring circularity" file anywhere) → SOURCE-NOT-FOUND for the
    algebra.
- Evidence (what the corpus *does* contain about MCI):
  - `snapshot/References.tsv` (Label `MCI+25`): "The Material Circularity Indicator
    (MCI) for a product measures the extent to which linear flow has been minimised and
    restorative flow maximised … constructed from a combination of three product
    characteristics: the mass … of virgin raw material used in manufacture, the mass …
    of unrecoverable waste that is attributed to the product, and a utility factor …"
  - data/literature/Papers/FAC+21-…transition perspective.pdf p.3: "The MCI was
    proposed in 2015 by the EMF and Granta Design to measure how restorative ﬂows can be
    maximized and linear ﬂows minimized, considering both the intensity and length of the
    [use]."
- Assessment:
  - The MCI concept (virgin mass + unrecoverable-waste mass + utility) is real and is
    what C4 is reaching for. But the **workbook formula is wrong**. As written:
    `1 - (Virgin Material Inflow + Wasted Material Outflow) / 2 * Total Mass Flow`
    (a) by operator precedence evaluates to `1 - [(V+W)/2]·M` — multiplying three masses,
    giving units of kg², not a dimensionless ratio, and not bounded to [0,1];
    (b) even read charitably as `1 - (V+W)/(2·M)`, the "/2" has no basis in MCI. The
    canonical MCI linear-flow term divides virgin+waste by **mass flow** (and folds in a
    utility factor F(X)); a flat "÷2" is not the MCI weighting. I could **not** retrieve
    the exact MCI algebra because the source PDF is absent, so I will not assert the
    precise correct constant — only that the cited concept does not support "/2".
  - **Strategy mismatch:** C4 is a *ratio* of masses that should resolve to a 0–100 %
    circularity figure. It is tagged `WEIGHTED_AVERAGE_STRATEGY` and its children are
    raw kg (C4-1/C4-2/C4-3) each carrying equal weights ~0.333. Weight-averaging raw kg
    is meaningless (you would be averaging virgin-kg, waste-kg and total-kg). This must
    be a **NORMALIZED_RATIO** computed from an intermediate formula, like every other
    leaf ratio in this sheet (C11, C12, C31…).
- Issues:
  - [blocker] Formula `1 - (V+W)/2 * M` is dimensionally invalid and unbounded; does not
    match the cited MCI concept (no "/2" weighting in MCI; utility factor omitted).
  - [blocker] `WEIGHTED_AVERAGE_STRATEGY` over raw-kg children is wrong; should be
    `NORMALIZED_RATIO_STRATEGY`.
  - [major] References `MCI+15` and `MCI+16` are orphan codes (use `MCI+25`).
  - [major] The MCI source PDF (`MCI+25`) is missing → formula cannot be fully verified.
- Recommendation:
  - Retag C4 → `NORMALIZED_RATIO_STRATEGY`. Intermediate (MCI linear-flow form, with the
    child bindings available):
    `LFI = (C4-1 [Virgin] + C4-2 [Wasted]) / (2 * C4-3 [Total Mass Flow])`
    then `Circular Flow Index = 1 - LFI` (optionally × utility factor F if/when added).
    Note: the EMF MCI does use `(V + W)/(2·M)` for the **linear-flow index** when virgin
    inflow and unrecoverable waste are each compared to mass flow — i.e. the "/2" is the
    average of the two half-flows, *each over total mass*, NOT `(V+W)/2`. So the fix is
    the **denominator `2·C4-3`**, which the current text drops. **This must be confirmed
    against the MCI source once `MCI+25` is added to the corpus** — flagged needs_review.
  - Min/Max: bound result to [0,1] (0 % = fully linear, 100 % = fully circular). With
    NORMALIZED_RATIO the natural Min=0, Max=1; no min/max stretch needed unless the
    author wants a target band.
  - Add `MCI+25` to References and obtain the PDF; replace `MCI+15`/`MCI+16` with `MCI+25`.

## C5 — Circular EoL handling (WEIGHTED_AVERAGE; children C1-5, C5-1…C5-5, all kg; no reference)

- Verdict: **PARTIAL (adapted)** — the concept is directly supported by ISO 59020, but
  C5 has no cited reference and uses the wrong strategy.
- Reference(s): none cited. (Leaf-style composite computing a mass ratio — a reference
  *should* exist; ISO 59020 supplies it.)
- Evidence (ISO 59020:2024):
  - ISO-59020.pdf p.34 (Fig A.2 region), §A.3.3 Formula (A.5): "P_REUO(X) = (m_REUO(X) /
    m_TO(X)) · 100" where "m_REUO(X) is the mass of reused … of an outflow" and
    "m_TO(X) is the mass of total … outflow" — i.e. circular-outflow share = circular
    mass ÷ total outflow mass × 100.
  - ISO-59020.pdf p.34 §A.3.1: "The following three core circularity indicators are
    intended to represent outflows that are mutually exclusive and represent the circular
    outflows: — components and products that are reused (see A.3.3); — per cent recycled
    material derived from outflow (see A.3.4); — products and materials for renewable
    recirculation (see A.3.5). The remaining outflows are considered as linear and do not
    count towards circularity."
  - ISO-59020.pdf p.34 §A.3.1: "The sum of the circular outflows and the remaining
    non-circular outflows represent 100 % of the resource outflows from the system in
    focus."
  - ISO-59020.pdf p.35 (Figure A.2): "Per cent (by mass) circular content of outflow (X)"
    + "Per cent non-circular outflow (e.g. waste, releases, losses …)" = "100 % of
    resource outflow".
- Assessment:
  - C5's intent ("amount of recycled, refurbished, repurposed components … goal … 100 %
    handling of EoL products, meaning no parts are wasted") is exactly ISO 59020's
    by-mass circular-outflow share. The numerator (Refurbished + Remanufactured +
    Repurposed + Recycled component weight) is the circular outflow; C5-5 Discarded is
    the non-circular outflow; the denominator is total reclaimed mass = the four circular
    streams + discarded. The workbook's stated numerator/denominator
    (`circular weights / Total reclaimed units weight`) matches A.3.3 form.
  - **Strategy mismatch:** tagged `WEIGHTED_AVERAGE_STRATEGY` over raw-kg children. As
    with C4, averaging raw kg is not meaningful; this is a single mass ratio.
  - **Denominator binding gap:** the child list is C1-5 (Reclaimed Units Weight),
    C5-1…C5-5. The formula's "Total reclaimed units weight" = C1-5. But note an
    accounting consistency requirement (ISO 59020 p.34: the streams must sum to 100 % of
    outflow): ideally `C5-1+C5-2+C5-3+C5-4+C5-5 = C1-5`. The comment already flags it
    "Does not consider the amount of non-usable components due to reclamation damages",
    so a residual is expected — recommend either (a) denominator = C1-5, or (b)
    denominator = sum of the five streams, and document which.
- Issues:
  - [blocker] `WEIGHTED_AVERAGE_STRATEGY` is wrong; should be `NORMALIZED_RATIO_STRATEGY`
    (single by-mass circular-outflow share).
  - [major] No Reference cited though a direct standard exists (ISO 59020 §A.3.3 /
    Fig A.2). Add it.
  - [minor] "OR Discarded component weight / Total reclaimed units weight" second formula
    line is the *non-circular* share (1 − circular share); keep only the circular share as
    the KPI, or label the second as a derived non-circular complement.
  - [minor] Child C1-5 is borrowed from C13's subtree as the denominator — fine, but make
    the binding explicit.
- Recommendation:
  - Retag C5 → `NORMALIZED_RATIO_STRATEGY`. Intermediate formula with child bindings:
    `CircularEoL = (C5-1 + C5-2 + C5-3 + C5-4) / C1-5`
    (circular-handled mass ÷ total reclaimed mass). Discarded mass C5-5 is the
    complement; optionally enforce `C5-1+…+C5-5 = C1-5`.
  - Min/Max: Min=0, Max=1 (0 % = all discarded, 100 % = no parts wasted, matching the
    stated goal). No stretch band needed unless a target is wanted.
  - Reference: cite `ISO 59020` (§A.3.3 Formula A.5; Fig A.2) — but `ISO 59020` is not yet
    a Label (see check A); add the row first.

## C231 — Remanufactured Component Share (NORMALIZED_RATIO; children C2-11 inflow, C2-13 remanufactured)

- Verdict: **CONTRADICTION (internal inconsistency)** — the prose formula, the
  description, and the bound child-IDs disagree three different ways. The underlying
  concept (secondary-content share of a remanufactured unit) is supported by DIN SPEC
  91472.
- Reference(s): none cited on C231. DIN SPEC 91472 (in corpus) and ISO 59020 both define
  the relevant ratio.
- The three-way conflict (all from `snapshot/Circular Efforts.tsv`):
  1. **Children bound:** C2-11 (Total components inflow = new + secondary) and C2-13
     (Total components remanufactured = actually integrated into the unit).
  2. **Prose formula:** "Ratio = Total new components inflow / Total secondary components
     inflow" — references *new* inflow and *secondary* inflow (C2-12), neither of which
     is C2-13, and inverts circularity (more new ⇒ higher score is backwards).
  3. **Description:** "ratio between the total components used and the secondary
     components used … 100 % … remanufactured components integrated … equal to the target
     amount" — i.e. secondary/target, again different from both (1) and (2).
- Evidence (DIN SPEC 91472:2023):
  - DIN SPEC 91472 …Remanufacturing.pdf p.24, Equation (1): "H = 1 − [ Quantity of new
    parts of the component (units per year) / (Annual sales quantity_Remanufactured
    product · Units of component / Remanufactured product) ]" where "H is the actual
    quota at which a component originates from the … targeted component origin … after
    use." (i.e. secondary share = 1 − new-share.)
  - DIN SPEC 91472 …Remanufacturing.pdf p.25, §7.2.3 Equation (2): "PCI = Σ (Mass
    fraction of component of total product (wt%) · H · VRP factor)" — the product
    composition circularity indicator is a **mass-weighted secondary-content share**,
    bounded "between 0 for purely linear to 1 for perfectly circular products".
  - DIN SPEC 91472 …Remanufacturing.pdf p.23 §7.1: product circularity is defined "by the
    degree of decoupling of products … from the use of primary raw materials [allowing] a
    mass balance quantification of product circularity."
  - Cross-support, ISO 59020 (Table 3, labeled p.17): mandatory inflow indicator "A.2.2
    Average reused content of an inflow (X) — Fraction of input material resources that
    are reused components and products" — i.e. secondary/total inflow, a 0–1 share.
- Assessment:
  - All three authoritative anchors (DIN SPEC PCI/H, ISO 59020 A.2.2) define the
    remanufactured/secondary-content share as **secondary (or remanufactured) mass ÷
    total mass**, bounded 0–1, where *higher = more circular*. The workbook's prose
    formula "new / secondary" is **inverted and wrong-signed** (it rises as the product
    gets *less* circular and is unbounded above 1).
  - Given the child masses available (all kg): the intended KPI is the share of the
    remanufactured unit's mass that comes from remanufactured/secondary components.
    The two bound children (C2-11 total inflow, C2-13 remanufactured-integrated) give the
    cleanest binding: `C2-13 / C2-11`. C2-12 (secondary inflow set for restoration) is the
    *input* to restoration and belongs to sibling C232 (Restored Components Share =
    C2-13 / C2-12, which the sheet already does correctly).
  - The "could be components instead, but now in kg for calculation simplicity" comment on
    C2-11 confirms a mass-fraction intent, matching DIN SPEC's wt%-based PCI.
- Issues:
  - [blocker] Prose formula "Total new components inflow / Total secondary components
    inflow" contradicts both the bound children (C2-11, C2-13) and the description, and is
    inverted (new-over-secondary rewards *less* circularity, unbounded). Wrong KPI sign.
  - [major] Numerator/denominator mapping ambiguous across description vs formula vs
    children (the `needs_review` flag is justified).
  - [major] No Reference cited though DIN SPEC 91472 §7.2.3 / ISO 59020 A.2.2 apply.
  - [minor] C2-11 unit/granularity (kg vs component count) noted by author — keep kg and
    state it.
- Recommendation:
  - Keep `NORMALIZED_RATIO_STRATEGY`. Replace the prose formula with the secondary-content
    share matching the bound children and DIN SPEC PCI intent:
    `Ratio = C2-13 (Total components remanufactured) / C2-11 (Total components inflow)`
    (remanufactured/secondary mass ÷ total component mass; 0 = all-new, 1 = fully
    secondary). Fix the description to "ratio of remanufactured/secondary component mass
    to total component mass."
  - Min/Max: Min=0, Max=1 (current Target min=0/max=1 is already correct for this form;
    it was the formula that was wrong).
  - Reference: cite `DIN SPEC 91472` (§7.2.3 PCI / Eq.1 H) and/or `ISO 59020` (A.2.2).
    Both must be added as Labels first (see check A).
  - Do NOT confuse with C232 (Restored Components Share = C2-13 / C2-12), which is the
    restoration-yield ratio and is already coherent.

---

## Recommended actions

1. **C4:** Retag `WEIGHTED_AVERAGE_STRATEGY → NORMALIZED_RATIO_STRATEGY`. Fix formula to
   the MCI linear-flow form `1 − (C4-1 + C4-2)/(2·C4-3)` (drop the stray `/2 * M`; the 2
   belongs in the denominator). Min=0, Max=1. **Confirm against the MCI source once added
   — needs_review.**
2. **C4 refs:** Replace orphan `MCI+15`/`MCI+16` with `MCI+25`; obtain & add the MCI PDF
   (currently SOURCE-NOT-FOUND).
3. **C5:** Retag → `NORMALIZED_RATIO_STRATEGY`. Formula `(C5-1+C5-2+C5-3+C5-4)/C1-5`.
   Min=0, Max=1. Cite ISO 59020 §A.3.3 / Fig A.2.
4. **C231:** Replace inverted prose formula with `C2-13 / C2-11`; rewrite the description
   to match; keep Min=0/Max=1. Cite DIN SPEC 91472 §7.2.3 / ISO 59020 A.2.2. Clear the
   `needs_review` flag after.
5. **References integrity:** Add Labels `ISO 59020`, `DIN SPEC 91472`, `MM+17`, and
   `MCI+25` (link its PDF) to `snapshot/References.tsv`; remove/replace orphan
   `MCI+15`/`MCI+16`. `MM+17` and `ISO 59020` already have files in the corpus.

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker | C4 formula | `1 - (V+W)/2 * Total Mass` is dimensionally invalid (kg²), unbounded, not the MCI formula; "/2" has no basis in cited MCI concept | Use `1 − (C4-1 + C4-2)/(2·C4-3)`; verify vs MCI source (needs_review) |
| 2 | blocker | C4 strategy | `WEIGHTED_AVERAGE` averaging raw-kg children (virgin/waste/total) is meaningless | Retag `NORMALIZED_RATIO_STRATEGY`, Min=0 Max=1 |
| 3 | blocker | C231 formula | Prose "new / secondary inflow" contradicts bound children (C2-11,C2-13) AND description, and is inverted/unbounded (rewards less circularity) | Use `C2-13 / C2-11`; rewrite description as secondary-content mass share |
| 4 | blocker | C5 strategy | `WEIGHTED_AVERAGE` over raw-kg streams; KPI is a single by-mass circular-outflow share | Retag `NORMALIZED_RATIO_STRATEGY`, `(C5-1+C5-2+C5-3+C5-4)/C1-5`, Min=0 Max=1 |
| 5 | major | C4 references | `MCI+15`, `MCI+16` are orphan codes (not Labels in References.tsv) | Replace with `MCI+25` |
| 6 | major | MCI source | `MCI+25` PDF absent from corpus → MCI algebra cannot be fully verified (SOURCE-NOT-FOUND) | Obtain & add the EMF MCI PDF; then confirm C4 formula |
| 7 | major | C231 ambiguity | numerator/denominator mapping inconsistent across formula/description/children (`needs_review`) | Resolve to `C2-13/C2-11` per DIN SPEC 91472 §7.2.3; clear flag |
| 8 | major | C5 reference | No reference cited though ISO 59020 §A.3.3/Fig A.2 directly defines this | Cite `ISO 59020` |
| 9 | major | C231 reference | No reference cited though DIN SPEC 91472 §7.2.3 / ISO 59020 A.2.2 apply | Cite `DIN SPEC 91472` / `ISO 59020` |
| 10 | major | References.tsv | `ISO 59020` orphan: used by C222/C31/C32/C5/C231 but not a Label; file exists at `ISO 59XXX/ISO-59020.pdf` | Add ISO 59020 row to References |
| 11 | major | References.tsv | `MM+17` orphan: used by C3-6, file exists in Papers/, no Label | Add MM+17 row to References |
| 12 | minor | C5 formula | Second line "Discarded / total" is the non-circular complement, not a separate KPI | Drop or label as derived `1 − CircularEoL` |
| 13 | minor | C231 / C2-11 | C2-11 measured in kg though conceptually component count (author-flagged) | Keep kg; state the convention explicitly |

### SOURCE-NOT-FOUND codes
- `MCI+15`, `MCI+16` — not in References.tsv; the bibliography's MCI entry is `MCI+25`,
  whose PDF is **also missing** from `data/literature/` (no `MCI+*` or "approach to
  measuring circularity" file found). The MCI *concept* is corroborated by FAC+21 p.3 and
  the `MCI+25` bibliography description, but the **algebraic MCI formula could not be
  retrieved**.

### Limits of this run
- The exact MCI linear-flow expression (and its utility factor F) could **not** be verified
  against a primary source because the MCI PDF is absent; my C4 formula recommendation is
  reconstructed from the corroborating descriptions (FAC+21 p.3; `MCI+25` entry) and is
  flagged needs_review until the source is added.
- I verified ISO 59020 outflow indicators (A.3.3 Formula A.5, Fig A.2, A.3.1) and DIN SPEC
  91472 PCI/ECI (Eq.1, Eq.2, §7.2.3) directly from the PDFs. ISO 59020 PDF page labels
  differ from file page numbers by ~8 (Annex A on file p.42 = label p.34); quotes above use
  the printed/label pages where stated and file pages where I read them.
- I did not re-audit siblings C232/C233 beyond confirming C232 (`C2-13/C2-12`) is internally
  coherent and distinct from C231; full sibling audit is out of scope for this batch.
