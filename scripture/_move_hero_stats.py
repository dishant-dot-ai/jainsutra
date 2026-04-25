#!/usr/bin/env python3
"""
Move the hero stats/credits div down into the About This Chapter section
(immediately before the closing </div> of the right column, after the
existing paragraphs).

For Tattvartha-style pill badges, just remove them from the hero.

Idempotent — re-running is a no-op.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path("/Users/thefounder/Projects/active/JainAwaken/scripture")
SKIP = ["-index", "sacred-sutras-index", "samaysaar-poorvarang", "/.claude/", "/.git/"]

# Stats div: <div class="flex gap-8 ...">...stats columns...</div>
# Identified by containing the stat marker
STATS_MARKER = re.compile(r'<(?:div|span|p)\s+class="[^"]*text-3xl font-headline font-bold text-primary')

# Pill badges: <div class="flex flex-wrap gap-4 ..."> with <span class="bg-primary/10 ... rounded-full ...">
PILL_DIV_RE = re.compile(
    r'\s*<div class="flex flex-wrap gap-4[^"]*">\s*(?:<span class="bg-primary/10[^"]*rounded-full[^"]*"[^>]*>[^<]*</span>\s*)+</div>',
    re.IGNORECASE,
)


def find_balanced_div(html: str, start_idx: int) -> int:
    """Given an index pointing at <div, return the index AFTER its matching </div>."""
    depth = 0
    i = start_idx
    n = len(html)
    while i < n:
        if html[i:i+5] == '<div ' or html[i:i+4] == '<div':
            # Confirm it is an opening <div tag
            j = html.find('>', i)
            if j == -1: return -1
            depth += 1
            i = j + 1
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return i + 6
            i += 6
        else:
            i += 1
    return -1


def find_hero_stats_div(html: str) -> tuple[int, int, str] | None:
    """Locate the hero stats div. Returns (start, end, content) or None.

    Strategy: find <h2 in hero, then look for the next sibling <div...> after </h2>.
    If that div contains the stat marker, treat it as the stats wrapper.
    """
    h1_m = re.search(r'<h1', html)
    if not h1_m: return None
    sec_end = html.find('</section>', h1_m.start())
    if sec_end == -1: return None
    hero_end = sec_end

    # Find <h2 within the hero
    h2_open = re.search(r'<h2[^>]*>', html[h1_m.start():hero_end])
    if not h2_open: return None
    h2_close_rel = html[h1_m.start():hero_end].find('</h2>', h2_open.end())
    if h2_close_rel == -1: return None
    h2_close_abs = h1_m.start() + h2_close_rel + len('</h2>')

    # Find the next opening <div after </h2>, but stop if we hit another tag like <h3, <img, etc.
    # The stats wrapper should be the very next sibling div.
    after_h2 = html[h2_close_abs:hero_end]
    next_div = re.search(r'<div\b', after_h2)
    if not next_div: return None
    div_start_abs = h2_close_abs + next_div.start()
    div_end_abs = find_balanced_div(html, div_start_abs)
    if div_end_abs == -1: return None
    block = html[div_start_abs:div_end_abs]
    if not STATS_MARKER.search(block):
        return None
    # Sanity: don't grab a giant column wrapper. Cap to ~3000 chars.
    if div_end_abs - div_start_abs > 3000:
        return None
    return (div_start_abs, div_end_abs, block)


def find_about_section_inject_point(html: str) -> int | None:
    """Return the index where stats should be inserted inside the About This Chapter
    section — preferring just before the </div> that closes the right col-span-8
    div (template A), falling back to just before the closing </section>
    (template B / single-column layouts)."""
    m_label = re.search(r'About This (?:Chapter|Backstory|Text|Section|Adhikar)', html)
    if not m_label: return None
    # Try template A: col-span-8 right column
    right = re.search(r'<div class="col-span-12 lg:col-span-8[^"]*"[^>]*>', html[m_label.end():])
    if right:
        right_start = m_label.end() + right.start()
        right_end = find_balanced_div(html, right_start)
        if right_end != -1:
            return right_end - 6  # before the closing </div>
    # Fallback: inject right before the closing </section> of the About section
    sec_end = html.find('</section>', m_label.end())
    if sec_end == -1: return None
    return sec_end


def process(path: Path) -> str:
    src = path.read_text(encoding="utf-8")

    # Idempotency: skip if no hero stats div found AND no pill div
    stats = find_hero_stats_div(src)
    pill_m = PILL_DIV_RE.search(src) if not stats else None

    if stats:
        s, e, block = stats
        inject = find_about_section_inject_point(src)
        if inject is None:
            return "no-about"
        # Don't move if About already contains an identical block (idempotency)
        if block.strip() in src[inject-2000:inject]:
            return "already"
        # Cut from hero, paste into About
        # Need to compute injection index AFTER removal of hero block
        if inject < e:  # injection point shifts when we cut earlier content
            return "weird-order"
        # Build new
        before_hero_cut = src[:s]
        after_hero_cut = src[e:]
        # Combined removed content
        new_src = before_hero_cut + after_hero_cut
        # The inject point in the new_src has shifted by -(e - s)
        new_inject = inject - (e - s)
        block_to_inject = "\n" + block.strip() + "\n"
        new_src = new_src[:new_inject] + block_to_inject + new_src[new_inject:]
        path.write_text(new_src, encoding="utf-8")
        return "moved"

    if pill_m:
        # Remove the pill div from the hero (cuts the matched span and surrounding whitespace)
        # Confirm the match is in the hero region
        h1_m = re.search(r'<h1', src)
        sec_end = src.find('</section>', h1_m.start() if h1_m else 0)
        if h1_m and pill_m.start() < sec_end:
            new_src = src[:pill_m.start()] + src[pill_m.end():]
            path.write_text(new_src, encoding="utf-8")
            return "pill-removed"
    return "no-op"


def main():
    files = sorted(ROOT.rglob("*.html"))
    targets = [f for f in files if not any(s in str(f) for s in SKIP) and not f.name.startswith("_")]
    counts = {}
    for f in targets:
        result = process(f)
        counts[result] = counts.get(result, 0) + 1
        if result in ("moved", "pill-removed"):
            print(f"  ✓ [{result}] {f.relative_to(ROOT)}")
    print()
    for k, v in counts.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
