#!/usr/bin/env python3
"""
Script to add Jain Principle, Caution, and Wrong-View banners to Uttaradhyana sutras.
Parses HTML, extracts sutra data, and adds banners at the right location.
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser

class SutraExtractor(HTMLParser):
    """Parse HTML and extract sutra elements."""
    def __init__(self):
        super().__init__()
        self.in_sutra = False
        self.sutra_depth = 0
        self.current_sutra = []
        self.sutras = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        if tag == "article" and any(k == "class" and "sutra-card" in v for k, v in attrs):
            self.in_sutra = True
            self.sutra_depth = 1
            self.current_sutra = [f"<{tag}"]
            for k, v in attrs:
                self.current_sutra[0] += f' {k}="{v}"'
            self.current_sutra[0] += ">"
        elif self.in_sutra:
            self.sutra_depth += 1
            tag_str = f"<{tag}"
            for k, v in attrs:
                tag_str += f' {k}="{v}"'
            tag_str += ">"
            self.current_sutra.append(tag_str)

    def handle_endtag(self, tag):
        if self.in_sutra:
            self.current_sutra.append(f"</{tag}>")
            self.sutra_depth -= 1
            if tag == "article" and self.sutra_depth == 0:
                self.sutras.append("\n".join(self.current_sutra))
                self.in_sutra = False
                self.current_sutra = []

    def handle_data(self, data):
        if self.in_sutra:
            self.current_sutra.append(data)

def extract_sutras(html_content):
    """Extract all sutra articles from HTML."""
    # Simple regex-based extraction
    sutra_pattern = r'<article class="sutra-card[^"]*"[^>]*id="sutra-(\d+)"[^>]*>.*?</article>'
    sutras = re.findall(sutra_pattern, html_content, re.DOTALL)
    return sutras

def find_insertion_point(sutra_html):
    """Find where to insert banner (after Sanskrit, before English translation)."""
    # Look for the sutra-sanskrit element end, then find the next <p> tag
    sanskrit_end = sutra_html.find('</p>') # End of Sanskrit
    if sanskrit_end == -1:
        return -1

    # Find next <p> after Sanskrit (should be English translation)
    translation_start = sutra_html.find('<p ', sanskrit_end)
    if translation_start == -1:
        return -1

    return translation_start

def get_chapter_num(filename):
    """Extract chapter number from filename."""
    match = re.search(r'ch(\d+)', filename)
    return int(match.group(1)) if match else None

# Test with chapter 1
ch1_path = Path("/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana/uttaradhyana-ch1.html")
if ch1_path.exists():
    with open(ch1_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find sutra articles
    sutra_matches = re.finditer(r'<article class="sutra-card[^>]*id="sutra-(\d+)"[^>]*>(.*?)</article>', content, re.DOTALL)

    sutra_data = []
    for match in sutra_matches:
        sutra_num = match.group(1)
        sutra_html = match.group(2)

        # Extract Sanskrit
        sanskrit_match = re.search(r'<p class="sutra-sanskrit[^>]*>(.*?)</p>', sutra_html, re.DOTALL)
        sanskrit = sanskrit_match.group(1) if sanskrit_match else "N/A"

        # Extract English translation
        trans_match = re.search(r'<p class="text-lg font-semibold[^>]*>(.*?)</p>', sutra_html, re.DOTALL)
        translation = trans_match.group(1) if trans_match else "N/A"

        # Extract commentary
        commentary_match = re.search(r'<p class="text-base text-on-surface-variant[^>]*>(.*?)</p>', sutra_html, re.DOTALL)
        commentary = commentary_match.group(1) if commentary_match else "N/A"

        sutra_data.append({
            'num': sutra_num,
            'sanskrit': sanskrit[:100],
            'translation': translation[:150],
            'commentary': commentary[:300] if commentary else "N/A"
        })

    print(f"Found {len(sutra_data)} sutras in Chapter 1\n")
    for s in sutra_data[:5]:  # Show first 5
        print(f"Sutra {s['num']}:")
        print(f"  Translation: {s['translation'][:100]}...")
        print(f"  Commentary snippet: {s['commentary'][:150]}...\n")
else:
    print("File not found")
