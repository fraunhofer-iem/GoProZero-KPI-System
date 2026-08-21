"""Encoded intermediate formulas for the 67 NORMALIZED_RATIO rows.

Each entry maps a KPI id to the expression that produces its *pre-normalization*
intermediate value, with variables bound to child KPI ids (``vars``) or to the row's own
``Reference Value`` cell (``refs``). The engine evaluates ``expr`` against those values,
then applies ``(intermediate - Target Min) / (Target Max - Target Min)`` clamped to [0, 1].

``needs_review=True`` marks an encoding whose prose->math mapping is uncertain (the
worklist for the deferred one-by-one literature review); the engine flags such scores
``(unverified)``.

Two rows declared NORMALIZED_RATIO are actually aggregations of child scores
(``EN14``, ``EN44``) — see ``AGGREGATE_OVERRIDE``; the engine treats them as a mean of
their children rather than a ratio.
"""
from __future__ import annotations

from pydantic import BaseModel, Field

REF = "reference_value"


class Formula(BaseModel):
    """One encoded intermediate formula."""

    expr: str
    vars: dict[str, str] = Field(default_factory=dict)   # var name -> child KPI id
    refs: dict[str, str] = Field(default_factory=dict)   # var name -> "reference_value"
    needs_review: bool = False
    # The engine has no direction flag: score = (intermediate - Min)/(Max - Min). A row whose
    # intermediate is *lower = better* (a non-complemented intensity/time/reduction) therefore
    # scores correctly only with an INVERTED band (Target Min > Target Max). `validate` warns
    # when the band's orientation contradicts this. Complemented rows (1 - bad/total) are
    # higher = better and stay False. See reviews/min-max-sourcing.md ("Setting the band
    # direction"). NB: the PEF/LCIA leaves are impact magnitudes (also lower = better) but are
    # deliberately left False — their direction is a separate open question, out of scope here.
    lower_is_better: bool = False
    note: str | None = None


# Previously held EN14/EN44 (NORMALIZED_RATIO rows that were really aggregations); those are
# now correctly tagged WEIGHTED_AVERAGE in the workbook, so no overrides remain.
AGGREGATE_OVERRIDE: frozenset[str] = frozenset()

def _self(lower_is_better: bool = False) -> "Formula":
    """A self-normalizing row: intermediate = the row's own entered Value cell.

    Used for measured leaves that normalise against a Target Min/Max (the engine then
    runs (value - Min)/(Max - Min)). `getattr(kpi, "value")` supplies the binding.
    """
    return Formula(expr="own", refs={"own": "value"}, lower_is_better=lower_is_better)


FORMULAS: dict[str, Formula] = {
    # --- Environmental: carbon footprint -------------------------------------------
    "EN11": Formula(expr="1 - product / industry",
                    vars={"product": "EN1-4", "industry": "EN1-5"}),
    "EN12": Formula(expr="1 - current / previous",
                    vars={"current": "EN1-4"}, refs={"previous": REF}),
    "EN13": Formula(expr="1 - now / previous",
                    vars={"now": "EN1-4"}, refs={"previous": REF}),
    # EN131-135 (carbon lifecycle-phase ratios) archived — see reviews/EN1-carbon-phases.md
    # --- Environmental: energy / water / land --------------------------------------
    "EN21": Formula(expr="renewable / total", vars={"renewable": "EN2-1", "total": "EN2-2"}),
    "EN22": Formula(expr="secondary / total", vars={"secondary": "EN2-3", "total": "EN2-4"}),
    "EN31": Formula(expr="(previous - actual) / previous",
                    vars={"actual": "EN3-1"}, refs={"previous": REF}),
    "EN32": Formula(expr="1 - hazardous / total",
                    vars={"hazardous": "EN3-2", "total": "EN3-3"}),
    "EN41": Formula(expr="water / units", vars={"water": "EN4-4", "units": "R2-7"},
                    lower_is_better=True),
    "EN42": Formula(expr="(previous - now) / previous",
                    vars={"now": "EN4-4"}, refs={"previous": REF}),
    # EN43 Water Independence = 1 - Blue / Absolute = (Green + Gray) / Absolute — the share of
    # the water footprint that is NOT freshwater withdrawal (higher = better). Complement form,
    # like EN32/S22/R12: Blue/Absolute is freshwater dependency (lower=better) and was never
    # complemented, so it scored backwards under the higher=better normalization. Flipped
    # 2026-06-28 (user decision), renamed from "Water Dependency Ratio"; now a bounded [0,1]
    # ratio seeded Min=0/Max=1 (Absolute = sum of blue+green+gray, so Blue ⊆ Absolute). Same fix
    # as R12. See reviews/min-max-sourcing.md.
    "EN43": Formula(expr="1 - blue / absolute", vars={"blue": "EN4-1", "absolute": "EN4-4"}),
    # EN441-445 (water lifecycle-phase ratios) archived — see reviews/EN4-water-phases.md
    "EN5": Formula(expr="quality * landuse", vars={"quality": "EN5-1", "landuse": "EN5-2"},
                   lower_is_better=True),
    # --- PEF impact leaves: self-normalize the characterised result against its EF
    # normalisation factor (seeded as the row's Target Max, with Min=0). See
    # reviews/EN-impact-pef.md and reviews/PEF-factors.md. EN6/EN7/EN8 then weight-average
    # these by the EF weighting factors (seeded as each leaf's Weight).
    "EN6-1": _self(), "EN6-2": _self(), "EN6-3": _self(), "EN6-4": _self(),
    "EN6-5": _self(), "EN6-6": _self(), "EN6-7": _self(), "EN6-8": _self(),
    "EN7-1": _self(), "EN7-2": _self(), "EN7-3": _self(),
    "EN8-1": _self(), "EN8-2": _self(), "EN8-3": _self(),
    # --- Economic ------------------------------------------------------------------
    # T3.6 re-tags: the monetary subtree mixed € totals into WEIGHTED_AVERAGE rows, so EC0/EC1
    # landed far outside [0,1]. EC11/EC111/EC112 are now SUM_AGGREGATE (€ roll-ups, no formula);
    # EC12 is FORMULA_VALUE (a € difference); EC1/EC2 are NORMALIZED_RATIO over those € totals.
    # ROI = Net Profit / Total Investment Cost (the workbook's "* 100" is dropped — the score is
    # normalized to [0,1] against company Target Min/Max instead of expressed as a percentage).
    "EC1": Formula(expr="profit / cost", vars={"profit": "EC12", "cost": "EC11"}),
    # Gross Margin = (Revenue - COGS) / Revenue.
    "EC2": Formula(expr="(revenue - cogs) / revenue", vars={"revenue": "EC1-4", "cogs": "EC121"}),
    # Net Profit = Revenue - (COGS + Operating + Lifecycle Management + EOL costs). A raw €
    # difference (FORMULA_VALUE_STRATEGY) feeding EC1's ROI ratio — not a mean, not normalized.
    "EC12": Formula(expr="revenue - (cogs + operating + lifecycle + eol)",
                    vars={"revenue": "EC1-4", "cogs": "EC121", "operating": "EC1-3",
                          "lifecycle": "EC111", "eol": "EC112"}),
    "EC3": Formula(expr="revenue / market", vars={"revenue": "EC1-4", "market": "EC3-1"}),
    "EC41": Formula(expr="profit / cost", vars={"profit": "EC4-1", "cost": "EC411"}),
    "EC42": Formula(expr="profit / cost", vars={"profit": "EC4-6", "cost": "EC421"}),
    "EC43": Formula(expr="profit / cost", vars={"profit": "EC4-12", "cost": "EC431"}),
    "EC44": Formula(expr="savings / cost", vars={"savings": "EC4-15", "cost": "EC441"}),
    "EC45": Formula(expr="savings / cost", vars={"savings": "EC4-19", "cost": "EC451"}),
    "EC46": Formula(expr="profit / cost", vars={"profit": "EC4-24", "cost": "EC461"}),
    "EC47": Formula(expr="nonvirgin / virgin",
                    vars={"nonvirgin": "EC4-32", "virgin": "EC4-31"}),
    "EC5": Formula(expr="co2cost * (pcf / units)",
                   vars={"co2cost": "EC5-1", "pcf": "EN1-4", "units": "R2-7"},
                   lower_is_better=True),
    # --- Circular: reclaim / recover -----------------------------------------------
    "C11": Formula(expr="reclaimed / total", vars={"reclaimed": "C1-3", "total": "C1-4"}),
    "C12": Formula(expr="reclaimed / sold", vars={"reclaimed": "C1-2", "sold": "C1-1"}),
    "C13": Formula(expr="valuable / reclaimed", vars={"valuable": "C1-6", "reclaimed": "C1-5"}),
    # --- Circular: refurbish / repair / remanufacture ------------------------------
    "C211": Formula(expr="success / assigned", vars={"success": "C2-2", "assigned": "C2-1"}),
    "C212": Formula(expr="refurbished / new", vars={"refurbished": "C2-3", "new": "C2-4"}),
    "C213": Formula(expr="time", vars={"time": "C2-5"}, lower_is_better=True),
    "C221": Formula(expr="success / assigned", vars={"success": "C2-7", "assigned": "C2-6"}),
    "C222": Formula(expr="repaired / original", vars={"repaired": "C2-8", "original": "C2-9"}),
    "C223": Formula(expr="time", vars={"time": "C2-10"}, lower_is_better=True),
    "C231": Formula(expr="remanufactured / total", vars={"remanufactured": "C2-13", "total": "C2-11"},
                    note="DIN SPEC 91472 p.24-25: secondary-content share (remanufactured / total inflow)"),
    "C232": Formula(expr="reman / secondary", vars={"reman": "C2-13", "secondary": "C2-12"}),
    "C4": Formula(expr="1 - (virgin + wasted) / (2 * total)",
                  vars={"virgin": "C4-1", "wasted": "C4-2", "total": "C4-3"}, needs_review=True,
                  note="MCI-style circular flow index; algebra unverified — MCI source PDF missing from corpus"),
    "C5": Formula(expr="(reused + recycled + recirculated + recovered) / total",
                  vars={"reused": "C5-1", "recycled": "C5-2", "recirculated": "C5-3",
                        "recovered": "C5-4", "total": "C1-5"},
                  note="ISO 59020 §A.3.3: circular-handled mass / total reclaimed outflow"),
    "C233": Formula(expr="count", vars={"count": "C2-14"}),
    # --- Circular: design for X ----------------------------------------------------
    "C31": Formula(expr="recyclable / total", vars={"recyclable": "C3-2", "total": "C3-1"}),
    "C32": Formula(expr="remanufacturable / total", vars={"remanufacturable": "C3-3", "total": "C3-1"}),
    "C33": Formula(expr="repurposable / total", vars={"repurposable": "C3-4", "total": "C3-1"}),
    # C34 (Ease of Disassembly) children self-normalize against company-supplied targets, so
    # C34 weight-averages two 0-1 scores instead of raw % / raw minutes (which left C34, C3 and
    # C0 far outside [0,1]). Min/Max blank in the master — contextual: instructions-availability
    # bounds, and a disassembly-time target where *lower is better* (set Max=worst time, so a
    # shorter time normalizes higher). See reviews/C-circular-indices.md.
    "C3-5": _self(), "C3-6": _self(lower_is_better=True),  # C3-6 disassembly time: shorter = better
    # --- Resource: material / energy / water outflow -------------------------------
    # T3.6 re-tags: WEIGHTED_RATIO_STRATEGY does not divide in the engine (it aliases
    # weighted_average), so these rows averaged their raw inputs instead of taking the ratio
    # their formula text declares. Re-tagged NORMALIZED_RATIO; the division is encoded here and
    # the result self-normalizes against company Target Min/Max.
    # R12 End-of-Life Recoverability = 1 - (Mass of Product Unit - Cyclable Potential) / Mass
    # = Cyclable Potential / Mass — the recoverable share of product mass (higher = better).
    # Written as a complement, like the system's other "lower is better" leaves (EN32, S22, C31),
    # so it scores the right way: the raw waste share (mass - cyclable)/mass is lower=better and
    # was NOT complemented, so under the higher=better 0/1 normalization more waste scored higher
    # (backwards). Flipped 2026-06-26 (user decision) and renamed from "End-of-Life Waste"; now a
    # bounded [0,1] ratio seeded Min=0/Max=1. The former R121 layer (same formula) and the R1-5
    # reference-product-waste input were folded in / archived (2026-06-25): R121 already WAS
    # end-of-life waste, and the "share / reference product waste" comparison added a kg-vs-share
    # dimensional mismatch for no real benefit. See reviews/min-max-sourcing.md and
    # reviews/KPI-system-gaps.md T3.6.
    "R12": Formula(expr="1 - (mass - cyclable) / mass",
                   vars={"mass": "R1-4", "cyclable": "R1-6"}),
    # End User Energy Efficiency = Operational Output Energy / Operational Input Energy.
    "R221": Formula(expr="output / input", vars={"output": "R2-5", "input": "R2-6"}),
    "R111": Formula(expr="recirculated / total", vars={"recirculated": "R1-2", "total": "R1-1"}),
    "R112": Formula(expr="repurposed / total", vars={"repurposed": "R1-3", "total": "R1-1"}),
    "R211": Formula(expr="generated / potential", vars={"generated": "R2-2", "potential": "R2-1"}),
    "R212": Formula(expr="recirculated / generated", vars={"recirculated": "R2-3", "generated": "R2-2"}),
    "R213": Formula(expr="stored / generated", vars={"stored": "R2-4", "generated": "R2-2"}),
    "R222": Formula(expr="energy / units", vars={"energy": "R2-11", "units": "R2-7"},
                    lower_is_better=True),
    "R223": Formula(expr="logistics / inflow", vars={"logistics": "R2-8", "inflow": "R2-9"},
                    lower_is_better=True),
    "R224": Formula(expr="current / previous", vars={"current": "R2-9", "previous": "R2-10"},
                    lower_is_better=True),
    "R311": Formula(expr="treated / total", vars={"treated": "R3-1", "total": "R3-2"}),
    "R312": Formula(expr="recirculated / total", vars={"recirculated": "R3-3", "total": "R3-2"}),
    "R32": Formula(expr="current / previous", vars={"current": "R3-4"}, refs={"previous": REF},
                   lower_is_better=True),
    "R33": Formula(expr="1 - discharge / consumption",
                   vars={"discharge": "R3-5", "consumption": "R3-4"}),
    # --- Social --------------------------------------------------------------------
    "S11": Formula(expr="ethical / total", vars={"ethical": "S1-2", "total": "S1-1"}),
    "S12": Formula(expr="local / total", vars={"local": "S1-3", "total": "S1-1"}),
    "S21": Formula(expr="feedback / surveyed", vars={"feedback": "S2-1", "surveyed": "S2-2"}),
    "S22": Formula(expr="1 - incidents / customers",
                   vars={"incidents": "S2-4", "customers": "S2-3"}),
    "S23": Formula(expr="response / inquiries", vars={"response": "S2-5", "inquiries": "S2-6"}),
    "S24": Formula(expr="feedback / inquiries", vars={"feedback": "S2-7", "inquiries": "S2-6"}),
    "S31": Formula(expr="feedback / employees", vars={"feedback": "S3-1", "employees": "S3-2"}),
    "S32": Formula(expr="local / total", vars={"local": "S3-3", "total": "S3-2"}),
    "S33": Formula(expr="1 - incidents / employees",
                   vars={"incidents": "S3-4", "employees": "S3-2"}),
    # S34 children self-normalize against a company-supplied target (Min/Max blank in the
    # master — contextual, e.g. a living-wage benchmark). See reviews/S-social-economic.md.
    "S3-5": _self(), "S3-6": _self(), "S3-7": _self(),
}
