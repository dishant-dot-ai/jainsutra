#!/usr/bin/env python3
"""
Reposition banners to after translation and before commentary.
Also update CSS for better visibility.
"""

import re
from pathlib import Path

def reposition_banners_in_chapter(chapter_num):
    """Move banners from after Sanskrit to after Translation."""
    html_file = Path(f"uttaradhyana-ch{chapter_num}.html")
    if not html_file.exists():
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find sutra articles with banners after Sanskrit
    # Matches: Sanskrit </p> [newline] banner [newline] translation
    # We want to move banners AFTER translation instead

    # Find all sutra-card articles
    sutra_pattern = r'(<article[^>]*id="sutra-[^"]*"[^>]*>.*?</article>)'

    def fix_sutra(match):
        sutra_html = match.group(0)

        # Extract the components
        sanskrit_match = re.search(r'(<p class="sutra-sanskrit[^>]*>.*?</p>)', sutra_html, re.DOTALL)
        banners_match = re.search(r'((?:<div class="(?:principle|caution|wrong-view)-banner"[^>]*>.*?</div>\s*)+)', sutra_html, re.DOTALL)
        translation_match = re.search(r'(<p class="text-lg font-semibold[^>]*>.*?</p>)', sutra_html, re.DOTALL)
        commentary_match = re.search(r'(<p class="text-base text-on-surface-variant[^>]*>.*?</p>)', sutra_html, re.DOTALL)

        if not (banners_match and translation_match and commentary_match):
            return sutra_html

        # Reconstruct: Sanskrit + Translation + Banners + Commentary + rest
        before_sanskrit = sutra_html[:sanskrit_match.start()]
        sanskrit = sanskrit_match.group(1)

        # Remove banners from their current position
        sutra_without_banners = sutra_html.replace(banners_match.group(0), '', 1)

        # Find translation and commentary in the modified HTML
        trans_start = sutra_without_banners.find(translation_match.group(1))
        trans_end = trans_start + len(translation_match.group(1))

        comm_start = sutra_without_banners.find(commentary_match.group(1))

        # Reconstruct with banners after translation
        result = (
            sutra_without_banners[:trans_end] + '\n' +
            banners_match.group(0) + '\n        ' +
            sutra_without_banners[trans_end:]
        )

        return result

    # Apply the fix to all sutras
    modified = re.sub(sutra_pattern, fix_sutra, content, flags=re.DOTALL)

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified)

    return True

def update_css(chapter_num):
    """Update banner CSS for better visibility and sizing."""
    html_file = Path(f"uttaradhyana-ch{chapter_num}.html")
    if not html_file.exists():
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and update banner CSS
    old_principle_css = r'\.principle-banner \{ display: flex; flex-direction: column; gap: 4px; margin-bottom: 1\.25rem; padding-bottom: 1rem; border-bottom: 1px solid rgba\(22,101,52,0\.12\); \}'
    new_principle_css = '.principle-banner { display: flex; flex-direction: column; gap: 8px; margin-bottom: 1.25rem; margin-top: 1rem; padding: 1rem; border-left: 3px solid #166534; background: rgba(22,101,52,0.05); }'

    old_caution_css = r'\.caution-banner \{ display: flex; flex-direction: column; gap: 4px; margin-bottom: 1\.25rem; padding-bottom: 1rem; border-bottom: 1px solid rgba\(30,64,175,0\.12\); \}'
    new_caution_css = '.caution-banner { display: flex; flex-direction: column; gap: 8px; margin-bottom: 1.25rem; margin-top: 1rem; padding: 1rem; border-left: 3px solid #1e40af; background: rgba(30,64,175,0.05); }'

    old_wv_css = r'\.wrong-view-banner \{ display: flex; flex-direction: column; gap: 4px; margin-bottom: 1\.25rem; padding-bottom: 1rem; border-bottom: 1px solid rgba\(186,26,26,0\.12\); \}'
    new_wv_css = '.wrong-view-banner { display: flex; flex-direction: column; gap: 8px; margin-bottom: 1.25rem; margin-top: 1rem; padding: 1rem; border-left: 3px solid #9b1515; background: rgba(186,26,26,0.05); }'

    # Update banner names and defs to match commentary size
    old_principle_name = r'\.principle-name \{ font-family: \'Noto Serif\', serif; font-size: 1\.05rem; font-weight: 600; color: #1d1c17; \}'
    new_principle_name = ".principle-name { font-family: 'Noto Serif', serif; font-size: 1.1rem; font-weight: 700; color: #166534; }"

    old_principle_def = r'\.principle-def \{ font-family: \'Inter\', sans-serif; font-size: 0\.92rem; color: #7e7665; line-height: 1\.5; font-style: italic; \}'
    new_principle_def = ".principle-def { font-family: 'Inter', sans-serif; font-size: 1rem; color: #4d4637; line-height: 1.6; }"

    old_caution_name = r'\.caution-name \{ font-family: \'Noto Serif\', serif; font-size: 1\.05rem; font-weight: 600; color: #1d1c17; \}'
    new_caution_name = ".caution-name { font-family: 'Noto Serif', serif; font-size: 1.1rem; font-weight: 700; color: #1e40af; }"

    old_caution_def = r'\.caution-def \{ font-family: \'Inter\', sans-serif; font-size: 0\.92rem; color: #7e7665; line-height: 1\.5; font-style: italic; \}'
    new_caution_def = ".caution-def { font-family: 'Inter', sans-serif; font-size: 1rem; color: #4d4637; line-height: 1.6; }"

    old_wv_name = r'\.wrong-view-name \{ font-family: \'Noto Serif\', serif; font-size: 1\.05rem; font-weight: 600; color: #1d1c17; \}'
    new_wv_name = ".wrong-view-name { font-family: 'Noto Serif', serif; font-size: 1.1rem; font-weight: 700; color: #9b1515; }"

    old_wv_def = r'\.wrong-view-def \{ font-family: \'Inter\', sans-serif; font-size: 0\.92rem; color: #7e7665; line-height: 1\.5; font-style: italic; \}'
    new_wv_def = ".wrong-view-def { font-family: 'Inter', sans-serif; font-size: 1rem; color: #4d4637; line-height: 1.6; }"

    # Badge styling - make more visible
    old_principle_badge = r'\.principle-badge \{ background: rgba\(22,101,52,0\.07\); border: 1px solid rgba\(22,101,52,0\.22\); color: #166534; font-family: \'Inter\', sans-serif; font-size: 10px; text-transform: uppercase; letter-spacing: 0\.18em; font-weight: 700; padding: 4px 14px; border-radius: 4px; \}'
    new_principle_badge = ".principle-badge { background: #166534; color: white; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; padding: 6px 12px; border-radius: 3px; }"

    old_caution_badge = r'\.caution-badge \{ background: rgba\(30,64,175,0\.07\); border: 1px solid rgba\(30,64,175,0\.22\); color: #1e40af; font-family: \'Inter\', sans-serif; font-size: 10px; text-transform: uppercase; letter-spacing: 0\.18em; font-weight: 700; padding: 4px 14px; border-radius: 4px; \}'
    new_caution_badge = ".caution-badge { background: #1e40af; color: white; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; padding: 6px 12px; border-radius: 3px; }"

    old_wv_badge = r'\.wrong-view-badge \{ background: rgba\(186,26,26,0\.07\); border: 1px solid rgba\(186,26,26,0\.22\); color: #9b1515; font-family: \'Inter\', sans-serif; font-size: 10px; text-transform: uppercase; letter-spacing: 0\.18em; font-weight: 700; padding: 4px 14px; border-radius: 4px; \}'
    new_wv_badge = ".wrong-view-badge { background: #9b1515; color: white; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; padding: 6px 12px; border-radius: 3px; }"

    # Apply all CSS updates
    content = re.sub(old_principle_css, new_principle_css, content)
    content = re.sub(old_caution_css, new_caution_css, content)
    content = re.sub(old_wv_css, new_wv_css, content)

    content = re.sub(old_principle_name, new_principle_name, content)
    content = re.sub(old_principle_def, new_principle_def, content)
    content = re.sub(old_caution_name, new_caution_name, content)
    content = re.sub(old_caution_def, new_caution_def, content)
    content = re.sub(old_wv_name, new_wv_name, content)
    content = re.sub(old_wv_def, new_wv_def, content)

    content = re.sub(old_principle_badge, new_principle_badge, content)
    content = re.sub(old_caution_badge, new_caution_badge, content)
    content = re.sub(old_wv_badge, new_wv_badge, content)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

# Process all chapters
chapters_to_process = list(range(1, 37))
chapters_to_process.remove(32)  # Skip chapter 32

for ch in chapters_to_process:
    print(f"Processing chapter {ch}...", end=" ")
    if update_css(ch):
        print("CSS ✓", end=" ")
    if reposition_banners_in_chapter(ch):
        print("Repositioned ✓")
    else:
        print("repositioned ✗")

print("\n✓ All chapters updated!")
