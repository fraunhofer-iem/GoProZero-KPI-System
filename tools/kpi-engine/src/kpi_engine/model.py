"""Pydantic data models for the KPI engine."""
from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Strategy(str, Enum):
    """Calculation strategy declared on a KPI row."""

    RAW = "RAW_VALUE_STRATEGY"
    NORMALIZED = "NORMALIZED_RATIO_STRATEGY"
    WEIGHTED_AVG = "WEIGHTED_AVERAGE_STRATEGY"
    WEIGHTED_RATIO = "WEIGHTED_RATIO_STRATEGY"
    SUM = "SUM_AGGREGATE_STRATEGY"  # total of child values (e.g. a cost roll-up)
    FORMULA = "FORMULA_VALUE_STRATEGY"  # raw value from an encoded formula over children
    # (e.g. a difference like Net Profit = Revenue - costs); NOT normalized, NOT range-checked


class Kpi(BaseModel):
    """One row of a domain sheet: a KPI definition plus its company-supplied inputs."""

    model_config = ConfigDict(frozen=False)

    id: str
    name: str
    sheet: str
    strategy: Strategy | None = None
    children: list[str] = Field(default_factory=list)
    parents: list[str] = Field(default_factory=list)
    level: int | None = None
    is_data: bool = False
    archived: bool = False  # intentionally dormant (unwired from its score); not a defect
    unit: str | None = None
    formula_text: str | None = None

    # company-supplied inputs (read from the workbook's right-hand input block)
    weight: float | None = None
    target_min: float | None = None
    target_max: float | None = None
    value: float | None = None
    reference_value: float | None = None


class Status(str, Enum):
    """Outcome of evaluating a KPI."""

    OK = "ok"
    MISSING = "missing"  # an input or parameter was absent -> not computed
    ERROR = "error"      # structurally broken (e.g. division by zero, bad formula)


class Result(BaseModel):
    """Computed result for one KPI."""

    id: str
    name: str
    sheet: str
    status: Status
    value: float | None = None
    reason: str | None = None
    unverified: bool = False  # score derived from a needs_review formula encoding

    @property
    def ok(self) -> bool:
        return self.status is Status.OK
