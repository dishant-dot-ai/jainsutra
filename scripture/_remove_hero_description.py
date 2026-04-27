#!/usr/bin/env python3
"""
Remove the hero description <p> (the paragraph that sits below the
subtitle and credit/stats section in the hero block) from every chapter
file across every scripture.

Identification: the first <p> AFTER the hero <h2> whose class string
contains "text-xl text-on-surface-variant leading-relaxed opacity-90 max-w-"
(matches both max-w-lg and max-w-2xl).

Idempotent — re-running is a no-op.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from typing import Tuple

sys.path.insert(0, str(Path(__file__).parent))
from _add_chapter_prefix import SKIP_PATTERNS

ROOT = Path("/Users/thefounder/Projects/active/JainSutra/scripture")

H2_RE = re.compile(r'<h2[\s>]', re.IGNORECASE)

# Match the hero description paragraph (first one after </h2>).
# Class fingerprint: text-xl text-on-surface-variant leading-relaxed opacity-90 max-w-...
HERO_P_RE = re.compile(
    r'(\s*)<p\s+class="[^"]*\btext-xl\s+text-on-surface-variant\s+leading-relaxed\s+opacity-90\s+max-w-[^"]*"\s*>.*?</p>',
    re.IGNORECASE | re.DOTALL,
)


def remove_hero_description(html: str) -> Tuple[str, bool]:
    m_h2 = H2_RE.search(html)
    if not m_h2:
        return html, False
    after_h2 = html[m_h2.end():]
    m_p = HERO_P_RE.search(after_h2)
    if not m_p:
        return html, False
    abs_start = m_h2.end() + m_p.start()
    abs_end = m_h2.end() + m_p.end()
    return html[:abs_start] + html[abs_end:], True


def should_skip(p: Path) -> bool:
    s = str(p)
    return any(pat in s for pat in SKIP_PATTERNS)


def main():
    files = sorted(ROOT.rglob("*.html"))
    targets = [f for f in files if not should_skip(f)]
    modified = 0
    for f in targets:
        src = f.read_text(encoding="utf-8")
        new, changed = remove_hero_description(src)
        if changed:
            f.write_text(new, encoding="utf-8")
            modified += 1
            print(f"  ✓ {f.relative_to(ROOT)}")
    print(f"\nRemoved hero description from {modified}/{len(targets)} files.")


if __name__ == "__main__":
    main()
