"""The four KPI calculation strategies, as pure functions over numbers.

Kept free of workbook/model concerns so they are trivially unit-testable.
"""
from __future__ import annotations

from collections.abc import Sequence


class StrategyError(ValueError):
    """Raised when a strategy cannot produce a value (e.g. degenerate Min==Max)."""


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def normalize(intermediate: float, target_min: float, target_max: float) -> float:
    """Min-max normalize to [0, 1] and clamp.

    ``(intermediate - min) / (max - min)`` clamped to [0, 1]. Raises if max == min.
    """
    span = target_max - target_min
    if span == 0:
        raise StrategyError("target_max == target_min (degenerate normalization range)")
    return clamp((intermediate - target_min) / span)


def weighted_average(weighted_scores: Sequence[tuple[float, float]]) -> float:
    """Weighted average with missing-data reweighting.

    ``weighted_scores`` are (weight, score) pairs for children that HAVE a score
    (missing children are dropped by the caller). The present weights are renormalized
    so they sum to 1, i.e. ``sum(w_i * s_i) / sum(w_i)``. Raises if no present weight.
    """
    total_w = sum(w for w, _ in weighted_scores)
    if total_w == 0:
        raise StrategyError("no present child weights to average")
    return sum(w * s for w, s in weighted_scores) / total_w


# WEIGHTED_RATIO behaves like a weighted average over already-normalized child scores
# in this workbook (the 3 rows differ only in intent), so it shares the implementation.
weighted_ratio = weighted_average
