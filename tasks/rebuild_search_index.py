#!/usr/bin/env python3
"""
Rebuild SEARCH_INDEX in all Uttaradhyana and Vipaak chapter pages
with full sutra-level entries (extracted from the English commentary text).
"""
import re, os, json

BASE = '/Users/thefounder/Projects/active/JainSutra'
UDHY_DIR = f'{BASE}/scripture/Aagama/uttaradhyana'
VIPK_DIR = f'{BASE}/scripture/Aagama/vipaak'

# ─── Chapter metadata (num, filename, display title) ────────────────────────

UTTARADHYANA_CHAPTERS = [
    (1,  "uttaradhyana-ch1.html",  "Uttaradhyana Ch 1 — Vinayashrut"),
    (2,  "uttaradhyana-ch2.html",  "Uttaradhyana Ch 2 — On Endurances"),
    (3,  "uttaradhyana-ch3.html",  "Uttaradhyana Ch 3 — Chaturangiya"),
    (4,  "uttaradhyana-ch4.html",  "Uttaradhyana Ch 4 — Impermanent Life"),
    (5,  "uttaradhyana-ch5.html",  "Uttaradhyana Ch 5 — Two Types of Death"),
    (6,  "uttaradhyana-ch6.html",  "Uttaradhyana Ch 6 — Minor Detachment"),
    (7,  "uttaradhyana-ch7.html",  "Uttaradhyana Ch 7 — The Goat Parable"),
    (8,  "uttaradhyana-ch8.html",  "Uttaradhyana Ch 8 — Story of Kapila"),
    (9,  "uttaradhyana-ch9.html",  "Uttaradhyana Ch 9 — King Nami's Renunciation"),
    (10, "uttaradhyana-ch10.html", "Uttaradhyana Ch 10 — Fallen Leaf"),
    (11, "uttaradhyana-ch11.html", "Uttaradhyana Ch 11 — Veneration of the Learned"),
    (12, "uttaradhyana-ch12.html", "Uttaradhyana Ch 12 — Harikeshiya"),
    (13, "uttaradhyana-ch13.html", "Uttaradhyana Ch 13 — Chitt-Sambhutiya"),
    (14, "uttaradhyana-ch14.html", "Uttaradhyana Ch 14 — Ishukariya"),
    (15, "uttaradhyana-ch15.html", "Uttaradhyana Ch 15 — Sabhikshu"),
    (16, "uttaradhyana-ch16.html", "Uttaradhyana Ch 16 — Foundations of Celibacy"),
    (17, "uttaradhyana-ch17.html", "Uttaradhyana Ch 17 — Marks of the Fallen Monk"),
    (18, "uttaradhyana-ch18.html", "Uttaradhyana Ch 18 — Sanjayiya"),
    (19, "uttaradhyana-ch19.html", "Uttaradhyana Ch 19 — Mrigaputriya"),
    (20, "uttaradhyana-ch20.html", "Uttaradhyana Ch 20 — Mahanirgranthiya"),
    (21, "uttaradhyana-ch21.html", "Uttaradhyana Ch 21 — Samudrapaliya"),
    (22, "uttaradhyana-ch22.html", "Uttaradhyana Ch 22 — Rathanemiya"),
    (23, "uttaradhyana-ch23.html", "Uttaradhyana Ch 23 — Kesi and Gautama"),
    (24, "uttaradhyana-ch24.html", "Uttaradhyana Ch 24 — Mothers of the Teaching"),
    (25, "uttaradhyana-ch25.html", "Uttaradhyana Ch 25 — The Sacrifice"),
    (26, "uttaradhyana-ch26.html", "Uttaradhyana Ch 26 — Monastic Conduct"),
    (27, "uttaradhyana-ch27.html", "Uttaradhyana Ch 27 — The Obstinate Ox"),
    (28, "uttaradhyana-ch28.html", "Uttaradhyana Ch 28 — Path of Liberation"),
    (30, "uttaradhyana-ch30.html", "Uttaradhyana Ch 30 — Path of Austerity"),
    (31, "uttaradhyana-ch31.html", "Uttaradhyana Ch 31 — Rule of Right Conduct"),
    (33, "uttaradhyana-ch33.html", "Uttaradhyana Ch 33 — The Nature of Karma"),
    (34, "uttaradhyana-ch34.html", "Uttaradhyana Ch 34 — Lesya"),
    (35, "uttaradhyana-ch35.html", "Uttaradhyana Ch 35 — Path of the Ascetic"),
    (36, "uttaradhyana-ch36.html", "Uttaradhyana Ch 36 — Jiva-Ajiva Vibhakti"),
]

VIPAAK_CHAPTERS = [
    ("D1",  "vipaak-ch1.html",             "Vipaak — Mrigaputra"),
    ("D2",  "vipaak-ch2.html",             "Vipaak — Ujjhitak"),
    ("D3",  "vipaak-ch3.html",             "Vipaak — Abhagrasena"),
    ("D4",  "vipaak-ch4.html",             "Vipaak — Shakatkumar"),
    ("D5",  "vipaak-ch5.html",             "Vipaak — Bruhaspatidat"),
    ("D6",  "vipaak-ch6.html",             "Vipaak — Nandivardhana"),
    ("D7",  "vipaak-ch7.html",             "Vipaak — Umbaradatt"),
    ("D8",  "vipaak-ch8.html",             "Vipaak — Shaurikadatt"),
    ("D9",  "vipaak-ch9.html",             "Vipaak — Devdatta"),
    ("D10", "vipaak-ch10.html",            "Vipaak — Anjushri"),
    ("S1",  "vipaak-sukhvipak-ch1.html",  "Vipaak — Subahukumar"),
    ("S2",  "vipaak-sukhvipak-ch2.html",  "Vipaak — Bhadranandi"),
    ("S3",  "vipaak-sukhvipak-ch3.html",  "Vipaak — Sujatkumar"),
    ("S4",  "vipaak-sukhvipak-ch4.html",  "Vipaak — Suvasankumar"),
    ("S5",  "vipaak-sukhvipak-ch5.html",  "Vipaak — Jindas"),
    ("S6",  "vipaak-sukhvipak-ch6.html",  "Vipaak — Dhanpati"),
    ("S7",  "vipaak-sukhvipak-ch7.html",  "Vipaak — Mahabhal"),
    ("S8",  "vipaak-sukhvipak-ch8.html",  "Vipaak — Bhadrandiikumar"),
    ("S9",  "vipaak-sukhvipak-ch9.html",  "Vipaak — Mahachandrakumar"),
    ("S10", "vipaak-sukhvipak-ch10.html", "Vipaak — Varadatt"),
]

TATTVARTHA_CHAPTERS = [
    (1,  "tattvartha-ch1-v4.html",  "Tattvartha Ch 1 — Right Faith & Knowledge"),
    (2,  "tattvartha-ch2-v4.html",  "Tattvartha Ch 2 — Category of the Living"),
    (3,  "tattvartha-ch3-v4.html",  "Tattvartha Ch 3 — Lower & Middle World"),
    (4,  "tattvartha-ch4-v4.html",  "Tattvartha Ch 4 — Celestial Beings"),
    (5,  "tattvartha-ch5-v4.html",  "Tattvartha Ch 5 — Non-Living Substances"),
    (6,  "tattvartha-ch6-v4.html",  "Tattvartha Ch 6 — Influx of Karma"),
    (7,  "tattvartha-ch7-v4.html",  "Tattvartha Ch 7 — The Five Vows"),
    (8,  "tattvartha-ch8-v4.html",  "Tattvartha Ch 8 — Bondage of Karma"),
    (9,  "tattvartha-ch9-v4.html",  "Tattvartha Ch 9 — Stoppage and Shedding"),
    (10, "tattvartha-ch10-v4.html", "Tattvartha Ch 10 — Liberation"),
]

# ─── Sutra extraction ────────────────────────────────────────────────────────

def clean_text(html):
    text = re.sub(r'<[^>]+>', '', html)
    text = re.sub(r'&ldquo;|&rdquo;', '"', text)
    text = re.sub(r'&lsquo;|&rsquo;', "'", text)
    text = re.sub(r'&mdash;', '—', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_sutras_from_file(filepath, chapter_num):
    """Extract sutra entries: list of {id, num, title}"""
    txt = open(filepath).read()
    articles = re.findall(
        r'<article[^>]+id="(sutra-[\d-]+|gatha-[\d-]+)"[^>]*>(.*?)</article>',
        txt, re.DOTALL
    )
    results = []
    for sid, body in articles:
        # Get the display number: strip chapter prefix if present
        # "sutra-1" -> "1", "sutra-16-1" -> "1", "sutra-3-1" -> "1", "gatha-16-1" -> "g1"
        num_match = re.match(r'(sutra|gatha)-(\d+)-(\d+)$', sid)
        if num_match:
            suffix = 'g' if num_match.group(1) == 'gatha' else ''
            display_num = f"{chapter_num}.{suffix}{num_match.group(3)}"
        else:
            plain_match = re.match(r'sutra-(\d+)$', sid)
            if plain_match:
                display_num = f"{chapter_num}.{plain_match.group(1)}"
            else:
                display_num = sid

        # Get English commentary
        m = re.search(r'<p class="text-base[^"]*"[^>]*>(.*?)</p>', body, re.DOTALL)
        if m:
            text = clean_text(m.group(1))[:120]
        else:
            m2 = re.search(r'<p(?![^>]*sutra-sanskrit)[^>]*>(.*?)</p>', body, re.DOTALL)
            text = clean_text(m2.group(1))[:100] if m2 else ''

        if text:
            results.append({"id": sid, "num": display_num, "title": text})

    return results

# ─── Build SEARCH_INDEX entries per chapter ──────────────────────────────────

def build_chapter_entry(file_path, prefix, fname, chnum, title, src_dir):
    sutras = extract_sutras_from_file(file_path, chnum)
    # Always include a chapter-level "entry" as first sutra so title is searchable
    chapter_sutra = {"id": "hero", "num": str(chnum), "title": title.split(' — ', 1)[-1] if ' — ' in title else title}
    all_sutras = [chapter_sutra] + sutras
    return {"file": prefix + fname, "num": str(chnum), "title": title, "sutras": all_sutras}

def build_full_index(book_type):
    entries = []

    # Uttaradhyana
    udhy_prefix = "" if book_type == "uttaradhyana" else "../uttaradhyana/"
    for num, fname, title in UTTARADHYANA_CHAPTERS:
        fp = os.path.join(UDHY_DIR, fname)
        if os.path.exists(fp):
            e = build_chapter_entry(fp, udhy_prefix, fname, f"U{num}", title, UDHY_DIR)
            entries.append(e)

    # Vipaak
    vipk_prefix = "" if book_type == "vipaak" else "../vipaak/"
    for num, fname, title in VIPAAK_CHAPTERS:
        fp = os.path.join(VIPK_DIR, fname)
        if os.path.exists(fp):
            e = build_chapter_entry(fp, vipk_prefix, fname, num, title, VIPK_DIR)
            entries.append(e)

    # Tattvartha (same relative path from both dirs)
    tatt_prefix = "../../tattvartha/"
    for num, fname, title in TATTVARTHA_CHAPTERS:
        entries.append({
            "file": tatt_prefix + fname,
            "num": f"T{num}",
            "title": title,
            "sutras": [{"id": "hero", "num": f"T{num}", "title": title.split(' — ', 1)[-1]}]
        })

    return json.dumps(entries, ensure_ascii=False, separators=(',', ':'))

# ─── Inject into files ───────────────────────────────────────────────────────

def update_search_index(filepath, index_json):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace existing SEARCH_INDEX
    new_content = re.sub(
        r'var SEARCH_INDEX = \[.*?\];',
        f'var SEARCH_INDEX = {index_json};',
        content,
        count=1,
        flags=re.DOTALL
    )

    if new_content == content:
        print(f"  WARNING: SEARCH_INDEX not found in {os.path.basename(filepath)}")
        return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  ✓ {os.path.basename(filepath)}")

def main():
    print("Building Uttaradhyana SEARCH_INDEX...")
    udhy_index = build_full_index('uttaradhyana')
    udhy_size = len(udhy_index) // 1024
    print(f"  Index size: ~{udhy_size}KB")

    print("\nBuilding Vipaak SEARCH_INDEX...")
    vipk_index = build_full_index('vipaak')
    vipk_size = len(vipk_index) // 1024
    print(f"  Index size: ~{vipk_size}KB")

    print("\n=== Updating Uttaradhyana chapter files ===")
    udhy_files = sorted([f for f in os.listdir(UDHY_DIR)
                         if f.startswith('uttaradhyana-ch') and f.endswith('.html')])
    for fname in udhy_files:
        update_search_index(os.path.join(UDHY_DIR, fname), udhy_index)

    print("\n=== Updating Vipaak chapter files ===")
    vipk_files = sorted([f for f in os.listdir(VIPK_DIR)
                         if (f.startswith('vipaak-ch') or f.startswith('vipaak-sukhvipak-ch'))
                         and f.endswith('.html')])
    for fname in vipk_files:
        update_search_index(os.path.join(VIPK_DIR, fname), vipk_index)

    print("\nDone.")

if __name__ == '__main__':
    main()
