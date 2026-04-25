#!/usr/bin/env python3
"""
Batch process all remaining chapters:
1. Extract sutra translations
2. Show them for review
3. Allow quick input of banner decisions
4. Generate JSON mapping
5. Run insertion script
"""

import re
import json
from pathlib import Path

def extract_chapter_sutras(chapter_num):
    """Extract all sutras from a chapter."""
    html_file = Path(f"uttaradhyana-ch{chapter_num}.html")
    if not html_file.exists():
        return None

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    sutra_pattern = r'<article[^>]*id="sutra-(\d+)"[^>]*>(.*?)</article>'
    matches = list(re.finditer(sutra_pattern, html_content, re.DOTALL))

    sutras = []
    for match in matches:
        sutra_num = match.group(1)
        sutra_content = match.group(2)

        trans_match = re.search(r'<p class="text-lg font-semibold[^>]*>(.*?)</p>', sutra_content, re.DOTALL)
        translation = trans_match.group(1) if trans_match else "N/A"
        translation_text = re.sub(r'<[^>]+>', '', translation).strip()[:120]

        sutras.append({
            'num': sutra_num,
            'translation': translation_text
        })

    return sutras

def show_chapter_summary(chapter_num):
    """Show summary of chapter for quick review."""
    sutras = extract_chapter_sutras(chapter_num)
    if not sutras:
        print(f"Chapter {chapter_num} not found")
        return None

    print(f"\n{'='*90}")
    print(f"CHAPTER {chapter_num} ({len(sutras)} sutras)")
    print(f"{'='*90}\n")

    for s in sutras:
        print(f"  {chapter_num}.{s['num']}: {s['translation']}")

    return sutras

# Show Chapter 2 for review
show_chapter_summary(2)
