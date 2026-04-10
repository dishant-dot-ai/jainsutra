#!/usr/bin/env python3
"""
Apply ch1 UI spec to Sutrakritanga ch2–ch23:
1. Fix banner CSS (background style, not border-bottom)
2. Fix simple-explanation (line-height 1.85, font-size 1.2rem, b label color #1d1c17)
3. Remove hover effects
4. Reposition banners: translation → banner(s) → commentary
"""
import re
import sys
from bs4 import BeautifulSoup

BASE = '/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/sutrakritang'

NEW_BANNER_CSS = """.wrong-view-banner { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; padding: 1rem 1.25rem 1rem 1.25rem; background: rgba(186,26,26,0.04); border-radius: 6px; }
.wrong-view-header { display: inline-flex; align-items: center; gap: 8px; }
.wrong-view-badge { background: rgba(186,26,26,0.1); border: 1px solid rgba(186,26,26,0.35); color: #9b1515; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 700; padding: 3px 11px; border-radius: 4px; }
.wrong-view-name { font-family: 'Noto Serif', serif; font-size: 1.0625rem; font-weight: 700; color: #1d1c17; }
.wrong-view-def { font-family: 'Inter', sans-serif; font-size: 0.9625rem; color: #7e7665; line-height: 1.65; font-style: italic; }
/* Green: Key Jain Principle */
.principle-banner { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; padding: 1rem 1.25rem 1rem 1.25rem; background: rgba(22,101,52,0.04); border-radius: 6px; }
.principle-header { display: inline-flex; align-items: center; gap: 8px; }
.principle-badge { background: rgba(22,101,52,0.1); border: 1px solid rgba(22,101,52,0.35); color: #166534; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 700; padding: 3px 11px; border-radius: 4px; }
.principle-name { font-family: 'Noto Serif', serif; font-size: 1.0625rem; font-weight: 700; color: #1d1c17; }
.principle-def { font-family: 'Inter', sans-serif; font-size: 0.9625rem; color: #7e7665; line-height: 1.65; font-style: italic; }
/* Blue: Caution / Warning */
.caution-banner { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; padding: 1rem 1.25rem 1rem 1.25rem; background: rgba(30,64,175,0.04); border-radius: 6px; }
.caution-header { display: inline-flex; align-items: center; gap: 8px; }
.caution-badge { background: rgba(30,64,175,0.1); border: 1px solid rgba(30,64,175,0.35); color: #1e40af; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 700; padding: 3px 11px; border-radius: 4px; }
.caution-name { font-family: 'Noto Serif', serif; font-size: 1.0625rem; font-weight: 700; color: #1d1c17; }
.caution-def { font-family: 'Inter', sans-serif; font-size: 0.9625rem; color: #7e7665; line-height: 1.65; font-style: italic; }"""

BANNER_CLASSES = {'wrong-view-banner', 'principle-banner', 'caution-banner'}


def fix_css(css):
    # Fix simple-explanation: font-size 1.2rem, line-height 1.85
    css = re.sub(
        r'(\.simple-explanation\s*\{[^}]*?)font-size\s*:\s*[\d.]+rem([^}]*\})',
        r'\g<1>font-size: 1.2rem\g<2>',
        css
    )
    css = re.sub(
        r'(\.simple-explanation\s*\{[^}]*?)line-height\s*:\s*[\d.]+([^}]*\})',
        r'\g<1>line-height: 1.85\g<2>',
        css
    )

    # Fix simple-explanation b: color #1d1c17
    css = re.sub(
        r'(\.simple-explanation\s+b\s*\{[^}]*?)color\s*:\s*#[0-9a-fA-F]+([^}]*\})',
        r'\g<1>color: #1d1c17\g<2>',
        css
    )

    # Remove hover CSS block comment + rules
    css = re.sub(r'/\*\s*Sutra card hover\s*\*/\s*', '', css)
    css = re.sub(r'\.sutra-card\s*\{\s*transition\s*:[^}]+\}\s*', '', css)
    css = re.sub(r'\.sutra-card:hover\s*\{[^}]+\}\s*', '', css)

    # Replace banner CSS block (wrong-view-banner through caution-def)
    css = re.sub(
        r'\.wrong-view-banner\s*\{.*?\.caution-def\s*\{[^}]*\}',
        NEW_BANNER_CSS,
        css,
        flags=re.DOTALL
    )

    return css


def fix_banner_positioning(soup):
    """Move banners that appear before the translation (text-lg) to after it."""
    for card in soup.find_all(class_='sutra-card'):
        content_div = card.find('div', class_=lambda c: c and 'space-y-4' in c)
        if not content_div:
            continue

        # Find translation paragraph
        translation = content_div.find('p', class_=lambda c: c and 'text-lg' in c.split())
        if not translation:
            continue

        # Collect banners that come BEFORE the translation in DOM order
        banners_before = []
        for child in list(content_div.children):
            if not hasattr(child, 'get'):
                continue  # skip NavigableStrings/whitespace
            if child is translation:
                break
            classes = child.get('class', [])
            if BANNER_CLASSES.intersection(classes):
                banners_before.append(child)

        if not banners_before:
            continue

        # Extract them from current position
        for banner in banners_before:
            banner.extract()

        # Re-insert in order after translation
        insertion_point = translation
        for banner in banners_before:
            insertion_point.insert_after(banner)
            insertion_point = banner

    return soup


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Fix CSS
    style_tag = soup.find('style')
    if style_tag and style_tag.string:
        fixed_css = fix_css(style_tag.string)
        style_tag.string = fixed_css

    # Fix banner positioning
    soup = fix_banner_positioning(soup)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))


def main():
    chapters = range(2, 24)
    if len(sys.argv) > 1:
        chapters = [int(x) for x in sys.argv[1:]]

    for ch in chapters:
        filepath = f'{BASE}/sutrakritang-ch{ch}.html'
        print(f'Processing ch{ch}...', end=' ', flush=True)
        process_file(filepath)
        print('done')

    print('All done.')


if __name__ == '__main__':
    main()
