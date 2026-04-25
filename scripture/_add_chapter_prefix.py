#!/usr/bin/env python3
"""
Add "Chapter N — " prefix to H2 (descriptive subtitle) of every chapter
hero. The prefix is wrapped in <span class="not-italic"> so it shows
upright (not italic) and is OUTSIDE the curly quotes.

Idempotent — re-running is a no-op.

Final H2 shape:
  <h2 class="text-5xl ... italic ...">
    <span class="not-italic">Chapter N — </span>“…existing italic, quoted subtitle…”
  </h2>

Special cases for the chapter number derived from filename:
  *-ch{N}*.html        → Chapter N           (most files)
  *-a{N}.html          → Chapter N           (PrashnaVyakaran gates)
  *-backstory-{N}.html → Backstory N         (Ramayana backstory)
  *-varga{V}-ch{N}.html→ Varga V · Chapter N (Nirayavali)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

ROOT = Path("/Users/thefounder/Projects/active/JainAwaken/scripture")

SKIP_PATTERNS = [
    "-index",
    "sacred-sutras-index",
    "samaysaar-poorvarang",
    "_restyle_hero.py",
    "_add_chapter_prefix.py",
    "/.claude/",
    "/.git/",
]

# Regexes for filename → chapter label
RX_VARGA_CH   = re.compile(r"-varga(\d+)-ch(\d+)\.html$", re.IGNORECASE)
RX_BACKSTORY  = re.compile(r"-backstory-(\d+)\.html$",     re.IGNORECASE)
RX_PRASHNA    = re.compile(r"-ss\d+-a(\d+)\.html$",        re.IGNORECASE)
RX_CHAPTER    = re.compile(r"-ch(\d+)(?:-v\d+)?\.html$",   re.IGNORECASE)

H2_RE = re.compile(
    r'<h2(\s+class="[^"]*")\s*>(.*?)</h2>',
    re.IGNORECASE | re.DOTALL,
)
PREFIX_SPAN_RE = re.compile(
    r'^\s*<span class="not-italic">[^<]*</span>\s*',
    re.IGNORECASE,
)
INTERNAL_CHAPTER_RE = re.compile(
    r'^[“"]\s*Chapter\s+(\d+)\s*[—–-]\s*',
    re.IGNORECASE,
)


def chapter_label(p: Path) -> Optional[str]:
    name = p.name
    m = RX_VARGA_CH.search(name)
    if m:
        return f"Varga {int(m.group(1))} · Chapter {int(m.group(2))}"
    m = RX_BACKSTORY.search(name)
    if m:
        return f"Backstory {int(m.group(1))}"
    m = RX_PRASHNA.search(name)
    if m:
        return f"Chapter {int(m.group(1))}"
    m = RX_CHAPTER.search(name)
    if m:
        return f"Chapter {int(m.group(1))}"
    return None


def transform_h2(html: str, label: str) -> Tuple[str, bool]:
    m = H2_RE.search(html)
    if not m:
        return html, False
    cls_attr, inner = m.group(1), m.group(2)
    inner_stripped = inner.strip()

    # Idempotency: if the not-italic prefix is already present with the right label, skip
    existing_prefix = PREFIX_SPAN_RE.match(inner_stripped)
    if existing_prefix:
        # If label already matches, nothing to do
        if existing_prefix.group(0).strip() == f'<span class="not-italic">{label} — </span>'.strip():
            return html, False
        # Otherwise strip old prefix and re-add
        inner_stripped = PREFIX_SPAN_RE.sub("", inner_stripped, count=1).lstrip()

    # If the existing italic/quoted content begins with "Chapter N —" *inside* the quotes
    # (Tattvartha case), peel it out of the quotes.
    # Find leading quote, then "Chapter N — "
    quote_chars = '“"'
    if inner_stripped and inner_stripped[0] in quote_chars:
        opening = inner_stripped[0]
        rest = inner_stripped[1:]
        m_int = re.match(r'\s*Chapter\s+\d+\s*[—–-]\s*', rest, re.IGNORECASE)
        if m_int:
            rest = rest[m_int.end():]
            inner_stripped = opening + rest

    new_inner = f'<span class="not-italic">{label} — </span>{inner_stripped}'
    new_h2 = f'<h2{cls_attr}>{new_inner}</h2>'
    if new_h2 == m.group(0):
        return html, False
    return html[:m.start()] + new_h2 + html[m.end():], True


def should_skip(p: Path) -> bool:
    s = str(p)
    return any(pat in s for pat in SKIP_PATTERNS)


def main():
    files = sorted(ROOT.rglob("*.html"))
    targets = [f for f in files if not should_skip(f)]
    print(f"HTML files total: {len(files)}, candidates: {len(targets)}")

    modified = 0
    skipped_no_label = []
    for f in targets:
        label = chapter_label(f)
        if not label:
            skipped_no_label.append(str(f.relative_to(ROOT)))
            continue
        src = f.read_text(encoding="utf-8")
        new, changed = transform_h2(src, label)
        if changed:
            f.write_text(new, encoding="utf-8")
            modified += 1
            print(f"  ✓ [{label}] {f.relative_to(ROOT)}")
        else:
            print(f"  - [{label}] {f.relative_to(ROOT)} (no change)")

    print(f"\nModified {modified}/{len(targets)} files.")
    if skipped_no_label:
        print(f"\nSkipped (no chapter pattern in filename):")
        for s in skipped_no_label:
            print(f"  {s}")


if __name__ == "__main__":
    main()
