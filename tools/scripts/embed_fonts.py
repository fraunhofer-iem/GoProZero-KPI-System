#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Inline a template's Google Fonts into it as base64 @font-face rules.

Why this exists
---------------
The manual templates are single self-contained files, with one exception: a
`<link>` to fonts.googleapis.com. That link is not a dependency of the *file*, but
it does make every visitor's browser fetch the fonts from Google at render time,
which sends the visitor's IP address to Google. For a page published by a German
research institute that is worth avoiding.

This script replaces the link tags with the font bytes themselves, so the page
makes no third-party requests at all. Run it once per template and commit the
result. The build stays offline: nothing is fetched when the site is built, which
matters because the GitHub Actions runner builds the page on every push.

Only the `latin` subset is embedded. That is already the only subset a browser
downloads for these pages, so the rendering does not change. Characters outside
the latin unicode-range (the arrows, the warning sign, the CO2 subscript) fall
back to a system font exactly as they do today.

Usage:
    uv run tools/scripts/embed_fonts.py tools/templates/kpi_manual_itsowl.html.template
    uv run tools/scripts/embed_fonts.py <template> --out /tmp/preview.html
    uv run tools/scripts/embed_fonts.py <template> --check   # verify, write nothing
"""
from __future__ import annotations

import argparse
import base64
import re
import sys
import urllib.request
from pathlib import Path

# Google serves woff2 only to browsers it recognises; a bare urllib UA gets ttf.
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")
FONT_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com")
# The two preconnects plus the stylesheet link, as one block.
LINK_BLOCK = re.compile(
    r'[ \t]*<link[^>]*rel="preconnect"[^>]*fonts\.googleapis\.com[^>]*>\s*'
    r'[ \t]*<link[^>]*rel="preconnect"[^>]*fonts\.gstatic\.com[^>]*>\s*'
    r'[ \t]*<link[^>]*href="(?P<url>https://fonts\.googleapis\.com/css2\?[^"]+)"[^>]*>\n')
FACE = re.compile(r'/\*\s*(?P<subset>[\w\- \[\]]+)\s*\*/\s*(?P<rule>@font-face\s*\{.*?\})', re.S)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def build_face_css(css_url: str) -> tuple[str, int, int]:
    """Return (css, face_count, embedded_bytes) for the latin subset of css_url."""
    css = fetch(css_url).decode("utf-8")
    rules, raw_total = [], 0
    for m in FACE.finditer(css):
        if m.group("subset").strip() != "latin":
            continue
        rule = m.group("rule")
        url_m = re.search(r'url\((https://[^)]+\.woff2)\)', rule)
        if not url_m:
            sys.exit("error: a latin @font-face carried no woff2 url")
        blob = fetch(url_m.group(1))
        raw_total += len(blob)
        data = "data:font/woff2;base64," + base64.b64encode(blob).decode("ascii")
        # Keep the rule Google wrote (family, weight, style, unicode-range) and swap
        # only the source, so the embedded faces behave like the fetched ones.
        rule = rule.replace(url_m.group(1), data)
        rules.append(re.sub(r'\s*\n\s*', ' ', rule).strip())
    if not rules:
        sys.exit("error: no latin @font-face rules found")
    body = "\n".join(rules)
    return (f"<style>\n/* Fonts embedded by tools/scripts/embed_fonts.py "
            f"({len(rules)} latin faces, {raw_total/1024:.0f} KB of woff2). "
            f"No third-party requests. */\n{body}\n</style>\n"), len(rules), raw_total


def main() -> None:
    ap = argparse.ArgumentParser(description="Inline Google Fonts into a template.")
    ap.add_argument("template", type=Path)
    ap.add_argument("--out", type=Path, default=None, help="write here instead of in place")
    ap.add_argument("--check", action="store_true",
                    help="report whether the file still references a font host")
    args = ap.parse_args()

    src = args.template.read_text(encoding="utf-8")

    if args.check:
        hits = [h for h in FONT_HOSTS if h in src]
        print(f"{args.template}: " + (f"still references {', '.join(hits)}" if hits
                                      else "no third-party font requests"))
        sys.exit(1 if hits else 0)

    m = LINK_BLOCK.search(src)
    if not m:
        sys.exit("error: no Google Fonts link block found (already embedded?)")

    style, faces, raw = build_face_css(m.group("url"))
    out_text = src[:m.start()] + style + src[m.end():]

    leftover = [h for h in FONT_HOSTS if h in re.sub(r'base64,[A-Za-z0-9+/=]+', '', out_text)]
    if leftover:
        sys.exit(f"error: {', '.join(leftover)} still referenced after embedding")

    dst = args.out or args.template
    dst.write_text(out_text, encoding="utf-8")
    print(f"embedded {faces} faces ({raw/1024:.0f} KB woff2) into {dst}")
    print(f"  {len(src)/1024:.0f} KB -> {len(out_text)/1024:.0f} KB")


if __name__ == "__main__":
    main()
