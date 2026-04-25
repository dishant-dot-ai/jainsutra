#!/usr/bin/env python3
"""
For chapter files that have NO H2 in the hero (Ramayana, Mahabharat):
insert an H2 with the canonical hero format:

  <h2 class="text-5xl font-headline italic text-on-surface-variant leading-tight font-light">
    <span class="not-italic">Chapter N — </span>“Chapter Title (from H1)”
  </h2>

The italic+quoted part reuses the chapter title from H1 (text before the
text-primary span), so we don't fabricate content.

Insertion point: immediately before the first <p> that follows the </h1>
in the hero block.

Idempotent — skips files that already contain an H2.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from _add_chapter_prefix import chapter_label, SKIP_PATTERNS  # reuse

ROOT = Path("/Users/thefounder/Projects/active/JainAwaken/scripture")

H2_CLASS = "text-5xl font-headline italic text-on-surface-variant leading-tight font-light"

H1_RE = re.compile(r'<h1[^>]*>(.*?)</h1>', re.IGNORECASE | re.DOTALL)
SPAN_INSIDE_H1_RE = re.compile(
    r'<span\s+class="text-primary[^"]*"[^>]*>.*?</span>',
    re.IGNORECASE | re.DOTALL,
)


def extract_chapter_title(h1_inner: str) -> str:
    # Drop the inline original-language span, keep the leading title text
    cleaned = SPAN_INSIDE_H1_RE.sub("", h1_inner)
    # Collapse whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    # Drop trailing dash/em-dash if any
    cleaned = cleaned.rstrip(" —–-")
    return cleaned


def insert_h2(html: str, label: str) -> Tuple[str, bool]:
    # Skip if any H2 already exists
    if re.search(r'<h2[\s>]', html, re.IGNORECASE):
        return html, False

    m_h1 = H1_RE.search(html)
    if not m_h1:
        return html, False

    title = extract_chapter_title(m_h1.group(1))
    if not title:
        return html, False

    # Find the first <p ...> after </h1>
    end_h1 = m_h1.end()
    m_p = re.search(r'(\s*)<p\b', html[end_h1:], re.IGNORECASE)
    if not m_p:
        return html, False
    insert_at = end_h1 + m_p.start()
    indent = m_p.group(1)  # capture whitespace/newline before <p>

    h2_block = (
        f'{indent}<h2 class="{H2_CLASS}">'
        f'<span class="not-italic">{label} — </span>“{title}”</h2>'
    )

    return html[:insert_at] + h2_block + html[insert_at:], True


def should_skip(p: Path) -> bool:
    s = str(p)
    return any(pat in s for pat in SKIP_PATTERNS)


def main():
    files = sorted(ROOT.rglob("*.html"))
    targets = [f for f in files if not should_skip(f)]
    modified = 0
    no_label = 0
    for f in targets:
        label = chapter_label(f)
        if not label:
            no_label += 1
            continue
        src = f.read_text(encoding="utf-8")
        new, changed = insert_h2(src, label)
        if changed:
            f.write_text(new, encoding="utf-8")
            modified += 1
            print(f"  ✓ [{label}] {f.relative_to(ROOT)}")
    print(f"\nInserted H2 in {modified} files (skipped {no_label} unlabeled).")


if __name__ == "__main__":
    main()
