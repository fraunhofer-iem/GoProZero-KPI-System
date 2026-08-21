"""KPI calculation engine.

Reads the product-sustainability KPI workbook (catalogue + company inputs filled in
Excel) and computes every score bottom-up: raw leaf values -> normalized ratios ->
weighted roll-ups -> the five domain scores -> the composite Sustainability score.
"""
from kpi_engine.catalog import Catalog, CatalogKpi, CatalogReference, load_catalog
from kpi_engine.model import Kpi, Result, Status, Strategy

__all__ = [
    "Catalog", "CatalogKpi", "CatalogReference", "load_catalog",
    "Kpi", "Result", "Status", "Strategy",
]
__version__ = "0.1.0"
