#!/usr/bin/env python3
"""
Insert banners (principle, caution, wrong-view) into chapter HTML files.
Uses banner mapping JSON files to determine placement.
"""

import re
import json
from pathlib import Path

def create_banner_html(banner_type, name, definition):
    """Create banner HTML based on type."""
    if banner_type == "principle":
        return f'''<div class="principle-banner"><div class="principle-header"><span class="principle-badge">Jain Principle</span><span class="principle-name">{name}</span></div><p class="principle-def">{definition}</p></div>'''
    elif banner_type == "caution":
        return f'''<div class="caution-banner"><div class="caution-header"><span class="caution-badge">Caution</span><span class="caution-name">{name}</span></div><p class="caution-def">{definition}</p></div>'''
    elif banner_type == "wrong-view":
        return f'''<div class="wrong-view-banner"><div class="wrong-view-header"><span class="wrong-view-badge">Wrong View Refuted</span><span class="wrong-view-name">{name}</span></div><p class="wrong-view-def">{definition}</p></div>'''
    return ""

def insert_banners_into_html(html_content, banner_mapping):
    """Insert banners into HTML based on mapping."""
    # For each sutra in the mapping, find it in the HTML and insert banners
    modified = html_content

    for sutra_num, sutra_data in banner_mapping['sutras'].items():
        if 'banners' not in sutra_data or not sutra_data['banners']:
            continue

        # Find the sutra article
        sutra_id = f'id="sutra-{sutra_num}"'
        sutra_pattern = rf'(<article[^>]*{re.escape(sutra_id)}[^>]*>.*?</p>)'

        # Find where to insert (after Sanskrit, before English translation)
        # Pattern: </p> (end of Sanskrit) then <p class="text-lg font-semibold (English translation)
        sutra_match = re.search(rf'(<article[^>]*{re.escape(sutra_id)}[^>]*>.*?</p>)\s*(<p class="text-lg font-semibold)', modified, re.DOTALL)

        if sutra_match:
            # Insert banners right before the English translation
            insertion_point = sutra_match.start(2)
            banner_html = '\n        '.join(create_banner_html(b['type'], b['name'], b['def']) for b in sutra_data['banners'])
            modified = modified[:insertion_point] + banner_html + '\n        ' + modified[insertion_point:]

    return modified

def process_chapter(chapter_num):
    """Process a single chapter."""
    # Load mapping
    mapping_file = Path(f"ch{chapter_num}_banners.json")
    if not mapping_file.exists():
        print(f"Mapping file not found for chapter {chapter_num}")
        return False

    with open(mapping_file, 'r') as f:
        banner_mapping = json.load(f)

    # Load HTML
    html_file = Path(f"uttaradhyana-ch{chapter_num}.html")
    if not html_file.exists():
        print(f"HTML file not found: {html_file}")
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Insert banners
    modified_html = insert_banners_into_html(html_content, banner_mapping)

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified_html)

    print(f"✓ Chapter {chapter_num} updated successfully")
    return True

# Test on Chapter 1
if process_chapter(1):
    print("\nBanners inserted into Chapter 1!")
else:
    print("Failed to process Chapter 1")
