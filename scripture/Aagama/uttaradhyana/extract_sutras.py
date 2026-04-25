#!/usr/bin/env python3
import re
from pathlib import Path

html_file = Path("uttaradhyana-ch1.html")
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract all sutras
sutra_pattern = r'<article[^>]*id="sutra-(\d+)"[^>]*>(.*?)</article>'
matches = re.finditer(sutra_pattern, html_content, re.DOTALL)

for match in matches:
    sutra_num = match.group(1)
    sutra_content = match.group(2)

    # Extract translation
    trans_match = re.search(r'<p class="text-lg font-semibold[^>]*>(.*?)</p>', sutra_content, re.DOTALL)
    translation = trans_match.group(1) if trans_match else "N/A"
    translation_text = re.sub(r'<[^>]+>', '', translation).strip()[:120]

    print(f"\n{'='*80}")
    print(f"SUTRA 1.{sutra_num}")
    print(f"Translation: {translation_text}")
    print(f"{'='*80}")
