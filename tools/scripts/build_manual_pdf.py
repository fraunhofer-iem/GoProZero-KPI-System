#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown>=3.5", "weasyprint>=60", "pymdown-extensions>=10"]
# ///
"""Render docs/USER_MANUAL.md to a PDF (the distribution format).

Self-contained: Markdown -> HTML (python-markdown) -> PDF (WeasyPrint). No system pandoc or
LaTeX needed; WeasyPrint uses the system pango/cairo libraries and fontconfig. Fonts default to
the DejaVu family (Sans / Sans Mono), which cover the manual's Unicode: CO₂, €, m³, →, ⇒, the
en/em dashes, curly quotes, and the box-drawing characters in the aggregation tree diagram.

Markdown features handled: tables, fenced code blocks, blockquotes/admonitions, nested lists,
and in-document links such as [Glossary](#glossary) / [Appendix](#appendix) (the `toc` extension
gives every heading a slug id, which WeasyPrint turns into clickable PDF anchors).

Usage:
    uv run tools/scripts/build_manual_pdf.py                 # docs/USER_MANUAL.md -> output/USER_MANUAL.pdf
    uv run tools/scripts/build_manual_pdf.py --src docs/USER_MANUAL.md --out output/USER_MANUAL.pdf
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import markdown
from weasyprint import HTML

DOC_TITLE = "Product Sustainability KPI System — User Manual"

CSS = """
@page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-left  { content: "Product Sustainability KPI System — User Manual";
                    font: 8pt "DejaVu Sans"; color: #888; }
    @bottom-right { content: "Page " counter(page) " of " counter(pages);
                    font: 8pt "DejaVu Sans"; color: #888; }
}
body { font-family: "DejaVu Sans", sans-serif; font-size: 10pt; line-height: 1.45;
       color: #1a1a1a; }

/* Headings */
h1, h2, h3, h4 { font-weight: bold; line-height: 1.2; page-break-after: avoid; }
h1 { font-size: 19pt; margin: 0 0 0.6em; padding-bottom: 0.2em;
     border-bottom: 2pt solid #2c6e49; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }   /* title + first section stay on page 1 */
h2 { font-size: 14pt; margin: 1.2em 0 0.4em; color: #2c6e49;
     border-bottom: 0.5pt solid #cfe0d6; padding-bottom: 0.1em; }
h3 { font-size: 11.5pt; margin: 1em 0 0.3em; color: #333; }
h4 { font-size: 10.5pt; margin: 0.8em 0 0.2em; color: #444; }

p { margin: 0.45em 0; }
ul, ol { margin: 0.4em 0; padding-left: 1.5em; }
li { margin: 0.15em 0; }
strong { font-weight: bold; }
a { color: #1b5e20; text-decoration: none; }

/* Tables */
table { border-collapse: collapse; width: 100%; margin: 0.7em 0; font-size: 8.8pt;
        page-break-inside: auto; }
th, td { border: 0.5pt solid #c4c4c4; padding: 3.5pt 6pt; text-align: left;
         vertical-align: top; }
th { background: #eef3f0; font-weight: bold; }
tr { page-break-inside: avoid; }
thead { display: table-header-group; }            /* repeat header on page breaks */

/* Code */
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt;
       background: #f3f4f6; padding: 0.5pt 2pt; border-radius: 2pt; }
pre { font-family: "DejaVu Sans Mono", monospace; font-size: 8.4pt; line-height: 1.3;
      background: #f6f8fa; border: 0.5pt solid #d9dde2; border-radius: 3pt;
      padding: 7pt 9pt; white-space: pre; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: inherit; }

/* Blockquotes (used for important callouts) */
blockquote { margin: 0.7em 0; padding: 4pt 10pt; border-left: 3pt solid #2c6e49;
             background: #f5f9f7; color: #333; page-break-inside: avoid; }
blockquote p { margin: 0.25em 0; }

hr { border: none; border-top: 0.5pt solid #ccc; margin: 1.2em 0; }
"""


def build(src: str, out: str) -> None:
    with open(src, encoding="utf-8") as f:
        text = f.read()

    body_html = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "toc", "attr_list", "def_list"],
        output_format="html5",
    )
    # python-markdown's `toc` slugs match GitHub's for our anchors (#glossary, #appendix);
    # warn if a same-page link has no matching id so broken cross-refs don't ship silently.
    ids = set(re.findall(r'id="([^"]+)"', body_html))
    for target in re.findall(r'href="#([^"]+)"', body_html):
        if target not in ids:
            print(f"  WARNING: in-document link #{target} has no matching heading id",
                  file=sys.stderr)

    html_doc = (
        f"<html><head><meta charset='utf-8'><title>{DOC_TITLE}</title>"
        f"<style>{CSS}</style></head><body>{body_html}</body></html>"
    )
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    HTML(string=html_doc, base_url=os.path.dirname(os.path.abspath(src))).write_pdf(out)
    print(f"wrote {out} ({os.path.getsize(out):,} bytes)")


def main() -> int:
    ap = argparse.ArgumentParser(description="Render the User Manual markdown to PDF.")
    ap.add_argument("--src", default="docs/USER_MANUAL.md")
    ap.add_argument("--out", default="output/USER_MANUAL.pdf")
    args = ap.parse_args()
    if not os.path.exists(args.src):
        print(f"ERROR: source not found: {args.src}", file=sys.stderr)
        return 1
    build(args.src, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
