"""Render engine results and validation issues for humans and machines."""
from __future__ import annotations

import json

from kpi_engine.catalog import Catalog
from kpi_engine.model import Kpi, Result, Status
from kpi_engine.validate import DOMAIN_ROOTS, Issue

_SUSTAINABILITY_CHILDREN = ("EN0", "EC0", "C0", "R0", "S0")


def _fmt(result: Result) -> str:
    if result.status is Status.OK and result.value is not None:
        flag = "  (unverified)" if result.unverified else ""
        return f"{result.value:6.3f}{flag}"
    return f"  {result.status.value.upper()}: {result.reason or ''}".rstrip()


def render_results(kpis: dict[str, Kpi], results: dict[str, Result]) -> str:
    """Human-readable per-domain table plus the composite Sustainability score."""
    lines: list[str] = []
    # count over real KPIs only (resolve() may create phantom results for dangling ids)
    real = [results[k] for k in kpis if k in results]
    ok = sum(1 for r in real if r.ok)
    unverified = sum(1 for r in real if r.unverified)
    lines.append(f"Computed {ok}/{len(kpis)} KPIs ({unverified} flagged unverified).")

    # composite Sustainability = mean of the five domain roots that computed
    domain_scores: list[float] = []
    for root_id in _SUSTAINABILITY_CHILDREN:
        res = results.get(root_id)
        if res is not None and res.ok and res.value is not None:
            domain_scores.append(res.value)
    if domain_scores:
        composite = sum(domain_scores) / len(domain_scores)
        lines.append(f"\nSUSTAINABILITY (mean of {len(domain_scores)}/5 domain scores): "
                     f"{composite:.3f}")
    else:
        lines.append("\nSUSTAINABILITY: not computable (no domain score available)")

    for sheet, root in DOMAIN_ROOTS.items():
        lines.append(f"\n== {sheet} ==")
        root_res = results.get(root)
        if root_res:
            lines.append(f"  {root:7} {root_res.name:34.34} {_fmt(root_res)}")
        for kid in sorted(k for k, v in kpis.items() if v.sheet == sheet and k != root):
            res = results[kid]
            lines.append(f"  {kid:7} {res.name:34.34} {_fmt(res)}")
    return "\n".join(lines)


def render_issues(issues: list[Issue]) -> str:
    if not issues:
        return "No structural issues found."
    by_kind: dict[str, list[Issue]] = {}
    for issue in issues:
        by_kind.setdefault(issue.kind, []).append(issue)
    lines = [f"{len(issues)} structural issue(s) found:"]
    for kind, group in sorted(by_kind.items()):
        lines.append(f"\n[{kind}] x{len(group)}")
        for issue in group:
            lines.append(f"  - {issue.message}")
    return "\n".join(lines)


def results_to_json(results: dict[str, Result]) -> str:
    payload = {kid: r.model_dump(exclude_none=True) for kid, r in results.items()}
    return json.dumps(payload, indent=2)


def catalog_to_json(catalog: Catalog) -> str:
    """Serialize the descriptive catalog with stable camelCase keys for the frontend."""
    return catalog.model_dump_json(indent=2, by_alias=True)


def render_catalog_summary(catalog: Catalog) -> str:
    """Short human summary of what the catalog export contains."""
    archived = sum(1 for k in catalog.kpis.values() if k.archived)
    raw = sum(1 for k in catalog.kpis.values() if k.is_raw_data_point)
    return (f"Catalog: {catalog.meta.kpi_count} KPIs "
            f"({raw} raw data points, {archived} archived), "
            f"{catalog.meta.reference_count} references.")
