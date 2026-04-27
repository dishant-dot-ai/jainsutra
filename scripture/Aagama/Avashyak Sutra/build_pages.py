"""Build avashyak-ch1.html through avashyak-ch6.html from the markdown translations."""
import re
import os
from pathlib import Path

ROOT = Path(__file__).parent
TRANS = ROOT / "translations"

# Chapter metadata: (number, slug, title_en, title_sk_devanagari, subtitle, sutra_count_label, key_pillars)
CHAPTERS = [
    {
        "num": 1,
        "title_en": "Sāmāyika",
        "title_sk": "સામાયિક",
        "subtitle": "The First Essential — Equanimity. The Namaskar Mahamantra and the Karemi Bhante vow: the foundation of every Jain practice and the doorway into the entire path.",
        "about_title": "The Foundation: Bowing to the Ideal, Vowing the Path",
        "about_p1": "The first essential is Sāmāyika — equanimity. Its name carries the meaning of <i>sama</i> (sameness toward all beings) and <i>aya</i> (gain). To practise it is to step out, even briefly, from the world of like and dislike, and to rest in that balanced state where every other living being is recognised as identical in essence to oneself. It is the first essential because no other practice can succeed until the mind has been first stilled into equanimity.",
        "about_p2": "Avashyak 1 contains two foundational sutras. The first is the <b>Namaskar Mahamantra</b> — the universal salutation to the five categories of awakened beings (Arihants, Siddhas, Acharyas, Upadhyayas, and all Sadhus). It bows not to people but to <i>qualities</i>, recognising no caste, lineage, or denomination. The second is the <b>Karemi Bhante</b> — the formal vow-formula in which the practitioner takes the Samayika vow before the Guru, renouncing all sinful activity by the three karanas and the three yogas.",
        "stats": [("2", "Sutras"), ("Namaskar", "Mahamantra"), ("Karemi Bhante", "Vow Formula"), ("Foundation", "of All Practice")],
        "prev": None,
        "next": 2,
    },
    {
        "num": 2,
        "title_en": "Chaturviṃśatistava",
        "title_sk": "ચતુર્વિંશતિસ્તવ",
        "subtitle": "The Second Essential — the Logassa Sūtra. Seven verses of praise to the twenty-four Tirthankaras, from Rishabh to Mahavir, recited standing in the upright Jin-mudrā.",
        "about_title": "The Praise of the Twenty-Four",
        "about_p1": "After establishing equanimity, the practitioner needs an object on which to fix the mind. The Tirthankaras are those who have already completed what the seeker has only begun. To praise them — to recall their names, contemplate their qualities, and invite their grace — is to align oneself with the direction in which one wishes to travel. As the Sanskrit verse reminds us: <i>śraddhāmayo'yaṃ puruṣaḥ</i> — 'A person becomes whatever they hold faith in.'",
        "about_p2": "The Logassa was asked of Lord Mahavira directly. In the Uttaradhyayana Sutra, Gautam Swami asks what the soul gains by praising the twenty-four. Mahavira's answer: 'By such praise, the karma of false belief is reduced; the practitioner attains the purity of right perception; through love of their qualities those qualities arise within the practitioner's own being.' The sutra has a precise five-part structure: the nature of the Tirthankaras, their names, their distinguishing marks, the devotee's request, and the closing similes.",
        "stats": [("7", "Gathas"), ("24", "Tirthankaras"), ("Jin-mudrā", "Posture"), ("Logassa", "Universal Name")],
        "prev": 1,
        "next": 3,
    },
    {
        "num": 3,
        "title_en": "Vandanā",
        "title_sk": "વંદના",
        "subtitle": "The Third Essential — formal reverence to the Guru. The Ichchhami Khamasamano sutra in its four-part structure: wish, request for entry, enquiry about welfare, and request for forgiveness.",
        "about_title": "Reverence to the Living Guide",
        "about_p1": "After the practitioner has steadied the mind in equanimity (Sāmāyika) and praised the perfected ones (Chaturvimshatistava), the current of devotion naturally flows toward the <i>living</i> guide who keeps the path visible. Without a Guru to correct the seeker's missteps, the texts are silent letters and the seeker walks blind.",
        "about_p2": "Acharya Umaswati gives the chain of cause and effect that begins with vandanā: humility leads to the wish to serve; serving the Guru leads to scriptural knowledge; knowledge leads to detachment; detachment to the stopping of inflow; the stopping of inflow to the gathering of austerity; austerity to the shedding of karma; the shedding of karma to liberation. The whole spiritual ladder rests on its first rung: humility expressed through reverence to the teacher.",
        "stats": [("1", "Sutra"), ("4 Parts", "Inner Structure"), ("3.5 Cubit", "Avagrah"), ("33", "Āshātanās")],
        "prev": 2,
        "next": 4,
    },
    {
        "num": 4,
        "title_en": "Pratikramaṇa",
        "title_sk": "પ્રતિક્રમણ",
        "subtitle": "The Fourth and Longest Essential — the daily turning back from every transgression. Ten paths of confession ending in universal forgiveness offered to every living being.",
        "about_title": "The Heart of Jain Practice",
        "about_p1": "The fourth and longest essential is Pratikramaṇa — literally, 'going back' — the daily ritual of confessing, withdrawing from, and atoning for every transgression of the day, fortnight, four months, or year. To do pratikraman is not merely to say 'sorry'; it is to actively return — by mind, speech, and body — to the place of right conduct from which one had drifted. Even the smallest unwitting harm — a step on an insect, a sharp word, a wandering thought — must be acknowledged daily, before sleep, lest it harden into karmic deposit.",
        "about_p2": "Avashyak 4 contains ten paths in a precise order: the renewed Karemi Bhante vow; the Chattari Mangalam (four refuges); the synoptic Ichchhami Padikkamiu confession; the Iriyavahiyam (confession for the violence of motion); five Shraman Sutras covering sleep, alms-tour, time-discipline, the great 33-fold enumeration of monastic conduct, and the affirmation of faith with salutation to all contemporary sadhus; and finally the Kshamapana — closing forgiveness offered to every living being in the universe.",
        "stats": [("10", "Paths"), ("33-fold", "Great Enumeration"), ("18,24,120", "Distinct Confessions"), ("Universal", "Forgiveness")],
        "prev": 3,
        "next": 5,
    },
    {
        "num": 5,
        "title_en": "Kāyotsarga",
        "title_sk": "કાયોત્સર્ગ",
        "subtitle": "The Fifth Essential — release of the body. The standing or seated meditation in which the practitioner sets down even the body, so that the mind can rest in pure consciousness.",
        "about_title": "The Healing of the Wound",
        "about_p1": "The body cannot literally be discarded while life remains; what is released is <i>attachment to the body</i> — the constant micro-pulse of identification that says 'this is me,' 'I must move,' 'I must protect this.' For the duration of the practice, the practitioner stands or sits absolutely still, suspends bodily activity, restrains speech, harnesses the mind into pure meditation, and rests in the consciousness that <i>is the soul</i> — separated from the bodily sheath that ordinarily disguises it.",
        "about_p2": "The Anuyogadwar Sutra calls Kāyotsarga the <i>vraṇa-cikitsā</i> — the 'dressing of the wound.' Pratikramana opens the wound; Kāyotsarga heals it. The Avashyak Niryukti gives five direct fruits: the inertness of the body is destroyed; the intelligence is purified; the capacity to bear both pleasure and pain develops; subtle contemplation increases; one-pointed concentration in wholesome meditation is gained.",
        "stats": [("4", "Paths"), ("Tassa Uttarīkaranenaṃ", "Vow Formula"), ("12", "Natural Exemptions"), ("3 Guptis", "Held Together")],
        "prev": 4,
        "next": 6,
    },
    {
        "num": 6,
        "title_en": "Pratyākhyāna",
        "title_sk": "પ્રત્યાખ્યાન",
        "subtitle": "The Sixth and Final Essential — the formal vow of renunciation. Ten time-bound pratyakhyana vows from Navkarshi to Upvas — the polishing-stroke that completes the day.",
        "about_title": "The Forward-Looking Vow",
        "about_p1": "Where the four earlier essentials looked backward (confession of past faults) or inward (cultivation of the present mind), Pratyākhyāna looks <i>forward</i>: it pre-emptively closes off the future possibility of certain karma-bindings. To do pratyakhyana is to <i>declare against</i> — to publicly and formally renounce. It is not a mere intention ('I should fast'); it is a binding promise ('from sunrise to sunrise, I shall not eat').",
        "about_p2": "The ten paths of this Avashyak are the ten forms of <i>aḍḍhā-pratyākhyāna</i> — the time-bound renunciations: Navkarshi (one muhurta), Porisi (one praharaḥ), Be Porisi (two praharas), Ekashanu (one sitting), Ekalathanu (one position), Ayambil (tasteless food), Upvas (full fast), Divas Charim (day-end), Abhigrah (conditional resolution), and Nirvigai (no enrichments). Each includes specified <i>āgārs</i> (exemptions) — practical wisdom built into every vow. The chapter closes with the Antim Mangal: the Namotthunaṃ Sūtra.",
        "stats": [("10", "Paths"), ("4 Foods", "Asana, Pana, Khadima, Svadima"), ("6 Vigaiyas", "Tasty Enrichments"), ("Namotthunaṃ", "Closing Mangal")],
        "prev": 5,
        "next": None,
    },
]


# Per-chapter sutra extraction from the markdown files. We do this by parsing the markdown.
def parse_markdown(md_text):
    """Parse a translation markdown file and return list of sutras as dicts.
    Each sutra has: num, title (after the dash if present), prakrit, english, commentary, simply_put."""
    sutras = []
    # Split by SUTRA headers. Match "## SUTRA X.Y" and "## SUTRA X.Y — Title"
    # Also match "## CLOSING SUTRA — Title" (treated as a final sutra in the chapter)
    sutra_re = re.compile(
        r'^##\s+(?:SUTRA\s+(\S+?)|CLOSING SUTRA)(?:\s*[—-]\s*(.+?))?\s*$',
        re.MULTILINE,
    )
    matches = list(sutra_re.finditer(md_text))
    for i, m in enumerate(matches):
        # group(1) is the sutra number for "SUTRA X.Y"; None for "CLOSING SUTRA"
        num = (m.group(1) or 'closing').strip()
        title = (m.group(2) or '').strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[start:end]
        # Sections
        prakrit = extract_section(body, "1. PRAKRIT TEXT", "2. ROMAN TRANSLITERATION")
        english = extract_section(body, "3. LITERAL ENGLISH TRANSLATION", "4. ANVAYARTHA")
        commentary = extract_section(body, "5. COMMENTARY", "6. SIMPLY PUT")
        simply_put = extract_section(body, "6. SIMPLY PUT", "7. CONTEMPLATE")
        sutras.append({
            "num": num,
            "title": title,
            "prakrit": clean_prakrit(prakrit),
            "english": clean_text(english),
            "commentary": clean_text(commentary),
            "simply_put": clean_text(simply_put),
        })
    return sutras


def extract_section(body, start_label, end_label):
    """Extract text between two ### section labels."""
    start_re = re.compile(r'^###\s+' + re.escape(start_label) + r'\s*$', re.MULTILINE)
    end_re = re.compile(r'^###\s+' + re.escape(end_label) + r'\s*$', re.MULTILINE)
    m_start = start_re.search(body)
    if not m_start:
        return ''
    m_end = end_re.search(body, m_start.end())
    end = m_end.start() if m_end else len(body)
    return body[m_start.end():end].strip()


def clean_prakrit(text):
    """Clean Prakrit: remove verse-marker, collapse whitespace, escape HTML."""
    if not text:
        return ''
    # Remove ॥X.Y॥ verse markers
    text = re.sub(r'॥\s*\d+\.\d+\s*॥', '', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return html_escape(text)


def clean_text(text):
    """Clean prose text: keep paragraphs but collapse intra-paragraph whitespace, escape HTML."""
    if not text:
        return ''
    # Get first paragraph for compact display (or full text concatenated)
    # For commentary we want full text but compact
    paras = re.split(r'\n\n+', text)
    cleaned = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        # Skip parenthetical "see above" notes
        if p.startswith('(See ') or p.startswith('Identical to '):
            continue
        # Convert markdown bold/italic to HTML before escaping the rest
        p = re.sub(r'\s+', ' ', p)
        cleaned.append(p)
    if not cleaned:
        return ''
    full = ' '.join(cleaned)
    return md_to_html(full)


def md_to_html(text):
    """Convert markdown bold/italic to HTML, escape rest."""
    # First escape HTML special chars (but preserve quotes for now)
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Bold: **text** -> <b>text</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic: *text* -> <i>text</i>  (but not inside bold already converted)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
    # Italic via _text_
    text = re.sub(r'(?<!\w)_([^_]+?)_(?!\w)', r'<i>\1</i>', text)
    return text


def html_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ---- HTML template ----

PAGE_TPL = '''<!DOCTYPE html>
<html class="light" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Avashyak {num}: {title_en} | JainSutra.org</title>
<meta name="description" content="Avashyak {num} of the Avashyak Sutra — {title_en} ({title_sk}). {subtitle}"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
tailwind.config = {{
  darkMode: "class",
  theme: {{
    extend: {{
      colors: {{
        "secondary-container":"#e6ded9","primary-fixed-dim":"#e6c364","surface":"#fef9f1","outline-variant":"#d0c5b2","outline":"#7e7665","on-secondary":"#ffffff","surface-dim":"#ded9d2","surface-container-high":"#ece8e0","primary":"#755b00","on-primary-container":"#503d00","secondary":"#625d59","on-secondary-container":"#67625e","on-primary":"#ffffff","on-error-container":"#93000a","secondary-fixed-dim":"#ccc5c0","surface-variant":"#e7e2da","surface-container-lowest":"#ffffff","surface-container-highest":"#e7e2da","primary-container":"#c9a84c","inverse-primary":"#e6c364","on-surface-variant":"#4d4637","tertiary":"#4d5a98","background":"#fef9f1","on-surface":"#1d1c17","surface-container":"#f2ede5","surface-container-low":"#f8f3eb"
      }},
      fontFamily: {{ "headline": ["Noto Serif", "serif"], "body": ["Inter", "sans-serif"], "label": ["Inter", "sans-serif"] }},
      borderRadius: {{"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"}},
    }},
  }},
}}
</script>
<style>
html {{ scroll-behavior: smooth; }}
.burnished-gradient {{ background: radial-gradient(circle at center, #755b00, #c9a84c); }}
.sutra-card {{ border: 1px solid rgba(201,168,76,0.25); border-left: 3px solid #c9a84c; background: white; }}
.sutra-sanskrit {{ font-size: 1.35rem; line-height: 2; color: #503d00; }}
.simple-explanation {{ margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed rgba(201,168,76,0.3); font-family: 'Inter', sans-serif; font-size: 1.2rem; line-height: 1.85; color: #4d4637; }}
.sutra-card p.text-base {{ font-size: 1.2rem; line-height: 1.85; }}
.simple-explanation b {{ color: #1d1c17; font-weight: 600; }}
.sutra-card p.text-lg {{ font-size: 1.2rem; line-height: 1.85; }}
.nav-button {{ position: fixed; bottom: 24px; z-index: 100; background: #ffffff; border: 1px solid #C9A84C; color: #755b00; transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; transform: translateY(20px); }}
.nav-button.visible {{ opacity: 1; pointer-events: auto; transform: translateY(0); }}
.nav-button:hover {{ border-color: #C9A84C; color: #503d00; }}
.glass-nav {{ background: rgba(248, 247, 246, 0.85); backdrop-filter: blur(20px); }}
@media (max-width: 768px) {{ .nav-button {{ bottom: 16px; }} .sutra-sanskrit {{ font-size: 1.15rem; }} }}
#search-dropdown {{ position:absolute; top:calc(100% + 8px); left:0; min-width:400px; max-width:520px; background:#fff; border-radius:8px; box-shadow:0 8px 32px rgba(0,0,0,0.13); border:1px solid rgba(201,168,76,0.25); overflow:hidden; display:none; z-index:1000; max-height:420px; overflow-y:auto; }}
.search-section-label {{ padding:8px 16px 4px; font-family:'Inter',sans-serif; font-size:9px; text-transform:uppercase; letter-spacing:0.12em; color:#C9A84C; font-weight:700; border-top:1px solid #f0ebe3; }}
.search-section-label:first-child {{ border-top:none; }}
.search-result-item {{ display:flex; align-items:baseline; gap:10px; padding:9px 16px; text-decoration:none; cursor:pointer; border:none; background:none; width:100%; text-align:left; transition:background 0.15s; }}
.search-result-item:hover {{ background:#fef9f1; }}
.search-result-num {{ font-family:'Noto Serif',serif; font-size:11px; color:#C9A84C; font-weight:700; flex-shrink:0; }}
.search-result-title {{ font-family:'Inter',sans-serif; font-size:12px; color:#1d1c17; line-height:1.4; }}
.search-no-results {{ padding:16px; color:#7e7665; font-family:'Inter',sans-serif; font-size:12px; text-align:center; }}
#main-nav a {{ text-decoration: none; }}
.nav-link {{ text-decoration: none; }}
.mesh-bg {{ background-color: #f8f7f6; background-image: radial-gradient(#C9A84C15 1px, transparent 1px); background-size: 40px 40px; }}
</style>
</head>
<body class="text-on-surface font-body selection:bg-primary-container selection:text-on-primary-container bg-white">
<nav class="glass-nav fixed top-0 w-full z-50 transition-all duration-500 border-b border-[#C9A84C]/10" id="main-nav">
<div class="flex justify-between items-center px-6 md:px-12 py-5 max-w-screen-2xl mx-auto">
<div class="flex items-center gap-12">
<a href="../../../index-v4.html#hero"><span class="nav-logo text-2xl font-headline text-primary tracking-tighter font-bold transition-colors duration-500">JainSutra.org</span></a>
<div class="hidden md:flex gap-10 items-center font-headline tracking-[0.1em] uppercase text-xs font-semibold">
<a class="nav-link text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../index-v4.html#foundations">Fundamentals</a>
<a class="nav-link text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../fundamentals/navkar-mantra-v4.html">Navkar</a>
<a class="nav-link text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../fundamentals/meditations.html">Meditations</a>
<a class="text-primary font-semibold hover:text-primary transition-colors" href="../sacred-sutras-index.html">Sacred Texts</a>
</div>
</div>
<div class="flex items-center gap-8">
<div class="relative group hidden lg:block">
<span class="nav-search-icon material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-sm transition-colors duration-500">search</span>
<input class="nav-search bg-surface-container-low border-none rounded-full py-2 pl-10 pr-6 text-sm font-label placeholder:italic transition-all duration-300 w-48 focus:w-72 focus:ring-1 focus:ring-primary/20" id="search-input" placeholder="Explore Wisdom..." type="text"/>
<div id="search-dropdown"></div>
</div>
<a class="burnished-gradient text-white px-8 py-2.5 rounded-full font-headline uppercase text-[10px] font-bold tracking-[0.2em] hover:opacity-90 transition-all shadow-sm" href="../../../fundamentals/donate-v4.html">Donate</a>
</div>
</div>
</nav>
<main class="pt-40">
<section class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-8 md:gap-16 items-center mb-40">
<div class="col-span-12 lg:col-span-5 flex flex-col gap-10 order-2 lg:order-1">
<div class="flex flex-col gap-3">
<span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Avashyak Sutra · Avashyak {num}</span>
<h1 class="text-7xl md:text-8xl font-headline font-bold text-on-surface leading-tight tracking-tighter">
{title_en} <span class="block text-primary font-normal text-3xl md:text-4xl mt-3">{title_sk}</span>
</h1>
</div>
<h2 class="text-2xl md:text-3xl font-headline text-on-surface-variant leading-tight font-light">{subtitle}</h2>
</div>
<div class="col-span-12 lg:col-span-7 order-1 lg:order-2 flex items-center justify-center">
<div class="w-full max-w-2xl aspect-[4/3] rounded-xl bg-surface-container-low flex items-center justify-center border border-outline-variant/30">
<p class="text-center font-headline text-on-surface/40 text-sm px-8">Avashyak {num}: {title_en}</p>
</div>
</div>
</section>
<section class="bg-[#f2f1f0] py-24 mesh-bg">
<div class="max-w-screen-xl mx-auto px-6 md:px-12">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
<div class="flex flex-col gap-8">
<div class="flex flex-col gap-3">
<span class="text-primary font-headline italic tracking-[0.2em] text-xs uppercase font-semibold">About This Essential</span>
<h3 class="text-3xl md:text-4xl font-headline font-bold text-on-surface leading-tight tracking-tighter">{about_title}</h3>
</div>
<p class="text-lg text-on-surface-variant leading-relaxed">{about_p1}</p>
<p class="text-lg text-on-surface-variant leading-relaxed">{about_p2}</p>
</div>
<div class="grid grid-cols-2 gap-6">
{stats_html}
</div>
</div>
</div>
</section>
<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-32 space-y-24">
<div class="flex flex-col gap-3 mb-16">
<span class="text-primary font-headline italic tracking-[0.2em] text-xs uppercase font-semibold">Sacred Text</span>
<h3 class="text-3xl md:text-4xl font-headline font-bold text-on-surface leading-tight tracking-tighter">The Sutras of Avashyak {num}</h3>
<p class="text-lg text-on-surface-variant max-w-2xl">Prakrit original with English translation, commentary, and the simple explanation.</p>
</div>
{sutras_html}
</section>
</main>
{prev_link}
{next_link}
<footer class="w-full py-20 bg-surface-container-low border-t border-primary/10">
<div class="max-w-screen-2xl mx-auto flex flex-col md:flex-row justify-between items-start px-6 md:px-12 gap-16">
<div class="flex flex-col gap-6 max-w-md">
<span class="font-headline text-primary font-bold tracking-[0.3em] uppercase text-sm">JainSutra</span>
<p class="font-body text-sm leading-relaxed text-on-surface/60 font-light">Exploring the profound depths of Jain philosophy through a modern lens. Dedicated to the path of Anekantavada and the purification of the soul.</p>
<p class="text-[10px] uppercase tracking-[0.2em] text-outline font-bold">&copy; 2024 JainSutra. All Rights Reserved.</p>
</div>
<div class="grid grid-cols-2 lg:grid-cols-3 gap-12 font-headline text-xs font-bold tracking-[0.2em] uppercase text-on-surface-variant">
<div class="flex flex-col gap-4">
<span class="text-primary/40 mb-2">Aagama</span>
<a class="hover:text-primary transition-colors" href="../sacred-sutras-index.html">Sacred Sutras</a>
<a class="hover:text-primary transition-colors" href="avashyak-index.html">Avashyak Index</a>
<a class="hover:text-primary transition-colors" href="../uttaradhyana/uttaradhyana-index.html">Uttaradhyayana</a>
</div>
<div class="flex flex-col gap-4">
<span class="text-primary/40 mb-2">Explore</span>
<a class="hover:text-primary transition-colors" href="../../../index-v4.html#foundations">Fundamentals</a>
<a class="hover:text-primary transition-colors" href="../../../fundamentals/navkar-mantra-v4.html">Navkar Mantra</a>
<a class="hover:text-primary transition-colors" href="../../../fundamentals/meditations.html">Meditations</a>
</div>
</div>
</div>
</footer>
<script>
window.addEventListener('scroll', () => {{
    const buttons = document.querySelectorAll('.nav-button');
    if (window.scrollY > 300) {{
        buttons.forEach(btn => btn.classList.add('visible'));
    }} else {{
        buttons.forEach(btn => btn.classList.remove('visible'));
    }}
}});
</script>
<script src="../../../js/global-search.js"></script>
</body>
</html>
'''


SUTRA_CARD_TPL = '''<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{num}">
<div class="flex items-start gap-6">
<span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{num}</span>
<div class="space-y-4 flex-1">
{title_block}
<p class="sutra-sanskrit font-headline">{prakrit}</p>
<p class="text-lg font-semibold text-on-surface leading-relaxed">{english}</p>
<p class="text-base text-on-surface-variant leading-relaxed">{commentary}</p>
<p class="simple-explanation"><b>Simply Put:</b> {simply_put}</p>
</div>
</div>
</article>'''


STAT_CARD_TPL = '''<div class="sutra-card p-6 rounded-xl">
<p class="{value_class} font-headline font-bold text-primary mb-1">{value}</p>
<p class="text-sm text-on-surface-variant font-label uppercase tracking-widest">{label}</p>
</div>'''


def render_stats(stats):
    out = []
    for value, label in stats:
        # Use bigger font for short numeric values
        cls = "text-3xl" if len(value) <= 4 else "text-lg"
        out.append(STAT_CARD_TPL.format(value=value, label=label, value_class=cls))
    return '\n'.join(out)


def render_sutras(sutras):
    cards = []
    for s in sutras:
        # Skip empty placeholder sutras (no Prakrit)
        if not s["prakrit"]:
            # Render a "see reference" notice card if title present
            if s["title"]:
                cards.append(make_reference_card(s))
            continue
        title_block = ''
        if s["title"]:
            title_block = f'<h4 class="text-xl font-headline font-bold text-on-surface mt-0">{s["title"]}</h4>'
        cards.append(SUTRA_CARD_TPL.format(
            num=s["num"],
            title_block=title_block,
            prakrit=s["prakrit"],
            english=s["english"] or '<em>(See above for full translation.)</em>',
            commentary=s["commentary"] or '',
            simply_put=s["simply_put"] or '',
        ))
    return '\n'.join(cards)


def make_reference_card(s):
    """A compact card for sutras that just reference earlier ones (no Prakrit text shown)."""
    title = s["title"]
    body = s["english"] or s["commentary"] or s["simply_put"] or 'See referenced sutra.'
    return f'''<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{s["num"]}">
<div class="flex items-start gap-6">
<span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{s["num"]}</span>
<div class="space-y-4 flex-1">
<h4 class="text-xl font-headline font-bold text-on-surface mt-0">{title}</h4>
<p class="text-base text-on-surface-variant leading-relaxed">{body}</p>
</div>
</div>
</article>'''


def render_nav_links(prev_num, next_num):
    prev_html = ''
    if prev_num is not None:
        prev_html = f'<a class="nav-button left-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="avashyak-ch{prev_num}.html"><span class="text-lg">←</span> Avashyak {prev_num}</a>'
    else:
        prev_html = '<a class="nav-button left-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="avashyak-index.html"><span class="text-lg">←</span> Index</a>'
    next_html = ''
    if next_num is not None:
        next_html = f'<a class="nav-button right-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="avashyak-ch{next_num}.html">Avashyak {next_num} <span class="text-lg">→</span></a>'
    else:
        next_html = '<a class="nav-button right-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="avashyak-index.html">Index <span class="text-lg">→</span></a>'
    return prev_html, next_html


def main():
    for chap in CHAPTERS:
        num = chap["num"]
        md_path = TRANS / f"avashyak-ch{num}-translation.md"
        md_text = md_path.read_text(encoding='utf-8')
        sutras = parse_markdown(md_text)
        sutras_html = render_sutras(sutras)
        stats_html = render_stats(chap["stats"])
        prev_link, next_link = render_nav_links(chap["prev"], chap["next"])
        page = PAGE_TPL.format(
            num=num,
            title_en=chap["title_en"],
            title_sk=chap["title_sk"],
            subtitle=chap["subtitle"],
            about_title=chap["about_title"],
            about_p1=chap["about_p1"],
            about_p2=chap["about_p2"],
            stats_html=stats_html,
            sutras_html=sutras_html,
            prev_link=prev_link,
            next_link=next_link,
        )
        out_path = ROOT / f"avashyak-ch{num}.html"
        out_path.write_text(page, encoding='utf-8')
        print(f"Wrote {out_path.name}: {len(sutras)} sutras parsed")


if __name__ == '__main__':
    main()
