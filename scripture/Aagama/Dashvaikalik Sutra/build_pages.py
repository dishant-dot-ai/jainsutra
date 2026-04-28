"""Build dashvaikalik chapter HTML pages from the markdown translations."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
TRANS = ROOT / "translations"

# Chapter metadata. Each chapter can pull from one or more markdown files.
CHAPTERS = [
    {
        "num": 1, "slug": "ch1",
        "title_en": "Drumapuṣpikā",
        "title_sk": "દ્રુમપુષ્પિકા",
        "subtitle": "The First Adhyayan — the Tree-and-Flower simile. The famous bee-and-blossom image for how the right monk takes alms: gathering a little here and a little there, never burdening any household, never uprooting the source.",
        "about_title": "The Bee Among the Blossoms",
        "about_p1": "The Dashvaikalik Sutra opens with one of the most beloved images in Jain literature. Just as the bee draws nectar from many flowers, taking only a little from each — never bending the stem, never bruising the petal, never exhausting one bloom — so does the right monk take alms from many households, accepting only a small portion from each, leaving every kitchen and every kitchen-keeper undisturbed. This image, called <i>madhukarī</i>, defines the entire Jain monastic ethic of receiving.",
        "about_p2": "The chapter establishes from the very first verse that dharma is supreme — <i>ahiṃsā saṃyamo tavo</i> — non-violence, restraint, austerity. From this triad flows the discipline that allows the monk to walk through the world receiving without taking, eating without grasping, living without harming. The chapter ends with the rule that the monk must hold himself to the standard of nirdosha bhiksha-charya — alms-conduct without fault.",
        "files": ["dashvaikalik-ch1-translation.md"],
        "stats": [("5", "Sutras"), ("Bee & Flower", "Master Image"), ("Ahimsa-Saṃyam-Tap", "Triad of Dharma"), ("Madhukarī", "Begging Style")],
        "prev": None, "next": 2,
    },
    {
        "num": 2, "slug": "ch2",
        "title_en": "Śrāmaṇyapūrvaka",
        "title_sk": "શ્રામણ્યપૂર્વક",
        "subtitle": "The Second Adhyayan — the Foundation of Monkhood. Includes the celebrated dialogue of Rajemati and Rathnemi: the noble lady who, at her wedding-eve renunciation, rebukes the wavering Rathnemi and restores him to the path.",
        "about_title": "When the Body Wavers, the Vow Holds",
        "about_p1": "The second adhyayan addresses the deepest test of the renunciate's life: the resurgence of desire after the vow has been taken. It teaches that the foundation of monkhood (śrāmaṇya) is the conquest of <i>kāmarāga</i> — sensual longing. The chapter unfolds with metaphors of the steady mind, the suppressed flame, the well-rooted tree.",
        "about_p2": "At its centre is one of the most moving episodes in all Jain narrative: Rajemati, the bride-to-be of Lord Neminath who became a nun on the day he renounced, encounters her brother-in-law Rathnemi who is wavering at the sight of her wet robes. Her four verses of rebuke — invoking the noble Agandhana serpents who refuse to swallow back what they have spat out, the disgrace (<i>dhiratthu</i>) of falling, the lineage of the Yadavas, and the rootless hada — restore Rathnemi instantly. The chapter closes with Acharya Shyambhava naming Rathnemi <i>puruṣottama</i>, the supreme among men.",
        "files": ["dashvaikalik-ch2-translation.md"],
        "stats": [("11", "Sutras"), ("Rajemati", "Spiritual Teacher"), ("Rathnemi", "Restored Renunciate"), ("Agandhana", "Serpent Image")],
        "prev": 1, "next": 3,
    },
    {
        "num": 3, "slug": "ch3",
        "title_en": "Kṣullakācārakathā",
        "title_sk": "ક્ષુલ્લકાચારકથા",
        "subtitle": "The Third Adhyayan — the 52 Anachara. A precise enumeration of every act forbidden to the monk: the small and the great improprieties that mark the difference between a true renunciate and a hypocrite.",
        "about_title": "What the Monk Will Not Do",
        "about_p1": "The third adhyayan is a list — but a list with the force of a vow. Fifty-two specific acts are named, each one absolutely forbidden to the Jain monk: from the obvious (no killing, no stealing) to the subtle (no praising tasty food, no looking at women's ornaments, no carrying medicines for vanity, no using fire for warmth). The chapter is the boundary line of monastic life. To cross it is to cease being a monk.",
        "about_p2": "Beyond the list, the chapter glorifies the <i>nirgranth</i> — the unknotted one, the monk who has cut every tie. It lifts up the dignity of the path: those who walk it are praised by gods, by humans, by the Tirthankaras themselves. The 52 anacharas are not arbitrary prohibitions but the negative shape of the monk's positive life. To know what he will not do is to see what he is.",
        "files": ["dashvaikalik-ch3-translation.md"],
        "stats": [("15+", "Sutras"), ("52", "Anacharas"), ("Nirgranth", "The Unknotted"), ("Boundary", "of Monkhood")],
        "prev": 2, "next": 4,
    },
    {
        "num": 4, "slug": "ch4",
        "title_en": "Ṣaḍ-Jīvanikāya",
        "title_sk": "ષટ્-જીવનિકાય",
        "subtitle": "The Fourth and Most Central Adhyayan — the Six Classes of Living Beings. The doctrinal heart of the Dashvaikalik: earth, water, fire, air, plants, and mobile beings — every drop, every spark, every blade alive.",
        "about_title": "The Universe Is Full of Souls",
        "about_p1": "The fourth adhyayan is the longest and most central chapter of the Dashvaikalik — and arguably of all Jain ethics. It announces that the universe contains six classes of living beings: <i>pṛthvī-kāya</i> (earth-bodies), <i>ap-kāya</i> (water-bodies), <i>tejas-kāya</i> (fire-bodies), <i>vāyu-kāya</i> (air-bodies), <i>vanaspati-kāya</i> (plant-bodies), and <i>trasa-kāya</i> (mobile beings). Each handful of soil, each drop of water, each spark, each gust, each blade of grass holds <i>aneka jīva</i> — countless individual souls. Modern science has only recently confirmed what Jain darshan asserted twenty-five centuries ago.",
        "about_p2": "From this metaphysical foundation flows the entire monastic ethic: the five mahāvrats (non-violence, truth, non-stealing, celibacy, non-possession), the prohibition against night-eating, and the six yatana sutras — one per kāya — teaching the monk how to walk, eat, drink, sit, sleep, and breathe without harming the lives that fill the world. The chapter closes with verses on yatana and ayatana, the importance of knowledge, and the spiritual development arc.",
        "files": ["dashvaikalik-ch4-translation.md"],
        "stats": [("48", "Sutras"), ("6", "Classes of Life"), ("5", "Mahāvrats"), ("Sarvajna", "Authority")],
        "prev": 3, "next": 5,
    },
    {
        "num": 5, "slug": "ch5",
        "title_en": "Piṇḍeṣaṇā",
        "title_sk": "પિણ્ડેષણા",
        "subtitle": "The Fifth Adhyayan — the Search for Food. The most extensive treatment of monastic alms-conduct in the Jain canon. In two uddeshas: the going-for-alms and the eating-after-alms.",
        "about_title": "The Daily Conduct of Receiving",
        "about_p1": "The fifth adhyayan is the largest single section of the Dashvaikalik — 112 PDF pages devoted entirely to the monastic alms-tour and the meal that follows. Uddesha 1 (Piṇḍeṣaṇā — 'the search for food') walks the monk through every step: when to leave for alms, which paths to take, which households to enter and which to avoid, what food to accept and what to refuse, the famous 42 doshas (faults) — 16 udgama (donor-side), 16 utpādana (monk-side), 10 eṣaṇā (acceptance).",
        "about_p2": "Uddesha 2 covers what happens after the alms are returned to the upashraya: how to eat, how to share with co-monks, how to handle leftovers (parishtāpanika), how to maintain inner detachment from taste even while the body is being nourished. Together the two uddeshas form the practical core of the Jain monastic life: receiving without taking, eating without grasping, sustaining the body without strengthening attachment to it.",
        "files": ["dashvaikalik-ch5-uddesha1-translation.md", "dashvaikalik-ch5-uddesha2-translation.md"],
        "stats": [("47", "Sutras Total"), ("42", "Doshas of Alms"), ("2", "Uddeshas"), ("112", "PDF Pages")],
        "prev": 4, "next": 6,
    },
    {
        "num": 6, "slug": "ch6",
        "title_en": "Mahācārakathā",
        "title_sk": "મહાચારકથા",
        "subtitle": "The Sixth Adhyayan — the Great Account of Conduct. Eighteen sthanas of right conduct: the five mahāvrats, night-eating prohibition, six classes of life, and twelve more disciplines that define the monk's daily life.",
        "about_title": "Eighteen Pillars of the Path",
        "about_p1": "The sixth adhyayan presents the complete framework of monastic conduct as eighteen <i>sthāna</i> — eighteen 'standing-places,' eighteen pillars on which the entire life of a monk rests. The first six are the foundation: non-violence, truth, non-stealing, celibacy, non-possession, and the prohibition against night-eating. The next six are the protections: care for the six classes of living beings (earth, water, fire, air, plants, mobile beings).",
        "about_p2": "The remaining six are the boundary disciplines: avoiding forbidden food (akalpya), householder's food, beds and luxurious furniture, certain houses, bathing, and bodily ornamentation (vibhūṣā). Together these eighteen sthanas form a complete diagram of what the monk does and does not do — the architecture of the monastic life.",
        "files": ["dashvaikalik-ch6-translation.md"],
        "stats": [("20+", "Sutras"), ("18", "Sthanas of Conduct"), ("5", "Mahāvrats"), ("Vibhūṣā", "Anti-Ornamentation")],
        "prev": 5, "next": 7,
    },
    {
        "num": 7, "slug": "ch7",
        "title_en": "Suvākyaśuddhi",
        "title_sk": "સુવાક્યશુદ્ધિ",
        "subtitle": "The Seventh Adhyayan — Purity of Speech. The comprehensive treatise on right speech: four kinds of language, what to avoid, what to say, and how to use words carefully about plants, beings, and conditions.",
        "about_title": "What to Say and What to Hold Back",
        "about_p1": "The seventh adhyayan is the most complete teaching on speech in the Jain canon. It begins by classifying language into four types: <i>satya</i> (truthful), <i>asatya</i> (false), <i>satya-asatya miśra</i> (mixed), and <i>asatya-anubhaya</i> (neither, i.e. neutral). The first and fourth are permissible to the monk; the second and third are forbidden. Beyond classification, the chapter teaches careful word-choice: never declarative speech about uncertain matters, never harsh or hurtful speech, never deceptive speech, never speech that predicts the future without omniscient warrant.",
        "about_p2": "The chapter is famous for its precision about plants and beings: the monk should not call a banyan tree 'the great tree' (which praises it and may invite cutting); should not call a calf 'meaty' (which suggests slaughter); should not call clouds 'about to rain' (which presumes prediction). Right speech, in Jain practice, is <i>mita-bhāṣaṇa</i> — measured, beneficial, true, and clear. The chapter closes with verses on the discipline of the wise speaker.",
        "files": ["dashvaikalik-ch7-translation.md"],
        "stats": [("21", "Sutras"), ("4", "Types of Language"), ("Mita-bhāṣaṇa", "Measured Speech"), ("Plants & Beings", "Careful Naming")],
        "prev": 6, "next": 8,
    },
    {
        "num": 8, "slug": "ch8",
        "title_en": "Ācāra-Praṇidhi",
        "title_sk": "આચારપ્રણિધિ",
        "subtitle": "The Eighth Adhyayan — the Resolution of Conduct. The complete daily conduct of a monk: care for six classes of life, eight kinds of subtle beings, restraint of all five senses, four kashayas, and the inner discipline.",
        "about_title": "The Daily Resolution",
        "about_p1": "The eighth adhyayan presents the monk's daily conduct as a single sustained <i>praṇidhi</i> — a resolution, a focused commitment held continuously through the day. It opens with care for the six classes of living beings, then expands to the eight kinds of subtle beings (different categories of micro-life), then to the careful use of monastic equipment through pratilekhana (visual inspection) and pramārjana (gentle cleansing).",
        "about_p2": "The chapter then turns inward: restraint of the five senses, control of the four kashayas (anger, pride, deceit, greed), the discipline of speech, the avoidance of pramāda (negligence). It is essentially a daily curriculum for the monk who has taken the vows in earlier chapters and now must live them out hour by hour. The chapter has 25-64 sutras depending on the edition, ending with the famous 'अध्ययन-૮ સંપૂર્ણ.'",
        "files": ["dashvaikalik-ch8-translation.md"],
        "stats": [("25+", "Sutras"), ("6", "Classes of Life"), ("4", "Kashayas"), ("Praṇidhi", "Sustained Resolution")],
        "prev": 7, "next": 9,
    },
    {
        "num": 9, "slug": "ch9",
        "title_en": "Vinaya-Samādhi",
        "title_sk": "વિનયસમાધિ",
        "subtitle": "The Ninth Adhyayan — Humility and Stillness. Four uddeshas on vinaya (humility/discipline) — the foundation of all spiritual progress — and on the four samadhis: vinaya, shruta, tapa, and achar.",
        "about_title": "Humility as the Root of All",
        "about_p1": "The ninth adhyayan is unique in being the only Dashvaikalik chapter divided into four uddeshas. Its subject is <i>vinaya</i> — humility, discipline, and reverence to the teacher. Uddesha 1 establishes the principle: indiscipline ruins the disciple as surely as a blocked root kills a tree. Uddesha 2 unfolds the fruit of dharma rooted in vinaya, with the vivid parable of the broken thorn.",
        "about_p2": "Uddesha 3 describes the qualities of the disciple worthy of worship — the well-trained monk in whom humility has become second nature. Uddesha 4 culminates with the four samadhis: <i>vinaya-samādhi</i> (stillness through humility), <i>shruta-samādhi</i> (stillness through scripture), <i>tapa-samādhi</i> (stillness through austerity), and <i>ācāra-samādhi</i> (stillness through conduct). Together these four samadhis are the inner equivalents of the outer disciplines covered in earlier chapters.",
        "files": ["dashvaikalik-ch9-translation.md"],
        "stats": [("17+", "Sutras"), ("4", "Uddeshas"), ("4", "Samadhis"), ("Vinaya", "Root of Path")],
        "prev": 8, "next": 10,
    },
    {
        "num": 10, "slug": "ch10",
        "title_en": "Sa-Bhikṣu",
        "title_sk": "સભિક્ષુ",
        "subtitle": "The Tenth and Culminating Adhyayan — Such a One Is a True Monk. Twenty-one verses each ending with the refrain 'sa bhikkhū' — 'such a one is a (true) monk.'",
        "about_title": "The Definition by Living Example",
        "about_p1": "The tenth adhyayan is one of the most beautiful in all Jain literature. It defines the true monk not by abstract characteristics but by twenty-one concrete examples — each verse naming a specific quality, a specific discipline, a specific relationship to the world, and concluding with the unforgettable refrain <i>sa bhikkhū</i> — 'such a one is a (true) monk.'",
        "about_p2": "Each verse paints a portrait: the one steady in celibacy is a true monk; the one restrained in alms is a true monk; the one equanimous in suffering is a true monk; the one who has set down anger, pride, deceit, and greed is a true monk. The chapter culminates the entire Dashvaikalik by gathering, in twenty-one images, every quality the previous nine chapters have built — and showing them all alive in a single human being. To read the chapter is to receive a living mirror of what the path produces.",
        "files": ["dashvaikalik-ch10-translation.md"],
        "stats": [("15+", "Sutras"), ("21", "Verses of Sa-Bhikkhū"), ("Refrain", "sa bhikkhū"), ("Culmination", "of the Sutra")],
        "prev": 9, "next": 11,
    },
    {
        "num": 11, "slug": "chulika1",
        "title_en": "Rativākyā",
        "title_sk": "રતિવાક્યા",
        "subtitle": "The First Chulika — the Speech Against Falling Back. A moving plea for steadfastness using eighteen similes for the sufferings of the householder life and the joys of liberation.",
        "about_title": "The Plea Against Wavering",
        "about_p1": "The two Chulikas (appendices) of the Dashvaikalik are not original to the sutra; tradition holds they were added later when specific spiritual needs arose. The first Chulika, <i>Rativākyā</i> ('the speech of restraint against falling back'), is said to have been composed when a wavering monk was on the verge of returning to householder life.",
        "about_p2": "The Chulika offers eighteen vivid similes — each one a comparison between the apparent comfort of the world and its hidden suffering, or between the apparent austerity of the monastic path and its hidden joy. By the end, the trembling monk is meant to see clearly that what looked like loss in renunciation is actually gain, and what looked like gain in worldly return is actually loss. The text is short but emotionally powerful.",
        "files": ["dashvaikalik-chulika1-translation.md"],
        "stats": [("Chulika", "Appendix"), ("18", "Similes"), ("Rativākyā", "Anti-falling Speech"), ("Restoration", "of Resolve")],
        "prev": 10, "next": 12,
    },
    {
        "num": 12, "slug": "chulika2",
        "title_en": "Vivikta-Caryā",
        "title_sk": "વિવિક્તચર્યા",
        "subtitle": "The Second Chulika — Solitary Conduct. The principles of solitary residence, careful conduct, and the qualities of the truly liberated monk.",
        "about_title": "The Solitary Path",
        "about_p1": "The second Chulika, <i>Vivikta-Caryā</i> ('solitary conduct'), addresses the monk who has progressed beyond the need for community guidance and is ready for the deepest stage of practice — solitary residence and complete inner withdrawal. It teaches the principles of choosing the right place, maintaining unbroken mindfulness, and the qualities of the truly liberated monk.",
        "about_p2": "Where the main ten chapters of the Dashvaikalik form a complete teaching for the new monk, the two Chulikas serve as supplements: the first to restore the wavering, the second to refine the advanced. Together they bring the Dashvaikalik to its final shape — a complete training manual for every stage of the monastic life, from initiation to mastery.",
        "files": ["dashvaikalik-chulika2-translation.md"],
        "stats": [("Chulika", "Appendix"), ("16", "Sutras"), ("Vivikta", "Solitary"), ("Mastery", "Stage of Path")],
        "prev": 11, "next": None,
    },
]


# ---- Markdown parsing ----

def parse_markdown(md_text):
    """Parse a translation markdown file and return list of sutras as dicts."""
    sutras = []
    # Match: "## SUTRA X.Y", "## CHULIKA X.Y", "## CHULIKA-1.5", "## CLOSING SUTRA"
    sutra_re = re.compile(
        r'^##\s+(?:SUTRA\s+(\S+?)|CHULIKA[-\s]+(\S+?)|CLOSING SUTRA)(?:\s+[—-]\s+(.+?))?\s*$',
        re.MULTILINE,
    )
    matches = list(sutra_re.finditer(md_text))
    for i, m in enumerate(matches):
        num = (m.group(1) or m.group(2) or 'closing').strip()
        title = (m.group(3) or '').strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[start:end]
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
    start_re = re.compile(r'^###\s+' + re.escape(start_label) + r'\s*$', re.MULTILINE)
    end_re = re.compile(r'^###\s+' + re.escape(end_label) + r'\s*$', re.MULTILINE)
    m_start = start_re.search(body)
    if not m_start:
        return ''
    m_end = end_re.search(body, m_start.end())
    end = m_end.start() if m_end else len(body)
    return body[m_start.end():end].strip()


def clean_prakrit(text):
    if not text:
        return ''
    text = re.sub(r'॥\s*\d+\.\d+\s*॥', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return html_escape(text)


def clean_text(text):
    if not text:
        return ''
    paras = re.split(r'\n\n+', text)
    cleaned = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        if p.startswith('(See ') or p.startswith('Identical to '):
            continue
        p = re.sub(r'\s+', ' ', p)
        cleaned.append(p)
    if not cleaned:
        return ''
    full = ' '.join(cleaned)
    return md_to_html(full)


def md_to_html(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
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
<title>Dashvaikalik {label}: {title_en} | JainSutra.org</title>
<meta name="description" content="Dashvaikalik Sutra {label} — {title_en} ({title_sk}). {subtitle}"/>
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
<a class="burnished-gradient text-white px-8 py-2.5 rounded-full font-headline uppercase text-[10px] font-bold tracking-[0.2em] hover:opacity-90 transition-all shadow-sm" href="../../../fundamentals/donate-v4.html">Donate</a>
</div>
</nav>
<main class="pt-40">
<section class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-8 md:gap-16 items-center mb-40">
<div class="col-span-12 lg:col-span-5 flex flex-col gap-10 order-2 lg:order-1">
<div class="flex flex-col gap-3">
<span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Dashvaikalik Sutra · {label}</span>
<h1 class="text-7xl md:text-8xl font-headline font-bold text-on-surface leading-tight tracking-tighter">
{title_en} <span class="block text-primary font-normal text-3xl md:text-4xl mt-3">{title_sk}</span>
</h1>
</div>
<h2 class="text-2xl md:text-3xl font-headline text-on-surface-variant leading-tight font-light">{subtitle}</h2>
</div>
<div class="col-span-12 lg:col-span-7 order-1 lg:order-2 flex items-center justify-center">
<div class="w-full max-w-2xl aspect-[4/3] rounded-xl bg-surface-container-low flex items-center justify-center border border-outline-variant/30">
<p class="text-center font-headline text-on-surface/40 text-sm px-8">{label}: {title_en}</p>
</div>
</div>
</section>
<section class="bg-[#f2f1f0] py-24 mesh-bg">
<div class="max-w-screen-xl mx-auto px-6 md:px-12">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
<div class="flex flex-col gap-8">
<div class="flex flex-col gap-3">
<span class="text-primary font-headline italic tracking-[0.2em] text-xs uppercase font-semibold">About This {label_kind}</span>
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
<h3 class="text-3xl md:text-4xl font-headline font-bold text-on-surface leading-tight tracking-tighter">The Sutras of {label}</h3>
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
<a class="hover:text-primary transition-colors" href="dashvaikalik-index.html">Dashvaikalik Index</a>
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
</body>
</html>
'''


SUTRA_CARD_TPL = '''<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{num_id}">
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
        cls = "text-3xl" if len(value) <= 6 else "text-lg"
        out.append(STAT_CARD_TPL.format(value=value, label=label, value_class=cls))
    return '\n'.join(out)


def render_sutras(sutras):
    cards = []
    for s in sutras:
        if not s["prakrit"]:
            if s["title"]:
                cards.append(make_reference_card(s))
            continue
        title_block = ''
        if s["title"]:
            title_block = f'<h4 class="text-xl font-headline font-bold text-on-surface mt-0">{s["title"]}</h4>'
        # Make num safe for ID
        num_id = re.sub(r'[^a-zA-Z0-9.-]', '_', s["num"])
        cards.append(SUTRA_CARD_TPL.format(
            num_id=num_id,
            num=s["num"],
            title_block=title_block,
            prakrit=s["prakrit"],
            english=s["english"] or '<em>(See above for full translation.)</em>',
            commentary=s["commentary"] or '',
            simply_put=s["simply_put"] or '',
        ))
    return '\n'.join(cards)


def make_reference_card(s):
    title = s["title"]
    body = s["english"] or s["commentary"] or s["simply_put"] or 'See referenced sutra.'
    num_id = re.sub(r'[^a-zA-Z0-9.-]', '_', s["num"])
    return f'''<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{num_id}">
<div class="flex items-start gap-6">
<span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{s["num"]}</span>
<div class="space-y-4 flex-1">
<h4 class="text-xl font-headline font-bold text-on-surface mt-0">{title}</h4>
<p class="text-base text-on-surface-variant leading-relaxed">{body}</p>
</div>
</div>
</article>'''


def slug_for(num):
    """Return slug for a chapter number (1-10 -> ch1-ch10, 11 -> chulika1, 12 -> chulika2)."""
    if num <= 10:
        return f"ch{num}"
    elif num == 11:
        return "chulika1"
    elif num == 12:
        return "chulika2"
    return f"ch{num}"


def render_nav_links(prev_num, next_num):
    if prev_num is not None:
        prev_slug = slug_for(prev_num)
        prev_label = f"Chulika {prev_num - 10}" if prev_num > 10 else f"Adhyayan {prev_num}"
        prev_html = f'<a class="nav-button left-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="dashvaikalik-{prev_slug}.html"><span class="text-lg">←</span> {prev_label}</a>'
    else:
        prev_html = '<a class="nav-button left-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="dashvaikalik-index.html"><span class="text-lg">←</span> Index</a>'
    if next_num is not None:
        next_slug = slug_for(next_num)
        next_label = f"Chulika {next_num - 10}" if next_num > 10 else f"Adhyayan {next_num}"
        next_html = f'<a class="nav-button right-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="dashvaikalik-{next_slug}.html">{next_label} <span class="text-lg">→</span></a>'
    else:
        next_html = '<a class="nav-button right-12 flex items-center gap-3 px-4 py-2 rounded-sm font-headline font-bold text-xs tracking-wide" href="dashvaikalik-index.html">Index <span class="text-lg">→</span></a>'
    return prev_html, next_html


def main():
    for chap in CHAPTERS:
        num = chap["num"]
        # Aggregate sutras from all source files
        sutras = []
        for fname in chap["files"]:
            md_path = TRANS / fname
            if not md_path.exists():
                print(f"  WARNING: missing {fname}")
                continue
            md_text = md_path.read_text(encoding='utf-8')
            sutras.extend(parse_markdown(md_text))
        sutras_html = render_sutras(sutras)
        stats_html = render_stats(chap["stats"])
        prev_link, next_link = render_nav_links(chap["prev"], chap["next"])
        # Determine label for hero
        if num <= 10:
            label = f"Adhyayan {num}"
            label_kind = "Adhyayan"
        else:
            label = f"Chulika {num - 10}"
            label_kind = "Chulika"
        page = PAGE_TPL.format(
            label=label,
            label_kind=label_kind,
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
        out_path = ROOT / f"dashvaikalik-{chap['slug']}.html"
        out_path.write_text(page, encoding='utf-8')
        print(f"Wrote {out_path.name}: {len(sutras)} sutras parsed")


if __name__ == '__main__':
    main()
