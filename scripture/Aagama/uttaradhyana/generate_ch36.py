import re
import os

def generate_html():
    template_path = '/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana/uttaradhyana-ch10.html'
    translation_path = '/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana/translations/uttaradhyana-ch36-translation.md'
    output_path = '/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana/uttaradhyana-ch36.html'

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    with open(translation_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract sections from template
    # Title
    template_content = template_content.replace('Uttaradhyayana Sutra Chapter 10: Fallen Leaf', 'Uttaradhyayana Sutra Chapter 36: Jīvājīva Vibhakti')
    
    # Hero Section replacement
    hero_pattern = re.compile(r'<section class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-8 md:gap-16 items-center mb-40">.*?</section>', re.DOTALL)
    new_hero = """
<section class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-8 md:gap-16 items-center mb-40">
  <div class="col-span-12 lg:col-span-5 flex flex-col gap-10 order-2 lg:order-1">
    <div class="flex flex-col gap-3">
      <span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Uttaradhyayana Sutra · Chapter 36</span>
      <h1 class="text-5xl md:text-8xl font-headline font-bold text-on-surface leading-tight tracking-tighter">
        Jīvājīva Vibhakti<span class="block text-primary font-normal">जीवाजीविभक्ति</span>
      </h1>
    </div>
    <h2 class="text-3xl md:text-5xl font-headline text-on-surface-variant leading-tight font-light">The Classification of Living and Non-Living Substances</h2>
    <p class="text-xl text-on-surface-variant leading-relaxed opacity-90 max-w-lg font-light">
      Lord Mahavira presents the systematic classification of jīva (living) and ajīva (non-living). This final chapter of the Uttaradhyayana Sutra provides the definitive ontological map of the Jain universe, essential for right knowledge and liberation.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
      <div><p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-1">Imparted By</p><p class="text-base font-headline font-bold text-on-surface">Lord Mahavira</p></div>
      <div><p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-1">Compiled By</p><p class="text-base font-headline font-bold text-on-surface">Twelve Chief Disciples</p></div>
      <div><p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-1">Translated By</p><p class="text-base font-headline font-bold text-on-surface">Dishant Shah</p></div>
    </div>
  </div>
  <div class="col-span-12 lg:col-span-7 order-1 lg:order-2 flex flex-col items-center justify-center gap-0">
    <div class="w-full max-w-2xl aspect-[4/3] rounded-xl overflow-hidden">
      <img src="../../../assets/ch9-hero.jpg" alt="Lord Mahavira teaching" class="w-full h-full object-cover grayscale-[0.1] hover:grayscale-0 transition-all duration-1000"/>
    </div>
    <div class="mt-8 text-center">
      <p class="font-headline text-2xl md:text-3xl text-primary leading-relaxed">जीवाजीविभभत्ति, सुणेह मे एगमणा इओ।<br/>जं जाणिऊण भિક્ખू, सम्मं जयइ संजमे ॥३६.१॥</p>
      <p class="text-base text-on-surface-variant mt-3 font-light italic">&ldquo;Listen to the classification of living and non-living from me with a focused mind — knowing which, a monk strives correctly in restraint.&rdquo;</p>
    </div>
  </div>
</section>
"""
    template_content = hero_pattern.sub(new_hero, template_content)

    # Intro Section replacement
    intro_pattern = re.compile(r'<!-- Chapter Introduction -->.*?<section class="bg-\[#f2f1f0\].*?</section>', re.DOTALL)
    new_intro = """
<!-- Chapter Introduction -->
<section class="bg-[#f2f1f0] py-24 border-y border-primary/5">
  <div class="max-w-screen-xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-12 md:gap-20">
    <div class="col-span-12 lg:col-span-4">
      <span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">About This Chapter</span>
      <h3 class="text-4xl font-headline font-bold text-on-surface leading-tight tracking-tight mt-4">Jīvājīva Vibhakti</h3>
    </div>
    <div class="col-span-12 lg:col-span-8 space-y-6">
      <p class="text-lg leading-relaxed text-on-surface-variant">
        Chapter 36 is the <span class="text-primary font-semibold">Jīvājīva Vibhakti</span> — the systematic classification of jīva (living substance) and ajīva (non-living substance). It is the most philosophically detailed chapter in the Uttaradhyayana, presenting the Jain ontological map of reality: the six fundamental substances, their divisions, and their characteristics.
      </p>
      <p class="text-lg leading-relaxed text-on-surface-variant">
        The entire universe is analysed into its constituents through four analytical lenses: substance (dravya), region (kṣetra), time (kāla), and mode (bhāva). This knowledge is the foundation of samyag-jñāna — right knowledge — essential for the soul to distinguish itself from matter and move toward liberation.
      </p>
      <div class="flex gap-8 items-center pt-4">
        <div class="flex flex-col gap-1">
          <span class="text-3xl font-headline font-bold text-primary">220</span>
          <span class="text-xs uppercase tracking-widest text-on-surface-variant font-semibold">Sutras</span>
        </div>
        <div class="w-px h-12 bg-outline-variant"></div>
        <div class="flex flex-col gap-1">
          <span class="text-3xl font-headline font-bold text-primary">Universe</span>
          <span class="text-xs uppercase tracking-widest text-on-surface-variant font-semibold">Mapped</span>
        </div>
        <div class="w-px h-12 bg-outline-variant"></div>
        <div class="flex flex-col gap-1">
          <span class="text-3xl font-headline font-bold text-primary">Final</span>
          <span class="text-xs uppercase tracking-widest text-on-surface-variant font-semibold">Chapter</span>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    template_content = intro_pattern.sub(new_intro, template_content)

    # Sutra Counter title
    template_content = template_content.replace('Adhyayana 10', 'Adhyayana 36')
    template_content = template_content.replace('The 37 Sutras', 'The 220 Sutras')
    template_content = template_content.replace('Each sutra is presented with the original Prakrit, English translation, and a simplified commentary.', 'The final chapter presents an exhaustive classification of all living and non-living substances in the universe.')

    # Navigation
    template_content = template_content.replace('href="uttaradhyana-ch9.html"', 'href="#"')
    template_content = template_content.replace('Chapter 9', 'Chapter 35')
    template_content = template_content.replace('href="uttaradhyana-ch11.html"', 'href="uttaradhyana-index.html"')
    template_content = template_content.replace('Chapter 11', 'Index')
    
    # Footer end marker
    template_content = template_content.replace('॥ अध्ययन-१० सम्पूर्ण ॥', '॥ अध्ययन-३६ सम्पूर्ण ॥')
    template_content = template_content.replace('End of Chapter 10 — The Fallen Leaf', 'End of Chapter 36 — Classification of Living and Non-Living')

    # Parse MD for sutras
    sutras_html = []
    
    # Split MD by ## SUTRA or ## SUTRAS or CHART:
    # Use lookahead to not consume the header
    sections = re.split(r'##\s+(?=SUTRA[S]?|CHART:)', md_content)
    
    current_part = 0
    
    for section in sections:
        section = section.strip()
        if not section: continue
        
        if section.startswith('CHART:'):
            lines = section.split('\n', 1)
            header = lines[0].strip()
            body = lines[1].strip() if len(lines) > 1 else ""
            chart_title = header.replace('CHART:', '').split('—', 1)[0].strip()
            # Clean up the chart text
            chart_content = body.strip()
            # Wrap chart in a styled block
            html = f'<div class="bg-surface-container-low p-8 rounded-xl mb-12 border border-primary/10 font-mono text-sm overflow-x-auto"><h4 class="text-primary font-headline font-bold mb-4">{chart_title}</h4><pre>{chart_content}</pre></div>'
            sutras_html.append(html)
            continue

        if section.startswith('SUTRA'):
            lines = section.split('\n', 1)
            header = lines[0].strip()
            body = lines[1].strip() if len(lines) > 1 else ""
            
            sutra_id_match = re.search(r'[\d\.\–\-]+', header)
            if not sutra_id_match: continue
            sutra_id = sutra_id_match.group(0)
            
            # Determine Part
            if "AJĪVA" in body and current_part == 0:
                sutras_html.append('<div class="section-divider" id="section-ajiva"><span>Part I &mdash; The Non-Living (Ajīva)</span></div>')
                current_part = 1
            elif "JĪVA" in body and current_part == 1:
                sutras_html.append('<div class="section-divider" id="section-jiva"><span>Part II &mdash; The Living (Jīva)</span></div>')
                current_part = 2

            # Extract components using a more robust method
            comp_sections = re.split(r'###\s+\d+\.\s+', body)
            
            prakrit = ""
            translation = ""
            commentary = ""
            simple = ""
            contemplate = ""
            
            # Map sub-headers to components
            # We'll use keyword matching since numbers might vary or be skipped
            for cs in comp_sections:
                cs = cs.strip()
                if not cs: continue
                if "PRAKRIT TEXT" in cs:
                    prakrit = cs.replace("PRAKRIT TEXT", "").strip().replace('\n', '<br/>')
                elif "LITERAL ENGLISH TRANSLATION" in cs:
                    translation = cs.replace("LITERAL ENGLISH TRANSLATION", "").strip()
                elif "COMMENTARY" in cs:
                    commentary = cs.replace("COMMENTARY", "").strip()
                elif "SIMPLY PUT" in cs:
                    simple = cs.replace("SIMPLY PUT", "").strip()
                elif "CONTEMPLATE" in cs:
                    contemplate = cs.replace("CONTEMPLATE", "").strip()
                # Handle cases where heading is different
                elif not translation and any(kw in cs for kw in ["Translation", "translation"]):
                     translation = cs
                elif not commentary and any(kw in cs for kw in ["Commentary", "commentary"]):
                     commentary = cs

            # Handle ranges like 174-193 which might just be a block of text
            if not prakrit and not translation and not commentary and body:
                commentary = body.strip()

            # Build card
            card_html = f"""
  <article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{sutra_id.replace('.', '-').replace('–', '-')}">
    <div class="flex items-start gap-6">
      <span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{sutra_id}</span>
      <div class="space-y-4 flex-1">
        {f'<p class="sutra-sanskrit font-headline">{prakrit}</p>' if prakrit else ''}
        {f'<p class="text-lg font-semibold text-on-surface leading-relaxed">{translation}</p>' if translation else ''}
        {f'<p class="text-base text-on-surface-variant leading-relaxed">{commentary}</p>' if commentary else ''}
        {f'<p class="simple-explanation"><b>The simple version:</b> {simple}</p>' if simple else ''}
        {f'<p class="mt-4 text-sm italic text-on-surface-variant/70 border-l-2 border-primary/20 pl-4">Contemplate: {contemplate}</p>' if contemplate else ''}
      </div>
    </div>
  </article>
"""
            sutras_html.append(card_html)

    all_sutras_html = "\n".join(sutras_html)
    
    # Find start of sutra section
    start_tag = '<!-- PART I -->'
    end_tag = '<div class="text-center py-16">'
    
    parts = template_content.split(start_tag)
    if len(parts) > 1:
        rest = parts[1].split(end_tag)
        if len(rest) > 1:
            final_content = parts[0] + start_tag + "\n" + all_sutras_html + "\n" + end_tag + rest[1]
        else:
            final_content = template_content # Fallback
    else:
        final_content = template_content # Fallback

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_html()
