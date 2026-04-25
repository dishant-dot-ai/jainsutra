#!/usr/bin/env python3
"""
Auto-map and insert banners for remaining chapters 3-36.
Uses keyword analysis + manual templates for efficiency.
"""

import re
import json
from pathlib import Path

# Template mappings for key concepts
KEYWORD_BANNERS = {
    # Green (Principle) keywords
    'principle_keywords': [
        ('tapa', 'Tapa · Austerity', 'Deliberate practice that weakens karma and strengthens the soul.'),
        ('kshama', 'Kshama · Forbearance', 'Patient endurance of hardship develops inner strength and freedom.'),
        ('vairagya', 'Vairāgya · Non-Attachment', 'Detachment from worldly desires allows the soul to perceive its true nature.'),
        ('brahmacharya', 'Brahmacharya · Celibacy', 'Mastery over sexual desire liberates immense spiritual energy.'),
        ('non-violence', 'Ahimsa · Non-Violence', 'Harmlessness toward all beings is the foundation of all virtues.'),
        ('renunciation', 'Tyaga · Renunciation', 'Voluntarily releasing worldly attachments leads to spiritual freedom.'),
        ('equanimity', 'Samata · Equanimity', 'Equal-mindedness in pleasure and pain reveals the soul\'s true nature.'),
        ('discipline', 'Vinaya · Discipline', 'Self-imposed order of thought, word, and deed transforms the soul.'),
        ('meditation', 'Dhyana · Meditation', 'Inward focus purifies the mind and awakens inner wisdom.'),
        ('wisdom', 'Prajna · Wisdom', 'Direct insight into reality transcends mere intellectual knowledge.'),
        ('liberation', 'Moksha · Liberation', 'Freedom from karma and rebirth is the soul\'s eternal home.'),
        ('detachment', 'Vairāgya · Detachment', 'Release from desire is the gateway to spiritual awakening.'),
    ],
    # Blue (Caution) keywords
    'caution_keywords': [
        ('death', 'Impermanence and Death', 'All worldly things are temporary—clinging to them brings suffering.'),
        ('suffering', 'Dukha · Suffering', 'Suffering arises from identifying with the perishable body and desires.'),
        ('ignorance', 'Avijja · Ignorance', 'Lack of spiritual vision perpetuates the cycle of rebirth.'),
        ('delusion', 'Moha · Delusion', 'False perception of reality keeps the soul bound in karma.'),
        ('greed', 'Lobha · Greed', 'Craving for possessions generates binding karma without ceasing.'),
        ('anger', 'Krodha · Anger', 'Anger destroys equanimity and generates the most intense karma.'),
        ('pride', 'Mana · Pride', 'Arrogance blocks the humility needed for genuine learning.'),
        ('attachment', 'Sanga · Attachment', 'Emotional bonds to people and things perpetuate suffering.'),
        ('negligence', 'Pamada · Negligence', 'Indifference to spiritual practice wastes the precious human birth.'),
        ('worldly', 'Samsara · Worldly Existence', 'Involvement in worldly activities generates binding karma.'),
    ]
}

def extract_chapter_sutras(chapter_num):
    """Extract sutra translations from chapter HTML."""
    html_file = Path(f"uttaradhyana-ch{chapter_num}.html")
    if not html_file.exists():
        return None

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    sutra_pattern = r'<article[^>]*id="sutra-(?:\d+-)?(\d+)"[^>]*>(.*?)</article>'
    matches = list(re.finditer(sutra_pattern, html_content, re.DOTALL))

    sutras = []
    for match in matches:
        sutra_num = match.group(1)
        sutra_content = match.group(2)

        trans_match = re.search(r'<p class="text-lg font-semibold[^>]*>(.*?)</p>', sutra_content, re.DOTALL)
        translation = trans_match.group(1) if trans_match else ""
        translation_text = re.sub(r'<[^>]+>', '', translation).strip().lower()

        comment_match = re.search(r'<p class="text-base text-on-surface-variant[^>]*>(.*?)</p>', sutra_content, re.DOTALL)
        commentary = comment_match.group(1) if comment_match else ""
        commentary_text = re.sub(r'<[^>]+>', '', commentary).strip().lower()

        combined = (translation_text + " " + commentary_text[:200]).lower()

        sutras.append({
            'num': sutra_num,
            'combined': combined
        })

    return sutras

def suggest_banners(sutra_text):
    """Suggest appropriate banners for a sutra based on content."""
    banners = []

    # Check principle keywords
    for keyword, name, definition in KEYWORD_BANNERS['principle_keywords']:
        if keyword in sutra_text:
            banners.append({'type': 'principle', 'name': name, 'def': definition})
            break

    # Check caution keywords (can have multiple)
    for keyword, name, definition in KEYWORD_BANNERS['caution_keywords']:
        if keyword in sutra_text:
            banners.append({'type': 'caution', 'name': name, 'def': definition})
            break

    return banners

def create_chapter_mapping(chapter_num):
    """Create banner mapping for a chapter."""
    sutras = extract_chapter_sutras(chapter_num)
    if not sutras:
        return None

    mapping = {
        'chapter': chapter_num,
        'sutras': {}
    }

    for sutra in sutras:
        banners = suggest_banners(sutra['combined'])
        if banners:
            mapping['sutras'][sutra['num']] = {'banners': banners}
        else:
            mapping['sutras'][sutra['num']] = {'banners': []}

    return mapping

def save_mapping(chapter_num, mapping):
    """Save mapping to JSON."""
    filename = f"ch{chapter_num}_banners.json"
    with open(filename, 'w') as f:
        json.dump(mapping, f, indent=2)
    return filename

# Generate mappings for chapters 3-36
for ch in range(3, 37):
    if ch == 32:  # Skip if missing
        continue

    print(f"Processing chapter {ch}...", end=" ")
    mapping = create_chapter_mapping(ch)
    if mapping:
        save_mapping(ch, mapping)
        sutra_count = len(mapping['sutras'])
        print(f"✓ ({sutra_count} sutras mapped)")
    else:
        print("✗ Not found")

print("\n✓ Auto-mapping complete for chapters 3-36")
