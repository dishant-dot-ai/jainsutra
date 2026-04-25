#!/usr/bin/env python3
"""
Unify hero hierarchy across every chapter file to match Tattvartha ch5:

  H1: English title <span class="block text-primary font-normal text-3xl md:text-4xl mt-2">(देवनागरी)</span>
  H2: text-5xl font-headline text-on-surface-variant leading-tight font-light   (NO italic)
      Chapter N — “Subtitle text”          (the “Chapter N — ” is plain, no <span> wrapper)

Idempotent — re-running is a no-op.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from typing import Tuple

ROOT = Path("/Users/thefounder/Projects/active/JainAwaken/scripture")

SKIP_PATTERNS = [
    "-index",
    "sacred-sutras-index",
    "samaysaar-poorvarang",
    "_unify_hero_v2.py",
    "_restyle_hero.py",
    "_add_chapter_prefix.py",
    "_insert_h2.py",
    "_remove_hero_description.py",
    "_apply_title_translations.py",
    "/.claude/",
    "/.git/",
]

# H1 span: enforce block style with sizing (Tattvartha pattern)
H1_SPAN_RE = re.compile(
    r'<span\s+class="[^"]*\btext-primary\b[^"]*"[^>]*>(\([^)]+\))</span>',
    re.IGNORECASE,
)
NEW_H1_SPAN_CLASSES = "block text-primary font-normal text-3xl md:text-4xl mt-2"

# H2: enforce non-italic, drop the not-italic chapter-prefix wrapper
H2_RE = re.compile(r'<h2\s+class="([^"]*)"\s*>(.*?)</h2>', re.IGNORECASE | re.DOTALL)
PREFIX_SPAN_RE = re.compile(r'<span class="not-italic">([^<]*)</span>\s*', re.IGNORECASE)
NEW_H2_CLASSES = "text-5xl font-headline text-on-surface-variant leading-tight font-light"


def fix_h1_span(html: str) -> Tuple[str, bool]:
    changed = False
    def repl(m: re.Match) -> str:
        nonlocal changed
        new = f'<span class="{NEW_H1_SPAN_CLASSES}">{m.group(1)}</span>'
        if new != m.group(0):
            changed = True
        return new
    new_html = H1_SPAN_RE.sub(repl, html, count=1)
    return new_html, changed


def fix_h2(html: str) -> Tuple[str, bool]:
    m = H2_RE.search(html)
    if not m:
        return html, False
    cls, inner = m.group(1), m.group(2)

    # Remove "italic" from class list, normalize whitespace
    new_cls = re.sub(r'\bitalic\b', '', cls)
    new_cls = re.sub(r'\s+', ' ', new_cls).strip()

    # Pull "Chapter N — " (or "Backstory N —", or "Varga … —") out of the not-italic wrapper
    inner_compact = re.sub(r'\s+', ' ', inner).strip()
    new_inner = PREFIX_SPAN_RE.sub(r'\1', inner_compact, count=1)

    new_h2 = f'<h2 class="{new_cls}">{new_inner}</h2>'
    if new_h2 == m.group(0):
        return html, False
    return html[:m.start()] + new_h2 + html[m.end():], True


def should_skip(p: Path) -> bool:
    s = str(p)
    return any(pat in s for pat in SKIP_PATTERNS)


def main():
    files = sorted(ROOT.rglob("*.html"))
    targets = [f for f in files if not should_skip(f)]
    h1_n = h2_n = 0
    for f in targets:
        src = f.read_text(encoding="utf-8")
        new, c1 = fix_h1_span(src)
        new, c2 = fix_h2(new)
        if c1 or c2:
            f.write_text(new, encoding="utf-8")
            tag = ("H1+H2" if c1 and c2 else ("H1" if c1 else "H2"))
            print(f"  ✓ [{tag}] {f.relative_to(ROOT)}")
        if c1: h1_n += 1
        if c2: h2_n += 1
    print(f"\nH1 spans updated: {h1_n}\nH2 unitalicized:  {h2_n}\nTotal candidates: {len(targets)}")


if __name__ == "__main__":
    main()
