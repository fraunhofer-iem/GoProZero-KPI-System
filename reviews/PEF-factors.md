# EU PEF / Environmental Footprint (EF 3.x) — Normalisation & Weighting factors extraction

Source audited: `data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf`
(Commission Recommendation (EU) 2021/2279 of 15 December 2021, OJ L 471, 30.12.2021).
Printed page numbers cited below are the Official Journal "L 471/N" numbers shown in the
page header (these are the citable page numbers). The PDF reader page index differs by a
constant offset (PDF page 85 = printed L 471/283).

## Headline result (read this first)

**The numeric normalisation factors (NF) and weighting factors (WF) are NOT contained in
this PDF.** This Recommendation defines the EF method and the impact-category list, but it
explicitly delegates the actual NF and WF *values* to external, online JRC resources:

- Normalisation — §5.2.1 (p. L 471/283): "Within the PEF method the normalisation factors
  are expressed **per capita based on a global value**." Footnote 77 (same page): "**The
  EF normalisation factors to be used are available at**
  http://eplca.jrc.ec.europa.eu/LCDN/developerEF.xhtml". No per-capita numeric NF table
  appears anywhere in the document.
- Weighting — §5.2.2 (p. L 471/283): "the normalised results are multiplied by a set of
  weighting factors (in %) ... **The weighting factors that shall be used in PEF studies
  are provided online**." Footnotes 78–80 (same page) point to
  `2018_JRC_Weighting_EF.pdf` and the LCDN developerEF page, and note "the weighting
  factors are expressed in % and thus shall be divided by 100 before applying."
- The characterisation factors are likewise external — Table 2 footnote 14 (p. L 471/226):
  "The full list of CFs that shall be used is provided within the EF reference package"
  (online, ILCD format).

Consequently, **every impact leaf's NF status is REFERENCED-ONLY and every leaf's WF
status is REFERENCED-ONLY** with respect to *this* PDF. The numbers must be pulled from
the JRC EF reference package / 2018 JRC weighting report, not from 2021/2279.

A note on the one numeric %-table that exists in the PDF: Table 28 "Contribution of
different impact categories based on normalised and weighted results — example"
(p. L 471/287) lists per-category percentages (Climate change 21.5, Ozone depletion 3.0,
Particulate matter 14.9, Water use 18.6, Land use 14.3, etc.). **These are explicitly a
fictitious worked example** of post-normalisation/weighting *contributions to one product's
total impact*, introduced by §6.3.7 (p. L 471/286): "Fictitious examples are provided
below, which are not based on any specific PEF study results." They are **not** the EF
weighting factors and must not be transcribed as WF values.

## Category reference units (FOUND in this PDF)

The category → reference-unit mapping IS fully tabulated here, in **Table 2 "EF impact
categories with respective impact category indicators and characterisation models"**
(pp. L 471/226–228). Verbatim from Table 2:

| EF impact category | Impact category indicator | Unit (verbatim) | Characterisation model (verbatim) | Robustness | Page |
|---|---|---|---|---|---|
| Climate change, total | Global warming potential (GWP100) | kg CO2 eq | Bern model - Global warming potentials (GWP) over a 100-year time horizon (based on IPCC 2013) | I | L 471/226 |
| Ozone depletion | Ozone depletion potential (ODP) | kg CFC-11 eq | EDIP model based on the ODPs of the World Meteorological Organisation (WMO) over an infinite time horizon (WMO 2014 + integrations) | I | L 471/226 |
| Human toxicity, cancer | Comparative toxic unit for humans (CTUh) | CTUh | based on USEtox2.1 model (Fantke et al. 2017), adapted as in Saouter et al. 2018 | III | L 471/227 |
| Human toxicity, non-cancer | Comparative toxic unit for humans (CTUh) | CTUh | based on USEtox2.1 model (Fantke et al. 2017), adapted as in Saouter et al. 2018 | III | L 471/227 |
| Particulate matter | Impact on human health | Disease incidence | PM model (Fantke et al., 2016 in UNEP 2016) | I | L 471/227 |
| Ionising radiation, human health | Human exposure efficiency relative to U235 | kBq U235 eq | Human health effect model as developed by Dreicer et al. 1995 (Frischknecht et al, 2000) | II | L 471/227 |
| Photochemical ozone formation, human health | Tropospheric ozone concentration increase | kg NMVOC eq | LOTOS-EUROS model (Van Zelm et al, 2008) as applied in ReCiPe 2008 | II | L 471/227 |
| Acidification | Accumulated exceedance (AE) | mol H+ eq | Accumulated exceedance (Seppälä et al. 2006, Posch et al, 2008) | II | L 471/227 |
| Eutrophication, terrestrial | Accumulated exceedance (AE) | mol N eq | Accumulated exceedance (Seppälä et al. 2006, Posch et al, 2008) | II | L 471/227 |
| Eutrophication, freshwater | Fraction of nutrients reaching freshwater end compartment (P) | kg P eq | EUTREND model (Struijs et al, 2009) as applied in ReCiPe | II | L 471/227 |
| Eutrophication, marine | Fraction of nutrients reaching marine end compartment (N) | kg N eq | EUTREND model (Struijs et al, 2009) as applied in ReCiPe | II | L 471/227 |
| Ecotoxicity, freshwater | Comparative toxic unit for ecosystems (CTUe) | CTUe | based on USEtox2.1 model (Fantke et al. 2017), adapted as in Saouter et al. 2018 | III | L 471/227 |
| Land use | Soil quality index | Dimensionless (pt) | Soil quality index based on LANCA model (De Laurentiis et al. 2019) and on the LANCA CF version 2.5 (Horn and Maier, 2018) | III | L 471/227 |
| Water use | User deprivation potential (deprivation-weighted water consumption) | m3 water eq of deprived water | Available WAter REmaining (AWARE) model (Boulay et al., 2018; UNEP 2016) | III | L 471/227 |
| Resource use, minerals and metals | Abiotic resource depletion (ADP ultimate reserves) | kg Sb eq | van Oers et al., 2002 as in CML 2002 method, v.4.8 | III | L 471/227 |
| Resource use, fossils | Abiotic resource depletion – fossil fuels (ADP-fossil) | MJ | van Oers et al., 2002 as in CML 2002 method, v.4.8 | III | L 471/228 |

Footnote 18 (p. L 471/228) on Resource use, fossils: "In the EF flow list, and for the
current recommendation, Uranium is included in the list of energy carriers, and it is
measured in MJ." Footnote 15 (p. L 471/226) on Climate change, total: it "is a combination
of three sub-indicators: Climate change –fossil; Climate change – biogenic; Climate change
– land use and land use change."

## Decision-ready mapping table (workbook leaf → EF category → factor status)

NF/WF columns record what is recoverable **from this PDF only**. Per the headline result,
all NF and WF values are REFERENCED-ONLY here.

| Workbook leaf | Leaf unit (workbook) | EF category | EF reference unit (Table 2, p.226-228) | Unit match | NF (value+unit+page) | WF (%+page) | Status |
|---|---|---|---|---|---|---|---|
| EN1-4 (Absolute PCF) | kg CO₂ eq | Climate change, total | kg CO2 eq (p.226) | match | not in PDF — NF "per capita, global value" only (§5.2.1, p.283; fn.77) | not in PDF — WF online (§5.2.2, p.283; fn.78-80) | REFERENCED-ONLY |
| EN5-2 (Land Use per FU) | m²a / FU | Land use | Dimensionless (pt) (p.227) | UNIT MISMATCH — see note | not in PDF (§5.2.1, p.283; fn.77) | not in PDF (§5.2.2, p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-1 (Ozone depletion) | kg CFC-11 eq | Ozone depletion | kg CFC-11 eq (p.226) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-2 (Respiratory inorganics) | Disease incidences per kg PM2.5 | Particulate matter | Disease incidence (p.227) | partial — see note | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-3 (Photochemical ozone formation) | kg NMVOC eq | Photochemical ozone formation, human health | kg NMVOC eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-4 (Eutrophication: Terrestrial) | Mole of N eq | Eutrophication, terrestrial | mol N eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-5 (Eutrophication: Marine) | kg N eq | Eutrophication, marine | kg N eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-6 (Eutrophication: Freshwater) | kg P eq | Eutrophication, freshwater | kg P eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-7 (Acidification) | Mole of H+ eq | Acidification | mol H+ eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN6-8 (Ionizing radiation) | kBq U-235 eq | Ionising radiation, human health | kBq U235 eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN7-1 (Human toxicity: cancer) | CTUh | Human toxicity, cancer | CTUh (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN7-2 (Human toxicity: non-cancer) | CTUh | Human toxicity, non-cancer | CTUh (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN7-3 (Ecotoxicity: freshwater) | CTUe | Ecotoxicity, freshwater | CTUe (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN8-1 (Water Use Scarcity) | m3 | Water use | m3 water eq of deprived water (p.227) | partial — see note | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN8-2 (Resource Use: Minerals & Metals) | kg Sb eq | Resource use, minerals and metals | kg Sb eq (p.227) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |
| EN8-3 (Resource Use: Fossil) | MJ | Resource use, fossils | MJ (p.228) | match | not in PDF (p.283; fn.77) | not in PDF (p.283; fn.78-80) | REFERENCED-ONLY |

All 16 EF categories are accounted for; the workbook's EN6/EN7/EN8 leaves plus EN1-4
(climate) and EN5-2 (land) cover the full EF 3.x category set one-to-one.

### Unit-match notes (FOUND in this PDF, factual)

- **EN5-2 / Land use — genuine unit mismatch.** Table 2 (p. L 471/227) gives the land-use
  reference unit as **"Dimensionless (pt)"** (soil quality index, LANCA model), not the
  `m²a / FU` used by the workbook leaf. The characterised EF land-use result is in points
  (pt), so the workbook's m²a/FU value is an *input quantity*, not the EF category
  indicator result. If EN5-2 is to be normalised against the EF land-use NF, the
  characterised result must first be expressed in the EF "pt" indicator; otherwise the NF
  (which is per the pt indicator) is unit-incompatible with an m²a/FU value. [flag]
- **EN6-2 / Particulate matter.** Table 2 reference unit is "Disease incidence"
  (p. L 471/227). The workbook unit "Disease incidences per kg of PM2.5" describes the
  *characterisation factor* dimension rather than the *category indicator* unit; the EF
  category indicator result is plain "Disease incidence". Compatible in substance but the
  workbook label is more precise than the EF indicator unit. [minor]
- **EN8-1 / Water use.** Table 2 reference unit is "m3 water eq of deprived water"
  (deprivation-weighted, AWARE; p. L 471/227). The workbook leaf unit is plain "m3". These
  are the same dimension but the EF unit is *deprivation-weighted* m3, so the workbook
  value must be the AWARE-weighted result, not raw m3 withdrawn, for the EF NF to apply.
  [minor]
- EN6-4 unit "mol N eq" maps to **Eutrophication, terrestrial** (correct: terrestrial AE is
  the mol N eq one; marine is kg N eq, freshwater is kg P eq), resolving the question posed
  in the task. EN6-5 "kg N eq" → marine; EN6-6 "kg P eq" → freshwater. All consistent with
  Table 2.

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker (for the re-modelling plan) | NF for every leaf (EN1-4, EN5-2, EN6-1..8, EN7-1..3, EN8-1..3) | The numeric EF normalisation factors are **not present** in 2021/2279; §5.2.1 + fn.77 (p.283) only point to the online JRC EF reference package | Leave each leaf's Target Max **blank** and source the NF values from the JRC EF reference package / developerEF (eplca.jrc.ec.europa.eu/LCDN/developerEF.xhtml); do not transcribe any NF from this PDF |
| 2 | blocker (for the re-modelling plan) | WF (Weight) for every leaf | The numeric EF weighting factors are **not present** in 2021/2279; §5.2.2 + fn.78-80 (p.283) point to `2018_JRC_Weighting_EF.pdf` and online; WFs are in % and must be /100 before use | Source the WF % per category from the 2018 JRC weighting report / online; do not use Table 28's example percentages as weights |
| 3 | major | Table 28 (p.287) | Risk of mis-using the only %-table in the PDF: it is a **fictitious example** of normalised+weighted *contributions* (§6.3.7, p.286), not the EF weighting factors | Do not populate any leaf Weight from Table 28; flag in the modelling notes |
| 4 | major | EN5-2 (Land Use per FU) | Workbook unit `m²a / FU` ≠ EF land-use reference unit **"Dimensionless (pt)"** (Table 2, p.227). NF for land use is defined per the pt soil-quality indicator | Either (a) carry the characterised EF land-use result in pt before normalising, or (b) leave EN5-2 Target Max blank and document that m²a/FU is an input quantity, not the EF indicator result |
| 5 | minor | EN8-1 (Water Use Scarcity) | Workbook unit `m3` vs EF "m3 water eq of **deprived** water" (AWARE-weighted) (Table 2, p.227) | Confirm EN8-1's value is the AWARE deprivation-weighted result, not raw m3, before applying the water-use NF |
| 6 | minor | EN6-2 (Respiratory inorganics) | Workbook unit "Disease incidences per kg PM2.5" vs EF category-indicator unit "Disease incidence" (Table 2, p.227) | Align EN6-2's stored value to the EF "Disease incidence" indicator result so the NF (per disease incidence) applies directly |

### SOURCE-NOT-FOUND codes
- None for this task: the cited PDF exists and was read. However, the actual NF and WF
  numeric tables are **outside** this corpus (online JRC EF reference package and
  `2018_JRC_Weighting_EF.pdf`); they are not present as files in `data/literature/`.

### Limits of this run
- I could **not** transcribe any numeric NF or WF value, because none exists in this PDF —
  only the per-capita/global and "online" delegations quoted above. Verdict for the
  factor-values task is therefore REFERENCED-ONLY across all 16 categories; the actual
  numbers require the JRC EF reference package (EF 3.0 / EF 3.1) which is not in the corpus.
- The category→unit and category→model mapping (Table 2) is FOUND and fully transcribed.
- Page citations use the OJ "L 471/N" printed numbers from the page headers. The `pdf_search`
  grounding tool could not be run in this session (the `uv run` Bash invocation was denied),
  so all quotes were obtained by reading the rendered PDF pages directly with the Read tool;
  Table 2 (pp.226-228), §5.2.1/§5.2.2 (p.283), and Table 28 / §6.3.7 (pp.286-287) were each
  read in full. I did not page through every one of the ~290 document pages, but the
  normalisation/weighting methodology lives entirely in §5.2 (read) and the impact-category
  list in Table 2 §3.2.3 (read); a numeric NF/WF table would conventionally sit in those
  sections or an annex table, and §5.2's explicit "available online" delegation indicates no
  such in-document table exists.
