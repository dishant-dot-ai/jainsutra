#!/usr/bin/env python3
"""
Fix nav paths and add cross-book search to all Uttaradhyana and Vipaak chapter pages.
"""
import re, os, json

BASE = '/Users/thefounder/Projects/active/JainAwaken'
UDHY_DIR = f'{BASE}/scripture/Aagama/uttaradhyana'
VIPK_DIR = f'{BASE}/scripture/Aagama/vipaak'
TATT_DIR = f'{BASE}/scripture/tattvartha'

# ─── Chapter data ───────────────────────────────────────────────────────────

UTTARADHYANA_CHAPTERS = [
    (1,  "uttaradhyana-ch1.html",  "Vinayashrut — On Discipline"),
    (2,  "uttaradhyana-ch2.html",  "On Endurances"),
    (3,  "uttaradhyana-ch3.html",  "Chaturangiya — Four Supreme Rarities"),
    (4,  "uttaradhyana-ch4.html",  "Impermanent Life"),
    (5,  "uttaradhyana-ch5.html",  "On the Two Types of Death"),
    (6,  "uttaradhyana-ch6.html",  "The Minor Detachment"),
    (7,  "uttaradhyana-ch7.html",  "The Goat Parable"),
    (8,  "uttaradhyana-ch8.html",  "Story of Kapila"),
    (9,  "uttaradhyana-ch9.html",  "The Renunciation of King Nami"),
    (10, "uttaradhyana-ch10.html", "Fallen Leaf"),
    (11, "uttaradhyana-ch11.html", "Veneration of the Greatly Learned"),
    (12, "uttaradhyana-ch12.html", "Harikeshiya"),
    (13, "uttaradhyana-ch13.html", "Chitt-Sambhutiya"),
    (14, "uttaradhyana-ch14.html", "Ishukariya"),
    (15, "uttaradhyana-ch15.html", "Sabhikshu"),
    (16, "uttaradhyana-ch16.html", "Foundations of Celibacy"),
    (17, "uttaradhyana-ch17.html", "The Marks of the Fallen Monk"),
    (18, "uttaradhyana-ch18.html", "Sanjayiya"),
    (19, "uttaradhyana-ch19.html", "Mrigaputriya"),
    (20, "uttaradhyana-ch20.html", "Mahanirgranthiya"),
    (21, "uttaradhyana-ch21.html", "Samudrapaliya"),
    (22, "uttaradhyana-ch22.html", "Rathanemiya"),
    (23, "uttaradhyana-ch23.html", "The Dialogue of Kesi and Gautama"),
    (24, "uttaradhyana-ch24.html", "Mothers of the Teaching"),
    (25, "uttaradhyana-ch25.html", "The Sacrifice — Yajniya"),
    (26, "uttaradhyana-ch26.html", "Monastic Conduct"),
    (27, "uttaradhyana-ch27.html", "The Obstinate Ox"),
    (28, "uttaradhyana-ch28.html", "Movement on the Path of Liberation"),
    (30, "uttaradhyana-ch30.html", "The Path of Austerity"),
    (31, "uttaradhyana-ch31.html", "Rule of Right Conduct"),
    (33, "uttaradhyana-ch33.html", "The Nature of Karma"),
    (34, "uttaradhyana-ch34.html", "Lesya — Soul Colorations"),
    (35, "uttaradhyana-ch35.html", "The Path of the Homeless Ascetic"),
    (36, "uttaradhyana-ch36.html", "Jiva-Ajiva Vibhakti"),
]

VIPAAK_CHAPTERS = [
    ("D1",  "vipaak-ch1.html",             "Duhkha Vipaak Ch 1 — Mrigaputra"),
    ("D2",  "vipaak-ch2.html",             "Duhkha Vipaak Ch 2 — Ujjhitak"),
    ("D3",  "vipaak-ch3.html",             "Duhkha Vipaak Ch 3 — Abhagrasena"),
    ("D4",  "vipaak-ch4.html",             "Duhkha Vipaak Ch 4 — Shakatkumar"),
    ("D5",  "vipaak-ch5.html",             "Duhkha Vipaak Ch 5 — Bruhaspatidat"),
    ("D6",  "vipaak-ch6.html",             "Duhkha Vipaak Ch 6 — Nandivardhana"),
    ("D7",  "vipaak-ch7.html",             "Duhkha Vipaak Ch 7 — Umbaradatt"),
    ("D8",  "vipaak-ch8.html",             "Duhkha Vipaak Ch 8 — Shaurikadatt"),
    ("D9",  "vipaak-ch9.html",             "Duhkha Vipaak Ch 9 — Devdatta"),
    ("D10", "vipaak-ch10.html",            "Duhkha Vipaak Ch 10 — Anjushri"),
    ("S1",  "vipaak-sukhvipak-ch1.html",  "Sukha Vipaak Ch 1 — Subahukumar"),
    ("S2",  "vipaak-sukhvipak-ch2.html",  "Sukha Vipaak Ch 2 — Bhadranandi"),
    ("S3",  "vipaak-sukhvipak-ch3.html",  "Sukha Vipaak Ch 3 — Sujatkumar"),
    ("S4",  "vipaak-sukhvipak-ch4.html",  "Sukha Vipaak Ch 4 — Suvasankumar"),
    ("S5",  "vipaak-sukhvipak-ch5.html",  "Sukha Vipaak Ch 5 — Jindas"),
    ("S6",  "vipaak-sukhvipak-ch6.html",  "Sukha Vipaak Ch 6 — Dhanpati"),
    ("S7",  "vipaak-sukhvipak-ch7.html",  "Sukha Vipaak Ch 7 — Mahabhal"),
    ("S8",  "vipaak-sukhvipak-ch8.html",  "Sukha Vipaak Ch 8 — Bhadrandiikumar"),
    ("S9",  "vipaak-sukhvipak-ch9.html",  "Sukha Vipaak Ch 9 — Mahachandrakumar"),
    ("S10", "vipaak-sukhvipak-ch10.html", "Sukha Vipaak Ch 10 — Varadatt"),
]

TATTVARTHA_CHAPTERS = [
    (1,  "tattvartha-ch1-v4.html",  "Right Faith & Knowledge"),
    (2,  "tattvartha-ch2-v4.html",  "Category of the Living"),
    (3,  "tattvartha-ch3-v4.html",  "The Lower World & the Middle World"),
    (4,  "tattvartha-ch4-v4.html",  "The Celestial Beings"),
    (5,  "tattvartha-ch5-v4.html",  "The Non-Living Substances"),
    (6,  "tattvartha-ch6-v4.html",  "Influx of Karma"),
    (7,  "tattvartha-ch7-v4.html",  "The Five Vows"),
    (8,  "tattvartha-ch8-v4.html",  "Bondage of Karma"),
    (9,  "tattvartha-ch9-v4.html",  "Stoppage and Shedding"),
    (10, "tattvartha-ch10-v4.html", "Liberation"),
]

def make_search_index(book_type):
    """
    Build SEARCH_INDEX array where file paths are relative to the book's directory.
    book_type: 'uttaradhyana' or 'vipaak'
    """
    entries = []

    # Uttaradhyana chapters
    udhy_prefix = "" if book_type == "uttaradhyana" else "../uttaradhyana/"
    for num, fname, title in UTTARADHYANA_CHAPTERS:
        entries.append({
            "file": udhy_prefix + fname,
            "num": f"U{num}",
            "title": f"Uttaradhyana Ch {num} — {title}",
            "sutras": [{"id": "hero", "num": f"U{num}", "title": title}]
        })

    # Vipaak chapters
    vipk_prefix = "" if book_type == "vipaak" else "../vipaak/"
    for num, fname, title in VIPAAK_CHAPTERS:
        entries.append({
            "file": vipk_prefix + fname,
            "num": num,
            "title": title,
            "sutras": [{"id": "hero", "num": num, "title": title}]
        })

    # Tattvartha chapters (same relative path from both Uttaradhyana and Vipaak dirs)
    tatt_prefix = "../../tattvartha/"
    for num, fname, title in TATTVARTHA_CHAPTERS:
        entries.append({
            "file": tatt_prefix + fname,
            "num": f"T{num}",
            "title": f"Tattvartha Ch {num} — {title}",
            "sutras": [{"id": "hero", "num": f"T{num}", "title": title}]
        })

    return json.dumps(entries, ensure_ascii=False, separators=(',', ':'))

SEARCH_CSS = """
    #search-dropdown { position:absolute; top:calc(100% + 8px); left:0; min-width:400px; max-width:520px; background:#fff; border-radius:8px; box-shadow:0 8px 32px rgba(0,0,0,0.13); border:1px solid rgba(201,168,76,0.25); overflow:hidden; display:none; z-index:1000; max-height:420px; overflow-y:auto; }
    .search-section-label { padding:8px 16px 4px; font-family:'Inter',sans-serif; font-size:9px; text-transform:uppercase; letter-spacing:0.12em; color:#C9A84C; font-weight:700; border-top:1px solid #f0ebe3; }
    .search-section-label:first-child { border-top:none; }
    .search-result-item { display:flex; align-items:baseline; gap:10px; padding:9px 16px; text-decoration:none; cursor:pointer; border:none; background:none; width:100%; text-align:left; transition:background 0.15s; }
    .search-result-item:hover { background:#fef9f1; }
    .search-result-num { font-family:'Noto Serif',serif; font-size:11px; color:#C9A84C; font-weight:700; flex-shrink:0; }
    .search-result-title { font-family:'Inter',sans-serif; font-size:12px; color:#1d1c17; line-height:1.4; }
    .search-no-results { padding:16px; color:#7e7665; font-family:'Inter',sans-serif; font-size:12px; text-align:center; }"""

SEARCH_INPUT_HTML = """<div class="relative group hidden lg:block">
                <span class="nav-search-icon material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-sm transition-colors duration-500">search</span>
                <input id="search-input" class="nav-search bg-surface-container-low border-none rounded-full py-2 pl-10 pr-6 text-sm font-label placeholder:italic transition-all duration-300 w-48 focus:w-72 focus:ring-1 focus:ring-primary/20" placeholder="Explore Wisdom..." type="text"/>
              </div>
              """

INIT_SEARCH_JS = """
<script>
(function () {
  var SEARCH_INDEX = {INDEX_PLACEHOLDER};

  function initSearch() {
    var input = document.getElementById("search-input");
    if (!input) return;
    var wrapper = input.closest(".relative");
    if (!wrapper) return;
    var dropdown = document.getElementById("search-dropdown");
    if (!dropdown) {
      dropdown = document.createElement("div");
      dropdown.id = "search-dropdown";
      wrapper.appendChild(dropdown);
    }
    var currentFile = (location.pathname.split("/").pop() || location.href.split("/").pop() || "").replace(/[?#].*$/, "");
    function highlight(text, query) {
      if (!query) return text;
      return text.replace(new RegExp("(" + query.replace(/[.*+?^${}()|[\\]\\\\]/g, "\\\\$&") + ")", "gi"), "<mark style='background:#fff3c4;color:inherit;border-radius:2px;'>$1</mark>");
    }
    function search(query) {
      if (query.length < 2) { dropdown.style.display = "none"; return; }
      var q = query.toLowerCase();
      var currentMatches = [];
      var otherMatches = [];
      SEARCH_INDEX.forEach(function (chapter) {
        var matches = chapter.sutras.filter(function (s) {
          return s.title.toLowerCase().includes(q) || String(s.num).toLowerCase().includes(q);
        }).slice(0, 4);
        if (!matches.length) return;
        var isCurrent = chapter.file === currentFile;
        (isCurrent ? currentMatches : otherMatches).push({ chapter: chapter, matches: matches });
      });
      var html = "";
      if (currentMatches.length) {
        html += "<div class='search-section-label'>This Chapter</div>";
        currentMatches.forEach(function (r) {
          r.matches.forEach(function (s) {
            html += "<button class='search-result-item' data-local='true' data-id='" + s.id + "'><span class='search-result-num'>" + s.num + "</span><span class='search-result-title'>" + highlight(s.title, query) + "</span></button>";
          });
        });
      }
      otherMatches.slice(0, 8).forEach(function (r) {
        html += "<div class='search-section-label'>" + r.chapter.title + "</div>";
        r.matches.forEach(function (s) {
          var link = r.chapter.file;
          if (s.id && s.id !== "hero") link += "#" + s.id;
          html += "<a class='search-result-item' href='" + link + "'><span class='search-result-num'>" + s.num + "</span><span class='search-result-title'>" + highlight(s.title, query) + "</span></a>";
        });
      });
      if (!html) html = "<div class='search-no-results'>No results for &ldquo;" + query + "&rdquo;</div>";
      dropdown.innerHTML = html;
      dropdown.style.display = "block";
      dropdown.querySelectorAll("[data-local='true']").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var el = document.getElementById(this.dataset.id);
          if (el) { el.scrollIntoView({ behavior: "smooth", block: "center" }); el.style.outline = "2px solid #C9A84C"; el.style.outlineOffset = "4px"; setTimeout(function () { el.style.outline = ""; el.style.outlineOffset = ""; }, 2000); }
          dropdown.style.display = "none";
          input.value = "";
        });
      });
    }
    input.addEventListener("input", function () { search(this.value.trim()); });
    input.addEventListener("keydown", function (e) { if (e.key === "Escape") { dropdown.style.display = "none"; input.value = ""; } });
    document.addEventListener("click", function (e) { if (!wrapper.contains(e.target)) dropdown.style.display = "none"; });
  }
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", initSearch) : initSearch();
})();
</script>"""

def process_file(filepath, book_type):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    filename = os.path.basename(filepath)
    changed = []

    # 1. Fix broken nav paths (Uttaradhyana only)
    if book_type == 'uttaradhyana' and '../../../../' in content:
        # Fix the main nav paths but not footer/other instances
        # Replace all ../../../../ occurrences in the nav area
        content = content.replace('../../../../index-v4.html', '../../../index-v4.html')
        content = content.replace('../../../../fundamentals/', '../../../fundamentals/')
        changed.append("fixed nav paths (../../../../ -> ../../../)")

    # 2. Add search CSS before </style> (only if not already present)
    if '#search-dropdown' not in content:
        content = content.replace('</style>', SEARCH_CSS + '\n</style>', 1)
        changed.append("added search CSS")

    # 3. Add search input to nav (before Donate button)
    if 'search-input' not in content:
        # Find the Donate button and insert search input before it
        donate_pattern = r'(<div class="flex items-center gap-8">)\s*\n(\s*<a href="[^"]*donate[^"]*")'
        replacement = r'\1\n              ' + SEARCH_INPUT_HTML.strip() + r'\n\2'
        new_content = re.sub(donate_pattern, replacement, content, count=1)
        if new_content == content:
            # Alternative pattern (no gap-8 class)
            donate_pattern2 = r'(<div[^>]*flex[^>]*items-center[^>]*>)\s*\n(\s*<a[^>]*donate[^>]*>)'
            new_content = re.sub(donate_pattern2, replacement, content, count=1)
        if new_content != content:
            content = new_content
            changed.append("added search input")
        else:
            print(f"  WARNING: Could not find donate button to insert search in {filename}")

    # 4. Add search JS before </body> (only if not already present)
    if 'initSearch' not in content:
        index_json = make_search_index(book_type)
        js = INIT_SEARCH_JS.replace('{INDEX_PLACEHOLDER}', index_json)
        content = content.replace('</body>', js + '\n</body>', 1)
        changed.append("added search JS")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {filename}: {', '.join(changed)}")
    else:
        print(f"  - {filename}: no changes needed")

def main():
    print("=== Processing Uttaradhyana chapters ===")
    udhy_files = sorted([f for f in os.listdir(UDHY_DIR)
                         if f.startswith('uttaradhyana-ch') and f.endswith('.html')])
    for fname in udhy_files:
        process_file(os.path.join(UDHY_DIR, fname), 'uttaradhyana')

    print("\n=== Processing Vipaak chapters ===")
    vipk_files = sorted([f for f in os.listdir(VIPK_DIR)
                         if (f.startswith('vipaak-ch') or f.startswith('vipaak-sukhvipak-ch'))
                         and f.endswith('.html')])
    for fname in vipk_files:
        process_file(os.path.join(VIPK_DIR, fname), 'vipaak')

    print("\nDone.")

if __name__ == '__main__':
    main()
