
import re

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by ## SUTRA or ## SUTRAS
    sections = re.split(r'^(## SUTRAS?\s+.*)$', content, flags=re.MULTILINE)
    
    cards = []
    for i in range(1, len(sections), 2):
        header = sections[i]
        body = sections[i+1]
        cards.append((header, body))
    
    return cards

def format_card(header, body, index):
    # Extract sutra number from header: "## SUTRA 36.1" -> "36.1"
    # match = re.search(r'36\.[0-9–\-]+', header)
    # sutra_num = match.group(0) if match else f"36.{index}"
    sutra_num = header.replace('## SUTRAS', '').replace('## SUTRA', '').split(':')[0].strip()
    
    # Extract sections
    prakrit = re.search(r'### 1\. PRAKRIT TEXT\s*(.*?)\s*(?=###|$)', body, re.S)
    prakrit = prakrit.group(1).strip() if prakrit else ""
    
    translation = re.search(r'### 3\. LITERAL ENGLISH TRANSLATION\s*(.*?)\s*(?=###|$)', body, re.S)
    translation = translation.group(1).strip() if translation else ""
    
    commentary = re.search(r'### 5\. COMMENTARY\s*(.*?)\s*(?=###|$)', body, re.S)
    commentary = commentary.group(1).strip() if commentary else ""
    
    simple = re.search(r'### 6\. SIMPLY PUT\s*(.*?)\s*(?=###|$)', body, re.S)
    simple = simple.group(1).strip() if simple else ""
    
    # If standard sections are missing, just use the whole body
    if not translation and not commentary:
        # Clean up body a bit
        content = body.strip()
        # Convert markdown headers in body to something nicer
        content = re.sub(r'### (.*?)\n', r'<b>\1</b><br/>', content)
        content = content.replace('\n\n', '</p><p class="text-base text-on-surface-variant leading-relaxed">')
        content = content.replace('\n', '<br/>')
        
        return f"""
  <article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{index}">
    <div class="flex items-start gap-6">
      <span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{sutra_num}</span>
      <div class="space-y-4 flex-1">
        <p class="text-base text-on-surface-variant leading-relaxed">{content}</p>
      </div>
    </div>
  </article>
"""

    # Clean up prakrit - might have multiple lines
    prakrit = prakrit.replace('\n', '<br/>')
    
    # Convert markdown links/bold in commentary
    commentary = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', commentary)
    commentary = re.sub(r' - ', r' &mdash; ', commentary)
    commentary = commentary.replace('\n\n', '</p><p class="text-base text-on-surface-variant leading-relaxed">')
    commentary = commentary.replace('\n', ' ')

    simple = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', simple)
    
    html = f"""
  <article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{index}">
    <div class="flex items-start gap-6">
      <span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{sutra_num}</span>
      <div class="space-y-4 flex-1">
        <p class="sutra-sanskrit font-headline">{prakrit}</p>
        <p class="text-lg font-semibold text-on-surface leading-relaxed">{translation}</p>
        <p class="text-base text-on-surface-variant leading-relaxed">{commentary}</p>
        <p class="simple-explanation"><b>The simple version:</b> {simple}</p>
      </div>
    </div>
  </article>
"""
    return html

file_path = '/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana/translations/uttaradhyana-ch36-translation.md'
cards = parse_markdown(file_path)

print(f"Total cards: {len(cards)}")

card_htmls = []
for i, (header, body) in enumerate(cards):
    card_htmls.append(format_card(header, body, i+1))

with open('cards.html', 'w') as f:
    f.write("\n".join(card_htmls))
