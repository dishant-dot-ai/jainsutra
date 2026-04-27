import re
import os

source_file = "/Users/thefounder/Projects/active/JainAwaken/scripture/aagama/uttaradhyana/translations/uttaradhyana-ch36-translation.md"
output_file = "/Users/thefounder/Projects/active/JainAwaken/scripture/aagama/uttaradhyana/uttaradhyana-ch36.html"

# Read the translation file
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split into sutra blocks
# Groups like "## SUTRAS 36.71–72" or "## SUTRA 36.1"
blocks = re.split(r'\n## SUTRA[S]? ', content)

sutras_data = []

# Skip the intro part of the md
for block in blocks[1:]:
    # Extract the numbers
    num_match = re.match(r'(\d+\.\d+(?:[–-]\d+)?)', block)
    if not num_match:
        continue
    
    num_range = num_match.group(1)
    
    # Extract Prakrit (usually starts with > )
    prakrit_match = re.findall(r'>\s*(.*?)\s*(?:॥\d+\.\d+॥|॥\s*–\s*ति बेमि\s*॥\d+\.\d+॥)', block)
    prakrit = "<br/>".join(prakrit_match) if prakrit_match else ""
    
    # Extract Translation
    trans_match = re.search(r'\*\*Literal Translation:\*\*\s*(.*?)\n', block, re.DOTALL)
    translation = trans_match.group(1).strip() if trans_match else ""
    
    # Extract Commentary
    comm_match = re.search(r'\*\*In-depth Commentary:\*\*\s*(.*?)\n\n', block, re.DOTALL)
    commentary = comm_match.group(1).strip() if comm_match else ""
    
    # Extract Simple Version
    simple_match = re.search(r'\*\*The Simple Version:\*\*\s*(.*?)\n', block, re.DOTALL)
    simple = simple_match.group(1).strip() if simple_match else ""
    
    # Extract Tags
    tags_match = re.search(r'\*\*Thematic Tags:\*\*\s*(.*?)\n', block)
    tags = [t.strip() for t in tags_match.group(1).split(',')] if tags_match else []

    # Handle grouping expansion (if 36.20-21, keep combined as requested, but others split)
    if '–' in num_range or '-' in num_range:
        if num_range == "36.20–21" or num_range == "36.20-21":
            sutras_data.append({
                "id": "36.20–21",
                "prakrit": prakrit,
                "translation": translation,
                "commentary": commentary,
                "simple": simple,
                "tags": tags
            })
        else:
            # Split the range and duplicate data for each (since MD grouped them)
            # This ensures every number has a card as requested.
            start, end = map(int, re.findall(r'\d+', num_range)[1:])
            for i in range(start, end + 1):
                sutras_data.append({
                    "id": f"36.{i}",
                    "prakrit": prakrit,
                    "translation": translation,
                    "commentary": commentary,
                    "simple": simple,
                    "tags": tags
                })
    else:
        sutras_data.append({
            "id": num_range,
            "prakrit": prakrit,
            "translation": translation,
            "commentary": commentary,
            "simple": simple,
            "tags": tags
        })

# HTML Generation
html_template = """<!DOCTYPE html>
<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Uttaradhyayana Sutra Chapter 36: Classification of Living and Non-Living | JainSutra.org</title>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "on-tertiary-fixed-variant": "#35437e","on-secondary-fixed-variant": "#4a4642","secondary-container": "#e6ded9","primary-fixed-dim": "#e6c364","surface-bright": "#fef9f1","tertiary-fixed": "#dde1ff","surface": "#fef9f1","primary-fixed": "#ffe08f","surface-container-low": "#f8f3eb","secondary-fixed": "#e9e1dc","outline-variant": "#d0c5b2","outline": "#7e7665","inverse-on-surface": "#f5f0e8","on-background": "#1d1c17","on-secondary": "#ffffff","on-tertiary-container": "#2e3b77","error": "#ba1a1a","on-error": "#ffffff","on-primary-fixed-variant": "#584400","surface-dim": "#ded9d2","surface-container-high": "#ece8e0","primary": "#755b00","on-primary-container": "#503d00","inverse-surface": "#32302b","secondary": "#625d59","error-container": "#ffdad6","tertiary-fixed-dim": "#b9c3ff","on-secondary-container": "#67625e","on-primary": "#ffffff","on-primary-fixed": "#241a00","on-error-container": "#93000a","surface-tint": "#755b00","secondary-fixed-dim": "#ccc5c0","surface-variant": "#e7e2da","surface-container-lowest": "#ffffff","on-tertiary-fixed": "#041451","surface-container-highest": "#e7e2da","primary-container": "#c9a84c","inverse-primary": "#e6c364","on-surface-variant": "#4d4637","tertiary": "#4d5a98","background": "#fef9f1","on-tertiary": "#ffffff","on-surface": "#1d1c17","tertiary-container": "#9ba8eb","surface-container": "#f2ede5","on-secondary-fixed": "#1e1b18"
      },
      fontFamily: { "headline": ["Noto Serif", "serif"], "body": ["Inter", "sans-serif"], "label": ["Inter", "sans-serif"] },
      borderRadius: { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" },
    },
  },
}
</script>
<style>
html { scroll-behavior: smooth; }
.burnished-gradient { background: radial-gradient(circle at center, #755b00, #c9a84c); }
.sutra-card { border: 1px solid rgba(201,168,76,0.25); border-left: 3px solid #c9a84c; background: white; }
.sutra-sanskrit { font-size: 1.35rem; line-height: 2; color: #503d00; }
.simple-explanation { margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed rgba(201,168,76,0.3); font-family: 'Inter', sans-serif; font-size: 1rem; line-height: 1.7; color: #4d4637; }
.simple-explanation b { color: #755b00; font-weight: 600; }
.concept-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 1rem; }
.concept-tag { display: inline-block; border: 1px solid #C9A84C; background: transparent; color: #1d1c17; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 100px; padding: 4px 13px; font-weight: 500; }
.nav-button { position: fixed; bottom: 24px; z-index: 100; background: transparent; border: 1px solid rgba(201,168,76,0.35); color: rgba(201,168,76,0.6); transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; transform: translateY(20px); }
.nav-button.visible { opacity: 1; pointer-events: auto; transform: translateY(0); }
.nav-button:hover { border-color: #C9A84C; color: #C9A84C; }
.glass-nav { background: rgba(248, 247, 246, 0.85); backdrop-filter: blur(20px); }
.section-divider { margin: 2rem 0 1.5rem; display: flex; align-items: center; gap: 1rem; }
.section-divider span { font-family: 'Noto Serif', serif; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.2em; color: #755b00; font-weight: 600; white-space: nowrap; }
.section-divider::before, .section-divider::after { content: ''; flex: 1; height: 1px; background: rgba(201,168,76,0.3); }
@media (max-width: 768px) { .nav-button { bottom: 16px; } .nav-button.left-btn { left: 12px !important; } .nav-button.right-btn { right: 12px !important; } .sutra-sanskrit { font-size: 1.15rem; } }
.graphic-detail { background: #fdfaf5; border: 1px solid #e6c364; border-radius: 8px; padding: 1.5rem; margin: 2rem 0; font-size: 0.95rem; line-height: 1.6; }
.graphic-detail h4 { color: #755b00; font-weight: 700; margin-bottom: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid #e6c364; padding-bottom: 0.5rem; }
.graphic-detail ul { list-style-type: none; padding-left: 0; }
.graphic-detail li { margin-bottom: 0.5rem; padding-left: 1.25rem; position: relative; }
.graphic-detail li::before { content: '•'; color: #c9a84c; position: absolute; left: 0; font-weight: bold; }
.graphic-detail table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
.graphic-detail th, .graphic-detail td { border: 1px solid #e6c364; padding: 8px; text-align: left; }
.graphic-detail th { background: rgba(201,168,76,0.1); color: #755b00; font-weight: 600; }
</style>
</head>
<body class="text-on-surface font-body selection:bg-primary-container selection:text-on-primary-container bg-white">

<nav id="main-nav" class="glass-nav fixed top-0 w-full z-50 transition-all duration-500 border-b border-[#C9A84C]/10">
  <div class="flex justify-between items-center px-6 md:px-12 py-5 max-w-screen-2xl mx-auto">
    <div class="flex items-center gap-12">
      <a href="../../../index-v4.html#hero"><span class="text-2xl font-headline text-primary tracking-tighter font-bold">JainSutra.org</span></a>
      <div class="hidden md:flex gap-10 items-center font-headline tracking-[0.1em] uppercase text-xs font-semibold">
        <a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../index-v4.html#foundations">Fundamentals</a>
        <a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../fundamentals/navkar-mantra-v4.html">Navkar</a>
        <a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../fundamentals/meditations.html">Meditations</a>
        <a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../sacred-sutras-index.html">Sacred Sutras</a>
      </div>
    </div>
    <div class="flex items-center gap-8">
      <a href="../../../fundamentals/donate-v4.html" class="burnished-gradient text-on-primary px-8 py-2.5 rounded-full font-headline uppercase text-[10px] font-bold tracking-[0.2em] hover:opacity-90 transition-all shadow-sm">Donate</a>
    </div>
  </div>
</nav>

<main class="pt-40">

<section class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-8 md:gap-16 items-center mb-40">
  <div class="col-span-12 lg:col-span-5 flex flex-col gap-10 order-2 lg:order-1">
    <div class="flex flex-col gap-3">
      <span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Uttaradhyayana Sutra · Chapter 36</span>
      <h1 class="text-5xl md:text-8xl font-headline font-bold text-on-surface leading-tight tracking-tighter">
        The Living & Non-Living<span class="block text-primary font-normal">जीवाजीविभभत्ति</span>
      </h1>
    </div>
    <h2 class="text-3xl md:text-5xl font-headline text-on-surface-variant leading-tight font-light">A definitive map of reality: souls, matter, and the structure of the cosmos.</h2>
    <p class="text-xl text-on-surface-variant leading-relaxed opacity-90 max-w-lg font-light">
      Chapter 36 is the scientific pinnacle of the scripture — a systematic map of every constituent of existence. It provides the essential clarity required to distinguish the living soul from non-living substance.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
      <div><p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-1">Imparted By</p><p class="text-base font-headline font-bold text-on-surface">Lord Mahavira</p></div>
      <div><p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-1">Compiled By</p><p class="text-base font-headline font-bold text-on-surface">Twelve Chief Disciples</p></div>
      <div><p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-1">Translated By</p><p class="text-base font-headline font-bold text-on-surface">Dishant Shah</p></div>
    </div>
  </div>
  <div class="col-span-12 lg:col-span-7 order-1 lg:order-2 flex flex-col items-center justify-center gap-0">
    <div class="w-full max-w-2xl aspect-[4/3] rounded-xl overflow-hidden">
      <img src="../../../assets/ch9-hero.jpg" alt="Classification of Living and Non-Living" class="w-full h-full object-cover grayscale-[0.1] hover:grayscale-0 transition-all duration-1000"/>
    </div>
    <div class="mt-8 text-center">
      <p class="font-headline text-2xl md:text-3xl text-primary leading-relaxed">जीवा चेव अजीवा य, एस लोए वियाहिए</p>
      <p class="text-base text-on-surface-variant mt-3 font-light italic">&ldquo;This universe is composed of living souls and non-living substances. Knowing the distinction is the foundation of truth.&rdquo;</p>
    </div>
  </div>
</section>

<!-- Chapter Introduction -->
<section class="bg-[#f2f1f0] py-24 border-y border-primary/5">
  <div class="max-w-screen-xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-12 md:gap-20">
    <div class="col-span-12 lg:col-span-4">
      <span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">About This Chapter</span>
      <h3 class="text-4xl font-headline font-bold text-on-surface leading-tight tracking-tight mt-4">Jīvājīva Vibhakti: Classification of Reality</h3>
    </div>
    <div class="col-span-12 lg:col-span-8 flex flex-col gap-8">
      <div class="flex flex-col gap-6">
        <p class="text-xl text-on-surface-variant leading-relaxed font-light">
          Chapter 36, the final and most extensive chapter, serves as the scientific pinnacle of the Uttaradhyayana Sutra. It provides a systematic map of every constituent of existence, offering the essential clarity required to distinguish the living soul from the non-living substance.
        </p>
        <p class="text-xl text-on-surface-variant leading-relaxed font-light">
          It traverses every substance, every being, and every realm, analyzing them through the fourfold lens of substance, space, time, and mode. This knowledge is the foundation of Samyag-jñāna (Right Knowledge), making liberation a real and directed possibility.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 pt-8 border-t border-primary/10">
        <div><p class="text-xs uppercase tracking-[0.2em] text-primary font-semibold mb-2">Number of Sutras</p><p class="text-3xl font-headline font-bold text-on-surface">274</p></div>
        <div><p class="text-xs uppercase tracking-[0.2em] text-primary font-semibold mb-2">Addressed To</p><p class="text-3xl font-headline font-bold text-on-surface">All Seekers</p></div>
        <div><p class="text-xs uppercase tracking-[0.2em] text-primary font-semibold mb-2">Sections</p><p class="text-3xl font-headline font-bold text-on-surface">6</p></div>
      </div>
      <div class="flex flex-col gap-4 mt-4">
        <p class="text-xs uppercase tracking-[0.2em] text-primary font-semibold">Chapter Structure</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-4">
          <div class="flex gap-4 items-center"><span class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">I</span><p class="text-sm font-medium">The Foundation of Reality (1–3)</p></div>
          <div class="flex gap-4 items-center"><span class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">II</span><p class="text-sm font-medium">Non-Living Substances (4–10)</p></div>
          <div class="flex gap-4 items-center"><span class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">III</span><p class="text-sm font-medium">The Matrix of Matter (11–47)</p></div>
          <div class="flex gap-4 items-center"><span class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">IV</span><p class="text-sm font-medium">The Perfected and the Bound (48–68)</p></div>
          <div class="flex gap-4 items-center"><span class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">V</span><p class="text-sm font-medium">The Hierarchy of Life (69–220)</p></div>
          <div class="flex gap-4 items-center"><span class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">VI</span><p class="text-sm font-medium">Lifespans & Conclusion (221–274)</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-32" id="sutras">
  <div class="mb-20">
    <span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Adhyayana 36</span>
    <h3 class="text-4xl md:text-6xl font-headline font-bold text-on-surface mt-4">The 274 Sutras</h3>
    <p class="text-lg text-on-surface-variant mt-6 max-w-2xl font-light">The complete map of existence, from the smallest particle of matter to the highest state of the soul.</p>
  </div>
"""

# Helper to generate a card
def make_card(data):
    tags_html = "".join([f'<span class="concept-tag">{t}</span>' for t in data["tags"]])
    return f'''
  <article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{data["id"].replace(".", "-").replace("–", "-")}">
    <div class="flex items-start gap-6">
      <span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{data["id"]}</span>
      <div class="space-y-4 flex-1">
        <p class="sutra-sanskrit font-headline">{data["prakrit"]}</p>
        <p class="text-lg font-semibold text-on-surface leading-relaxed">{data["translation"]}</p>
        <p class="text-base text-on-surface-variant leading-relaxed">{data["commentary"]}</p>
        <p class="simple-explanation"><b>The simple version:</b> {data["simple"]}</p>
        <div class="concept-tags">{tags_html}</div>
      </div>
    </div>
  </article>
'''

html_content = html_template

# Sections dividers
sections = {
    1: "Part I — The Foundation of Reality",
    4: "Part II — Non-Living Substances",
    11: "Part III — The Matrix of Matter",
    48: "Part IV — The Perfected and the Bound",
    69: "Part V — The Hierarchy of Life",
    221: "Part VI — Lifespans and Conclusion"
}

# Add graphic details at specific points
graphics = {
    11: """
  <div class="graphic-detail">
    <h4>Classification: The 14 Types of Non-Living Substance</h4>
    <p>The universe is structured through a precise hierarchy of fourteen non-living constituents:</p>
    <ul>
        <li><strong>The Formless (Arūpī) — 10 categories:</strong> Medium of Motion (3), Medium of Rest (3), Space (3), Time (1).</li>
        <li><strong>Those with Form (Rūpī) — 4 categories:</strong> Aggregate, Portion, Point-unit, and Particle.</li>
    </ul>
  </div>""",
    48: """
  <div class="graphic-detail">
    <h4>The Matrix: 530 Sub-types of Material Substance</h4>
    <p>By analyzing how each primary quality (Color, Smell, Taste, Touch, Shape) combines with the others, we arrive at 530 variations mapping the incredible diversity of the physical universe.</p>
  </div>""",
    56: """
  <div class="graphic-detail">
    <h4>The Summit: The Abode of the Liberated (Siddha-Shila)</h4>
    <ul>
        <li><strong>Position:</strong> Absolute ceiling of the universe.</li>
        <li><strong>Shape:</strong> Crescent / Inverted Umbrella.</li>
        <li><strong>Nature:</strong> Pure, luminous, and blissful.</li>
    </ul>
  </div>""",
    158: """
  <div class="graphic-detail">
    <h4>The Depths: Seven Levels of the Infernal Realms</h4>
    <p>Descending from Ratna-prabhā to Mahātamaḥ-prabhā, organizing suffering into seven intense geological layers.</p>
  </div>""",
    176: """
  <div class="graphic-detail">
    <h4>The Animal Kingdom (Tiryañca)</h4>
    <p>Classification by habitat (Aquatic, Terrestrial, Aerial) and method of birth (Womb or Spontaneous).</p>
  </div>""",
    196: """
  <div class="graphic-detail">
    <h4>The Human Realm: 303 Types of Humans</h4>
    <p>Only those in the 15 "Lands of Action" (Karmabhūmi) can reach liberation.</p>
  </div>""",
    211: """
  <div class="graphic-detail">
    <h4>The Heavens: Celestial Hierarchy</h4>
    <p>From Bhavanapati to the supreme Vaimānika realms like Sarvārthasiddhi.</p>
  </div>"""
}

# Sort sutras to ensure order
sutras_data.sort(key=lambda x: float(x["id"].split('-')[0].split('–')[0].replace("36.", "")))

for i, data in enumerate(sutras_data):
    sutra_num = int(re.findall(r'\d+', data["id"])[1])
    
    if sutra_num in sections:
        html_content += f'\n  <div class="section-divider"><span>{sections[sutra_num]}</span></div>\n'
    
    if sutra_num in graphics:
        html_content += graphics[sutra_num]
        
    html_content += make_card(data)

# Footer and script
html_content += """
<footer class="bg-[#1d1c17] text-white py-24">
  <div class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-12 border-b border-white/10 pb-20 mb-12">
    <div class="col-span-12 md:col-span-4 flex flex-col gap-8">
      <a href="../../../index-v4.html#hero" class="text-3xl font-headline font-bold tracking-tighter">JainSutra.org</a>
      <p class="text-white/60 font-light leading-relaxed max-w-sm">A digital sanctuary dedicated to ancient sacred texts.</p>
    </div>
    <div class="col-span-6 md:col-span-2 flex flex-col gap-6">
      <p class="text-xs uppercase tracking-[0.2em] font-bold text-primary-fixed">Explore</p>
      <div class="flex flex-col gap-4 text-sm font-light text-white/80">
        <a href="../../../index-v4.html#foundations">Foundations</a>
        <a href="../tattvartha/tattvartha-index-v4.html">Sacred Texts</a>
      </div>
    </div>
    <div class="col-span-12 md:col-span-4 flex flex-col gap-6">
      <a href="../../../fundamentals/donate-v4.html" class="burnished-gradient text-on-primary px-10 py-4 rounded-full font-headline uppercase text-xs font-bold tracking-[0.2em] hover:opacity-90 transition-all text-center">Donate Now</a>
    </div>
  </div>
</footer>

<a href="uttaradhyana-ch35.html" class="nav-button left-btn left-6 md:left-12 flex items-center gap-3 px-4 py-2 rounded-lg font-headline font-bold text-xs tracking-wide">
  <span class="text-lg">&larr;</span> Chapter 35
</a>
<a href="../../../index-v4.html#scriptures" class="nav-button right-btn right-6 md:right-12 flex items-center gap-3 px-4 py-2 rounded-lg font-headline font-bold text-xs tracking-wide">
  Index <span class="text-lg">&rarr;</span>
</a>

<script>
window.addEventListener('scroll', () => {
  const visible = window.scrollY > 300;
  document.querySelectorAll('.nav-button').forEach(b => b.classList.toggle('visible', visible));
});
</script>

</section>
</main>
</body></html>
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {len(sutras_data)} sutras into {output_file}")
