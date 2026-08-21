# EN1 Carbon-footprint phase ratios — literature cross-check

Scope of this run: rows **EN131, EN132, EN133, EN134, EN135** (the five "Lifecycle Phase
Emission" ratios), audited together with their context EN14 (parent), EN1 (grandparent),
their listed children EN1-1/EN1-2/EN1-3 (Scopes 1/2/3), and related EN1-4/EN1-5.
Source: `snapshot/Environmental Impact.tsv` and `snapshot/References.tsv`.

The central question is methodological: every phase row is tagged `NORMALIZED_RATIO`,
formula `(Actual - Min)/(Max - Min)`, and **all five list the same three children
(EN1-1, EN1-2, EN1-3 = GHG-Protocol Scopes 1/2/3)** with no phase-specific input. The
engine currently sets `Actual = Scope1 + Scope2 + Scope3` for every phase (flagged
`needs_review`). The findings below test whether the literature supports that encoding.

## Summary table

| Row | Name | Verdict | Core issue |
|-----|------|---------|-----------|
| EN131 | Sourcing Emission Ratio | UNSUPPORTED (under-specified) | "Actual" = Scope1+2+3 conflates entity scopes with a life-cycle stage; no per-phase input |
| EN132 | Production Emission Ratio | UNSUPPORTED (under-specified) | same conflation; identical children to all other phases |
| EN133 | Distribution Emission Ratio | UNSUPPORTED (under-specified) | same |
| EN134 | Use and Maintenance Emission Ratio | UNSUPPORTED (under-specified) | same |
| EN135 | End-of-Life Emission Ratio | UNSUPPORTED (under-specified) | same |
| EN14 (context) | Lifecycle Phase Emission | PARTIAL (adapted) | concept (per-stage breakdown / hotspots) is well supported; children are mis-wired |
| EN1-1 (context) | Scope 1 – Direct | VERIFIED | ESRS E1-6 / IFRS S2 / SASB RT-CP-110a.1 all define Scope 1 |
| EN1-2 (context) | Scope 2 – Purchased Indirect | PARTIAL (adapted) | ESRS E1-6 / IFRS S2 support Scope 2 (SASB code dropped — correct) |
| EN1-3 (context) | Scope 3 – Other Indirect | PARTIAL (adapted) | ESRS E1-6 / IFRS S2 support Scope 3 |

Verdict note: the five phase ratios are **leaf-adjacent composites that DO cite sources
indirectly through their children**, so the "composite, internal check" exemption does not
fully apply — the internal check itself fails (wrong children), which is why they are
UNSUPPORTED rather than VERIFIED.

---

## Evidence base (verbatim quotes)

### 1. Life-cycle stage / module structure — EN 15804+A2 and ISO 14067

**EN 15804+A2, Figure 1** (`data/literature/EN15804+A2.pdf`, PDF p.17; "Figure 1 — Types
of EPD with respect to life cycle stages covered and life cycle stages and modules for the
construction works assessment") lays out the canonical module structure:

- **A1–A3 Product stage**: A1 "Raw material supply", A2 "Transport", A3 "Manufacturing"
- **A4–A5 Construction process stage**: A4 "Transport", A5 "Construction – Installation process"
- **B1–B7 Use stage**: B1 Use, B2 Maintenance, B3 Repair, B4 Replacement, B5 Refurbishment,
  B6 Operational energy use, B7 Operational water use
- **C1–C4 End of life stage**: C1 "Deconstruction demolition", C2 "Transport",
  C3 "Waste processing", C4 "Disposal"
- **D**: "Benefits and loads beyond the system boundary … Reuse, recovery, recycling, potential"

EN 15804+A2 table of contents confirms these headings verbatim:
> "6.2.2 A1-A3, Product stage … 6.2.3 A4-A5, Construction process stage … 6.2.4 B1-B5,
> Use stage … 6.2.6 C1-C4 End-of-life stage … 6.2.7 D, Benefits and loads beyond the
> system boundary" — `data/literature/EN15804+A2.pdf` p.6.

**ISO 14067:2018** describes the same life-cycle ordering for a product CFP:
> "The aim of this document is to quantify GHG emissions associated with the life cycle
> stages of a product, beginning with resource extraction and raw material sourcing and
> extending through the production, use and end-of-life stages of the product."
> — `data/literature/ISO 14XXX/ISO 14067.pdf` p.7.
> "GHGs can be emitted and removed throughout the life cycle of a product which includes
> acquisition of raw material, design, production, transportation/delivery, use and the
> end-of-life treatment." — same file, p.8.

**Do the workbook's five phases correspond to these modules?** Yes, as a coarsened mapping
(quotes above ground each correspondence):

| Workbook phase (row) | EN 15804+A2 module(s) | ISO 14067 stage |
|----------------------|------------------------|------------------|
| EN131 Sourcing | A1 Raw material supply (+A2 Transport) | "raw material sourcing" |
| EN132 Production | A3 Manufacturing (A1–A3 product stage) | "production" |
| EN133 Distribution | A4 Transport (and A5) | "transportation/delivery" |
| EN134 Use & Maintenance | B1–B7 Use stage | "use" |
| EN135 End-of-Life | C1–C4 End of life stage | "end-of-life" |

So the **phase names are well-founded** in the cited literature. (Note: module D
"benefits/loads beyond the system boundary" has no corresponding workbook phase; that is a
defensible scoping choice for a screening KPI, not a defect.)

### 2. Is "Scope 1 + Scope 2 + Scope 3" a valid figure for a single life-cycle phase?

No. The literature treats per-phase emissions as a **partial CFP** built from
phase-specific processes, which is a different axis from the GHG-Protocol organizational
scopes.

> "**partial carbon footprint of a product**, partial CFP: sum of GHG emissions … and GHG
> removals … of **one or more selected process(es) … in a product system**, expressed as
> CO2 equivalents …" — ISO 14067 §3.1.1.2, `data/literature/ISO 14XXX/ISO 14067.pdf` p.12.

A phase emission = the partial CFP of the processes belonging to that phase. It is
**not** a re-summation of the whole-product Scopes 1/2/3. The GHG-Protocol scopes are an
**organizational inventory boundary** (own operations vs upstream/downstream value chain),
explicitly entity-level in every cited source:

> "Disclosure Requirement E1-6 – **Gross Scopes 1, 2, 3 and Total GHG emissions**. 44. The
> undertaking shall disclose in metric tonnes of CO2eq its: (a) gross Scope 1 GHG
> emissions; …" — ESRS E1, `data/literature/ESRS - European Sustainability Reporting
> Standards/ESRS E1 Delegated-act-2023-5303-annex-1_en.pdf` p.1 and p.9.
> "… an overall understanding of the undertaking's GHG emissions and whether they occur
> from its **own operations or the upstream and downstream value chain**." — same file,
> p.10.

> "(a) greenhouse gases—the entity shall: (i) disclose its **absolute gross greenhouse gas
> emissions** generated during the reporting period … classified as: (1) Scope 1 …; (2)
> Scope 2 …; and (3) Scope 3 …; (ii) measure its greenhouse gas emissions in accordance
> with the **Greenhouse Gas Protocol: A Corporate Accounting and Reporting** [Standard]"
> — IFRS S2, `data/literature/IFRS Sustainability - International Financial Reporting
> Standards/issb-2023-a-ifrs-s2-climate-related-disclosures.pdf` p.15.

**Conclusion:** setting `Actual = Scope1 + Scope2 + Scope3` for *every* phase is a
conflation of two orthogonal axes (organizational scope vs life-cycle stage) and, worse,
yields the **identical** value for all five phases (since the children are identical),
which defeats the stated purpose of EN14 ("identify hotspots … stages with the highest
emissions"). The model is **missing its per-phase inputs**. The correct inputs are
phase/stage-level CFP figures (EN 15804+A2 module values A1–A3, A4–A5, B1–B7, C1–C4, or
the ISO 14067 partial-CFP of each stage's processes).

This is not merely my inference — EN14's own Comment field already says the unweighted
result "should be the same as EN1-4" (the absolute PCF). That is precisely the symptom:
with identical Scope children, each phase reproduces the total instead of a stage share.

### 3. What should Min / Max represent for a normalized phase ratio?

The cited LCA/EPD standards deliberately **do not** provide benchmark or reference values:

> "NOTE 3 For the interpretation of a comparison, benchmarks or reference values are
> needed. **This standard does not set benchmarks or reference values.**"
> — EN 15804+A2 §5.3, `data/literature/EN15804+A2.pdf` p.19.

So Min/Max cannot be sourced from EN 15804 or ISO 14067. For a per-phase normalized ratio,
Min/Max must come from outside these standards — e.g. a per-phase target the company sets,
or a sector/PEF-EPD category benchmark for that stage. (The workbook already uses an
external "PEF/EPD sector reference value" idea in EN1-5; the same external-benchmark logic
is what the phase Min/Max should reference.) No quote in the cited corpus prescribes a
specific Min/Max for per-stage emissions; treat them as user-supplied targets/benchmarks
and document the source per product.

### 4. Do the scope-leaf reference codes actually concern Scope 1/2/3, and do any support
a per-life-cycle-phase decomposition?

- **ESRS E1-6** — yes, it is exactly "Gross Scopes 1, 2, 3 and Total GHG emissions"
  (quotes above, ESRS E1 p.1/p.9). Entity-level inventory; **no per-life-cycle-phase
  decomposition**.
- **IFRS S2** — yes, Scope 1/2/3 absolute gross GHG per GHG Protocol Corporate Standard
  (quote above, p.15). Entity-level; **no per-phase decomposition**.
- **SASB RT-CP-110a.1** — **Scope 1 ONLY**:
  > "Gross global Scope 1 emissions, percentage covered under emissions-limiting
  > regulations … RT-CP-110a.1" — `data/literature/SASB - Sustainability Account Standards
  > Board/RT-CP-containers-and-packaging-standard_en-gb.pdf` p.6; and "The entity shall
  > disclose its gross global Scope 1 greenhouse [gas] …" p.8.
  This code supports **EN1-1 (Scope 1) only**; it does **not** cover Scope 2 or Scope 3,
  and it offers **no** per-phase decomposition.

None of the three codes provides a life-cycle-stage breakdown. The per-phase axis is
supported only by ISO 14067 and EN 15804+A2 (Section 1 above) — neither of which is cited
on the phase rows.

---

## Per-row assessment

## EN131  Sourcing Emission Ratio
- Verdict: **UNSUPPORTED (under-specified)**
- Reference(s) on row: none cited. Inherited children: EN1-1/2/3 (Scopes 1/2/3) → ESRS
  E1-6, IFRS S2, SASB RT-CP-110a.1.
- Evidence: EN 15804+A2 p.17/p.6 (A1 "Raw material supply"); ISO 14067 p.7 ("raw material
  sourcing"); ISO 14067 §3.1.1.2 p.12 (partial CFP = selected processes); EN15804 p.19
  (no benchmarks).
- Assessment: The *name/concept* "sourcing emissions" maps cleanly to EN 15804 A1(–A2)
  and ISO 14067's raw-material-sourcing stage — that part is a faithful adaptation. The
  *computation* is not supported: the row's children are the three organizational Scopes,
  not the sourcing-stage processes, so `Actual` = whole-product Scope1+2+3, identical to
  every other phase. No source endorses equating a single life-cycle stage with the sum of
  all entity scopes.
- Issues: **[blocker]** wrong intermediate — `Actual` must be the sourcing-stage partial
  CFP, not Scope1+2+3. **[major]** no phase-specific emission input exists in the model.
  **[minor]** Min/Max source unspecified (EN15804 explicitly sets none).
- Recommendation: (c) flag under-specified + (b) change intermediate. `Actual` should be
  the EN 15804+A2 module **A1–A3** value (or at minimum A1–A2) / the ISO 14067 partial CFP
  of sourcing processes. Add a phase-emission raw input child (e.g. "Sourcing CO₂e") feeding
  this row; do not reuse EN1-1/2/3.

## EN132  Production Emission Ratio
- Verdict: **UNSUPPORTED (under-specified)**
- Reference(s): none on row; children as above.
- Evidence: EN 15804+A2 p.17 (A3 "Manufacturing"); ISO 14067 p.7 ("production"); §3.1.1.2 p.12.
- Assessment: Concept ("manufacturing & assembly emissions") = EN 15804 A3 / ISO 14067
  production stage — faithful. Computation identical defect to EN131.
- Issues: **[blocker]** `Actual`=Scope1+2+3 instead of production-stage partial CFP.
  **[major]** missing per-phase input. **[minor]** Min/Max source.
- Recommendation: (b)+(c). `Actual` = EN 15804+A2 module **A3** (production within A1–A3) /
  ISO 14067 partial CFP of manufacturing-and-assembly processes.

## EN133  Distribution Emission Ratio
- Verdict: **UNSUPPORTED (under-specified)**
- Reference(s): none on row; children as above.
- Evidence: EN 15804+A2 p.17 (A4 "Transport"); ISO 14067 p.8 ("transportation/delivery"); §3.1.1.2 p.12.
- Assessment: Concept ("distribution to end users") = EN 15804 A4 (transport) / ISO 14067
  transportation-delivery — faithful. Computation identical defect.
- Issues: **[blocker]** wrong intermediate. **[major]** missing per-phase input.
  **[minor]** Min/Max source.
- Recommendation: (b)+(c). `Actual` = EN 15804+A2 module **A4** (distribution transport) /
  partial CFP of distribution processes.

## EN134  Use and Maintenance Emission Ratio
- Verdict: **UNSUPPORTED (under-specified)**
- Reference(s): none on row; children as above.
- Evidence: EN 15804+A2 p.17/p.6 (B1–B7 Use stage: B1 Use, B2 Maintenance, … B6
  operational energy use); ISO 14067 p.8 ("use"); §3.1.1.2 p.12.
- Assessment: Concept ("operational use and maintenance over useful life") = EN 15804
  B1–B7 use stage / ISO 14067 use stage — faithful, and the row name even mirrors B1 "Use"
  + B2 "Maintenance". Computation identical defect.
- Issues: **[blocker]** wrong intermediate. **[major]** missing per-phase input.
  **[minor]** Min/Max source.
- Recommendation: (b)+(c). `Actual` = EN 15804+A2 modules **B1–B7** (or the maintenance-
  relevant subset B1–B5 + operational B6–B7) / partial CFP of use-and-maintenance processes.

## EN135  End-of-Life Emission Ratio
- Verdict: **UNSUPPORTED (under-specified)**
- Reference(s): none on row; children as above.
- Evidence: EN 15804+A2 p.17/p.6 (C1–C4 End-of-life: C1 Deconstruction/demolition, C2
  Transport, C3 Waste processing, C4 Disposal); ISO 14067 p.8 ("end-of-life treatment");
  §3.1.1.2 p.12.
- Assessment: Concept ("processing/handling at end of life") = EN 15804 C1–C4 / ISO 14067
  end-of-life — faithful. Computation identical defect. (Note: module D, recovery/recycling
  benefits beyond the boundary, is not represented; acceptable for a screening KPI but worth
  a comment.)
- Issues: **[blocker]** wrong intermediate. **[major]** missing per-phase input.
  **[minor]** Min/Max source; optional module-D note.
- Recommendation: (b)+(c). `Actual` = EN 15804+A2 modules **C1–C4** / partial CFP of
  end-of-life processes.

## EN14  Lifecycle Phase Emission  (context — parent)
- Verdict: **PARTIAL (adapted)**
- Reference(s): none on row (composite). Children EN131–135.
- Evidence: ISO 14067 p.7/p.8 (per-stage CFP); EN 15804+A2 p.17/p.6 (module breakdown).
- Assessment: The *concept* — break emissions down by life-cycle stage to find hotspots —
  is exactly what ISO 14067 and EN 15804+A2 enable, so EN14 is a sound, well-grounded
  composite. The defect is inherited: because all five children currently resolve to the
  same Scope1+2+3 sum, EN14's weighted average degenerates (its own Comment notes the
  unweighted result equals EN1-4, the total PCF). Once the children carry true per-stage
  inputs, EN14 becomes a valid hotspot indicator.
- Issues: **[major]** depends on under-specified children EN131–135. **[minor]** consider
  citing ISO 14067 / EN 15804+A2 on this row to document the stage-breakdown basis.
- Recommendation: keep the composite; fix the children first. Add ISO 14067 / EN 15804+A2
  as the reference for the stage breakdown.

## EN1-1  Scope 1 – Direct Emissions  (context — leaf)
- Verdict: **VERIFIED**
- Reference(s): ESRS E1-6 [→ ESRS E1, p.1/p.9], IFRS S2 [→ p.15], SASB-RT-CP-110a.1 [→
  RT-CP p.6/p.8].
- Evidence: ESRS E1 "gross Scope 1 GHG emissions" (p.9); IFRS S2 "(1) Scope 1 greenhouse
  gas emissions" (p.15); SASB "Gross global Scope 1 emissions … RT-CP-110a.1" (p.6),
  "direct (Scope 1) greenhouse gas (GHG) emissions from fossil fuel combustion in
  manufacturing" (p.8).
- Assessment: All three codes define Scope 1 direct emissions; the description (owned/
  controlled sources, fuel combustion, vehicles) matches. Unit kg CO₂e is consistent.
- Issues: none.
- Recommendation: keep as-is.

## EN1-2  Scope 2 – Purchased Indirect Emissions  (context — leaf)
- Verdict: **PARTIAL (adapted)**
- Reference(s): ESRS E1-6 [→ ESRS E1], IFRS S2 [→ p.15]. (SASB code correctly NOT cited.)
- Evidence: ESRS E1-6 "Gross Scopes 1, 2, 3" (p.1); IFRS S2 "(2) Scope 2 greenhouse gas
  emissions" (p.15); ESRS E1 energy list "purchased or acquired electricity, heat, steam,
  or cooling" (p.9).
- Assessment: ESRS E1-6 and IFRS S2 both cover Scope 2 (purchased electricity/heat/steam).
  Description matches. Correctly drops SASB RT-CP-110a.1 (which is Scope 1 only).
- Issues: none material.
- Recommendation: keep as-is.

## EN1-3  Scope 3 – Other Indirect Emissions  (context — leaf)
- Verdict: **PARTIAL (adapted)**
- Reference(s): ESRS E1-6 [→ ESRS E1, p.10], IFRS S2 [→ p.15].
- Evidence: ESRS E1 "downstream value chain beyond its Scope 1 and 2 GHG emissions … Scope
  3 GHG emissions may be the main component of their GHG inventory" (p.10); IFRS S2 "(3)
  Scope 3 greenhouse gas emissions" (p.15).
- Assessment: Both codes cover Scope 3 (value-chain indirect). Description matches.
- Issues: none material.
- Recommendation: keep as-is.

---

## Recommended actions (for the editor)

1. **Re-model EN131–135 inputs (blocker).** Stop using EN1-1/EN1-2/EN1-3 (Scopes 1/2/3) as
   the children of the phase ratios. Introduce five **phase-level emission raw inputs**
   (one per phase), each = the EN 15804+A2 module value(s) / ISO 14067 partial CFP for that
   stage:
   - EN131 Sourcing → A1–A3 (or A1–A2)
   - EN132 Production → A3
   - EN133 Distribution → A4 (and A5 if relevant)
   - EN134 Use & Maintenance → B1–B7
   - EN135 End-of-Life → C1–C4
   Set each row's `Actual` to its own phase input, not Scope1+2+3.
2. **Add a reference to the phase rows and EN14**: cite `ISO 14067` and `EN 15804`
   (both already resolve in References.tsv) as the basis for the life-cycle-stage breakdown.
3. **Document Min/Max as external** (target or PEF/EPD sector benchmark per phase). EN 15804
   p.19 explicitly sets no benchmarks, so the Min/Max cannot be standard-derived; record the
   source per product. Until phase inputs exist, keep the `needs_review` flag.
4. **EN1-1 — keep SASB RT-CP-110a.1 only on Scope 1** (already correct). Do **not** add it
   to EN1-2/EN1-3; it is Scope 1 only (RT-CP p.6/p.8). Current wiring is fine.
5. **Reference-integrity nit:** the grandparent **EN1** cites `WBCSD`, which has **no
   matching Label** in References.tsv (orphan code). Either add a WBCSD/GHG-Protocol row to
   References or replace it with a resolving code (e.g. ISO 14067, already present).

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker | EN131/132/133/134/135 | All five phase ratios use the same children EN1-1/2/3 (Scopes 1/2/3); engine sets `Actual = Scope1+2+3` for every phase, conflating org-scopes with life-cycle stages and making all phases equal (ISO 14067 p.12 partial-CFP is per-process; EN15804 p.17 stages are A/B/C modules) | Replace children with per-phase emission inputs mapped to EN15804 modules (A1–A3 / A3 / A4 / B1–B7 / C1–C4) or ISO 14067 partial CFP per stage |
| 2 | major | EN131–135 | No phase-specific emission input exists in the model; phase decomposition is not derivable from Scope 1/2/3 totals | Add five phase-level raw-emission inputs (one per phase) |
| 3 | major | EN14 | Composite degenerates: with identical Scope children, unweighted EN14 equals EN1-4 total (per its own Comment), so it cannot reveal hotspots | Fix children (item 1); concept is otherwise sound |
| 4 | major | EN1 | Reference code `WBCSD` does not resolve to any Label in References.tsv (orphan) | Add a WBCSD/GHG-Protocol row to References, or replace with ISO 14067 (already present) |
| 5 | minor | EN131–135 | `Min`/`Max` for the normalized ratio have no standard source; EN15804 §5.3 (p.19) explicitly sets no benchmarks/reference values | Document Min/Max as user target or PEF/EPD sector benchmark per phase; keep `needs_review` until set |
| 6 | minor | EN131–135, EN14 | Phase rows cite no reference for the stage-breakdown basis | Cite ISO 14067 and EN 15804 (both resolve) on these rows |
| 7 | minor | EN135 | End-of-life phase omits EN15804 module D (recovery/recycling benefits beyond boundary) | Acceptable for screening KPI; add a Comment noting module D is excluded |
| 8 | minor | EN14 / Formula | Formula text reads `Sum (weight * EN131 + … + weight * EN134)` — it stops at EN134 and omits the 5th child EN135 (End-of-Life), even though `Underlying Metrics` lists all five | Extend the formula's terminal term to include EN135 so the text matches the wired children |

**SOURCE-NOT-FOUND codes:** none among the audited rows. (`WBCSD`, cited on context row
EN1, is an unresolved Label in References.tsv — a reference-integrity orphan, item 4 — not a
missing PDF.)

**Limits of this run:** I verified module/stage names from EN 15804+A2 Figure 1 (PDF p.17)
and its TOC (p.6) plus the ISO 14067 definitions and stage list (p.7/8/12); I did not read
every module's full normative body text (EN15804 §6.2.x, §7.3.x) — the per-module emission
*calculation rules* were not audited line-by-line, only the module identity and the
partial-CFP definition. The exact numeric phase-to-module mapping a company should adopt
(e.g. whether Sourcing = A1–A3 or A1–A2, where to place A5) is a modelling decision to
confirm with the LCA practitioner; the literature supports the stage existence and naming,
not a single canonical phase grouping. Min/Max benchmark values were not found in the cited
standards (by design, EN15804 p.19) and remain external inputs.
