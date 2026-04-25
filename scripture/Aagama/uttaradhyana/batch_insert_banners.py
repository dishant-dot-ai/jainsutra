#!/usr/bin/env python3
"""
Batch insert all banners for chapters 3-36.
"""

import re
import json
from pathlib import Path

def create_banner_html(banner_type, name, definition):
    if banner_type == "principle":
        return f'<div class="principle-banner"><div class="principle-header"><span class="principle-badge">Jain Principle</span><span class="principle-name">{name}</span></div><p class="principle-def">{definition}</p></div>'
    elif banner_type == "caution":
        return f'<div class="caution-banner"><div class="caution-header"><span class="caution-badge">Caution</span><span class="caution-name">{name}</span></div><p class="caution-def">{definition}</p></div>'
    return ""

def process_chapter(chapter_num):
    mapping_file = Path(f"ch{chapter_num}_banners.json")
    if not mapping_file.exists():
        return False

    with open(mapping_file, 'r') as f:
        banner_mapping = json.load(f)

    html_file = Path(f"uttaradhyana-ch{chapter_num}.html")
    if not html_file.exists():
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    modified = html_content
    for sutra_num, sutra_data in banner_mapping['sutras'].items():
        if 'banners' not in sutra_data or not sutra_data['banners']:
            continue

        # Handle both sutra-N and sutra-N-M formats
        ch_str = str(chapter_num)
        sutra_match = re.search(rf'(<article[^>]*id="sutra-(?:{ch_str}-)?{sutra_num}"[^>]*>.*?</p>)\s*(<p class="text-lg font-semibold)', modified, re.DOTALL)

        if sutra_match:
            insertion_point = sutra_match.start(2)
            banner_html = '\n        '.join(create_banner_html(b['type'], b['name'], b['def']) for b in sutra_data['banners'])
            modified = modified[:insertion_point] + banner_html + '\n        ' + modified[insertion_point:]

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified)

    return True

# Process all chapters except 1-2 (already done)
successful = []
for ch in range(3, 37):
    if ch == 32:
        continue

    if process_chapter(ch):
        successful.append(ch)
        print(f"✓ Chapter {ch}")
    else:
        print(f"✗ Chapter {ch}")

print(f"\n✓ Successfully processed {len(successful)} chapters: {successful}")
