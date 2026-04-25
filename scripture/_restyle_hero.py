#!/usr/bin/env python3
"""
Restyle hero block (H1 + H2 + P) of every chapter file to match
Tattvartha ch5 hierarchy. Content preserved verbatim.

Target hierarchy (from tattvartha-ch5-v4.html):
  H1: text-8xl font-headline font-bold text-on-surface leading-tight tracking-tighter
      inner: <span class="text-primary font-normal">(ORIGINAL_WORD)</span>     # inline parens
  H2: text-5xl font-headline italic text-on-surface-variant leading-tight font-light
      content wrapped in curly quotes  "..."
  P : (left alone)
"""
import re
import sys
from pathlib import Path

ROOT = Path("/Users/thefounder/Projects/active/JainAwaken/scripture")

# Skip these (already match, or are not chapters)
SKIP_PATTERNS = [
    "tattvartha/",          # already matches
    "-index",               # any index file
    "sacred-sutras-index",
    "samaysaar-poorvarang", # not a numbered chapter; leave
    "_restyle_hero.py",
    "/.claude/",            # agent worktree leftovers; not user-facing
    "/.git/",
]

NEW_H1_CLASS = "text-8xl font-headline font-bold text-on-surface leading-tight tracking-tighter"
NEW_H2_CLASS = "text-5xl font-headline italic text-on-surface-variant leading-tight font-light"

# Match the H1 opening tag with any class attribute
H1_OPEN_RE = re.compile(r'<h1\s+class="[^"]*"\s*>', re.IGNORECASE)
# Match the inner span (the "block" Sanskrit subtitle) with any attributes (incl. malformed)
# It begins with <span ... text-primary font-normal ... > WORD </span>
SPAN_RE = re.compile(
    r'<span\s+[^>]*text-primary\s+font-normal[^>]*>\s*([^<]+?)\s*</span>',
    re.IGNORECASE | re.DOTALL,
)
# Match the H2 opening tag and capture inner content up to </h2>
H2_BLOCK_RE = re.compile(
    r'<h2\s+class="[^"]*"\s*>(.*?)</h2>',
    re.IGNORECASE | re.DOTALL,
)

def restyle_hero(html: str) -> tuple[str, bool]:
    changed = False

    # --- H1 block: find opening h1, then within the h1..</h1>, restyle span to inline parens ---
    m_h1 = re.search(r'(<h1\s+class="[^"]*"\s*>)(.*?)(</h1>)', html, re.IGNORECASE | re.DOTALL)
    if m_h1:
        h1_open, h1_inner, h1_close = m_h1.group(1), m_h1.group(2), m_h1.group(3)

        # Replace span with inline-parens version
        new_inner = h1_inner
        m_span = SPAN_RE.search(new_inner)
        if m_span:
            word = m_span.group(1).strip()
            # Idempotency: don't re-wrap if already in (parens)
            if not (word.startswith("(") and word.endswith(")")):
                word = f"({word})"
            new_span = f' <span class="text-primary font-normal">{word}</span>'
            new_inner = SPAN_RE.sub(new_span, new_inner, count=1)
            # Collapse any whitespace immediately before the new span
            new_inner = re.sub(r'\s+<span class="text-primary font-normal">', ' <span class="text-primary font-normal">', new_inner)

        new_h1_open = f'<h1 class="{NEW_H1_CLASS}">'
        new_h1 = new_h1_open + new_inner + h1_close

        if new_h1 != m_h1.group(0):
            html = html[:m_h1.start()] + new_h1 + html[m_h1.end():]
            changed = True

    # --- H2 block: restyle class + wrap content in curly quotes (if not already) ---
    m_h2 = H2_BLOCK_RE.search(html)
    if m_h2:
        inner = m_h2.group(1).strip()
        # Strip outer whitespace/newlines
        inner_compact = re.sub(r'\s+', ' ', inner).strip()
        # Already wrapped in curly quotes?
        if not (inner_compact.startswith('“') and inner_compact.endswith('”')):
            inner_compact = f'“{inner_compact}”'
        new_h2 = f'<h2 class="{NEW_H2_CLASS}">{inner_compact}</h2>'
        if new_h2 != m_h2.group(0):
            html = html[:m_h2.start()] + new_h2 + html[m_h2.end():]
            changed = True

    return html, changed


def should_skip(p: Path) -> bool:
    s = str(p)
    return any(pat in s for pat in SKIP_PATTERNS)


def main():
    files = sorted(ROOT.rglob("*.html"))
    chapter_files = [f for f in files if not should_skip(f)]
    print(f"Total HTML files: {len(files)}")
    print(f"Chapter files to process: {len(chapter_files)}")

    modified = 0
    for f in chapter_files:
        original = f.read_text(encoding="utf-8")
        new, changed = restyle_hero(original)
        if changed:
            f.write_text(new, encoding="utf-8")
            modified += 1
            print(f"  ✓ {f.relative_to(ROOT)}")
        else:
            print(f"  - {f.relative_to(ROOT)} (no change)")

    print(f"\nModified {modified}/{len(chapter_files)} files.")


if __name__ == "__main__":
    main()
