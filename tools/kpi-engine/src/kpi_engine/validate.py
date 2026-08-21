"""Structural pre-flight checks over the loaded KPI model.

Reports the integrity problems documented in reviews/KPI-system-gaps.md (orphans, dangling
ids, cross-domain edges, degenerate normalization ranges) without attempting to fix them.
"""
from __future__ import annotations

import re

from pydantic import BaseModel

from kpi_engine.formulas import FORMULAS
from kpi_engine.model import Kpi, Strategy

DOMAIN_ROOTS: dict[str, str] = {
    "Environmental Impact": "EN0", "Economic Viability": "EC0", "Circular Efforts": "C0",
    "Resource Efficiency": "R0", "Social Impact": "S0",
}

# Rows intentionally not reachable from a domain root (standalone reference scores), so the
# orphan check should not flag them. Archived rows (Kpi.archived) are likewise excluded.
INTENTIONAL_STANDALONE: frozenset[str] = frozenset({"EN9"})

_AGG_STRATEGIES = {Strategy.WEIGHTED_AVG, Strategy.WEIGHTED_RATIO}
# Aggregate parents exempt from the "child weights sum to 1" check: a node reused across
# parents (a DAG, not a tree) shares one Weight cell, so it cannot sum to 1 under every
# parent at once. EN9 (PEF single score) weights the same impact nodes EN0 already weights.
WEIGHT_SUM_EXEMPT: frozenset[str] = INTENTIONAL_STANDALONE
_WEIGHT_TOL = 1e-6


class Issue(BaseModel):
    """A single structural finding."""

    kind: str
    ids: list[str]
    message: str


def _prefix(kid: str) -> str:
    m = re.match(r"[A-Za-z]+", kid)
    return m.group(0) if m else ""


def validate(kpis: dict[str, Kpi]) -> list[Issue]:
    issues: list[Issue] = []
    ids = set(kpis)

    # dangling child / parent references
    for kid, kpi in sorted(kpis.items()):
        for child in kpi.children:
            if child not in ids:
                issues.append(Issue(kind="dangling_child", ids=[kid, child],
                                    message=f"{kid} lists non-existent child {child}"))
        for parent in kpi.parents:
            if parent not in ids:
                issues.append(Issue(kind="dangling_parent", ids=[kid, parent],
                                    message=f"{kid} lists non-existent parent {parent}"))

    # orphans: unreachable from the domain root via Underlying Metrics
    by_sheet: dict[str, set[str]] = {}
    for kpi in kpis.values():
        by_sheet.setdefault(kpi.sheet, set()).add(kpi.id)
    for sheet, root in DOMAIN_ROOTS.items():
        sheet_ids = by_sheet.get(sheet, set())
        if root not in sheet_ids:
            continue
        seen: set[str] = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            child_kpi = kpis.get(node)
            if child_kpi:
                stack.extend(c for c in child_kpi.children if c in sheet_ids)
        for orphan in sorted(sheet_ids - seen):
            if kpis[orphan].archived or orphan in INTENTIONAL_STANDALONE:
                continue  # intentionally dormant / standalone — not a defect
            issues.append(Issue(kind="orphan", ids=[orphan],
                                message=f"{orphan} ({kpis[orphan].name}) unreachable from {root}"))

    # cross-domain edges
    seen_edges: set[tuple[str, str]] = set()
    for kid, kpi in kpis.items():
        for other in kpi.children + kpi.parents:
            if other in ids and _prefix(other) != _prefix(kid):
                lo, hi = sorted((kid, other))
                edge = (lo, hi)
                if edge not in seen_edges:
                    seen_edges.add(edge)
                    issues.append(Issue(kind="cross_domain", ids=[lo, hi],
                                        message=f"cross-domain edge {lo} <-> {hi}"))

    # degenerate normalization range
    for kid, kpi in sorted(kpis.items()):
        if kpi.strategy is Strategy.NORMALIZED and kpi.target_min is not None \
                and kpi.target_max is not None and kpi.target_min == kpi.target_max:
            issues.append(Issue(kind="degenerate_range", ids=[kid],
                                message=f"{kid} has Target Min == Target Max"))

    # band direction vs metric direction. The engine has no direction flag:
    # score = (value - Min)/(Max - Min). A lower-is-better row (marked lower_is_better on its
    # Formula) scores correctly only with an INVERTED band (Min > Max); a higher-is-better row
    # needs an ascending band (Min < Max). A band set the wrong way silently inverts the score,
    # so warn. (Min == Max is reported above; rows missing a band or a formula are skipped, as is
    # any row whose direction is unknown.) See reviews/min-max-sourcing.md ("Setting the band
    # direction").
    for kid, kpi in sorted(kpis.items()):
        if kpi.strategy is not Strategy.NORMALIZED \
                or kpi.target_min is None or kpi.target_max is None \
                or kpi.target_min == kpi.target_max:
            continue
        formula = FORMULAS.get(kid)
        if formula is None:
            continue
        ascending = kpi.target_min < kpi.target_max
        if formula.lower_is_better and ascending:
            issues.append(Issue(kind="band_direction", ids=[kid],
                                message=f"{kid} ({kpi.name}) is lower-is-better but its band is "
                                        f"ascending (Min={kpi.target_min} < Max={kpi.target_max}); "
                                        f"a lower-is-better row needs an inverted band (Min > Max) "
                                        f"or it scores backwards"))
        elif not formula.lower_is_better and not ascending:
            issues.append(Issue(kind="band_direction", ids=[kid],
                                message=f"{kid} ({kpi.name}) is higher-is-better but its band is "
                                        f"inverted (Min={kpi.target_min} > Max={kpi.target_max}); "
                                        f"expected an ascending band (Min < Max)"))

    # weight integrity on aggregate parents (USER_MANUAL §A.5: children under one parent
    # carry weights that sum to 1). A child with no weight silently defaults to 1.0 at compute
    # time and distorts the average, so flag that too. Archived children are skipped.
    for kid, kpi in sorted(kpis.items()):
        if kpi.strategy not in _AGG_STRATEGIES:
            continue
        present = [c for c in kpi.children if c in ids and not kpis[c].archived]
        if not present:
            continue
        unweighted = [c for c in present if kpis[c].weight is None]
        if unweighted:
            issues.append(Issue(kind="weight_missing", ids=[kid, *unweighted],
                                message=f"{kid} has child(ren) with no weight (default to 1.0, "
                                        f"distorting the average): {', '.join(unweighted)}"))
        if kid in WEIGHT_SUM_EXEMPT:
            continue
        total = sum(kpis[c].weight or 0.0 for c in present)
        if abs(total - 1.0) > _WEIGHT_TOL:
            issues.append(Issue(kind="weight_sum", ids=[kid],
                                message=f"{kid} child weights sum to {total:.4f}, not 1.0"))

    return issues
