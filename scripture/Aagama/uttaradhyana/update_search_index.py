#!/usr/bin/env python3
"""Propagate updated SEARCH_INDEX (containing ch32) from ch32.html to all other chapter files."""
import re
from pathlib import Path

BASE = Path('/Users/thefounder/Projects/active/JainSutra/scripture/Aagama/uttaradhyana')

# Extract the SEARCH_INDEX JSON blob from ch32.html (it's the authoritative source)
ch32 = (BASE / 'uttaradhyana-ch32.html').read_text(encoding='utf-8')
m = re.search(r'var SEARCH_INDEX = (\[.*?\]);', ch32, re.DOTALL)
if not m:
    print('ERROR: Could not find SEARCH_INDEX in ch32.html')
    exit(1)

new_index_json = m.group(1)
print(f'Extracted SEARCH_INDEX: {len(new_index_json):,} chars')

# All HTML files in the directory except ch32 (already correct)
html_files = sorted(BASE.glob('uttaradhyana-*.html'))
html_files = [f for f in html_files if f.name != 'uttaradhyana-ch32.html']

updated = 0
skipped = 0
for fp in html_files:
    html = fp.read_text(encoding='utf-8')
    if 'SEARCH_INDEX' not in html:
        print(f'  SKIP (no SEARCH_INDEX): {fp.name}')
        skipped += 1
        continue

    new_html, n = re.subn(
        r'var SEARCH_INDEX = \[.*?\];',
        f'var SEARCH_INDEX = {new_index_json};',
        html,
        flags=re.DOTALL
    )
    if n == 0:
        print(f'  SKIP (no match): {fp.name}')
        skipped += 1
        continue

    fp.write_text(new_html, encoding='utf-8')
    print(f'  Updated: {fp.name}')
    updated += 1

print(f'\nDone: {updated} updated, {skipped} skipped')
