"""Bottom-up evaluation of the KPI tree.

Recursive with memoization and cycle protection. Each KPI resolves to a ``Result`` that is
either OK (with a value), MISSING (an input/parameter was absent), or ERROR (structurally
broken, e.g. degenerate normalization range). ``unverified`` propagates upward so any score
that depends on a needs_review formula is flagged.
"""
from __future__ import annotations

from kpi_engine import strategies
from kpi_engine.expr import ExprError, evaluate
from kpi_engine.formulas import AGGREGATE_OVERRIDE, FORMULAS
from kpi_engine.model import Kpi, Result, Status, Strategy

_AGG_STRATEGIES = {Strategy.WEIGHTED_AVG, Strategy.WEIGHTED_RATIO}

# A WEIGHTED_AVERAGE / WEIGHTED_RATIO row aggregates already-normalized child scores, so its
# result must land in [0, 1]. A value outside this band means the children are not all
# normalized scores (a mis-tagged strategy feeding raw quantities into an average, e.g. the
# T3.6 class). The engine treats that as a hard ERROR rather than emitting a silent bad score.
_SCORE_LO, _SCORE_HI, _SCORE_EPS = 0.0, 1.0, 1e-9


def evaluate_all(kpis: dict[str, Kpi]) -> dict[str, Result]:
    """Evaluate every KPI in ``kpis`` and return ``{id: Result}``."""
    results: dict[str, Result] = {}
    in_progress: set[str] = set()

    def resolve(kid: str) -> Result:
        if kid in results:
            return results[kid]
        kpi = kpis.get(kid)
        if kpi is None:
            return _store(Result(id=kid, name="(unknown)", sheet="",
                                 status=Status.MISSING, reason="id not found"))
        if kid in in_progress:
            return _store(Result(id=kid, name=kpi.name, sheet=kpi.sheet,
                                 status=Status.ERROR, reason="cycle in hierarchy"))
        in_progress.add(kid)
        result = evaluate_one(kpi)
        in_progress.discard(kid)
        return _store(result)

    def _store(result: Result) -> Result:
        results[result.id] = result
        return result

    def evaluate_one(kpi: Kpi) -> Result:
        if kpi.id in AGGREGATE_OVERRIDE or kpi.strategy in _AGG_STRATEGIES:
            return _aggregate(kpi)
        if kpi.strategy is Strategy.SUM:
            return _sum(kpi)
        if kpi.strategy is Strategy.FORMULA:
            return _formula_value(kpi)
        if kpi.strategy is Strategy.NORMALIZED:
            return _normalized(kpi)
        if kpi.strategy is Strategy.RAW:
            if kpi.value is None:
                return _missing(kpi, "no Value input")
            return _ok(kpi, kpi.value)
        return _missing(kpi, f"unsupported strategy {kpi.strategy}")

    def _sum(kpi: Kpi) -> Result:
        # total of present child values (a cost/quantity roll-up); not weighted, not normalized
        values: list[float] = []
        unverified = False
        for child_id in kpi.children:
            child = resolve(child_id)
            if not child.ok or child.value is None:
                continue
            values.append(child.value)
            unverified = unverified or child.unverified
        if not values:
            return _missing(kpi, "no child values to sum")
        return _ok(kpi, float(sum(values)), unverified=unverified)

    def _aggregate(kpi: Kpi) -> Result:
        pairs: list[tuple[float, float]] = []
        unverified = False
        for child_id in kpi.children:
            child = resolve(child_id)
            if not child.ok or child.value is None:
                continue  # missing-data reweighting: drop absent children
            child_kpi = kpis.get(child_id)
            weight = child_kpi.weight if (child_kpi and child_kpi.weight is not None) else 1.0
            pairs.append((weight, child.value))
            unverified = unverified or child.unverified
        if not pairs:
            return _missing(kpi, "no child scores available")
        try:
            value = strategies.weighted_average(pairs)
        except strategies.StrategyError as exc:
            return _error(kpi, str(exc))
        if not _SCORE_LO - _SCORE_EPS <= value <= _SCORE_HI + _SCORE_EPS:
            return _error(kpi, f"aggregate score {value:.3f} outside [0, 1] — children are "
                               f"not all normalized scores (mis-tagged strategy?)")
        return _ok(kpi, value, unverified=unverified)

    def _compute_formula(kpi: Kpi) -> tuple[tuple[float, bool] | None, Result | None]:
        """Bind a row's encoded formula and evaluate it over children + refs.

        Returns ``((intermediate, unverified), None)`` on success, or ``(None, failure)``
        where ``failure`` is a MISSING/ERROR Result. Shared by NORMALIZED_RATIO (which then
        normalizes the intermediate) and FORMULA_VALUE (which uses it raw).
        """
        formula = FORMULAS.get(kpi.id)
        if formula is None:
            return None, _missing(kpi, "no encoded formula")
        namespace: dict[str, float] = {}
        unverified = formula.needs_review
        for var, child_id in formula.vars.items():
            child = resolve(child_id)
            if not child.ok or child.value is None:
                return None, _missing(kpi, f"input {child_id} unavailable "
                                           f"({child.reason or child.status.value})")
            namespace[var] = child.value
            unverified = unverified or child.unverified
        for var, source in formula.refs.items():
            ref_value = getattr(kpi, source, None)
            if ref_value is None:
                return None, _missing(kpi, f"{source.replace('_', ' ')} not provided")
            namespace[var] = ref_value
        try:
            intermediate = evaluate(formula.expr, namespace)
        except ExprError as exc:
            return None, _error(kpi, f"formula: {exc}")
        return (intermediate, unverified), None

    def _normalized(kpi: Kpi) -> Result:
        computed, failure = _compute_formula(kpi)
        if computed is None:
            assert failure is not None
            return failure
        intermediate, unverified = computed
        if kpi.target_min is None or kpi.target_max is None:
            return _missing(kpi, "Target Min/Max not set")
        try:
            score = strategies.normalize(intermediate, kpi.target_min, kpi.target_max)
        except strategies.StrategyError as exc:
            return _error(kpi, str(exc))
        return _ok(kpi, score, unverified=unverified)

    def _formula_value(kpi: Kpi) -> Result:
        # A raw computed value (e.g. a € difference); not normalized and not range-checked,
        # since it legitimately falls outside [0, 1] and feeds a downstream ratio.
        computed, failure = _compute_formula(kpi)
        if computed is None:
            assert failure is not None
            return failure
        value, unverified = computed
        return _ok(kpi, value, unverified=unverified)

    for kid in kpis:
        resolve(kid)
    return results


def _ok(kpi: Kpi, value: float, *, unverified: bool = False) -> Result:
    return Result(id=kpi.id, name=kpi.name, sheet=kpi.sheet, status=Status.OK,
                  value=value, unverified=unverified)


def _missing(kpi: Kpi, reason: str) -> Result:
    return Result(id=kpi.id, name=kpi.name, sheet=kpi.sheet, status=Status.MISSING, reason=reason)


def _error(kpi: Kpi, reason: str) -> Result:
    return Result(id=kpi.id, name=kpi.name, sheet=kpi.sheet, status=Status.ERROR, reason=reason)
