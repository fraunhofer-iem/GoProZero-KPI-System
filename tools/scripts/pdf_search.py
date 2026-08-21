#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.24"]
# ///
"""Search literature PDFs for terms and print page-numbered, quotable snippets.

This is the grounding tool for KPI<->literature cross-checking: it returns the exact
text and page number where a term appears, so claims can be cited verbatim instead of
recalled from memory (which is how hallucinations creep in).

Usage:
    # search one PDF
    uv run tools/scripts/pdf_search.py "data/literature/ISO 14XXX/ISO 14067.pdf" "carbon footprint"

    # search every PDF in a folder (recursive)
    uv run tools/scripts/pdf_search.py "data/literature/GRI - Global Reporting Initiative" "biodiversity"

    # multiple terms (OR), wider context, cap hits per file
    uv run tools/scripts/pdf_search.py <path> "scope 1" "scope 2" --context 200 --max 5

Output per hit:  <file>  p.<page>:  ...<snippet with the match>...
"""
from __future__ import annotations
import argparse
import os
import re
import sys

import fitz  # pymupdf

# On Windows, stdout defaults to cp1252 and chokes on characters like "₂" (CO₂).
sys.stdout.reconfigure(encoding="utf-8")


def iter_pdfs(path: str):
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in sorted(files):
                if f.lower().endswith(".pdf"):
                    yield os.path.join(root, f)
    else:
        yield path


def search_pdf(path: str, terms: list[str], context: int, max_hits: int) -> int:
    try:
        doc = fitz.open(path)
    except Exception as e:  # noqa: BLE001
        print(f"  [could not open {path}: {e}]", file=sys.stderr)
        return 0
    pat = re.compile("|".join(re.escape(t) for t in terms), re.IGNORECASE)
    hits = 0
    rel = os.path.relpath(path)
    for pno in range(doc.page_count):
        if hits >= max_hits:
            break
        text = doc[pno].get_text()
        if not text:
            continue
        for m in pat.finditer(text):
            if hits >= max_hits:
                break
            start = max(0, m.start() - context)
            end = min(len(text), m.end() + context)
            snippet = re.sub(r"\s+", " ", text[start:end]).strip()
            print(f"{rel}  p.{pno + 1}:  ...{snippet}...")
            hits += 1
    return hits


def main():
    ap = argparse.ArgumentParser(description="Search literature PDFs and print page-cited snippets.")
    ap.add_argument("path", help="a .pdf file OR a folder (searched recursively)")
    ap.add_argument("terms", nargs="+", help="one or more search terms (case-insensitive, OR-matched)")
    ap.add_argument("--context", type=int, default=140, help="characters of context around each match")
    ap.add_argument("--max", type=int, default=8, help="max hits to print per file")
    args = ap.parse_args()

    total = 0
    files = 0
    for pdf in iter_pdfs(args.path):
        n = search_pdf(pdf, args.terms, args.context, args.max)
        total += n
        files += 1
    if total == 0:
        print(f"No matches for {args.terms!r} in {args.path!r} ({files} file(s) searched).")
    else:
        print(f"\n{total} hit(s) across {files} file(s).")


if __name__ == "__main__":
    main()
