# C description audit — refine + ground KPI descriptions

**Scope:** the full **Circular Efforts (C) domain — all 59 KPIs**, audited family by family
(C1 Reclamation, the C2 Process-Quality sub-trees + raw leaves, C3 Design for Circularity,
C4 Circular Flow Index, C5 EoL handling, C0 root). Goal: reconcile each handmade description
with its *current* implementation (Calculation Strategy, Formula, parent/child relations after
the gap-fix re-model) and ground it in the cited literature where a source applies.
**Date:** 2026-06-29.
**Method:** current state from `snapshot/Circular Efforts.tsv` (+ `References.tsv`); every
literature claim is a verbatim page-cited quote via `tools/scripts/pdf_search.py`; conservative
stance — intentional adaptations kept faithful + flagged, not rewritten to match a source.
**Verdict legend:** CONSISTENT = text matches current implementation (+ literature where cited);
DRIFTED = text no longer matches the current Formula / Strategy / relations (propose a fix);
ADAPTED = faithful adaptation of a source concept (keep + flag); UNVERIFIABLE = author-defined,
no citable source (legitimate).
Columns on the sheet: C=Description, G=Potential Reference Values, H=Unit, I=Formula,
J=Reference, R=Comment.

---

## C domain — consolidated summary & decisions

**Verdicts across all 59 C KPIs:** CONSISTENT 39 · DRIFTED 10 · ADAPTED 8 · UNVERIFIABLE 2.
Strong literature coverage (DIN SPEC 91472, ISO 59020, Cradle to Cradle, MCI). The dominant
defect is the same stale-text pattern seen in EN/EC — aggregate Formula cells and descriptions
that didn't follow the gap-fix re-model — plus several citation problems. Per-family detail
follows; nothing applied yet — all proposals.

### A. Description rewrites — DRIFTED rows (10)

| KPI | Problem | Proposed |
|---|---|---|
| C0 | stale Formula `…+C3` (children are C1–C5); desc "R3-R7" conflicts with C3's "R1-R3" | name all 5 children; extend formula to C5 |
| C1 | desc names only the C11+C12 arms, drops C13 (recovery yield) | 3-arm rewrite |
| C2 | Formula `…C21+C22` omits C23; desc drops remanufacturing | name C21/C22/C23 |
| C23 | Formula `…C231+C233` omits C232 (prose is fine) | add C232 to formula |
| C231 ⚠️ | Formula text `new inflow / secondary inflow` names non-children + is inverted vs the live `C2-13/C2-11` | rewrite formula text + desc to remanufactured-component share |
| C32 | Formula carries a stray "Reusability" token (should be Remanufacturability) | fix token + desc |
| C34 | desc still pre-re-model ("ease of separating"); ignores the self-normalized children | rewrite to weighted-average of C3-5/C3-6 |
| C3-5 | desc omits self-normalization; **blank Formula**; "User Feedback" wrongly in Parent-Metrics col | rewrite + add formula + move stray token |
| C3-6 | desc omits normalization + the lower-is-better direction | rewrite; mirror the load-bearing Comment |
| C4 | desc narrates linear LFI but formula outputs `1−LFI` (circular) — direction mismatch | rewrite to the circular-flow index — **see D-formula** |

### B. Adjacent-cell drift — Formula text & a precedence bug (apply with the rewrites)

- Stale child lists: `C0` (`…+C3`→C5), `C2` (add C23), `C23` (add C232), `C231` (inverted →
  `C2-13/C2-11`), `C32` (stray "Reusability"→"Remanufacturability"), `C3-5` (blank → add formula).
- **C4 precedence bug:** the Formula text `… / 2 * Total Mass Flow` evaluates to `(…/2)·M`, not
  `…/(2·M)` — needs parentheses; and C4-3 should hold product mass **M** (the formula already
  doubles it), not 2M. *(Engine computation is encoded separately in formulas.py and is correct;
  this is the displayed-formula text.)*

### C. Citation issues

- **C4 / C4-1 / C4-2 / C4-3 — MCI** → **decision D1**. `MCI+15`/`MCI+16` don't resolve, but
  `data/literature/MCI.pdf` IS in the corpus under label **`MCI+25`**, which grounds C4 verbatim
  (LFI = (V+W)/2M, p.28).
- **C233 — "success rate" name vs count-only formula** → **decision D2**.
- **C3 family unciteable codes** → **decision D3**: `FB+16` (on C34/C3-5) resolves to a
  **mis-filed PDF** (a maintenance essay, not the Flipsen reparability indicator); `FHC+14`,
  `ZP+06` (C34), `EN 45554` (C34), `EN 45557` (C31) have **no PDF** in the corpus (the concepts
  are independently grounded by ISO 59020 / C2C / ESRS E5).
- **C1 — wrong SASB code** → **decision D4**: `SASB RT-250a.1` resolves but the cited metric
  (RT-CP-250a.1) is *chemicals-of-concern disclosure*, not reclamation/take-back.
- Blank References with a citable concept: **C13**, **C5** → add `ISO 59020`; **C32** → add
  `DIN SPEC 91472`.

### D. Decisions — RESOLVED 2026-06-29

1. **C4 MCI → re-cite `MCI+25`. ✓** Set C4/C4-1/C4-2/C4-3 Reference to `MCI+25` (the corpus
   MCI.pdf label); also fix the C4 formula-text parentheses (`…/(2·M)`) + the LFI→circular
   direction in the description.
2. **C233 → reword to match the formula. ✓** Rename/redescribe as "remanufactured output
   volume (normalized)" so the text matches the count-normalization it actually computes
   (no intake denominator). No model change.
3. **C3-family unciteable codes → drop them. ✓** Remove `FB+16` (mis-filed), `FHC+14`, `ZP+06`,
   `EN 45554`, `EN 45557` from the Reference cells; rely on the groundable ISO 59020 / C2C /
   ESRS E5 (added where the cell would otherwise go blank).
4. **C1 wrong SASB code → drop `SASB RT-250a.1`. ✓** Off-topic chemicals disclosure; add a
   Comment noting no clean SASB reclamation code exists.

### E. ADAPTED Comment flags (non-obvious only)

C11 (weight-based, packaging-only vs GRI 301-3's count-based products+packaging), C21
(refurbishment-to-saleable vs DIN SPEC 91472 §3.6 "not placed on the market"), C32/C33, C4-3,
C5 — keep the description, add a short Comment-cell note where the adaptation isn't self-evident;
skip obvious ones, matching the EN/EC policy.

## C1 — Reclamation Efficiency

### C1 — Reclamation Efficiency  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures the effectiveness of the product's return and reclamation processes. Includes how effective are the packaging and product recovered from the market."
- **Verdict:** DRIFTED (description omits the third arm) + citation content-mismatch on `SASB RT-250a.1`.
- **Grounding:**
  - GRI 301-3, `…/GRI 301_ Materials 2016.pdf` p.10: "Disclosure 301-3 Reclaimed products and their packaging materials … Percentage of reclaimed products and their packaging materials = Products and their packaging materials reclaimed within the reporting period / Products sold within the reporting period x 100." (grounds the *reclaimed products + packaging* concept the parent aggregates)
  - C2C §5.2, `…/c2c-certified-full-scope_v4.1_final_011525.pdf` p.36: "5.2: Partnerships for cycling (recovery and processing) of the product have been initiated." (grounds the take-back/recovery-program intent of "To assess the effectiveness of the reclamation method / program")
  - CS+16, `…/CS+16-Design of Indicators…pdf` p.29: "What take-back scheme is available for this product? Product Recovery - Availability of Take Back Schemes. Take-back schemes enables customers to dispose of their unwanted products and provide a mechanism for the recapture of materials and their [r]eintroduction into the supply chain."
- **Implementation check:** `Underlying Metrics = C11\nC12\nC13`, strategy WEIGHTED_AVERAGE; Formula `Sum (weight * C11 + … + weight * C13)`. The three children are (C11) reclaimed *packaging* rate, (C12) reclaimed *products* (EoL take-back) rate, (C13) *recovery yield* of what is reclaimed. The current description names only two arms — "packaging and product recovered" — and silently drops C13 (recovery yield/quality of the reclamation). Unit % matches a weighted average of three ratio children. Children all exist and are wired.
- **Proposed revision (C):** "Aggregates how effective the product's return and reclamation processes are, combining the reclaimed-packaging rate (C11), the end-of-life product take-back rate (C12), and the recovery yield of the reclaimed products (C13). Indicates how much of what is sold returns and how usefully it is recovered."
- **Notes (adjacent fixes):**
  - **[major] Citation content-mismatch (J).** `SASB RT-250a.1` resolves to a Label but the actual metric in the cited PDF is off-topic: `…/RT-CP-containers-and-packaging-standard_en-gb.pdf` p.6: "RT-CP-250a.1 Discussion of process to identify and manage emerging materials and chemicals of concern." That is chemicals-of-concern disclosure, not reclamation/take-back. **Fix:** drop `SASB RT-250a.1` from C1's Reference. If a SASB anchor is wanted, the nearest on-topic code is RT-CP-410a.2 (same PDF p.7: "Revenue from products that are reusable, recyclable, or compostable") — but that is revenue-based, only a loose fit, so a Comment note ("SASB has no direct reclamation-rate metric") is preferable to swapping in a weak code.
  - GRI 301-3 / C2C 5.2 / CS+16 / FE+16 all stay (each grounds an arm of the parent). Composite/parent — no single source computes this exact weighted score; that is by design.

### C11 — Reclaimed Packaging Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of returned packaging. Normalized through the expected or target number of reclaimed packaging."
- **Verdict:** ADAPTED — faithful weight-based adaptation of the *packaging* arm of GRI 301-3.
- **Grounding:**
  - GRI 301-3, `…/GRI 301_ Materials 2016.pdf` p.10 (guidance): "The reporting organization can also report recycling or reuse of packaging separately." (supports splitting packaging out as its own ratio — exactly what C11 does)
  - GRI 301-3 formula, same page: "= Products and their packaging materials reclaimed within the reporting period / Products sold within the reporting period x 100."
- **Implementation check:** Children `C1-3` (Reclaimed Packaging Materials Weight, kg) and `C1-4` (Total Sold Packaging Weight, kg); Formula `Reclaimed = Reclaimed packaging material weight / Total Sold Packaging Weight`, then `(Reclaimed - Min)/(Max - Min)`. So the ratio is **weight/weight (kg)**, not a count. The description says "share of returned packaging" (consistent) but the normalization sentence ("Normalized through the expected or target number of reclaimed packaging") is loose: (a) it is normalized by *weight* of packaging *sold*, not a "number", and (b) the Min/Max band is the score normalization, distinct from the denominator. Unit % consistent. Note: G="Target Value: min, max"; Comment already explains Min/Max default 0/1.
- **Proposed revision (C):** "Measures the share, by weight, of sold packaging that is returned/reclaimed (reclaimed packaging weight C1-3 ÷ total sold packaging weight C1-4). A weight-based, packaging-only adaptation of the GRI 301-3 reclaimed-packaging disclosure; the result is scored against the company's target band (Min/Max)."
- **Notes (adjacent fixes):**
  - Adaptation is **non-obvious** (GRI 301-3 is count/product-category based and combines products+packaging; C11 is weight-based and packaging-only). **[minor] Propose Comment flag (R):** "Weight-based, packaging-only adaptation of GRI 301-3 (which is count-based over products sold and combines products + packaging)."
  - J = `GRI 301-3` stays — correct and exact-fit for the packaging arm.

### C12 — End-of-Life Product Reclamation Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of returned products  after the expected use time. An existing program such as take-back policies must exist. Does NOT include recalls and rejects. The focus is to reclaim products that have fulfilled their use purpose."
- **Verdict:** CONSISTENT (with literature) / ADAPTED (count-based product-only ratio) — and notably the description's "Does NOT include recalls and rejects" is *directly* grounded in GRI 301-3.
- **Grounding:**
  - GRI 301-3, `…/GRI 301_ Materials 2016.pdf` p.10: "2.4.1 exclude rejects and recalls of products" (verbatim basis for "Does NOT include recalls and rejects").
  - GRI 301-3 formula, same page: "= Products … reclaimed within the reporting period / Products sold within the reporting period x 100" (count of products over products sold — matches C12).
  - FE+16, `…/FE+16-Resource duration…pdf` p.4: "Where w is the percentage of products returned, x is the percentage of these products refur-bished …" — grounds using a product-return percentage as a managerial CE input; p.1: "managers should encourage … increase product return levels for initial use and refurbished phones."
  - C2C §5.2 (p.36, take-back partnerships, quoted under C1) grounds the "existing take-back program must exist" condition.
- **Implementation check:** Children `C1-1` (Number of Units Sold) and `C1-2` (Amount of Reclaimed Units); Formula `Reclaimed = Number of reclaimed product / Number of units sold`, then normalized. Count/count ratio. Description matches the formula and the GRI 301-3 product arm precisely; the "after expected use time / fulfilled their use purpose" qualifier is the author's EoL scoping (consistent with separating EoL returns from in-warranty recalls). Unit % consistent.
- **Proposed revision (C):** "Measures the share of sold products that are returned at end of life through a take-back program (reclaimed units C1-2 ÷ units sold C1-1). Counts only products that have fulfilled their use purpose; excludes recalls and rejects (per GRI 301-3). Requires an existing take-back/return program."
- **Notes (adjacent fixes):**
  - **[minor] Double space** in current text ("products  after").
  - Adaptation (product-only, count-based, EoL-scoped) is reasonably **self-evident** given the name — a Comment flag is optional, not required. J = `GRI 301-3\nFE+16` both stay (correct).

### C13 — Recovery Yield of Reclaimed Products  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the proportion of material or components that can be effectively reused, refurbished, or recycled from the EoL reclamations. Due to various reasons, not 100% of the reclaimed product could be used."
- **Verdict:** CONSISTENT (with implementation); UNVERIFIABLE-leaning on citation (no Reference cited; concept is groundable in ISO 59020 if a code is wanted).
- **Grounding (optional, if a code is added):**
  - ISO 59020, `…/ISO-59020.pdf` p.12: "asset refers to physical resources such as natural resources, virgin resources, recoverable resources and recovered resources" and "3.3.13 losses: unmanaged outflows of a resource … that are not recovered." (grounds the recovered-vs-not-recovered yield framing)
  - GRI 301-3 does **not** cover *yield/quality* of reclaimed material (it is a reclamation-rate disclosure), so C13 is correctly *not* a GRI 301-3 metric.
- **Implementation check:** Children `C1-5` (Reclaimed Units Weight, kg) and `C1-6` (Valuable components weight, kg); Formula `Recovered = Weight of valuable unit components / Weight of Reclaimed Units`, then normalized. The description ("proportion of material/components that can be effectively reused/refurbished/recycled … not 100% usable") matches the valuable/reclaimed weight ratio. Unit % consistent. Reference cell (J) is **blank**.
- **Proposed revision (C):** "Measures the proportion, by weight, of reclaimed end-of-life products that yields valuable, reusable components (valuable component weight C1-6 ÷ reclaimed units weight C1-5). Reflects that not all of a reclaimed product can be recovered; the rest becomes scrap. Indicates the quality of the reclamation/recovery pipeline."
- **Notes (adjacent fixes):**
  - **[minor] Blank Reference (J).** The recovery-yield concept is groundable in ISO 59020 (recovered vs. not-recovered resource outflows). **Optional fix:** add `ISO 59020` to J (consistent with how sibling families C31/C32 already cite ISO 59020). Leave blank only if the author prefers to treat C13 as author-defined. Either is defensible; flag for the author to decide.

### C1-1 — Number of Units Sold  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total number of units sold to customers."
- **Verdict:** CONSISTENT — clear raw count; Unit `#` fits; Parent `C12` exists and uses it as the denominator. No citation expected on a raw leaf.
- **Proposed revision (C):** keep as-is (clear and unambiguous).
- **Notes:** none. (No Reference appropriate; raw input.)

### C1-2 — Amount of Reclaimed Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total number of units reclaimed from their EoL."
- **Verdict:** CONSISTENT — raw count, Unit `#`, feeds C12 numerator. `GRI 301-3` on a raw leaf is harmless (it is the family's source) though the disclosure itself is the *ratio*, not this raw count.
- **Grounding:** GRI 301-3 p.10 (reclaimed-products numerator, quoted above).
- **Proposed revision (C):** "Total number of end-of-life units reclaimed/returned within the reporting period (numerator of C12)."
- **Notes:** [minor] J=`GRI 301-3` is acceptable as a family anchor; optional to drop on the raw leaf since the GRI metric is the ratio, not the raw count. Low priority.

### C1-3 — Reclaimed Packaging Materials Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total amount of packaging of unit reclaimed after the purchase."
- **Verdict:** CONSISTENT — raw weight (kg) feeding C11 numerator; slightly awkward wording.
- **Grounding:** GRI 301-3 p.10 guidance ("report recycling or reuse of packaging separately") supports a packaging-specific input.
- **Proposed revision (C):** "Total weight of packaging reclaimed/returned after purchase (numerator of C11)."
- **Notes:** [minor] tidy wording ("packaging of unit reclaimed" → "packaging reclaimed"). J=`GRI 301-3` acceptable as family anchor.

### C1-4 — Total Sold Packaging Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total weight of packaging materials sold to customer."
- **Verdict:** CONSISTENT — raw weight (kg), C11 denominator; Unit fits. No citation (J blank) — fine for a raw leaf.
- **Proposed revision (C):** keep as-is (clear).
- **Notes:** none.

### C1-5 — Reclaimed Units Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total weight of units reclaimed from their EoL."
- **Verdict:** CONSISTENT — raw weight (kg); Parents `C13\nC5` both exist (C13 denominator; also feeds the Circular EoL-handling parent C5, out of this batch). No citation needed.
- **Proposed revision (C):** keep as-is. (Optional: "Total weight of end-of-life units reclaimed (denominator of C13; also feeds C5).")
- **Notes:** none.

### C1-6 — Valuable components weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total weight of valuable components recovered from the overall reclaimed units. The rest of the non-valuable components will be used for scrap."
- **Verdict:** CONSISTENT — raw weight (kg), C13 numerator; description matches and explains the scrap remainder. No citation (J blank) — fine for a raw leaf.
- **Proposed revision (C):** keep as-is. (Optional: capitalize "Valuable components weight" → "Valuable Components Weight" for naming consistency with siblings.)
- **Notes:** [minor] inconsistent name casing vs. peers (lower-case "components weight"); cosmetic.

---

## Batch summary

**Verdicts (10 rows):** CONSISTENT 7 (C1-1, C1-2, C1-3, C1-4, C1-5, C1-6, C12 also literature-consistent) · DRIFTED 1 (C1) · ADAPTED 2 (C11, C12) · UNVERIFIABLE 0.
- Counting the sub-scores explicitly: **C1** DRIFTED (omits C13 arm + bad SASB code); **C11** ADAPTED; **C12** CONSISTENT/ADAPTED (literature-exact on the recalls/rejects exclusion); **C13** CONSISTENT impl., citation-blank; the six leaves C1-1…C1-6 CONSISTENT.

**Adjacent fixes proposed (Formula / citation):**
- C1 Reference (J): **drop `SASB RT-250a.1`** — its resolved metric (RT-CP-250a.1, chemicals of concern) does not cover reclamation. [major]
- C1 description (C): rewrite to name all three children (C11 packaging, C12 product take-back, **C13 recovery yield**). [DRIFTED]
- C13 Reference (J): optionally **add `ISO 59020`** to ground recovery-yield (recovered vs. not-recovered resource). [minor, author decision]
- C11 Comment (R): add a non-obvious-adaptation flag (weight-based, packaging-only vs. GRI 301-3 count-based products+packaging). [minor]
- C12 description (C): remove double space; otherwise keep (well-grounded). [minor]
- C1-2 / C1-3 naming/citation tidy-ups; C1-6 name casing. [minor, cosmetic]

**SOURCE-NOT-FOUND:** none — every cited code in this batch resolves to a Label and a PDF.

**Decisions the user must make:**
1. **C1 SASB code:** confirm dropping `SASB RT-250a.1` (recommended). Optionally note in C1's Comment that SASB has no direct reclamation-rate metric (RT-CP-410a.2 is revenue-based, weak fit). 
2. **C13 citation:** add `ISO 59020` as the recovery-yield anchor, or leave C13 as an author-defined (no-citation) ratio. Both defensible.
3. **C11 framing:** confirm C11 stays weight-based packaging-only (current formula) vs. aligning to GRI 301-3's count/product-category form. The proposed revision assumes the weight-based form stays.

**Limits of this run:** Only the C1 family was audited. C5 (Circular EoL handling) shares the
leaf C1-5 as a child and overlaps conceptually with C13 (recovery yield); the C1↔C5 relationship
and any double-counting were **not** assessed here. The Min/Max scoring band (G, Target Min/Max) is
out of scope per `reviews/min-max-sourcing.md` and was not re-derived. No quote was taken from
memory; all grounding is from the five PDFs listed in the reference-integrity table. The SASB
RT-CP PDF was searched for take-back/reclamation/recovery; no reclamation-*rate* metric exists in
it (only RT-CP-410a.2 revenue-from-reusable/recyclable and RT-CP-250a.x chemicals/recalls).


---

## C2 — Process Quality & Performance: refurbish / repair / remanufacture sub-trees

### C2 — Process Quality and Performance  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the effectiveness and efficiency of the refurbishment and repair
  processes for the product."
- **Verdict:** DRIFTED — the description names only **two** processes ("refurbishment and
  repair"), but `Underlying Metrics = C21\nC22\nC23` now wires **three** children
  (refurbishment C21, repair C22, **remanufacturing C23**). The displayed Formula
  `Sum (weight * C21 + weight * C22)` also omits C23. Classic gap-fix drift: the
  remanufacturing arm was added as a child but the prose + formula text still describe the
  two-process model.
- **Grounding:** DIN SPEC 91472 p.14 (5.1 Process quality, quote above) grounds the
  "process quality" framing of the parent; the three process families map onto DIN SPEC 3.6 /
  3.9 / 3.7 (refurbishment / repair / remanufacturing). Composite parent — no single source
  expected to cover the aggregate.
- **Implementation check:** Children C21, C22, C23 all exist; strategy WEIGHTED_AVERAGE,
  Unit % consistent with averaging three 0–1/% sub-scores. The two cited codes resolve:
  `C2C 5.3` (References line 59) and `ESRS E5-2` (References line 64). Both are org/standard-
  level circularity-process anchors, defensible for an aggregate but neither prescribes the
  3-arm roll-up (author-defined composite). No child-existence problem; the drift is prose +
  formula text only.
- **Proposed revision (C):** "Aggregates the product's circular-process performance into one
  score by combining the refurbishment (C21), repair (C22), and remanufacturing (C23) process
  sub-scores. Provides an overview of all circular processes to locate potential improvements."
- **Notes / adjacent fixes:**
  - **[major] Formula (I) is stale:** `Sum (weight * C21 + weight * C22)` → should read
    `Sum (weight * C21 + weight * C22 + weight * C23)` to match the three current children.
  - Stage cell shows only `E`; the children span M,E (refurb) / P,U,E (repair) / E (reman) —
    optional: broaden to `M,P,U,E`. Not a description issue; flagged for consistency.
  - Composite parent — keeping `C2C 5.3` + `ESRS E5-2` is fine; no Comment flag needed (the
    aggregate nature is self-evident from the children).

---

## C21 family — Refurbishment

### C21 — Refurbishment Process Performance  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the overall effectiveness of the refurbishment processes, focusing on
  the ability to restore products to a saleable condition."
- **Verdict:** CONSISTENT (composite; internal check) — prose correctly rolls up the three
  refurbishment children: success rate (C211), quality vs new (C212), timeliness (C213).
  `Underlying = C211\nC212\nC213`, Formula `Sum (weight * C211 + … + weight * C213)`, strategy
  WEIGHTED_AVERAGE, Unit %. Formula text matches children (no stale-child drift here).
- **Grounding:** DIN SPEC 91472 p.7 (3.6 refurbishment, quote above) defines refurbishment as
  restoring functionality/performance to a "fully functional high-quality used product that
  can be used again for the original purpose" — the standard says **"is not placed on the
  market"**, whereas the KPI scopes refurbishment to a *saleable* condition. Minor scope
  nuance worth a Comment flag (see notes). `FAC+21` (cited) p.7 grounds Refurbish (R5) =
  "Restore an old product and bring it up to date."
- **Implementation check:** All three children exist; composite roll-up internally consistent.
- **Proposed revision (C):** "Aggregates the refurbishment process into one score by combining
  its success rate (C211), the quality of refurbished products versus new (C212), and process
  timeliness (C213). Reflects the overall ability to restore returned products to a resalable,
  fully-functional condition."
- **Notes / adjacent fixes:**
  - [minor] Comment-cell flag (NON-obvious adaptation): DIN SPEC 91472 (3.6) defines
    refurbishment as resulting in a used product **"not placed on the market"**; this KPI
    treats refurbishment as restoring to a *saleable* condition — a deliberate product-business
    adaptation. Note in R: "Refurbishment here = restore-to-resalable; DIN SPEC 91472 §3.6
    defines refurbishment as not placed on the market — product-level adaptation."
  - `FAC+21` citation is appropriate as conceptual/framework grounding (keep).

### C211 — Refurbishment Success Rate  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the rate at which products that pass the refurbishment process.
  Ideally all incoming products should pass the refurbishment process, not all units can be
  restored to a sellable or usable condition due to varying issues."
- **Verdict:** ADAPTED (concept) / UNVERIFIABLE (exact ratio) — the pass-rate concept maps to
  DIN SPEC 91472's end-of-line testing (Table 1 "Quality monitoring", p.16), but the specific
  `successful / processed-intake` success-rate formula is author-defined; no retrieved source
  prescribes it. Text matches the formula and children, so no drift.
- **Grounding:** DIN SPEC 91472 p.16 (Table 1, Quality monitoring, Class A): *"End of line
  testing where functionality is tested according to the new product, or as-new functionality
  is ensured via process capability"* — grounds the "pass the process" / functional-check
  concept. The yield *ratio* itself is author-defined.
- **Implementation check:** Children C2-1 (units assigned for refurbishment) and C2-2
  (successful refurbished units) both exist; Formula
  `Success = Number of successful refurbished products / Number of processed products intake`
  then `(Success - Min)/(Max - Min)`. Unit % consistent; strategy NORMALIZED_RATIO matches.
  Min/Max seeded default (Comment documents the 0–1 score). No drift.
- **Proposed revision (C):** "Measures the yield of the refurbishment pipeline: the share of
  units entering refurbishment (C2-1) that pass quality checks and are restored to a usable/
  resalable condition (C2-2). Higher means fewer units are lost in refurbishment."
- **Notes / adjacent fixes:**
  - First sentence is grammatically broken ("the rate at which products that pass") — the
    proposed revision fixes it.
  - [minor] Reference (J) currently `FAC+21` only — defensible as conceptual anchor; the
    success-rate formula is author-defined. Optional Comment-cell flag (NON-obvious): "Yield
    ratio is author-defined; FAC+21 grounds the refurbishment concept, not this formula;
    end-of-line pass concept per DIN SPEC 91472 Table 1 (Quality monitoring)."

### C212 — Quality of Refurbished Products  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the test performance of refurbished products against new products.
  Depends highly on its testing standards. Applicable to companies with an established testing
  process. Ideally achieves the same or better test results as new-products."
- **Verdict:** CONSISTENT (with the formula) / ADAPTED (grounding) — prose matches
  `Quality = Avg(test results of refurbished) / Avg(test results of new-products)` over
  children C2-3 (refurbished test result) and C2-4 (new test result). No drift.
- **Grounding:** DIN SPEC 91472 p.16 (Table 1, Quality monitoring, Class A): *"End of line
  testing where functionality is tested according to the new product"* — directly grounds
  benchmarking refurbished performance **against the new product**. `NB+20` (cited, References
  line 35) is about quality *certification* of refurbished products (incentive alignment),
  conceptually adjacent but not a test-ratio formula.
- **Implementation check:** Children C2-3, C2-4 exist; ratio dimensionless then normalized to
  %, Unit % consistent. Strategy NORMALIZED_RATIO matches. No drift.
- **Proposed revision (C):** "Benchmarks the average test performance of refurbished units
  (C2-3) against that of new units (C2-4); higher when refurbished units perform as well as or
  better than new. Requires an established, consistent product-testing process."
- **Notes / adjacent fixes:**
  - `NB+20` citation is defensible as a refurbished-quality anchor; keep. DIN SPEC 91472
    "tested according to the new product" is the cleaner formula ground — optional to add
    `DIN SPEC 91472` to J. No Comment flag needed (the new-vs-refurbished benchmark is the
    obvious reading of the formula).

### C213 — Timeliness of Refurbishment  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the time taken to produce one unit of product from start to finish
  compared to planned time."
- **Verdict:** UNVERIFIABLE (author-defined) / minor wording drift — the metric is a cycle-time
  ratio normalized against a Min/Max band; the description's "produce one unit of product"
  reads like a *manufacturing* throughput line rather than a *refurbishment* cycle time.
- **Grounding:** none citable — no retrieved source (DIN SPEC 91472, ISO 59020, FAC+21)
  prescribes a refurbishment-timeliness ratio. DIN SPEC 91472 mentions process steps (p.11)
  but no time-based KPI. Legitimately author-defined.
- **Implementation check:** Child C2-5 (Refurbishment Process Time, days) exists; Formula
  `(Avg (Refurbishment Process Times) - Min)/(Max - Min)`, NORMALIZED_RATIO, Unit %. Note
  Potential Reference Values (G) lists "Target Value: min, max\nIndustry Average". The
  Example Values "2\n5" represent the band, not a computed value. Lower time is better, so the
  Min/Max band direction matters (Max = worst-acceptable time) — consistent with the C3-6
  pattern flagged elsewhere.
- **Proposed revision (C):** "Measures how quickly the refurbishment process completes a unit
  (average refurbishment cycle time, C2-5) relative to a target or planned time. Lower cycle
  times score higher. Intended to reduce time-to-resale."
- **Notes / adjacent fixes:**
  - [minor] Reference (J) blank — appropriate (author-defined timeliness ratio; no citable
    formula). Mark verdict UNVERIFIABLE (legitimate), no Comment flag required.
  - [minor] band-direction note in R (lower time is better — set Max = worst-acceptable time),
    mirroring the existing C3-6 guidance, would help.

---

## C22 family — Repair

### C22 — Repair Process Performance  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the efficiency and effectiveness of repair operations of the product."
- **Verdict:** CONSISTENT (composite; internal check) — prose correctly summarizes a roll-up of
  repair success (C221), longevity of repair (C222), and repair timeliness (C223).
  `Underlying = C221\nC222\nC223`, Formula `Sum (weight * C221 + … + weight * C223)`, strategy
  WEIGHTED_AVERAGE, Unit %. Formula text matches children — no drift.
- **Grounding:** DIN SPEC 91472 p.7 (3.9 repair, quote above): *"targeted elimination of
  defects or damage to a defective product to restore it to the same condition as it was in
  before it needed repair."* `FAC+21` p.7 (Repair R4) corroborates. Composite parent — no
  single source for the roll-up.
- **Implementation check:** All three children exist; roll-up internally consistent. Reference
  (J) blank — appropriate for a composite parent.
- **Proposed revision (C):** "Aggregates the repair process into one score by combining repair
  success rate (C221), the longevity gained from repairs (C222), and repair timeliness (C223).
  Reflects the overall quality, durability and speed of repair operations."
- **Notes / adjacent fixes:** none beyond the optional explicit-children rewrite. No Comment
  flag needed.

### C221 — Repair Success Rate  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the rate at which products that pass the repair process. Ideally all
  incoming products should pass the repair process. Gives overall overview on the
  effectiveness of current repair processes."
- **Verdict:** ADAPTED (concept) / UNVERIFIABLE (exact ratio) — same shape as C211: the
  pass-rate concept is groundable, the specific `successful / assigned` ratio is author-defined.
  Text matches formula and children, so no drift (aside from the broken first sentence).
- **Grounding:** DIN SPEC 91472 p.7 (3.9 repair) grounds the "restore to working condition"
  concept; the pass/yield concept aligns with end-of-line functional checks (p.16, Table 1).
  The success ratio itself is author-defined.
- **Implementation check:** Children C2-6 (units assigned for repair) and C2-7 (successful
  repaired units) exist; Formula `Success = Successful Repaired Units / Units assigned for
  Repair`, NORMALIZED_RATIO, Unit %. Note Example Values `100\n0` are a band example (the
  Comment documents the 0–1 score), not a computed value. No drift.
- **Proposed revision (C):** "Measures the yield of the repair pipeline: the share of units
  entering repair (C2-6) that pass post-repair quality checks (C2-7). Higher means fewer
  repair failures or re-work iterations."
- **Notes / adjacent fixes:**
  - First sentence grammatically broken ("the rate at which products that pass") — fixed above.
  - [minor] Reference (J) blank, while its refurbishment sibling C211 carries `FAC+21`. The
    repair concept is groundable in DIN SPEC 91472 (3.9). Add `DIN SPEC 91472` (and optionally
    `FAC+21`) so the row is auditable; mark verdict ADAPTED. Optional Comment flag (NON-obvious):
    "Yield ratio author-defined; repair concept per DIN SPEC 91472 §3.9."

### C222 — Longevity of repaired product  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the additional lifespan a product achieves after undergoing repairs.
  It assesses how effectively repairs can prolong the usability of products."
- **Verdict:** CONSISTENT (with formula) / ADAPTED (grounding) — prose matches
  `Longevity = Lifespan of Repaired Units / Original Lifespan of Units` over children C2-8
  (repaired lifespan) and C2-9 (original lifespan). No drift. Note the formula is a *ratio of
  lifespans* (repaired ÷ original), not strictly "additional" lifespan — minor wording nuance.
- **Grounding:** FE+16 p.1 (longevity indicator, quote above): *"the longevity indicator,
  which measures contribution to material retention based on the amount of time a resource is
  kept in use … initial lifetime, earned refurbished lifetime and earned recycled lifetime."*
  — grounds the lifetime-extension framing (cited `FE+16`, `RE+20` also on row). ISO 59020 p.13
  (3.3.20 durability, quote above) grounds durability at standard level (cited `ISO 59020`).
  `ESRS E5-5`, `SRS+20`, `RE+20` also cited — all resolve in References. The specific
  repaired/original lifespan *ratio* is the author's adaptation of FE+16's longevity idea.
- **Implementation check:** Children C2-8, C2-9 exist (both years); ratio dimensionless then
  normalized %, Unit % consistent. Strategy NORMALIZED_RATIO matches. All five cited codes
  resolve.
- **Proposed revision (C):** "Measures how much repairs extend a product's usable life, as the
  ratio of post-repair lifespan (C2-8) to original lifespan (C2-9). Higher means repairs
  restore more lasting value and reduce repeat repairs."
- **Notes / adjacent fixes:**
  - Description says "additional lifespan" but the formula computes the *ratio* of repaired-to-
    original lifespan; the proposed revision aligns the wording to the ratio. Minor.
  - Citation set is rich and resolves; no Comment flag needed (longevity-of-repair adaptation
    of FE+16 is reasonably self-evident given the cited paper).

### C223 — Timeliness of Repair  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the punctuality of repaired products."
- **Verdict:** UNVERIFIABLE (author-defined) / minor wording — the metric is a repair cycle-time
  ratio against a Min/Max band; "punctuality of repaired products" is vague and does not state
  what is timed.
- **Grounding:** none citable — no retrieved source prescribes a repair-timeliness ratio
  (DIN SPEC 91472 / ISO 59020 / FAC+21 give no time-based repair KPI). Legitimately
  author-defined.
- **Implementation check:** Child C2-10 (Repair Process Time, days) exists; Formula
  `(Avg (Repair Process Times) - Min)/(Max - Min)`, NORMALIZED_RATIO, Unit %. Example Values
  `1\n4` are the band. Lower time is better (band-direction caveat as for C213).
- **Proposed revision (C):** "Measures how quickly repairs are completed (average repair cycle
  time, C2-10) relative to a target time. Lower repair times score higher, reducing customer
  waiting time and improving throughput."
- **Notes / adjacent fixes:**
  - [minor] Reference (J) blank — appropriate (author-defined). Verdict UNVERIFIABLE
    (legitimate); no Comment flag required.
  - [minor] band-direction note in R (lower time better → Max = worst-acceptable time).

---

## C23 family — Remanufacturing

### C23 — Remanufacturing Process Performance  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the overall effectiveness of the remanufacturing processes, focusing
  on the ability to restore products to the same quality (or better) than its new unit
  counterpart."
- **Verdict:** DRIFTED (formula text) — **prose is well-grounded and matches the children**, but
  the displayed Formula `Sum (weight * C231 + weight * C233)` **omits C232**, while
  `Underlying Metrics = C231\nC232\nC233`. The gap-fix re-added the orphan C233 under C23 — and
  the children list now correctly shows **C231/C232/C233** (verified below) — but the formula
  text still references only the C231+C233 pair.
- **Grounding:** DIN SPEC 91472 p.7 (3.7 remanufacturing, quote above): a remanufactured product
  "with at least the functionality and performance of the original product is created from
  restored components of one or more used parts as well as new components" — grounds the
  "same quality or better than new" framing precisely. DIN SPEC 91472 p.14 (5.1, process
  quality) grounds the parent "process performance" framing. Composite parent — no single
  source for the roll-up.
- **Implementation check (brief verification):** `Underlying Metrics = C231\nC232\nC233`
  ✅ — all three children present (the re-added orphan **C233 Remanufacture Success Rate** is
  listed; its `Parent Metrics = C23` on row 35 matches). C231/C232/C233 all exist as rows
  33/34/35. Strategy WEIGHTED_AVERAGE, Unit %. The only defect is the stale Formula text.
- **Proposed revision (C):** "Aggregates the remanufacturing process into one score by combining
  the remanufactured-component share (C231), the restored-component share (C232), and the
  remanufacture success rate (C233). Reflects the ability to restore used products to at least
  new-equivalent quality while maximizing reuse of secondary components."
- **Notes / adjacent fixes:**
  - **[major] Formula (I) is stale:** `Sum (weight * C231 + weight * C233)` → should read
    `Sum (weight * C231 + weight * C232 + weight * C233)` to include C232.
  - Reference (J) blank — appropriate for a composite parent. Optional: add `DIN SPEC 91472`
    on this row to anchor the remanufacturing-process-quality basis (Comment not required).

### C231 — Remanufactured Component Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the ratio between the total components used and the secondary
  components used for the remanufactured unit. Ideally, the whole unit would use secondary
  components. A 100% value would mean that the number of remanufactured components integrated
  into the unit is equal to the target amount."
- **Current (I):** "Ratio = Total new components inflow / Total secondary components inflow
  \n\n (Ratio - Min)/(Max - Min)"
- **Verdict:** DRIFTED — **three-way internal contradiction.** (a) The gap-fix context states
  C231 was given the formula **`C2-13 / C2-11`** (Total components remanufactured ÷ Total
  components inflow), grounded in DIN SPEC 91472. (b) `Underlying Metrics = C2-11\nC2-13`
  (Total components inflow; Total components remanufactured) — consistent with `C2-13 / C2-11`.
  (c) But the **displayed Formula text** reads `Total new components inflow / Total secondary
  components inflow` — which names **neither child** (no "new components" or "secondary
  components inflow" leaf is wired to C231; "secondary components inflow" is C2-12, a child of
  C232, not C231). And (d) the **description** says "ratio between the total components used
  and the secondary components used," matching neither the intended `C2-13/C2-11` nor the
  displayed formula. The formula text and description are stale relative to the gap-fixed
  `C2-13 / C2-11` wiring.
- **Grounding:** DIN SPEC 91472 p.16 (Table 1, "Use of new parts", Class A): *"100 % of spare
  parts in compliance with new or remanufacturing specifications"* (Class B *"< 100 % …"*) —
  grounds a **share of components meeting remanufacturing spec**. DIN SPEC 91472 p.6 (3.2 used
  part, Note 2) grounds "used parts … also called cores" = the secondary-component concept. The
  *specific* ratio is an author construction within that frame.
- **Implementation check:** Children C2-11 (Total components inflow, kg — both new and secondary)
  and C2-13 (Total components remanufactured, kg — actually integrated) exist. The
  brief-specified `C2-13 / C2-11` = remanufactured ÷ total inflow ∈ [0,1] = the share of the
  unit's components that are remanufactured (secondary-origin) — this is the coherent reading
  and matches the indicator **name** ("Remanufactured Component Share"). The displayed Formula
  text (`new inflow / secondary inflow`) is **inverted/wrong** and references the wrong leaves.
  Unit % consistent with a 0–1 share; NORMALIZED_RATIO matches.
- **Proposed revision (C):** "Measures the share of a remanufactured unit's components that are
  remanufactured (secondary-origin) parts, computed as remanufactured components (C2-13) ÷
  total component inflow (C2-11). Higher means a larger fraction of the unit is built from
  restored/secondary components rather than new ones."
- **Notes / adjacent fixes:**
  - **[blocker] Formula (I) contradicts the children and the intended `C2-13 / C2-11`:** the
    displayed text `Total new components inflow / Total secondary components inflow` names
    leaves that are not C231's children (and "secondary components inflow" is C2-12, owned by
    C232). Replace with: `Ratio = Total components remanufactured (C2-13) / Total components
    inflow (C2-11)` then `(Ratio - Min)/(Max - Min)`. This aligns formula ↔ children ↔ name
    ↔ the gap-fix decision.
  - [minor] description's "A 100% value would mean … equal to the target amount" is confusing
    (mixes share with target) — the proposed revision drops it.
  - [minor] Reference (J) blank; add `DIN SPEC 91472` (Use of new parts / used-part "cores")
    to ground the secondary-component share. Verdict on grounding = ADAPTED once cited.

### C232 — Restored Components Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the ratio of successfully restored components and the inflow of EoL
  components set for restoration."
- **Current (I):** "Restored = Total components remanufactured / Total secondary components
  inflow \n\n (Ratio - Min)/(Max - Min)"
- **Verdict:** CONSISTENT — prose matches the formula and children: `Total components
  remanufactured (C2-13) / Total secondary components inflow (C2-12)`. `Underlying = C2-12\nC2-13`.
  The "EoL components set for restoration" = C2-12 (Total secondary components inflow, defined
  as "components set for quality restoration to the new product standard"); "successfully
  restored" = C2-13. No drift.
- **Grounding:** DIN SPEC 91472 p.11 (4.3.1) lists **"Restoring"** as a generic process step;
  DIN SPEC 91472 p.16 (Table 1, "Use of new parts") grounds the share-of-components-meeting-spec
  concept. `FAC+21` (cited) p.7 grounds remanufacturing (R6) at framework level. The
  restored ÷ inflow *ratio* is the author's construction.
- **Implementation check:** Children C2-12 (secondary components inflow set for restoration) and
  C2-13 (components remanufactured) exist; ratio ∈ [0,1], Unit % consistent, NORMALIZED_RATIO
  matches. Note: C2-13 is shared as a child of **both C231 and C232** (C2-13 `Parent = C231\nC232`)
  — intentional (it is the numerator for C231's "remanufactured ÷ total inflow" and for C232's
  "remanufactured ÷ secondary inflow"). Internally consistent.
- **Proposed revision (C):** "Measures the success of the restoration step: the share of
  secondary (EoL) components taken in for restoration (C2-12) that are successfully restored and
  integrated into remanufactured units (C2-13). Higher means more secondary components are
  recovered to new-product standard rather than discarded."
- **Notes / adjacent fixes:**
  - [minor] Formula text labels the LHS `Restored =` but the normalization line says
    `(Ratio - Min)…`; harmonize the variable name (`Restored` vs `Ratio`) for clarity.
  - `FAC+21` citation is appropriate as a framework anchor; optionally add `DIN SPEC 91472`
    ("Restoring" step / "Use of new parts" share). No Comment flag needed.

### C233 — Remanufacture Success Rate  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the ratio of successfully remanufactured unit."
- **Current (I):** "(Total remanufactured unit - Min)/(Max - Min)"
- **Verdict:** ADAPTED (concept) / UNVERIFIABLE (exact ratio) — re-added orphan now wired under
  C23 (verified: `Parent = C23`, and C23's `Underlying` lists C233). The description is thin and
  the **formula does not actually compute a "rate"**: it normalizes the *count* of remanufactured
  units (C2-14) against a Min/Max band, with no denominator (e.g. units taken in). So as written
  it is a normalized *throughput count*, not a success *rate/ratio* as the name and description
  imply.
- **Grounding:** DIN SPEC 91472 p.16 (Table 1, "Quality monitoring", Class A): *"End of line
  testing where functionality is tested according to the new product"* — grounds a
  pass/success concept for remanufacturing. `FAC+21` (cited) p.7 grounds remanufacture (R6).
  No source prescribes the unit-count ratio/band; author-defined.
- **Implementation check:** Child **C2-14 (Total remanufactured products, #)** exists and
  `C2-14 Parent = C233` (row 39) — wiring is correct. But C233 has **only one child** (C2-14),
  so a true *success rate* (successful ÷ attempted) is not computable from the current wiring;
  the formula normalizes the single count against a band (Example Values `600\n400`). Unit %,
  NORMALIZED_RATIO. The **name + description ("success rate / successfully remanufactured")
  overstate** what a single-input band-normalized count delivers.
- **Proposed revision (C) — two options:**
  - *(matches current single-input formula, recommended given the wiring):* "Measures the
    remanufacturing output volume — the total number of units successfully remanufactured
    (C2-14) — normalized against a target band. Higher means more units are remanufactured to
    new-equivalent standard."
  - *(if a true success rate is intended, requires a wiring change, not just a description fix):*
    add an "attempted/intake for remanufacturing" leaf as the denominator and compute
    `successful ÷ attempted`, mirroring C211/C221. **Flag as a decision** — do not silently
    rename.
- **Notes / adjacent fixes:**
  - **[major] name/description ↔ formula mismatch:** "Success Rate" / "ratio of successfully
    remanufactured unit" implies a ratio with a denominator, but the formula is a band-normalized
    single count (C2-14). Either (a) reword the description to "remanufacture output volume
    (normalized)" to match the current single-input formula, or (b) re-wire a denominator to
    make it a genuine rate. Recommend (a) unless the author confirms intent (b).
  - `FAC+21` citation is fine as the remanufacturing concept anchor. Verdict UNVERIFIABLE for
    the band-normalization; no Comment flag required beyond the decision note.

---

## Batch summary

| ID | Name | Verdict | Description action |
|----|------|---------|--------------------|
| C2 | Process Quality and Performance | DRIFTED | name all three children (refurb/repair/reman); fix stale formula |
| C21 | Refurbishment Process Performance | CONSISTENT (composite) | optional explicit-children rewrite; non-obvious DIN-SPEC scope flag |
| C211 | Refurbishment Success Rate | ADAPTED / UNVERIFIABLE | fix broken sentence; rewrite to yield-of-pipeline |
| C212 | Quality of Refurbished Products | CONSISTENT | light tighten to refurbished-vs-new test ratio |
| C213 | Timeliness of Refurbishment | UNVERIFIABLE | reword "produce one unit" → refurbishment cycle time |
| C22 | Repair Process Performance | CONSISTENT (composite) | optional explicit-children rewrite |
| C221 | Repair Success Rate | ADAPTED / UNVERIFIABLE | fix broken sentence; rewrite to yield-of-pipeline; add citation |
| C222 | Longevity of repaired product | CONSISTENT / ADAPTED | align "additional" wording to the lifespan ratio |
| C223 | Timeliness of Repair | UNVERIFIABLE | reword vague "punctuality" → repair cycle time |
| C23 | Remanufacturing Process Performance | DRIFTED (formula) | prose ok; fix stale formula (omits C232) |
| C231 | Remanufactured Component Share | DRIFTED | rewrite to `C2-13/C2-11` share; **fix wrong formula text** |
| C232 | Restored Components Share | CONSISTENT | light tighten; harmonize variable name |
| C233 | Remanufacture Success Rate | ADAPTED / UNVERIFIABLE | name/desc overstate a single-input band — reword or re-wire |

**Counts (13):** CONSISTENT 4 (C21, C212, C22, C232) · DRIFTED 4 (C2, C23, C231, C233 borderline)
· ADAPTED 2 (C222, C211/C221 as concept) · UNVERIFIABLE 3 (C213, C223, C233 formula). (C211/C221
carry both an ADAPTED concept verdict and an UNVERIFIABLE-formula note.)

**Brief gap-fix verifications:**
- **C231 = `C2-13 / C2-11`:** the gap-fix *children* (`C2-11\nC2-13`) and intent are correct,
  but the **displayed Formula text was NOT updated** — it still reads `new inflow / secondary
  inflow`, which is wrong and references non-children. **[blocker]** fix the formula text.
- **C233 re-added under C23:** ✅ verified — C23 `Underlying Metrics = C231\nC232\nC233`, and
  C233 `Parent = C23`; C2-14 `Parent = C233`. Wiring is sound. The remaining issue is that the
  C233 name/description ("success rate") overstate a single-input band-normalized count.

### Inconsistencies & fixes (compiled)

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker | C231 / col I | Formula text `Total new components inflow / Total secondary components inflow` names leaves that are not C231's children (secondary inflow = C2-12, child of C232); contradicts children `C2-11\nC2-13` and the intended `C2-13/C2-11` | Set I to `Ratio = Total components remanufactured (C2-13) / Total components inflow (C2-11)` then `(Ratio-Min)/(Max-Min)`; rewrite C (col C) to the remanufactured-component share text |
| 2 | major | C2 / col I | Formula `Sum (weight * C21 + weight * C22)` omits C23 (children are C21/C22/C23); description names only refurbishment + repair | Update I to include `+ weight * C23`; rewrite C to name all three process arms |
| 3 | major | C23 / col I | Formula `Sum (weight * C231 + weight * C233)` omits C232 (children are C231/C232/C233) | Update I to `Sum (weight * C231 + weight * C232 + weight * C233)` |
| 4 | major | C233 / cols C,I | Name "Success Rate" + desc "ratio of successfully remanufactured unit" imply a ratio, but I normalizes a single count (C2-14) with no denominator | Reword C to "remanufacture output volume (normalized)" to match the single-input formula, OR re-wire an intake denominator for a true rate (author decision) |
| 5 | minor | C211 / col C | First sentence grammatically broken ("the rate at which products that pass") | Apply proposed yield-of-pipeline rewrite |
| 6 | minor | C221 / cols C,J | Broken first sentence; Reference blank while sibling C211 cites FAC+21 and repair concept is groundable | Apply rewrite; add `DIN SPEC 91472` (§3.9) and optionally `FAC+21` to J |
| 7 | minor | C213 / col C | "produce one unit of product" reads as manufacturing throughput, not refurbishment cycle time | Reword to refurbishment cycle-time-vs-target |
| 8 | minor | C223 / col C | "punctuality of repaired products" is vague; doesn't state what is timed | Reword to repair cycle-time-vs-target |
| 9 | minor | C222 / col C | "additional lifespan" vs formula = repaired ÷ original lifespan *ratio* | Align wording to the lifespan ratio |
| 10 | minor | C231 / col J | Reference blank; secondary-component share is groundable | Add `DIN SPEC 91472` (Use of new parts / used-part "cores") |
| 11 | minor | C232 / col I | Variable name mismatch: `Restored =` on line 1, `(Ratio - Min)…` on line 2 | Harmonize the variable name |
| 12 | minor | C21 / col R | DIN SPEC 91472 §3.6 says refurbished product is "not placed on the market"; KPI scopes refurbishment to *saleable* condition (non-obvious adaptation) | Add Comment-cell flag noting the product-level adaptation |
| 13 | minor | C2 / stage cell | Stage shows only `E`; children span M,P,U,E | Optional: broaden to `M,P,U,E` |

**SOURCE-NOT-FOUND codes:** none. All cited codes in this batch resolve in References.tsv —
`C2C 5.3` (line 59), `ESRS E5-2` (line 64), `FAC+21` (line 24), `NB+20` (line 35),
`ISO 59020` (line 55), `ESRS E5-5` (line 66), `SRS+20` (line 26), `RE+20` (line 29),
`FE+16` (line 30) — and `DIN SPEC 91472` (line 103) is present and was read.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above (DIN SPEC
91472 §3 + §4.2/4.3 + §5, pp.6–17; ISO 59020 §3.3; FAC+21 p.7; FE+16 p.1). I did not re-audit
the raw `C2-1 … C2-14` leaf rows (separate batch) beyond confirming their existence, parents,
units, and the C231/C233 wiring. Min/Max band values, weights, and example values were not
validated numerically. ISO 59020 was confirmed to define durability/circularity aspects but
**no** process success/timeliness/longevity *formula*; the success/timeliness/longevity ratios
are therefore correctly treated as author-defined (UNVERIFIABLE for the formula, ADAPTED for the
underlying concept). Nothing was applied to the workbook — every change above is a proposal.


---

## C2 — Raw process data inputs C2-1…C2-14

### C2-1 — Number of Units assigned for Refurbishment  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Number of units put into the refurbishment process."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined process count; no citable datapoint source. (J blank, correct.)
- **Implementation check:** Unit `#` fits a unit count; feeds C211 (Refurbishment Success Rate) as the **denominator** `Number of processed products intake for refurbishment`. Description matches that role.
- **Proposed revision:** keep as-is.
- **Notes:** none. Obvious raw leaf — no Comment flag.

### C2-2 — Number of Successful Refurbished Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Number of units passing the refurbishment quality check."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined process count.
- **Implementation check:** Unit `#`; feeds C211 as the **numerator** `Number of successful refurbished products`. Description (units passing quality check) matches the success numerator and is consistent with C211's prose ("not all units can be restored to a sellable or usable condition").
- **Proposed revision:** keep as-is.
- **Notes:** none.

### C2-3 — Test Result of Refurbished Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The result of refurbished units after undergoing performance and quality testing."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined; the test metric/scale is company-specific (C212 prose: "Depends highly on its testing standards").
- **Implementation check:** Unit `-` (dimensionless score) fits an arbitrary test score; feeds C212 as the numerator `Avg(test results of refurbished)`. Description matches.
- **Proposed revision:** keep as-is. (Optional, only if a scale is meant: note it is an average test score on the company's own scale — but Unit `-` already signals this; no change needed.)
- **Notes:** Unit `-` is intentional (scale-agnostic). No flag.

### C2-4 — Test Result of New Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The result of new units after undergoing performance and quality testing."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined baseline score.
- **Implementation check:** Unit `-`; feeds C212 as the denominator `Avg(test results of new-products)`. Description matches. Unit basis matches C2-3 (both `-`), so the C212 ratio is well-formed (same scale on both sides).
- **Proposed revision:** keep as-is.
- **Notes:** Life-cycle stage `M` (vs `E` on C2-3) is plausible — new-unit testing sits at manufacturing. Not an issue.

### C2-5 — Refurbishment Process Time  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Time taken to finish the refurbishment of a unit."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined cycle-time input.
- **Implementation check:** Unit `d` (days) fits a per-unit duration; feeds C213 (Timeliness of Refurbishment) as `Avg(Refurbishment Process Times)`. Description matches.
- **Proposed revision:** keep as-is.
- **Notes:** none. (C213 is lower-is-better and self-normalized; out of scope here.)

### C2-6 — Total Units assigned for Repair  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Number of units put into the repairment process."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined process count.
- **Implementation check:** Unit `#`; feeds C221 (Repair Success Rate) as the denominator `Number of Units assigned for Repair`. Description matches.
- **Proposed revision:** keep as-is. (Optional hygiene: "repairment" → "repair" for register consistency with the rest of the sheet; cosmetic only.)
- **Notes:** [minor] non-standard word "repairment" (also in C2-10) — purely stylistic.

### C2-7 — Total Successful Repaired Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Number of units passing the repair quality check."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined process count.
- **Implementation check:** Unit `#`; feeds C221 as the numerator `Number of Successful Repaired Units`. Description matches the success numerator.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### C2-8 — Lifespan of Repaired Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The duration for which a product remains functional and usable after it has been repaired."
- **Verdict:** ADAPTED (concept-grounded raw input)
- **Grounding:** `RE+20` and `FE+16` both cited (J) and both resolve in References.tsv. FE+16 (longevity indicator) frames product lifetime / earned lifetime as the basis for a longevity measure; the cited pair grounds the *lifespan* concept that C222 (Longevity of repaired product) divides. Conservative note: I did not re-open the PDFs in this light pass — the codes resolve and the concept (extended/earned lifetime after repair) matches FE+16's longevity framing per the References description ("metrics to assess the longevity of a product").
- **Implementation check:** Unit `years` fits a lifespan; feeds C222 as the numerator `Lifespan of Repaired Units`. Description matches. Same unit as C2-9 (`years`), so the C222 ratio is well-formed.
- **Proposed revision:** keep as-is.
- **Notes:** Citations are correct and resolve. Grounding restated from References metadata, not re-verified against the PDFs in this pass (see Limits).

### C2-9 — Original Lifespan of Units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The estimated or documented time period for which a product remains functional after purchase."
- **Verdict:** ADAPTED (concept-grounded raw input)
- **Grounding:** `RE+20` / `FE+16` cited (J), both resolve. FE+16's "initial lifetime" component is the natural anchor for an original/baseline lifespan. Same conservative caveat as C2-8.
- **Implementation check:** Unit `years`; feeds C222 as the denominator `Original Lifespan of Units`. Description matches. Unit basis matches C2-8.
- **Proposed revision:** keep as-is.
- **Notes:** Stage `P` (vs `E` on C2-8) is reasonable — baseline/design lifespan is set at production. Not an issue.

### C2-10 — Repair Process Time  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Time taken to finish the repairment of a unit."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined cycle-time input.
- **Implementation check:** Unit `d`; feeds C223 (Timeliness of Repair) as `Avg(Repair Process Times)`. Description matches.
- **Proposed revision:** keep as-is. (Optional: "repairment" → "repair", cosmetic, same as C2-6.)
- **Notes:** [minor] "repairment" wording only.

### C2-11 — Total components inflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total components (both new and secondary) included in the remanufactured product."
- **Verdict:** CONSISTENT (with a flag on the parent, see Notes)
- **Grounding:** UNVERIFIABLE — author-defined remanufacturing-inflow input.
- **Implementation check:** Unit `kg` (Comment R: "Could be components instead, but now in kg for calculation simplicity" — documents the count-vs-mass choice; acceptable). Parent = C231 (Remanufactured Component Share). Per the brief, C231 is intended to compute the ratio `C2-13/C2-11`, i.e. C2-11 is the **denominator (total inflow)** and C2-13 the **numerator (remanufactured/integrated)**. C2-11's description ("total components, both new and secondary, included in the remanufactured product") correctly reads as the total-inflow denominator. **Consistent with its C2-13/C2-11 role.**
- **Proposed revision:** keep as-is. Description already matches the denominator role.
- **Notes:**
  - The **parent C231's Formula text drift is real but out of scope** (C231 is an aggregate, not a raw leaf): C231 reads `Ratio = Total new components inflow / Total secondary components inflow`, which names neither of its actual children (C2-11 "total inflow", C2-13 "remanufactured"). The brief's intended ratio is `C2-13/C2-11`. C2-11's own description is fine; flag the C231 formula text for a separate (C2-aggregate) pass — do **not** edit C2-11 to chase it.
  - Existing Comment R (kg-vs-count) is appropriate and non-obvious — keep it.

### C2-12 — Total secondary components inflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total components set for quality restoration to the new product standard."
- **Verdict:** CONSISTENT
- **Grounding:** UNVERIFIABLE — author-defined restoration-inflow input.
- **Implementation check:** Unit `kg` (matches C2-13 for the ratio). Parent = C232 (Restored Components Share), whose formula `Restored = Total components remanufactured / Total secondary components inflow` = `C2-13/C2-12`, so C2-12 is the **denominator (secondary inflow set for restoration)**. Description ("components set for quality restoration to the new product standard") matches the secondary/EoL-inflow denominator and aligns with C232's prose ("inflow of EoL components set for restoration").
- **Proposed revision:** keep as-is.
- **Notes:** Wording "secondary components" (name) vs "components set for quality restoration" (description) — consistent in intent. No flag. Same mass basis as C2-13 keeps the C232 ratio well-formed.

### C2-13 — Total components remanufactured  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total components actually integrated into a remanufactured unit."
- **Verdict:** CONSISTENT (serves two parents)
- **Grounding:** UNVERIFIABLE — author-defined remanufacturing output input.
- **Implementation check:** Unit `kg`. **Parent = C231 AND C232** (two parents). It is the **numerator** in both intended ratios: C231 `C2-13/C2-11` (remanufactured ÷ total inflow) and C232 `C2-13/C2-12` (remanufactured ÷ secondary inflow). The description "total components actually integrated into a remanufactured unit" reads cleanly as that shared numerator and matches its C2-13/C2-11 role called out in the brief. Same mass basis (kg) as C2-11 and C2-12, so both ratios are well-formed.
- **Proposed revision:** keep as-is.
- **Notes:** Dual-parent wiring (C231\nC232) is intentional and the description supports both numerator roles. No change. (The C231 formula-text mismatch noted under C2-11 is the parent's issue, not C2-13's.)

### C2-14 — Total remanufactured products  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total product / unit remanufactured."
- **Verdict:** CONSISTENT (re-wire verified)
- **Grounding:** UNVERIFIABLE — author-defined process count.
- **Implementation check:** Unit `#` fits a unit/product count. **Parent = C233** (Remanufacture Success Rate), whose formula `(Total remanufactured unit - Min)/(Max - Min)` consumes exactly this count, and whose child list is `C2-14`. The orphan re-wire flagged in the brief is **resolved**: C2-14's Parent (C233) and C233's Underlying Metrics (C2-14) now agree, and the description ("total product/unit remanufactured") matches C233's "Total remanufactured unit". No longer an orphan.
- **Proposed revision:** keep as-is.
- **Notes:**
  - Re-wire confirmed CONSISTENT (Parent C233 ↔ child C2-14, description ↔ C233 formula).
  - Observation (not a C2-14 defect): C233 measures a "success **rate**" but its formula normalizes a raw **count** (`Total remanufactured unit`) with no denominator (no processed-intake count akin to C211/C221). That is a C233-level question — C2-14 itself is a correctly-described raw count. Flag for the C2-aggregate pass; do not alter C2-14.
  - Unit `#` here vs `kg` on C2-11/12/13 is correct: C233 counts whole products, the C231/C232 shares weigh components. Internally consistent.

---

## Batch summary

| ID | Name | Verdict | Description action |
|----|------|---------|--------------------|
| C2-1 | Number of Units assigned for Refurbishment | CONSISTENT | keep |
| C2-2 | Number of Successful Refurbished Units | CONSISTENT | keep |
| C2-3 | Test Result of Refurbished Units | CONSISTENT | keep |
| C2-4 | Test Result of New Units | CONSISTENT | keep |
| C2-5 | Refurbishment Process Time | CONSISTENT | keep |
| C2-6 | Total Units assigned for Repair | CONSISTENT | keep (optional "repairment"→"repair") |
| C2-7 | Total Successful Repaired Units | CONSISTENT | keep |
| C2-8 | Lifespan of Repaired Units | ADAPTED | keep (RE+20/FE+16 resolve) |
| C2-9 | Original Lifespan of Units | ADAPTED | keep (RE+20/FE+16 resolve) |
| C2-10 | Repair Process Time | CONSISTENT | keep (optional "repairment"→"repair") |
| C2-11 | Total components inflow | CONSISTENT | keep (matches C2-13/C2-11 denominator role) |
| C2-12 | Total secondary components inflow | CONSISTENT | keep |
| C2-13 | Total components remanufactured | CONSISTENT | keep (shared numerator C231 & C232) |
| C2-14 | Total remanufactured products | CONSISTENT | keep (orphan re-wire verified) |

**Counts (14 leaves):** CONSISTENT 12 · ADAPTED 2 (C2-8, C2-9) · DRIFTED 0 · UNVERIFIABLE
status applies to the 12 non-cited leaves (legitimate — author-defined raw process inputs).
**No description rewrites required.** This leaf family is well-aligned with its current
implementation; all 14 descriptions match their Unit, RAW_VALUE strategy, and parent role.

**Targeted checks from the brief — results:**
- **C2-11 (total inflow) & C2-13 (remanufactured) feeding C231's `C2-13/C2-11`:** both
  descriptions match their roles — C2-11 reads as the total-inflow denominator, C2-13 as the
  remanufactured-integrated numerator. CONSISTENT. (Caveat below: C231's *own* formula text is
  mis-worded, but that is an aggregate-level issue, not a leaf-description defect.)
- **C2-14 orphan re-wire:** RESOLVED — Parent C233 ↔ C233.UnderlyingMetrics C2-14 now agree;
  description matches C233's "Total remanufactured unit". CONSISTENT.

**Adjacent drift noted (NOT leaf-description issues — for a separate C2-aggregate pass):**
1. [minor] **C231 Formula text** `Ratio = Total new components inflow / Total secondary components inflow` names neither of its children (C2-11 "total inflow", C2-13 "remanufactured"); the intended ratio is `C2-13/C2-11`. Reconcile the C231 formula wording — leaves are correct.
2. [minor] **C233 "success rate" vs count formula** — C233 normalizes a raw count (C2-14) with no processed-intake denominator, unlike the C211/C221 success rates. Possible C233 design gap; C2-14 itself is correctly described.
3. [minor, cosmetic] "repairment" on C2-6 and C2-10 — register inconsistency with the rest of the sheet ("repair"). Optional.

**Rows needing a decision from the author:** none at the leaf level. The two adjacent items
above (C231 formula text; C233 success-rate denominator) are decisions for the C2-aggregate
review, deliberately left untouched here.

**SOURCE-NOT-FOUND codes:** none. The only codes cited on these leaves are `RE+20` and
`FE+16` (on C2-8/C2-9); both resolve to Labels in References.tsv (and to PDFs already in
`data/literature/Papers/`).

**Limits of this run:** Per the brief this was a light, implementation-consistency pass — no
PDFs were re-opened. The two ADAPTED groundings (C2-8/C2-9 → RE+20/FE+16) rest on the codes
resolving and on the References.tsv descriptions of those papers, not on freshly retrieved
verbatim quotes (the longevity/lifetime concept was grounded in detail in the EN-domain
review for the same papers). I did not audit C2's normalized parent ratios (C21/C211/C212/
C213, C22/C221/C222/C223, C23/C231/C232/C233), their weights, Min/Max bands, or the C231/C233
formula questions beyond flagging them — those belong to the C2-aggregate pass.


---

## C3 — Design for Circularity (incl. the C34 disassembly re-model)

### A. Description rewrites — DRIFTED rows (description contradicts current implementation)

| KPI | Problem | Proposed |
|---|---|---|
| C32 | desc "designed to be remanufactured into a new product" + Formula numerator `Remanufacturable Component Weight` but Formula's normalization line reads `(Reusability - Min)…` (stray "Reusability") | rewrite + fix stray Formula token |
| C34 | desc is the pre-re-model "ease of separating components" prose; says nothing about the two re-tagged 0–1 sub-scores it now weighted-averages | rewrite to name C3-5 + C3-6 as 0–1 inputs |
| C3-5 | desc "quality and clarity of disassembly instructions" but Unit=`%`, now a self-normalized 0–1 score; "User Feedback" parent text & Formula blank | rewrite to a normalized instructions-availability score |
| C3-6 | desc "time required to disassemble" + Unit text says minutes-basis but cell Unit=`%`; **lower-is-better direction not stated in desc**; Formula `(Time - Min)/(Max - Min)` is rising-in-time (worse = higher) — needs the direction convention spelled out | rewrite to a normalized score where Max = worst-acceptable time |

### B. Adjacent-cell drift — Formula text, Unit & citation codes

- **C32 Formula (col I):** normalization line reads `(Reusability - Min) / (Max - Min)` — stray
  "Reusability" left over from an earlier copy; should read `(Remanufacturability - Min)/(Max - Min)`.
- **C3-5 / C3-6 Unit (col H):** both cells say `%`. C3-6's *Description text* still says "minutes";
  the raw input is minutes but the **scored output** is a 0–1/% normalized value — keep Unit `%`
  for the score and move the "minutes" basis into the Description as the raw input.
- **C3-5 Formula (col I) is blank** despite being re-tagged NORMALIZED_RATIO; add the self-normalization
  `(Score - Min)/(Max - Min)` to match its sibling C3-6 and the C34 re-model.
- **C3-5 Parent-text "User Feedback" (col F):** the Parent Metrics cell carries the literal string
  "User Feedback" rather than a metric ID — this is a data-source note misplaced into the relations
  column; should be empty (C3-5 is a leaf whose only parent is C34) with the source noted in col R.
- **Citation codes (col J):**
  - `C34` cites `FB+16` — **the PDF filed as `FB+16` is the wrong paper** (see SOURCE-NOT-FOUND note);
    `RM+23`, `VP+18`, `DS+22`, `MM+17` are the groundable disassembly/instructions sources actually present.
  - `C34` cites `FHC+14` and `ZP+06` — **neither PDF is in the corpus** (SOURCE-NOT-FOUND).
  - `C34` cites `EN 45554` and `C31` cites `EN 45557` — **neither EN 455xx PDF is in the corpus**
    (SOURCE-NOT-FOUND); the concepts are independently grounded (ISO 59020, C2C, ESRS E5, DS+22).
  - `C32` Reference cell omits a remanufacturing-specific source; `DIN SPEC 91472` (present) grounds
    the remanufacturing concept directly — add it.

### C. Comment-cell flags (conservative; non-obvious only)

- **C3-6** — add a lower-is-better direction note (the existing Comment already notes "set Max =
  worst-acceptable time"; confirm it stays after any Comment edit — this is the load-bearing flag).
- **C32 / C33** — Comment flag that these are product-level *design* shares adapted from org-level
  ESRS E5 circular-design rates (Remanufacture / Repurposing) — non-obvious because the cited
  ISO 59020 / WS+24 do not supply the weight-share formula.
- **C31** — keep the existing in/out-of-loop caveat Comment; no new flag needed (recyclable-share
  concept is self-evident and grounded).

### D. Decisions needed from the author

1. **C34 citation cleanup (major).** `FB+16` resolves to a mis-filed PDF (a maintenance essay, not
   the Flipsen reparability paper); `FHC+14`, `ZP+06`, `EN 45554` have no PDF in the corpus. Decide:
   supply the correct PDFs, or trim the C34 Reference cell to the codes that actually ground it
   (`RM+23`, `DS+22`, `MM+17`, `VP+18`).
2. **C3-5 source of truth (minor-but-load-bearing).** Confirm "Instructions Availability" is scored
   from a user-feedback / rubric input (move "User Feedback" out of Parent Metrics into the
   data-source / Comment column) and add the missing self-normalization Formula.
3. **C32 Formula token (minor).** Confirm the normalization line should read "Remanufacturability",
   not the stray "Reusability".

---

### C3 — Design for Circularity  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (col C):** "Measures the design effort for which the product supports the circular economy principles. This KPI aligns with the R1-R3 principle, where the efforts for a circular product comes from the design."
- **Verdict:** CONSISTENT (composite parent; internal check) — the prose correctly frames a roll-up of
  four design sub-scores (recyclability C31, remanufacturability C32, repurposing C33, ease of
  disassembly C34), matching `Underlying = C31\nC32\nC33\nC34` and `Formula = Sum (weight * C31 + … + weight * C34)`.
- **Grounding:**
  - CS+16 p.4 (the cited code): "EMF suggests a number of approaches for revalorization through its CE principles (EMF 2012) including: Design out waste; treat waste as a resource; Design for disassembly; standardise and modularise; Select feedstock materials based on circularity potential". (`data/literature/Papers/CS+16-Design of Indicators for Measuring Product Performance in the Circular Economy.pdf`) — grounds the "circularity comes from design" framing the parent describes.
  - ISO 59020 p.10: "circularity aspect element of an organization's activities or solutions that interacts with the circular economy … EXAMPLE Durability, recyclability, reusability, repairability, recoverability." (`data/literature/ISO 59XXX/ISO-59020.pdf`) — grounds treating recyclability/repairability/etc. as distinct design aspects, i.e. the four children.
- **Implementation check:** All four children (C31, C32, C33, C34) exist as rows; strategy
  WEIGHTED_AVERAGE; each child weight 0.25; Unit % is compatible with averaging four 0–1/% sub-scores.
  Formula text matches the four current children (no stale-grandchild drift). The Comment ("The exact
  circular efforts in practice are … in the 'Circular EoL Handling' KPI") correctly delimits C3 (design
  intent) from C5 (realized actions).
- **Proposed revision (col C):** keep as-is. (Optional, only if you want children explicit: "Aggregates
  the product's design-for-circularity performance into one score by combining the recyclability of its
  materials (C31), the remanufacturability (C32) and repurposability (C33) of its components, and its ease
  of disassembly (C34). Higher means the product's *design* better enables circular end-of-life pathways;
  realized circular actions are scored separately in Circular EoL Handling (C5).")
- **Notes:** Composite/parent — CS+16 grounds the design-for-circularity concept only; the weighting is
  author-defined (appropriate). [minor] the R-principle label "R1-R3" in the description is the author's
  own R-ladder numbering and is not asserted by CS+16/ISO 59020 — leave as-is but do not treat it as
  literature-grounded. Parent C0 is outside this batch.

### C31 — Recyclability of Materials  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (col C):** "Measures the share of materials that can be recycled after disassembly."
- **Verdict:** CONSISTENT — text matches `Recyclability = Recyclable Material Weight / Total Product Weight`,
  then `(Recyclability - Min)/(Max - Min)`, over children C3-2 (recyclable material weight) and C3-1
  (total product weight).
- **Grounding:**
  - ISO 59020 p.10: "circularity aspect … EXAMPLE Durability, recyclability, reusability, repairability, recoverability." (`data/literature/ISO 59XXX/ISO-59020.pdf`) — grounds recyclability as a measurable circularity aspect.
  - C2C v4.1 p.36: "5.4: ≥ 50% of materials by weight are compatible with the intended cycling pathway(s) (i.e., recyclable, compostable, or biodegradable)." (`data/literature/Cradle To Cradle/c2c-certified-full-scope_v4.1_final_011525.pdf`) — grounds a recyclable-share-of-mass metric exactly (% of materials by weight that are recyclable).
  - ESRS E5 p.6 (E5-5): "(c) The rates of recyclable content in products and their packaging." (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E5 Delegated-act-2023-5303-annex-1_en.pdf`) — grounds a "recyclable content rate" disclosure.
- **Implementation check:** Children C3-2 (recyclable material weight, kg) and C3-1 (total product weight, kg)
  both exist and share unit kg, so the ratio is well-formed; Unit % consistent. Min/Max seeded 0/1 (Comment
  documents this). Prose ("share of materials that can be recycled") matches the recyclable-weight ÷
  total-weight share. No drift.
- **Proposed revision (col C):** keep as-is. (Optional sharpen: "Measures the share of the product's total
  mass made of materials that can be recycled at end of life (recyclable material weight ÷ total product
  weight). Higher means more of the product can re-enter a recycling loop.")
- **Notes:**
  - [major] `C31` cites `EN 45557` (recycled-content assessment method) — **no EN 45557 PDF is in the
    corpus** (SOURCE-NOT-FOUND). The concept is independently grounded by ISO 59020 / C2C / ESRS E5
    (all cited and present); recommend either supplying the EN 45557 PDF or relying on the present sources.
    Note also EN 45557 is about *recycled-content* (input) whereas C31 measures *recyclability* (output
    design property) — EN 45555 (recyclability assessment) would be the closer EN code if available.
  - Keep the existing Comment ("Does not consider whether the materials are recycled in- or out-of-loop")
    — accurate and useful; C2C p.37–38 distinguishes "high-value cycling," so the in/out-of-loop caveat is
    well-placed.

### C32 — Remanufacturability of Components  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (col C):** "Measures the share of components that are designed to be remanufactured into a new product."
- **Verdict:** DRIFTED (Formula text) — the *description* is faithful, but the Formula cell's normalization
  line reads `(Reusability - Min) / (Max - Min)` while the ratio line computes `Remanufacturability =
  Remanufacturable Component Weight / Total Product weight`. The stray "Reusability" token is left over from
  a copied row and does not match this metric (remanufacturability ≠ reusability). Substance CONSISTENT;
  Formula text DRIFTED.
- **Grounding:**
  - DIN SPEC 91472 p.7 (definition, present in corpus): a remanufacturing process creates "a remanufactured product with at least the functionality and performance of the original product … from restored components of one or more used parts as well as new components". (`data/literature/DIN SPEC/DIN SPEC 91472_2023-06-00_EN_3447241 Remanufacturing.pdf`) — grounds "components designed to be remanufactured into a new product".
  - ESRS E5 p.4: "application of circular design, leading to increased product durability and optimisation of use, and higher rates of: Reuse, Repair, Refurbishing, Remanufacture, Repurposing". (`…/ESRS E5 …annex-1_en.pdf`) — grounds remanufacturability as a circular-design property.
  - ISO 59020 p.10 (circularity aspect list, quote above) — grounds remanufacturability as a measurable aspect.
- **Implementation check:** Children C3-3 (remanufacturable component weight, kg) and C3-1 (total product
  weight, kg) both exist, share unit kg; ratio well-formed; Unit % consistent. Strategy NORMALIZED_RATIO
  matches. Min/Max seeded 0/1 (Comment documents this). The only mismatch is the Formula's stray
  "Reusability" label.
- **Proposed revision (col C):** "Measures the share of the product's total mass made of components designed
  to be remanufactured — i.e. restored to at-least-as-new functionality and reused in a new product
  (remanufacturable component weight ÷ total product weight). Higher means more of the product is designed
  for value-retaining remanufacturing."
- **Notes:**
  - [minor] **Formula (col I) fix:** change the normalization line `(Reusability - Min) / (Max - Min)` →
    `(Remanufacturability - Min) / (Max - Min)`.
  - [minor] **Reference (col J):** C32 cites `ISO 59020\nESRS E5-5`; add `DIN SPEC 91472` (present, and the
    most direct remanufacturing definition). Comment-cell flag (ADAPTED): "Product-level design share of
    remanufacturable components; remanufacturing concept per DIN SPEC 91472 / ESRS E5; the weight-share
    formula is author-defined."

### C33 — Repurposing of Components  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (col C):** "Measures the share of components that can be repurposed into other uses. A repurposing pipeline needs to exist."
- **Verdict:** CONSISTENT — text matches `Repurposability = Repurposable Component Weight / Total Product Weight`,
  then `(Repurposability - Min)/(Max - Min)`, over children C3-4 (repurposable component weight) and C3-1
  (total product weight).
- **Grounding:**
  - WS+24 p.1 (the cited code): "Repurposing is a decommissioning strategy that enables multiple life cycles for a product or its components. However, repurposing is challenging since it requires finding an alternative use for an existing product." (`data/literature/Papers/WS+24-A Repurposable Attribute Basis for Identifying Repurposing Opportunities in Decommissioned Products.pdf`) — grounds "components repurposed into other uses".
  - ESRS E5 p.4: "… higher rates of: Reuse, Repair, Refurbishing, Remanufacture, Repurposing". (`…/ESRS E5 …annex-1_en.pdf`) — grounds repurposing as a circular-design rate.
- **Implementation check:** Children C3-4 (repurposable component weight, kg) and C3-1 (total product weight, kg)
  exist, share unit kg; ratio well-formed; Unit % consistent. Min/Max seeded 0/1 (Comment documents this).
  Prose matches the formula and children. The "repurposing pipeline needs to exist" clause is an operational
  caveat (consistent with WS+24's premise that an alternative use must be found) — keep.
- **Proposed revision (col C):** keep as-is. (Optional sharpen: "Measures the share of the product's total mass
  made of components that can be repurposed for an alternative use rather than discarded (repurposable component
  weight ÷ total product weight). Requires an existing repurposing pipeline to realize the value.")
- **Notes:** Comment-cell flag (ADAPTED): "Product-level design share of repurposable components; repurposing
  concept per WS+24 / ESRS E5; the weight-share formula is author-defined (WS+24 gives a qualitative attribute
  basis, not a mass-share metric)."

### C34 — Ease of Disassembly  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]  ← re-modelled, verify
- **Current (col C):** "Measures the ease of separating different components and materials after use of product."
- **Verdict:** DRIFTED — the description is the pre-re-model "ease of separating components" prose and says
  nothing about the new structure. Post-re-model, C34 `WEIGHTED_AVERAGE`s **two normalized 0–1 sub-scores**:
  C3-5 (Instructions Availability) and C3-6 (Disassembly Time). The Formula text `Sum (weight * C3-5 + weight *
  C3-6)` is correct for the new structure, but the Description does not reflect that C34 now combines an
  instructions score with a disassembly-time score.
- **Grounding:**
  - VP+18 p.1 (cited): "a reduction of the disassembly time and the related costs will increase the economic feasibility of product lifetime extension … The article proposes a robust method 'eDiM' (ease of Disassembly Metric), to calculate the disassembly time based on the Maynard operation sequence technique (MOST)." (`data/literature/Papers/VP+18-Ease of disassembly of products to support circular economy strategies.pdf`) — grounds ease-of-disassembly via disassembly time (C3-6) and lower-is-better.
  - RM+23 p.1 (cited): the Product Repairability Index "considers the intrinsic repairability of the product components, their assembly/disassembly complexity, repairing instructions, availability of spare parts, and the self-diagnosis aids". (`data/literature/Papers/RM+23-Proposing an integrated indicator to measure product repairability.pdf`) — grounds combining a disassembly metric with an instructions metric (the two C34 arms).
  - DS+22 p.5: "Disassembly — The product is taken apart so that it can subsequently be reassembled and made operational … Required to access components for most repairs." (`data/literature/Papers/DS+22-Design Aspects in Repairability Scoring Systems Comparing Their Objectivity and Completeness.pdf`) — grounds the disassembly design feature.
- **Implementation check:** `Underlying = C3-5\nC3-6`; strategy WEIGHTED_AVERAGE; Formula `Sum (weight * C3-5 +
  weight * C3-6)`. Both children exist and are now NORMALIZED_RATIO (each a self-normalized 0–1 score), so
  averaging them is well-formed; Unit % consistent. The re-tag is correctly reflected in the Calculation
  Strategy cells and C34's own Comment. **Description is the only structural drift in C34 itself.**
- **Proposed revision (col C):** "Measures how easily the product can be disassembled at end of life, combining
  two normalized (0–1) sub-scores: the availability and clarity of disassembly instructions (C3-5) and the
  product's disassembly time (C3-6, where less time scores better). Higher means lower labour/time to separate
  components and materials, enabling higher recovery rates."
- **Notes:**
  - [major] **Reference (col J) is broken/over-stated.** C34 cites `RM+23\nVP+18\nFB+16\nDS+22\nFHC+14\nZP+06\nEN 45554`.
    Of these: `RM+23`, `VP+18`, `DS+22` resolve to correct present PDFs. `FB+16` resolves to a **mis-filed PDF**
    (a maintenance essay, not the Flipsen reparability paper — see SOURCE-NOT-FOUND). `FHC+14`, `ZP+06`,
    `EN 45554` have **no PDF in the corpus**. `MM+17` (cited on C3-6, present) is the cleanest disassembly-time
    source and could also be cited here. Recommend trimming the cell to the codes that actually ground C34
    (`RM+23`, `VP+18`, `DS+22`, `MM+17`) pending supply of the missing PDFs.
  - The re-model itself is sound and faithfully grounded (RM+23 combines instructions + disassembly complexity;
    VP+18/MM+17 ground the disassembly-time arm).

### C3-1 — Total Product Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (col C):** "Total weight of a product unit."
- **Verdict:** CONSISTENT — accurate raw denominator definition; feeds C31, C32, C33 as the total-mass denominator.
- **Grounding:** denominator of mass-share ratios; no dedicated source needed (a plain mass quantity). C2C v4.1
  p.36 frames the C31/C32/C33 ratios as "% of materials by weight," confirming total mass is the natural
  denominator (`…/c2c-certified-full-scope_v4.1_final_011525.pdf`).
- **Implementation check:** Raw leaf, no formula; Parents C31\nC32\nC33; Unit kg consistent with the numerator
  leaves (C3-2/C3-3/C3-4, all kg). No drift.
- **Proposed revision (col C):** keep as-is.
- **Notes:** none. Reference cell blank is appropriate for a plain raw mass input.

### C3-2 — Recyclable Material Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (col C):** "Total weight of the recyclable material in the product. Adhering to ISO 14021 specifications."
- **Verdict:** CONSISTENT — accurate raw numerator for C31; cites ISO 14021 for what counts as "recyclable."
- **Grounding:**
  - ISO 59020 p.10 (recyclability as a circularity aspect, quote above).
  - C2C v4.1 p.36 (≥ X% of materials by weight recyclable, quote above) — grounds a recyclable-mass quantity.
  - (ISO 14021, cited on this row, is present in the corpus per References.tsv line 91; it is the Type-II
    self-declared-claims standard that defines "recyclable" claims — the row's "adhering to ISO 14021" is the
    appropriate basis for what may be counted as recyclable.)
- **Implementation check:** Raw leaf; Parent C31; numerator of C31. Unit kg consistent with C3-1 denominator.
  Cites `ISO 14021\nRE+20` (both resolve in References.tsv). No drift.
- **Proposed revision (col C):** keep as-is.
- **Notes:** none. (Optional: ISO 14021 grounds the "recyclable" *claim* definition, not a share; that is fine
  for a raw input leaf.)

### C3-3 — Remanufacturable Component Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (col C):** "Total weight of remanufacturable components in the product's design."
- **Verdict:** CONSISTENT — accurate raw numerator for C32.
- **Grounding:** DIN SPEC 91472 p.7 (remanufactured product "with at least the functionality and performance of
  the original product … from restored components", quote above) grounds what a "remanufacturable component" is.
  ESRS E5 p.4 ("higher rates of: … Remanufacture") grounds the design property.
- **Implementation check:** Raw leaf; Parent C32; numerator of C32. Unit kg consistent with C3-1. Cites `RE+20`
  (resolves). No drift.
- **Proposed revision (col C):** keep as-is.
- **Notes:** [minor] consider adding `DIN SPEC 91472` to this leaf's Reference to mirror the C32 grounding
  (optional for a raw input).

### C3-4 — Repurposable Component Weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (col C):** "Total weight of repurposable components in the product's design."
- **Verdict:** CONSISTENT — accurate raw numerator for C33.
- **Grounding:** WS+24 p.1 (repurposing "requires finding an alternative use for an existing product", quote
  above) grounds what a "repurposable component" is.
- **Implementation check:** Raw leaf; Parent C33; numerator of C33. Unit kg consistent with C3-1. Cites `WS+24`
  (resolves). No drift.
- **Proposed revision (col C):** keep as-is.
- **Notes:** none.

### C3-5 — Instructions Availability  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]  ← re-tagged, verify
- **Current (col C):** "The quality and clarity of disassembly instructions provided."
- **Verdict:** DRIFTED — the description still reads like a raw qualitative rating, but the row was re-tagged
  `RAW_VALUE → NORMALIZED_RATIO` (per the Comment: "Re-tagged from RAW_VALUE 2026-06 (T3.5)") and Unit is `%`
  — so the live row is now a **self-normalized 0–1 score** feeding C34, not a raw quality rating. The
  description does not state that it self-normalizes against company Target Min/Max, and the **Formula cell is
  blank** despite the NORMALIZED_RATIO tag. Also the Parent Metrics cell (col F) carries the literal string
  "User Feedback" instead of a metric ID.
- **Grounding:**
  - RM+23 p.5 (precise grounding): "Producer repairability instructions (P3): This parameter is associated with the number and degree of repair tasks the user can perform following the product manual or handbook. When a product has instructions and troubleshooting guidelines, the designer/manufacturer enables the repair process." (`…/RM+23-Proposing an integrated indicator to measure product repairability.pdf`)
  - DS+22 p.11: "Information Availability … repair Instructions/manual/bulletin … Product identification … Component identification … exploded view". (`…/DS+22-Design Aspects in Repairability Scoring Systems Comparing Their Objectivity and Completeness.pdf`) — grounds scoring "instructions availability" as a graded criterion.
  - DS+22 p.13: "'Information accessibility' scores the ability of the public and of repairers to access repair information." (same file) — grounds turning it into a 0–1 score.
- **Implementation check:** Leaf of C34; strategy NORMALIZED_RATIO; Unit %. The Target Min/Max columns are
  populated (Target Min `0.7`, Target Max `0.5`) and the example values `0.7 / 0.5` are the band, consistent
  with the "self-normalizes against company Target Min/Max" Comment. **But the Formula cell is empty** (the
  sibling C3-6 carries `(Time - Min)/(Max - Min)`), so the self-normalization is not documented in col I.
  "User Feedback" sitting in Parent Metrics is a misplaced data-source note.
- **Proposed revision (col C):** "A normalized (0–1) score for how well disassembly/repair instructions are
  provided — covering the availability, completeness and clarity of the product manual, exploded views and
  troubleshooting guidance. Self-normalized against the company's Target Min/Max band; higher means clearer,
  more complete instructions."
- **Notes:**
  - [minor] **Formula (col I):** add the self-normalization `(Instructions score - Min) / (Max - Min)` to match
    the NORMALIZED_RATIO tag and sibling C3-6.
  - [minor] **Parent Metrics (col F):** remove the literal "User Feedback" string (C3-5's parent is C34); record
    "User Feedback" as the data source in the Data Source column or the Comment.
  - [minor] **Unit (col H):** `%` is correct for a normalized score (was previously a raw rating) — keep.
  - Citation: `FB+16\nDS+22` — `DS+22` resolves and grounds instructions-availability scoring; `FB+16` is a
    **mis-filed PDF** (see SOURCE-NOT-FOUND). Add `RM+23` (P3 "repairability instructions", the tightest
    grounding) and drop or correct `FB+16`.

### C3-6 — Disassembly Time  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]  ← re-tagged, lower-is-better, verify
- **Current (col C):** "Measures the time required to disassemble the product completely."
- **Verdict:** DRIFTED — the row was re-tagged `RAW_VALUE → NORMALIZED_RATIO` (Comment: "Re-tagged from
  RAW_VALUE 2026-06 (T3.5)") with Formula `(Time - Min)/(Max - Min)` and Unit `%`, so the live row is a
  **self-normalized 0–1 score**, not a raw minutes value. The description still describes only the raw time
  and **does not state the lower-is-better direction**. Critically, the formula `(Time - Min)/(Max - Min)`
  *increases with time* (more time → higher value), so to make "less time = better score" the company must set
  **Max = the worst-acceptable disassembly time** and interpret/invert accordingly. This direction convention
  is the single most important thing the description must capture and currently does not.
- **Grounding:**
  - MM+17 p.1 (cited): "Time-based disassembly method: how to assess the best disassembly sequence and time of target components in complex products … integrating new concepts for the assessment of the disassembly time. … Keywords Design for disassembly … Disassembly time calculation". (`data/literature/Papers/MM+17-Time-based disassembly method how to assess the best disassembly sequence and time of target components in complex products.pdf`) — grounds disassembly time as the measured quantity.
  - VP+18 p.1: "a reduction of the disassembly time and the related costs will increase the economic feasibility of product lifetime extension and therefore increase the viability of a circular economy". (`…/VP+18-Ease of disassembly … strategies.pdf`) — directly grounds **lower-is-better**: less disassembly time is better for circularity.
- **Implementation check:** Leaf of C34; strategy NORMALIZED_RATIO; Formula `(Time - Min)/(Max - Min)`; Unit %.
  Target Min `0.7` / Target Max `0.5` are populated; the Comment already documents the direction ("for C3-6
  lower time is better — set Max = worst-acceptable time"). The raw input is minutes; the scored output is a
  0–1/% value. **Description is the drift** — it omits both the normalization and the lower-is-better direction.
- **Proposed revision (col C):** "A normalized (0–1) score derived from the time required to fully disassemble
  the product (raw input in minutes). Self-normalized against the company's Target Min/Max band, where less
  disassembly time is better — so the Max is set to the worst-acceptable disassembly time. Higher score means
  faster, easier disassembly."
- **Notes:**
  - **[blocker for the re-model] Direction must be explicit.** Keep/confirm the existing Comment-cell flag:
    "for C3-6 lower time is better — set Max = worst-acceptable time." This is the load-bearing flag for the
    re-model; without it the rising `(Time-Min)/(Max-Min)` formula would reward *slower* disassembly. The flag
    is already present in col R (good) — ensure it survives any Comment edit, and mirror the direction into the
    Description (proposed revision above).
  - [minor] **Unit (col H):** the cell is `%` (correct for the normalized score); the Description's "minutes"
    refers to the raw input — keep both, clearly separated as proposed.
  - Citation: `MM+17` resolves and grounds the time quantity; add `VP+18` here (present, and the explicit
    lower-is-better / circular-feasibility grounding) since C3-6 is the disassembly-time arm of C34.

---

## Batch summary

| ID | Name | Verdict | Description action |
|----|------|---------|--------------------|
| C3 | Design for Circularity | CONSISTENT (composite) | keep (optional sharpen) |
| C31 | Recyclability of Materials | CONSISTENT | keep (optional sharpen) |
| C32 | Remanufacturability of Components | DRIFTED (Formula token) | rewrite + fix stray "Reusability" in Formula |
| C33 | Repurposing of Components | CONSISTENT (ADAPTED flag) | keep (optional sharpen) |
| C34 | Ease of Disassembly | DRIFTED | rewrite to name C3-5 + C3-6 as 0–1 inputs; trim Reference |
| C3-1 | Total Product Weight | CONSISTENT | keep |
| C3-2 | Recyclable Material Weight | CONSISTENT | keep |
| C3-3 | Remanufacturable Component Weight | CONSISTENT | keep |
| C3-4 | Repurposable Component Weight | CONSISTENT | keep |
| C3-5 | Instructions Availability | DRIFTED (re-tag) | rewrite to normalized instructions score; add Formula; move "User Feedback" out of Parent |
| C3-6 | Disassembly Time | DRIFTED (re-tag, direction) | rewrite to normalized score, Max = worst-acceptable time; keep direction Comment |

**Counts (11 rows):** CONSISTENT 6 (C3, C31, C33, C3-1, C3-2, C3-3, C3-4 — note C33 carries an ADAPTED
flag; 7 rows are CONSISTENT in substance), DRIFTED 4 (C32 Formula-only, C34, C3-5, C3-6), with ADAPTED
Comment flags attached to C32/C33 and product-level adaptation throughout. UNVERIFIABLE 0 standalone (the
weight-share *formulas* on C31/C32/C33 and the band normalization on C3-5/C3-6 are author-defined, but each
underlying *concept* is grounded, so none is wholly UNVERIFIABLE).

**Re-model verification result (C34 / C3-5 / C3-6):**
- The `RAW_VALUE → NORMALIZED_RATIO` re-tag is correctly reflected in the **Calculation Strategy** cells of
  C3-5 and C3-6, and C34 correctly `WEIGHTED_AVERAGE`s the two 0–1 scores (Formula `Sum (weight * C3-5 +
  weight * C3-6)` matches the children). The structure is sound and literature-grounded (RM+23 combines
  instructions + disassembly; VP+18/MM+17 ground the time arm).
- **Descriptions did not follow the re-model:** C34 (still pre-re-model prose), C3-5 (no mention of
  self-normalization; Formula blank), C3-6 (no mention of normalization or lower-is-better direction).
- **C3-6 lower-is-better:** confirmed correct that Max = worst-acceptable time; the existing Comment-cell flag
  is present and load-bearing — keep it and mirror it into the Description.

**Proposed description rewrites (4):** C32, C34, C3-5, C3-6. C3, C31, C33 + the four weight leaves keep
current text (optional sharpening offered only).

**Proposed adjacent-cell fixes:**
1. [minor] C32 Formula (col I): `(Reusability - Min)/(Max - Min)` → `(Remanufacturability - Min)/(Max - Min)`.
2. [minor] C32 Reference (col J): add `DIN SPEC 91472`.
3. [minor] C3-5 Formula (col I): add `(Instructions score - Min)/(Max - Min)`.
4. [minor] C3-5 Parent Metrics (col F): remove literal "User Feedback"; record it as data source / in Comment.
5. [major] C34 Reference (col J): drop the non-resolving/mis-filed codes (`FB+16`, `FHC+14`, `ZP+06`, `EN 45554`);
   keep `RM+23`, `VP+18`, `DS+22`; optionally add `MM+17`.
6. [minor] C3-5 Reference (col J): add `RM+23`; drop/correct `FB+16`.
7. [minor] C3-6 Reference (col J): add `VP+18` alongside `MM+17`.
8. [major] C31 Reference (col J): `EN 45557` has no PDF (SOURCE-NOT-FOUND) — supply it or rely on the present
   ISO 59020 / C2C / ESRS E5 grounding; note EN 45557 is recycled-*content* not recycl-*ability*.

**Decisions needed (human):** see §D above (C34 citation cleanup; C3-5 data source + missing Formula;
C32 Formula token).

**SOURCE-NOT-FOUND codes (recorded, not substituted):**
- `FB+16` (cited on C34 and C3-5) — a PDF exists at `data/literature/Papers/FB+16-Developing a Reparability
  Indicator for Electronic Products.pdf`, but its **content is the wrong paper** ("Before Breakdown, After
  Repair: The Art of Maintenance" by Denis & Pontille — confirmed on pp.1–3). The intended Flipsen reparability
  indicator (whose "Repair manual available" criterion RM+23 p.3 attributes to "iFixit/Flipsen (Flipsen et al.,
  2017)") is **not** the document in this file. Treat as a mis-filed source.
- `FHC+14` (cited on C34) — no PDF in `data/literature/Papers/`.
- `ZP+06` (cited on C34) — no PDF in `data/literature/Papers/`.
- `EN 45554` (cited on C34) and `EN 45557` (cited on C31) — no EN 455xx PDF anywhere under
  `data/literature/` (checked EPD, DPP, and recursive search). Both codes resolve to a Label row in
  References.tsv (lines 14 and 13) but have no file to read; the concepts are independently grounded by present
  sources (ISO 59020, C2C, ESRS E5, DS+22, RM+23, VP+18, MM+17, DIN SPEC 91472).

**Limits of this run:** Grounding quotes are confined to the files actually opened (CS+16, ISO 59020, C2C v4.1,
ESRS E5, DIN SPEC 91472, WS+24, RM+23, DS+22, VP+18, MM+17). The FB+16 mismatch was detected by reading its
first pages; I did not exhaustively page through it, but pp.1–3 unambiguously show a different paper. I did not
audit weights, the numeric Target Min/Max bands (only confirmed they are populated and that C3-6's direction
convention requires Max = worst-acceptable time), Example Values, or the cross-domain parent C0. I did not
verify that EN 45554/EN 45557 cover the cited concepts (their PDFs are absent). No workbook cells were edited —
every change above is a proposal.


---

## C4 / C5 / C0 — Circular Flow Index (MCI), EoL handling, Domain Root

### C4 — Circular Flow Index  [Level 2, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the proportion of material sourced from virgin resources that ultimately becomes unrecoverable waste, indicating the circularity of the product's material flow."
- **Verdict:** DRIFTED — two defects. (i) The description describes the **Linear Flow Index** (the *linear* proportion: virgin→unrecoverable-waste), but the re-tagged Formula `1 − (Virgin + Wasted)/(2·Total Mass Flow)` computes **1 − LFI**, i.e. the *circular* score (higher = more circular). The prose narrates the quantity being subtracted, not the index the KPI actually outputs. (ii) The citation `MCI+15` does not resolve (orphan code), though MCI.pdf grounds it.
- **Grounding:**
  - MCI p.28 (§2.1.2.3, Eq. 2.9 / simplified Eq. 2.10): "The Linear Flow Index (LFI) measures the proportion of material flowing in a linear fashion, that is, sourced from virgin materials and ending up as unrecoverable waste. So the LFI is computed by dividing the amount of material flowing in a linear fashion by the sum of the amounts of material flowing in a linear and a restorative fashion (or total mass flow, for short). The index takes a value between 1 and 0, where 1 is a completely linear flow and 0 a completely restorative flow." and Eq. 2.10: "LFI = (V + W) / 2M." (`data/literature/MCI.pdf`)
  - MCI p.30 (§2.1.2.5, Eq. 2.12): "The equation used to calculate the MCI of a product is MCI*_P = 1 − LFI · F(X)." (`data/literature/MCI.pdf`) — with the utility factor F(X)=1 (the KPI omits the utility term), this reduces exactly to the KPI's `1 − LFI = 1 − (V+W)/2M`.
- **Implementation check:** `Underlying Metrics = C4-1\nC4-2\nC4-3`; Formula (I) `1 - (Virgin Material Inflow + Wasted Material Outflow) / 2 * Total Mass Flow`; strategy NORMALIZED_RATIO; Unit %. Children: C4-1 = Virgin Material Inflow (V), C4-2 = Wasted Material Outflow (W), C4-3 = Total Mass Flow (M) — all three exist and map cleanly onto MCI's V, W, M. **Formula precedence bug:** as plain text `… / 2 * Total Mass Flow` evaluates left-to-right to `(…/2)·M`, not `…/(2·M)`. The intended denominator is `2·M` (per Eq. 2.9/2.10), so the cell needs parentheses: `1 − (Virgin + Wasted) / (2 · Total Mass Flow)`. Min/Max seeded 0/1 (Comment documents this; the index is already a 0–1 score).
- **Proposed revision (C):** "Scores the circularity of the product's material flow as one minus the share of material that flows linearly — i.e. one minus the proportion sourced from virgin resources (C4-1) and ending as unrecoverable waste (C4-2), relative to the total mass flow (C4-3). Higher means a more restorative, less linear material flow. Adapts the Ellen MacArthur Foundation Material Circularity Indicator (Linear Flow Index), without the product-utility factor."
- **Proposed adjacent fixes:**
  - **J (Reference):** `MCI+15` → **`MCI+25`** (resolvable label for MCI.pdf). [major]
  - **I (Formula):** add parentheses → `1 − (Virgin Material Inflow + Wasted Material Outflow) / (2 · Total Mass Flow)`. [minor, load-bearing]
  - **R (Comment):** add ADAPTED flag (non-obvious — the "1 − LFI" framing and the dropped utility factor are not self-evident): *"Product-level adaptation of the MCI (MCI+25): scores 1 − Linear Flow Index (MCI Eq. 2.9/2.10) and omits the MCI utility factor F(X). Denominator is 2·Total Mass Flow."*
- **Notes:** The verbatim MCI definition describes the LFI as the *linear* proportion → the current description (which also describes the linear proportion) reads as if the KPI *outputs* that linear proportion, but the formula outputs `1 − LFI`. This direction mismatch is the core drift to fix. The 0–1 band and "%" unit are consistent with a circularity score.

### C4-1 — Virgin Material Inflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total amount of raw materials going in to the process. It includes all materials NOT processed from secondary materials."
- **Verdict:** CONSISTENT — accurate raw input; matches MCI's "mass of virgin material" V and the C4 numerator term.
- **Grounding:** MCI p.24 (§2.1.2.1, Eq. 2.1): "…the mass of virgin material is given by V = M(1 − F_R − F_U − F_S)…" where F_R is "the fraction from recycled sources, [F_U] represents the fraction from reused sources and F_S represents the fraction of the biological materials used which originate from Sustained Production." (`data/literature/MCI.pdf`) — grounds "virgin = total minus recycled/reused content".
- **Implementation check:** Raw leaf, no formula; Parent = C4; Unit kg; feeds the C4 numerator (V). Description ("all materials NOT processed from secondary materials") matches MCI's V definition. The C4-1 Comment "Implicitly contains how much recycled materials are used for the product" is consistent with Eq. 2.1 (V is total minus the recycled/reused fractions). No drift.
- **Proposed revision (C):** keep as-is. (Optional sharpen: "Mass of virgin (primary) material in the product — total material mass minus any recycled or reused content (MCI variable V).")
- **Proposed adjacent fixes:** **J:** `MCI+15\nCS+16` → `MCI+25\nCS+16` (re-cite the orphan MCI code; `CS+16` resolves). [major]
- **Notes:** No Comment flag needed beyond the citation fix (raw-input definition is self-evident).

### C4-2 — Wasted Material Outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total amount of wasted materials going out of the process. \"Wasted\" means not further processed for other uses."
- **Verdict:** CONSISTENT — accurate raw input; matches MCI's "mass of unrecoverable waste" W and the C4 numerator term.
- **Grounding:** MCI p.28 (Eq. 2.8): "the overall amount of unrecoverable waste is given by W = W_0 + (W_F + W_C)/2." (`data/literature/MCI.pdf`) — grounds W as unrecoverable waste attributed to the product. (MCI p.4 also: the MCI is constructed from "the mass … of unrecoverable waste that is attributed to the product".)
- **Implementation check:** Raw leaf; Parent = C4; Unit kg; feeds the C4 numerator (W). Description ("not further processed for other uses") matches MCI's "unrecoverable" framing. No drift.
- **Proposed revision (C):** keep as-is. (Optional: "Mass of unrecoverable waste attributed to the product — material leaving the process that is not recovered for further use (MCI variable W).")
- **Proposed adjacent fixes:** **J:** `MCI+15` → `MCI+25`. [major]
- **Notes:** none beyond citation fix.

### C4-3 — Total Mass Flow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total amount of mass involved in the process either going in OR going out of the system in a closed loop system."
- **Verdict:** ADAPTED — the concept (the denominator `2M` / total mass flow) is grounded in MCI, but the prose "going in OR going out … closed loop" is looser than MCI's definition, where the total mass flow denominator is `2M` (mass in + mass out = 2× product mass in the symmetric case). Minor wording adaptation, not a contradiction.
- **Grounding:** MCI p.28 (§2.1.2.3): "…the sum of the amounts of material flowing in a linear and a restorative fashion (or total mass flow, for short)." and "in this case 0 ≤ V ≤ M and 0 ≤ W ≤ M and the total mass flow is equal to 2M." (`data/literature/MCI.pdf`)
- **Implementation check:** Raw leaf; Parent = C4; Unit kg; supplies M (the C4 denominator uses `2·M`). The KPI variable name "Total Mass Flow" maps to MCI's M (product mass), and the formula multiplies by 2 — so C4-3 should be **M (the product/finished mass), not the already-doubled 2M**. The current description ("total mass involved … in OR out") risks being read as 2M, which would double-count. Worth a one-line clarification so the input is the product mass M, with the ×2 applied in C4's formula.
- **Proposed revision (C):** "Total mass of the product (the finished-product mass M). C4's formula multiplies this by two to obtain the total mass flow (2M) — the sum of the linear and restorative flows — so enter the product mass here, not the doubled value."
- **Proposed adjacent fixes:** **J:** `MCI+16` → `MCI+25`. [major]
- **Notes:** [minor] confirm the intended input is M (product mass), since C4's `2 · Total Mass Flow` already doubles it. If the author truly intends C4-3 to hold the full 2M, then C4's formula must drop the `2·` factor — these two cells must agree. Comment-cell flag (non-obvious): *"Holds product mass M; C4 applies the ×2 (total mass flow 2M) per MCI Eq. 2.10."*

---

### C5 — Circular EoL handling  [Level 2, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the circular actions in practice for which the product supports the circular economy principles such as the amount of recycled, refurbished, repurposed components."
- **Verdict:** ADAPTED — the concept is a faithful product-level adaptation of ISO 59020's resource-outflow circularity (Figure A.2 / A.3.3 Formula A.5), but the description is **vague about the actual computation** (it lists examples, not the ratio) and omits the discarded/non-circular arm (C5-5) that the Formula's "OR" branch now uses. Reference cell (J) is **blank** while a strong source exists. Treat as ADAPTED with a description sharpen.
- **Grounding:**
  - ISO 59020 §A.3 p.42 (printed p.34): "The following three core circularity indicators are intended to represent outflows that are mutually exclusive and represent the circular outflows: — components and products that are reused (see A.3.3); — per cent recycled material derived from outflow (see A.3.4), — products and materials for renewable recirculation (see A.3.5). The remaining outflows are considered as linear and do not count towards circularity." (`data/literature/ISO 59XXX/ISO-59020.pdf`)
  - ISO 59020 §A.3 p.43 (printed p.35), Figure A.2 — "100 % resource outflow formula": "Per cent (by mass) circular content of outflow (X)" [reused + recycled + renewable recirculation] "+ Per cent non-circular outflow (e.g. waste, releases, losses, products and resources that will not be recovered) = 100 % of resource outflow." (`data/literature/ISO 59XXX/ISO-59020.pdf`) — grounds C5's circular-fraction = (circular components)/(total outflow), and the inverse discarded-fraction arm.
  - ISO 59020 §A.3.3 p.44 (printed p.36), Formula (A.5): "P_REUO(X) = (m_REUO(X) / m_TO(X)) · 100" where m_REUO is the mass of reused outflow and m_TO is the mass of total outflow. (`data/literature/ISO 59XXX/ISO-59020.pdf`) — the exact mass-ratio structure C5 uses.
- **Implementation check:** `Underlying Metrics = C1-5\nC5-1\nC5-2\nC5-3\nC5-4\nC5-5`; Formula (I) `(Refurbished product weight + Remanufactured component weight + Repurposed component weight + Recycled component weight) / Total reclaimed units weight  OR  Discarded component weight / Total reclaimed units weight`; strategy NORMALIZED_RATIO; Unit %. Denominator C1-5 = "Reclaimed Units Weight" (kg) — exists, dual-parented to C13 and C5. Numerator children: C5-1 (refurbished), C5-2 (remanufactured), C5-3 (repurposed), C5-4 (recycled) — all exist, all kg. The **C5-5 orphan re-add is correctly wired**: C5-5 (discarded component weight) exists, Parent = C5, and is the numerator of the "OR" (non-circular) arm `Discarded / Total reclaimed`. So C5 = circular fraction (C5-1+C5-2+C5-3+C5-4)/C1-5, with C5-5/C1-5 as the complementary linear fraction — matching ISO 59020 Figure A.2 (circular + non-circular = 100%). Units consistent (kg/kg → 0–1 → %). Min/Max seeded 0/1.
- **Proposed revision (C):** "Measures the share, by mass, of reclaimed end-of-life product (C1-5) that re-enters a circular pathway — refurbished (C5-1), remanufactured (C5-2), repurposed (C5-3) or recycled (C5-4) — versus the share discarded as waste (C5-5). Computed as circular component weight ÷ total reclaimed weight; the discarded share (C5-5 ÷ C1-5) is its non-circular complement. Higher means more of the EoL product is kept in use rather than wasted."
- **Proposed adjacent fixes:**
  - **J (Reference):** currently **blank** → add **`ISO 59020`** (resolves; §A.3.3 / Figure A.2 ground the outflow-circularity ratio). [major]
  - **R (Comment):** the existing Comment ("Does not consider the amount of non-usable components due to reclamation damages…") is fine; append ADAPTED flag (non-obvious): *"Product-level adaptation of ISO 59020 §A.3.3 (Formula A.5) / Figure A.2 outflow-circularity: circular outflow mass ÷ total reclaimed outflow mass; ISO splits reuse/recycle/renewable-recirculation, here grouped as refurbish/remanufacture/repurpose/recycle."*
  - **I (Formula):** consider noting the two arms are complementary (circular arm + C5-5 arm sum to the full reclaimed mass) so a reader does not read "OR" as "either-or input"; optional clarity only.
- **Notes:** The description's "supports the circular economy principles" is generic; the proposed revision pins it to the actual mass-ratio over C1-5. C5-5 wiring verified present and used. ISO 59020's A.3.3 is literally a *reuse* fraction; the KPI broadens "reused" to refurbish/remanufacture/repurpose/recycle (which ISO splits across A.3.3–A.3.5) — a defensible product-level grouping, flagged.

### C5-1 — Refurbished product weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total product weight sent to the refurbishing pipeline."
- **Verdict:** CONSISTENT — accurate raw input; one of the circular-outflow numerator terms of C5.
- **Grounding:** ISO 59020 §A.3.3 p.44 (Formula A.5, m_REUO = mass of reused outflow, quote above) grounds reuse-type outflow mass as a circular-outflow term. (`data/literature/ISO 59XXX/ISO-59020.pdf`)
- **Implementation check:** Raw leaf; Parent = C5; Unit kg; numerator term of C5. Consistent with C1-5 (kg) for the ratio.
- **Proposed revision (C):** keep as-is. (Optional: "Mass of reclaimed EoL product routed to refurbishment (circular-outflow term of C5).")
- **Notes:** none. Reference blank is acceptable for a raw leaf; ISO 59020 could be mirrored from C5 if leaf-level citations are desired.

### C5-2 — Remanufactured component weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total component weight sent to the remanufacturing pipeline."
- **Verdict:** CONSISTENT — accurate raw input; circular-outflow numerator term of C5.
- **Grounding:** ISO 59020 §A.3 p.42 (circular outflows comprise reuse/recycle/renewable-recirculation, quote above). (`data/literature/ISO 59XXX/ISO-59020.pdf`)
- **Implementation check:** Raw leaf; Parent = C5; Unit kg; numerator term. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** none.

### C5-3 — Repurposed component weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total component weight sent for repurposing as another product."
- **Verdict:** CONSISTENT — accurate raw input; circular-outflow numerator term of C5.
- **Grounding:** ISO 59020 §A.3 p.42 (circular outflows, quote above). (`data/literature/ISO 59XXX/ISO-59020.pdf`)
- **Implementation check:** Raw leaf; Parent = C5; Unit kg; numerator term. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** none.

### C5-4 — Recycled component weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total component weight recycled into secondary materials. Does not consider the quality difference after recycling."
- **Verdict:** CONSISTENT — accurate raw input; circular-outflow numerator term of C5.
- **Grounding:** ISO 59020 §A.3 p.42: circular outflows include "per cent recycled material derived from outflow (see A.3.4)." (`data/literature/ISO 59XXX/ISO-59020.pdf`)
- **Implementation check:** Raw leaf; Parent = C5; Unit kg; numerator term. The "does not consider quality" caveat is consistent with ISO 59020 treating recycled mass as a circular outflow regardless of downcycling (downcycling handled separately in MCI §2.2.4; not in scope here). Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** none.

### C5-5 — Discarded component weight  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total component weight scrapped, discarded, or marked as waste."
- **Verdict:** CONSISTENT — accurate raw input; the **non-circular (linear) outflow** term that feeds C5's "OR" arm. Orphan re-add verified correctly wired (Parent = C5).
- **Grounding:** ISO 59020 §A.3 p.42: "The remaining outflows are considered as linear and do not count towards circularity. The linear (non-circular) outflow can be calculated by subtracting the circular outflows from 100 %." and Figure A.2 p.43: "Per cent non-circular outflow (e.g. waste, releases, losses, products and resources that will not be recovered)." (`data/literature/ISO 59XXX/ISO-59020.pdf`)
- **Implementation check:** Raw leaf; Parent = C5; Unit kg; numerator of the non-circular arm `Discarded / Total reclaimed`. Re-add verified: row present (snapshot row 60), Parent = C5, weight 0.1665 (the six C5 leaves share ~1/6 each). Consistent with ISO 59020's linear-outflow complement.
- **Proposed revision (C):** keep as-is. (Optional: "Mass of reclaimed EoL product scrapped or sent to disposal — the non-circular (linear) outflow term of C5 (ISO 59020 Figure A.2).")
- **Notes:** Orphan re-add **confirmed correct** — wiring (Parent=C5), unit (kg, matches the C1-5 denominator), and role (non-circular complement) all consistent with the C5 formula's second arm. No defect.

---

### C0 — Circular Efforts Score  [Level 1, domain root, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures how well the current circular initiatives within the product's lifecycle are. Consists of indicators concerning the implementation and process of the R3-R7 principles. It does NOT include any KPIs directly related to aspects of social, cost, environmental, and efficiency."
- **Verdict:** DRIFTED (description content is acceptable, but the **Formula text (I) is stale** — same defect as EN0/EC0). The description itself is broadly CONSISTENT as an author-defined composite, with one wording mismatch (children count vs the R-principle range named).
- **Grounding:** Author-defined composite — no single literature source expected (Reference cell J blank by design, correct). Aggregation of sub-indicators into a higher-level score is supported by ISO 59020 §7.5 p.27 (printed p.20): "Aggregation of circularity indicators — Complex systems can necessitate an aggregation of data from multiple systems or subsystems. Complex products or product portfolios often require data from various constituent components. … Aggregation can also be needed for higher system levels. The organization should ensure reliable aggregation in terms of the system boundaries, the indicators used, the source of data…" (`data/literature/ISO 59XXX/ISO-59020.pdf`) — grounds *that* a weighted higher-level circularity roll-up is legitimate, not the specific weights.
- **Implementation check:** `Underlying Metrics = C1\nC2\nC3\nC4\nC5`; Parent = None (domain root); strategy WEIGHTED_AVERAGE; Unit %; weights on C1–C5 each 0.2 (sum = 1.0, consistent). **Formula text (I) reads "Sum (weight * C1 + … + weight * C3)" — it stops at C3 and omits C4 and C5.** This is stale gap-fix drift identical to the EN0/EC0 pattern: children were extended to C1…C5 but the displayed formula still ends at C3. The five children all exist (C1 Reclamation Efficiency, C2 Process Quality, C3 Design for Circularity, C4 Circular Flow Index, C5 Circular EoL handling). Unit % is compatible with averaging five 0–1/% sub-scores.
- **Proposed revision (C):** "Aggregates the product's circular-economy performance into one score by combining the five level-2 circular indicators: reclamation efficiency (C1), process quality and performance (C2), design for circularity (C3), the circular flow index (C4) and circular end-of-life handling (C5). Covers the implementation and process of circular (R-strategy) principles only; it excludes social, cost, environmental and efficiency aspects, which are scored in their own domains."
- **Proposed adjacent fixes:**
  - **I (Formula):** "Sum (weight * C1 + … + weight * C3)" → **"Sum (weight \* C1 + weight \* C2 + weight \* C3 + weight \* C4 + weight \* C5)"** to match the five wired children. [major — stale formula text, EN0/EC0-style]
  - **C (Description):** the phrase "R3-R7 principles" is questionable — C3 (Design for Circularity) explicitly states it "aligns with the R1-R3 principle" in its own Description, so C0's children span (at least) R1–R7, not R3–R7. Recommend dropping the specific numeric R-range or widening it; the proposed revision drops the contested range. [minor]
- **Notes:** Blank Reference (J) is correct for a domain-root composite — not a defect. The description's substance (a circular-only roll-up excluding other pillars) is consistent with the WEIGHTED_AVERAGE of C1–C5; the only hard defect is the truncated Formula text. ISO 59020 §7.5 grounds the legitimacy of a higher-level weighted aggregation but not the chosen 0.2 weights (author-defined — acceptable).

---

## Batch summary

| ID | Name | Verdict | Description action | Key adjacent fix |
|----|------|---------|--------------------|------------------|
| C4 | Circular Flow Index | DRIFTED | rewrite to "1 − LFI" circularity framing + name C4-1/2/3 | J `MCI+15`→`MCI+25`; I add parentheses `/(2·M)` |
| C4-1 | Virgin Material Inflow | CONSISTENT | keep (optional sharpen to MCI V) | J `MCI+15`→`MCI+25` |
| C4-2 | Wasted Material Outflow | CONSISTENT | keep (optional sharpen to MCI W) | J `MCI+15`→`MCI+25` |
| C4-3 | Total Mass Flow | ADAPTED | rewrite to clarify input = M (×2 in C4) | J `MCI+16`→`MCI+25` |
| C5 | Circular EoL handling | ADAPTED | rewrite to circular-mass ÷ reclaimed ratio + discarded complement | J blank→`ISO 59020` |
| C5-1 | Refurbished product weight | CONSISTENT | keep | — |
| C5-2 | Remanufactured component weight | CONSISTENT | keep | — |
| C5-3 | Repurposed component weight | CONSISTENT | keep | — |
| C5-4 | Recycled component weight | CONSISTENT | keep | — |
| C5-5 | Discarded component weight | CONSISTENT | keep (orphan re-add verified) | — |
| C0 | Circular Efforts Score | DRIFTED | rewrite to name C1–C5; drop R3–R7 range | I formula truncated at C3 → extend to C5 |

**Counts (11 rows):** CONSISTENT 7 (C4-1, C4-2, C5-1, C5-2, C5-3, C5-4, C5-5); ADAPTED 2
(C4-3, C5); DRIFTED 2 (C4, C0). No standalone UNVERIFIABLE (C0 is an author-defined
composite but its only hard defect is the stale formula text, so it is tagged DRIFTED for
that, not UNVERIFIABLE).

**Proposed description rewrites:** C4, C4-3, C5, C0 (4 rows). The seven CONSISTENT raw
leaves keep their text (optional clarifications offered).

**Decisions needed from you:**
1. **[D1 — MCI citation, major] `MCI+15`/`MCI+16` are orphan codes; MCI.pdf is in the corpus as label `MCI+25`.** Recommended: re-cite all four occurrences (C4, C4-1, C4-2, C4-3) to **`MCI+25`**. The gap-audit "SOURCE-NOT-FOUND" was a *code* miss, not a *file* miss — the source exists and grounds the concept (verbatim LFI Eq. 2.9/2.10 and MCI Eq. 2.12 quoted above). Alternative: add explicit `MCI+15` and `MCI+16` Label rows to References.tsv pointing at MCI.pdf — but one label suffices (the single PDF is the 2015 method "adapted in 2019").
2. **[D2 — C4 formula precedence, minor but load-bearing] Add parentheses** to C4's Formula so the denominator is `(2 · Total Mass Flow)`, not `(…/2) · Total Mass Flow`. Also confirm C4-3 holds product mass **M** (C4 applies the ×2), not the already-doubled 2M — the two cells must agree.
3. **[D3 — C5 reference, major] C5's Reference cell is blank** though ISO 59020 §A.3.3 / Figure A.2 grounds it strongly. Add `ISO 59020`.
4. **[D4 — C0 formula text, major] Extend C0's truncated Formula** "…+ weight \* C3" to include C4 and C5 (EN0/EC0-style stale-formula fix). Also reconsider the "R3-R7" range in C0's description (C3 itself claims R1–R3).

**SOURCE-NOT-FOUND codes:** none in the file sense — `MCI+15`/`MCI+16` do not resolve as
*codes* (no matching Label), but the *source* (MCI.pdf, label `MCI+25`) is present and was
read; recorded as a code-vs-file mismatch (D1), not a missing source. ISO 59020 is present
and was read.

**Limits of this run:** Grounding quotes are confined to the pages actually opened in
`data/literature/MCI.pdf` (pp.4, 24, 28, 30) and `data/literature/ISO 59XXX/ISO-59020.pdf`
(pp.27, 42, 43, 44, with TOC pp.3–4 and taxonomy pp.24–25). Page citations for ISO 59020
use the search-tool/extraction page index; the printed ISO page numbers (e.g. A.3.3 on
printed p.36) differ by the front-matter offset — content identical. I verified C5-5's
wiring (Parent=C5, kg, role) from the snapshot but did not recompute the example values or
the 0.2/0.1667 weight bands. C1/C2/C3 (the other C0 children) were not re-audited here —
only confirmed to exist as wired children of C0. The MCI utility factor F(X) and the
biological-cycle extensions are out of scope (the KPI deliberately omits them). No numeric
reference values, Min/Max bands, or cross-domain relations were validated.
