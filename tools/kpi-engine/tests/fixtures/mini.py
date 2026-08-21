"""A small synthetic KPI model built from real ids so the encoded formulas apply.

Uses the renewable-energy (EN21) and water (EN22) normalized ratios plus the carbon
phase ratio (EN131, which is needs_review) under a synthetic weighted parent.
"""
from __future__ import annotations

from kpi_engine.model import Kpi, Strategy


def build() -> dict[str, Kpi]:
    def raw(kid: str, value: float | None) -> Kpi:
        return Kpi(id=kid, name=kid, sheet="Environmental Impact",
                   strategy=Strategy.RAW, is_data=True, value=value)

    kpis: dict[str, Kpi] = {
        # raw leaves
        "EN2-1": raw("EN2-1", 30.0),   # renewable
        "EN2-2": raw("EN2-2", 100.0),  # total energy
        "EN2-3": raw("EN2-3", 50.0),   # secondary water
        "EN2-4": raw("EN2-4", 100.0),  # total water
        # C4 (Circular Flow Index) is a needs_review formula: 1 - (virgin+wasted)/(2*total)
        "C4-1": raw("C4-1", 10.0),   # virgin
        "C4-2": raw("C4-2", 10.0),   # wasted
        "C4-3": raw("C4-3", 100.0),  # total mass flow
        # normalized ratios (EN21 = renewable/total, EN22 = secondary/total)
        "EN21": Kpi(id="EN21", name="Renewable share", sheet="Environmental Impact",
                    strategy=Strategy.NORMALIZED, children=["EN2-1", "EN2-2"],
                    target_min=0.0, target_max=1.0),
        "EN22": Kpi(id="EN22", name="Secondary water share", sheet="Environmental Impact",
                    strategy=Strategy.NORMALIZED, children=["EN2-3", "EN2-4"],
                    target_min=0.0, target_max=1.0),
        # needs_review formula: C4 = 1 - (10+10)/(2*100) = 0.9, flagged unverified
        "C4": Kpi(id="C4", name="Circular Flow Index", sheet="Circular Efforts",
                  strategy=Strategy.NORMALIZED, children=["C4-1", "C4-2", "C4-3"],
                  target_min=0.0, target_max=1.0),
        # synthetic weighted parent over EN21 + EN22
        "P": Kpi(id="P", name="Parent", sheet="Environmental Impact",
                 strategy=Strategy.WEIGHTED_AVG, children=["EN21", "EN22"]),
        # synthetic SUM node (a cost-style roll-up) over two raw leaves: 30 + 100 = 130
        "TOTAL": Kpi(id="TOTAL", name="Total", sheet="Environmental Impact",
                     strategy=Strategy.SUM, children=["EN2-1", "EN2-2"]),
        # self-normalizing leaf (PEF pattern): normalize own value 5 against Max=10 -> 0.5
        "EN6-1": Kpi(id="EN6-1", name="Ozone depletion", sheet="Environmental Impact",
                     strategy=Strategy.NORMALIZED, is_data=True,
                     value=5.0, target_min=0.0, target_max=10.0),
        # Economic monetary subtree (T3.6): € totals feed a FORMULA_VALUE difference and a
        # NORMALIZED ratio, so EC0's children stay in [0, 1].
        "EC1-4": raw("EC1-4", 200.0),   # Revenue
        "EC1-3": raw("EC1-3", 20.0),    # Operating Costs
        "EC121": raw("EC121", 100.0),   # COGS (raw here; SUM_AGGREGATE in the real workbook)
        "EC111": raw("EC111", 10.0),    # Lifecycle Management Costs
        "EC112": raw("EC112", 5.0),     # EOL Costs
        "EC11": raw("EC11", 50.0),      # Total Investment Cost (raw here; SUM in the workbook)
        # Net Profit = 200 - (100 + 20 + 10 + 5) = 65 (a raw € difference, not normalized)
        "EC12": Kpi(id="EC12", name="Net Profit", sheet="Economic Viability",
                    strategy=Strategy.FORMULA,
                    children=["EC1-3", "EC1-4", "EC111", "EC112", "EC121"]),
        # ROI = Net Profit / Total Investment Cost = 65/50 = 1.3, normalized 0..2 -> 0.65
        "EC1": Kpi(id="EC1", name="ROI", sheet="Economic Viability",
                   strategy=Strategy.NORMALIZED, children=["EC11", "EC12"],
                   target_min=0.0, target_max=2.0),
        # a mis-tagged aggregate: weighted-averaging raw € values -> ~150, must hard-ERROR
        "BADAGG": Kpi(id="BADAGG", name="Mis-tagged €", sheet="Economic Viability",
                      strategy=Strategy.WEIGHTED_AVG, children=["EC1-4", "EC121"]),
    }
    kpis["EN21"].weight = 0.25
    kpis["EN22"].weight = 0.75
    return kpis
