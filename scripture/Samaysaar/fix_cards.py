#!/usr/bin/env python3
"""Restructure Samaysaar sutra cards to match sutrakritang design."""

import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

BASE = Path('/Users/thefounder/Projects/active/JainSutra/scripture/Samaysaar')

ADHIKAR_MAP = {
    'samaysaar-ch2.html': 1,
    'samaysaar-ch3.html': 2,
    'samaysaar-ch4.html': 3,
    'samaysaar-ch5.html': 4,
    'samaysaar-ch6.html': 5,
    'samaysaar-ch7.html': 6,
    'samaysaar-ch8.html': 7,
    'samaysaar-ch9.html': 8,
}

def build_article(gatha_num, adhikar, parts):
    label = f'{adhikar}.{gatha_num}'
    content = '\n'.join(p for p in parts if p.strip())
    return (
        f'<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{gatha_num}">\n'
        f'<div class="flex items-start gap-6">\n'
        f'<span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{label}</span>\n'
        f'<div class="space-y-4 flex-1">\n'
        f'{content}\n'
        f'</div>\n'
        f'</div>\n'
        f'</article>'
    )

def fix_simple(html):
    return re.sub(r'<b>Simply[^<]*:</b>', '<b>The simple version:</b>', html)

def transform_ch2_6_card(card_str, adhikar):
    soup = BeautifulSoup(card_str, 'html.parser')
    card = soup.find('div', class_='sutra-card')
    if not card:
        return card_str

    # Gatha number
    header = card.find('div', class_='justify-between')
    if not header:
        return card_str
    gatha_span = header.find('span')
    gatha_text = gatha_span.get_text(strip=True) if gatha_span else ''
    m = re.search(r'\d+', gatha_text)
    gatha_num = m.group() if m else '0'

    # Concept tags
    tags_div = header.find('div', class_='concept-tags')
    tags_html = str(tags_div).strip() if tags_div else ''

    # Sanskrit
    sanskrit_p = card.find('p', class_='sutra-sanskrit')
    sanskrit_html = sanskrit_p.decode_contents() if sanskrit_p else ''

    # Translation (italic paragraph, not sanskrit)
    trans_p = None
    for p in card.find_all('p'):
        cls = ' '.join(p.get('class', []))
        if 'italic' in cls and p != sanskrit_p:
            trans_p = p
            break
    trans_html = trans_p.decode_contents() if trans_p else ''

    # Banners (in document order)
    banners = []
    for child in card.children:
        if not isinstance(child, Tag):
            continue
        cls = ' '.join(child.get('class', []))
        if any(x in cls for x in ['principle-banner', 'wrong-view-banner', 'caution-banner']):
            banners.append(str(child).strip())

    # Commentary paragraphs (leading-relaxed, not italic, not sanskrit)
    commentary = []
    for p in card.find_all('p'):
        if p == sanskrit_p or p == trans_p:
            continue
        cls = ' '.join(p.get('class', []))
        if 'leading-relaxed' in cls and 'italic' not in cls:
            commentary.append(p.decode_contents())

    # Simple explanation
    simple_tag = card.find(class_='simple-explanation')
    simple_inner = fix_simple(simple_tag.decode_contents()) if simple_tag else ''

    parts = []
    if sanskrit_html:
        parts.append(f'<p class="sutra-sanskrit font-headline">{sanskrit_html}</p>')
    if trans_html:
        parts.append(f'<p class="text-lg font-semibold text-on-surface leading-relaxed">{trans_html}</p>')
    parts.extend(banners)
    for cp in commentary:
        parts.append(f'<p class="text-base text-on-surface-variant leading-relaxed">{cp}</p>')
    if simple_inner:
        parts.append(f'<p class="simple-explanation">{simple_inner}</p>')
    if tags_html:
        parts.append(tags_html)

    return build_article(gatha_num, adhikar, parts)


def transform_ch7_9_card(card_str, adhikar):
    soup = BeautifulSoup(card_str, 'html.parser')
    card = soup.find('div', class_='sutra-card')
    if not card:
        return card_str

    # Gatha number from title span
    title_span = card.find('span', class_='tracking-widest')
    if not title_span:
        return card_str
    title_text = title_span.get_text(strip=True)
    m = re.search(r'G(\d+)', title_text)
    gatha_num = m.group(1) if m else '0'

    # Sanskrit
    sanskrit_p = card.find('p', class_='sutra-sanskrit')
    sanskrit_html = sanskrit_p.decode_contents() if sanskrit_p else ''

    # All paragraphs (direct children only, excluding title span + sanskrit)
    all_direct_ps = []
    for child in card.children:
        if not isinstance(child, Tag):
            continue
        if child == title_span or child == sanskrit_p:
            continue
        if child.name == 'p':
            all_direct_ps.append(child)

    # Banners
    banners = []
    for child in card.children:
        if not isinstance(child, Tag):
            continue
        cls = ' '.join(child.get('class', []))
        if any(x in cls for x in ['principle-banner', 'wrong-view-banner', 'caution-banner']):
            banners.append(str(child).strip())

    # Simple explanation (div or p with that class)
    simple_tag = card.find(class_='simple-explanation')
    simple_inner = fix_simple(simple_tag.decode_contents()) if simple_tag else ''

    # Concept tags
    tags_div = card.find('div', class_='concept-tags')
    tags_html = str(tags_div).strip() if tags_div else ''

    # Classify paragraphs
    italic_ps = []
    main_ps = []   # non-italic, non-small → translation + commentary
    small_ps = []  # text-sm (contemplate notes)
    for p in all_direct_ps:
        cls = ' '.join(p.get('class', []))
        if p == simple_tag:
            continue
        if 'text-sm' in cls:
            small_ps.append(p)
        elif 'italic' in cls:
            italic_ps.append(p)
        elif 'leading-relaxed' in cls:
            main_ps.append(p)

    # First main paragraph = translation; rest = commentary
    trans_html = main_ps[0].decode_contents() if main_ps else ''
    commentary = [p.decode_contents() for p in main_ps[1:]]

    parts = []
    if sanskrit_html:
        parts.append(f'<p class="sutra-sanskrit font-headline">{sanskrit_html}</p>')
    for ip in italic_ps:
        parts.append(str(ip).strip())
    if trans_html:
        parts.append(f'<p class="text-lg font-semibold text-on-surface leading-relaxed">{trans_html}</p>')
    parts.extend(banners)
    for cp in commentary:
        parts.append(f'<p class="text-base text-on-surface-variant leading-relaxed">{cp}</p>')
    for sp in small_ps:
        parts.append(str(sp).strip())
    if simple_inner:
        parts.append(f'<p class="simple-explanation">{simple_inner}</p>')
    if tags_html:
        parts.append(tags_html)

    return build_article(gatha_num, adhikar, parts)


def find_card_extents(html, marker):
    """Find (start, end) of each div.sutra-card block containing marker in its opening tag."""
    results = []
    search = 0
    while True:
        idx = html.find(marker, search)
        if idx == -1:
            break
        # Walk back to find the opening <div
        tag_start = html.rfind('<div', 0, idx)
        if tag_start == -1:
            search = idx + 1
            continue
        tag_close = html.find('>', tag_start)
        tag_text = html[tag_start:tag_close + 1]
        if 'sutra-card' not in tag_text:
            search = idx + 1
            continue
        # Walk forward to find matching </div>
        depth = 0
        i = tag_start
        found = False
        while i < len(html):
            if html[i:i+4] == '<div':
                depth += 1
                i += 4
            elif html[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    end = i + 6
                    results.append((tag_start, end))
                    search = end
                    found = True
                    break
                i += 6
            else:
                i += 1
        if not found:
            search = idx + 1
    return results


def remove_key_principles(html):
    marker = '<!-- Key Principles -->'
    pos = html.find(marker)
    if pos == -1:
        return html
    # Find next <div after the comment
    div_start = html.find('<div', pos)
    if div_start == -1:
        return html
    # Find matching </div>
    depth = 0
    i = div_start
    while i < len(html):
        if html[i:i+4] == '<div':
            depth += 1
            i += 4
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                html = html[:pos] + html[end:]
                break
            i += 6
        else:
            i += 1
    return html


def process_file(filepath, adhikar):
    is_ch7_9 = adhikar >= 6
    html = filepath.read_text(encoding='utf-8')

    # Remove Key Principles block (ch2-ch6 only)
    if not is_ch7_9:
        before = len(html)
        html = remove_key_principles(html)
        removed = before - len(html)
        if removed > 0:
            print(f'  Removed Key Principles block ({removed} chars)')

    # Marker differs by chapter type
    if is_ch7_9:
        marker = 'sutra-card rounded-xl p-7 flex flex-col gap-4'
    else:
        marker = 'sutra-card rounded-xl p-8 md:p-10 mb-6'

    extents = find_card_extents(html, marker)
    print(f'  {len(extents)} cards to transform')

    # Process in reverse so positions stay valid
    for start, end in reversed(extents):
        card_str = html[start:end]
        if is_ch7_9:
            new_card = transform_ch7_9_card(card_str, adhikar)
        else:
            new_card = transform_ch2_6_card(card_str, adhikar)
        html = html[:start] + new_card + html[end:]

    filepath.write_text(html, encoding='utf-8')
    print(f'  ✓ Saved')


if __name__ == '__main__':
    for filename, adhikar in ADHIKAR_MAP.items():
        fp = BASE / filename
        if not fp.exists():
            print(f'MISSING: {filename}')
            continue
        print(f'\n{filename} (Adhikar {adhikar}):')
        process_file(fp, adhikar)
    print('\nAll done.')
