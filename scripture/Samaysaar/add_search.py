#!/usr/bin/env python3
"""Add Samaysaar-only search functionality to all Samaysaar HTML files.
Follows the Uttaradhyana search pattern exactly."""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, Tag

BASE = Path('/Users/thefounder/Projects/active/JainSutra/scripture/Samaysaar')

FILES = [
    'samaysaar-index.html',
    'samaysaar-ch1.html',
    'samaysaar-poorvarang.html',
    'samaysaar-ch2.html',
    'samaysaar-ch3.html',
    'samaysaar-ch4.html',
    'samaysaar-ch5.html',
    'samaysaar-ch6.html',
    'samaysaar-ch7.html',
    'samaysaar-ch8.html',
    'samaysaar-ch9.html',
    'samaysaar-ch10.html',
    'samaysaar-ch11.html',
]

FILE_NUMS = {
    'samaysaar-index.html':    'Idx',
    'samaysaar-ch1.html':      'P',
    'samaysaar-poorvarang.html': 'P·Full',
    'samaysaar-ch2.html':      'A1',
    'samaysaar-ch3.html':      'A2',
    'samaysaar-ch4.html':      'A3',
    'samaysaar-ch5.html':      'A4',
    'samaysaar-ch6.html':      'A5',
    'samaysaar-ch7.html':      'A6',
    'samaysaar-ch8.html':      'A7',
    'samaysaar-ch9.html':      'A8',
    'samaysaar-ch10.html':     'A9',
    'samaysaar-ch11.html':     'Concl',
}

SEARCH_CSS = """
    #search-dropdown { position:absolute; top:calc(100% + 8px); left:0; min-width:400px; max-width:520px; background:#fff; border-radius:8px; box-shadow:0 8px 32px rgba(0,0,0,0.13); border:1px solid rgba(201,168,76,0.25); overflow:hidden; display:none; z-index:1000; max-height:420px; overflow-y:auto; }
    .search-section-label { padding:8px 16px 4px; font-family:'Inter',sans-serif; font-size:9px; text-transform:uppercase; letter-spacing:0.12em; color:#C9A84C; font-weight:700; border-top:1px solid #f0ebe3; }
    .search-section-label:first-child { border-top:none; }
    .search-result-item { display:flex; align-items:baseline; gap:10px; padding:9px 16px; text-decoration:none; cursor:pointer; border:none; background:none; width:100%; text-align:left; transition:background 0.15s; }
    .search-result-item:hover { background:#fef9f1; }
    .search-result-num { font-family:'Noto Serif',serif; font-size:11px; color:#C9A84C; font-weight:700; flex-shrink:0; }
    .search-result-title { font-family:'Inter',sans-serif; font-size:12px; color:#1d1c17; line-height:1.4; }
    .search-no-results { padding:16px; color:#7e7665; font-family:'Inter',sans-serif; font-size:12px; text-align:center; }
"""

# Raw string so JS backslashes are not mangled by Python
JS_BODY = r"""<script>
(function () {
  var SEARCH_INDEX = %%SEARCH_INDEX%%;
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
      return text.replace(new RegExp("(" + query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi"), "<mark style='background:#fff3c4;color:inherit;border-radius:2px;'>$1</mark>");
    }
    function search(query) {
      if (query.length < 2) { dropdown.style.display = "none"; return; }
      var q = query.toLowerCase();
      var currentMatches = [];
      var otherMatches = [];
      SEARCH_INDEX.forEach(function (chapter) {
        var matches = (chapter.sutras || []).filter(function (s) {
          return (s.title && s.title.toLowerCase().includes(q)) ||
                 (s.num && String(s.num).toLowerCase().includes(q)) ||
                 (chapter.title && chapter.title.toLowerCase().includes(q));
        }).slice(0, 5);
        if (!matches.length) return;
        var isCurrent = chapter.file === currentFile;
        (isCurrent ? currentMatches : otherMatches).push({ chapter: chapter, matches: matches });
      });
      var html = "";
      if (currentMatches.length) {
        html += "<div class='search-section-label'>This Chapter</div>";
        currentMatches.forEach(function (r) {
          r.matches.forEach(function (s) {
            if (!s.id) return;
            html += "<button class='search-result-item' data-local='true' data-id='" + s.id + "'>"
                  + "<span class='search-result-num'>" + s.num + "</span>"
                  + "<span class='search-result-title'>" + highlight(s.title, query) + "</span></button>";
          });
        });
      }
      otherMatches.slice(0, 8).forEach(function (r) {
        html += "<div class='search-section-label'>" + r.chapter.title + "</div>";
        r.matches.forEach(function (s) {
          var link = r.chapter.file + (s.id ? "#" + s.id : "");
          html += "<a class='search-result-item' href='" + link + "'>"
                + "<span class='search-result-num'>" + s.num + "</span>"
                + "<span class='search-result-title'>" + highlight(s.title, query) + "</span></a>";
        });
      });
      if (!html) html = "<div class='search-no-results'>No results for &ldquo;" + query + "&rdquo;</div>";
      dropdown.innerHTML = html;
      dropdown.style.display = "block";
      dropdown.querySelectorAll("[data-local='true']").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var el = document.getElementById(this.dataset.id);
          if (el) {
            el.scrollIntoView({ behavior: "smooth", block: "center" });
            el.style.outline = "2px solid #C9A84C";
            el.style.outlineOffset = "4px";
            setTimeout(function () { el.style.outline = ""; el.style.outlineOffset = ""; }, 2000);
          }
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


def clean(tag):
    return re.sub(r'\s+', ' ', tag.get_text()).strip()


def gnum(card_id):
    """Convert card id to display gatha number."""
    if not card_id or card_id == 'hero':
        return '§'
    m = re.match(r'sutra-(.+)', card_id)
    if m:
        return f'G{m.group(1)}'
    m = re.match(r'g(\d+)', card_id)
    if m:
        return f'G{m.group(1)}'
    if 'kalasa' in card_id:
        n = card_id.replace('kalasa-', '')
        return f'K·{n}'
    return card_id


def snum(text):
    """Compact section number from divider text."""
    m = re.search(r'Part\s+(\d+)', text)
    if m:
        return f'Part {m.group(1)}'
    m = re.search(r'Section\s+(\d+)', text)
    if m:
        return f'Sec {m.group(1)}'
    return '§'


def cls_str(elem):
    return ' '.join(elem.get('class', []))


def extract_index_sutras(soup):
    entries = [{'id': 'hero', 'num': 'Idx', 'title': 'Samaysaar — The Essence of the Self · All Chapters'}]
    for a in soup.find_all('a', class_='index-card'):
        h3 = a.find('h3')
        if not h3:
            continue
        spans = a.find_all('span')
        num = ''
        for sp in spans:
            sp_cls = cls_str(sp)
            if 'tracking-widest' in sp_cls or 'uppercase' in sp_cls:
                num = clean(sp)
                break
        title = clean(h3)
        desc_ps = [p for p in a.find_all('p') if 'text-on-surface-variant' in cls_str(p)]
        if desc_ps:
            title = f'{title} — {clean(desc_ps[0])[:55]}'
        entries.append({'id': '', 'num': num, 'title': title})
    return entries


def extract_chapter_sutras(soup):
    entries = []
    main = soup.find('main') or soup.find('body') or soup

    pending_div_text = None
    pending_div_num = None

    for elem in main.find_all(True, recursive=True):
        if not isinstance(elem, Tag):
            continue
        ec = cls_str(elem)

        if 'section-divider' in ec and elem.name == 'div':
            span = elem.find('span')
            if span:
                text = clean(span)
                if text:
                    if pending_div_text:
                        # Orphan divider (no sutra followed)
                        entries.append({'id': '', 'num': pending_div_num, 'title': pending_div_text})
                    pending_div_text = text
                    pending_div_num = snum(text)

        elif 'sutra-card' in ec and elem.name == 'article':
            card_id = elem.get('id', '')
            if not card_id:
                continue

            g = gnum(card_id)

            # Flush pending section divider → anchor it to this card
            if pending_div_text:
                entries.append({'id': card_id, 'num': pending_div_num, 'title': pending_div_text})
                pending_div_text = None
                pending_div_num = None

            # Find translation paragraph
            trans_p = None
            for p in elem.find_all('p'):
                pc = cls_str(p)
                if 'text-lg' in pc and 'font-semibold' in pc:
                    trans_p = p
                    break
            if not trans_p:
                for p in elem.find_all('p'):
                    pc = cls_str(p)
                    if 'leading-relaxed' in pc and 'italic' not in pc and 'sutra-sanskrit' not in pc:
                        trans_p = p
                        break

            trans = clean(trans_p)[:85] if trans_p else f'Gatha {g}'
            entries.append({'id': card_id, 'num': g, 'title': trans})

    if pending_div_text:
        entries.append({'id': '', 'num': pending_div_num, 'title': pending_div_text})

    return entries


def build_search_index():
    index = []
    for filename in FILES:
        fp = BASE / filename
        if not fp.exists():
            print(f'  MISSING: {filename}')
            continue
        html = fp.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        title_tag = soup.find('title')
        title = title_tag.get_text(strip=True).replace(' | JainSutra.org', '') if title_tag else filename

        if filename == 'samaysaar-index.html':
            sutras = extract_index_sutras(soup)
        else:
            sutras = extract_chapter_sutras(soup)

        index.append({
            'file': filename,
            'num': FILE_NUMS.get(filename, '?'),
            'title': title,
            'sutras': sutras,
        })
        print(f'  {filename}: {len(sutras)} entries')
    return index


def build_js(search_index):
    idx_json = json.dumps(search_index, ensure_ascii=False, separators=(',', ':'))
    return JS_BODY.replace('%%SEARCH_INDEX%%', idx_json)


def fix_index_nav(html):
    """Add id="search-input" and dropdown div to index file nav."""
    old = ('<input class="bg-surface-container-low border-none rounded-full py-2 pl-10 pr-6 '
           'text-sm font-label placeholder:italic transition-all duration-300 w-48 focus:w-72 '
           'focus:ring-1 focus:ring-primary/20" placeholder="Explore Wisdom..." type="text"/>')
    new = ('<input id="search-input" class="bg-surface-container-low border-none rounded-full py-2 pl-10 pr-6 '
           'text-sm font-label placeholder:italic transition-all duration-300 w-48 focus:w-72 '
           'focus:ring-1 focus:ring-primary/20" placeholder="Explore Wisdom..." type="text"/>\n'
           '<div id="search-dropdown"></div>')
    if old in html:
        html = html.replace(old, new)
        print('  → Fixed index nav search input')
    return html


def add_search_css(html):
    if '#search-dropdown' in html:
        return html
    updated = html.replace('</style>', SEARCH_CSS + '</style>', 1)
    if updated != html:
        print('  → Added search CSS')
    return updated


def remove_existing_search_js(html):
    """Remove any previously injected search JS block."""
    pattern = r'\n?<script>\n\(function \(\) \{[\s\S]*?SEARCH_INDEX[\s\S]*?\}\)\(\);\n</script>'
    cleaned, n = re.subn(pattern, '', html)
    if n:
        print(f'  → Removed {n} old search block(s)')
    return cleaned


def inject_js(html, js):
    if '</body>' in html:
        return html.replace('</body>', js + '\n</body>', 1)
    return html + '\n' + js


def main():
    print('=== Building SEARCH_INDEX ===')
    search_index = build_search_index()
    total = sum(len(c['sutras']) for c in search_index)
    print(f'\nTotal search entries: {total}')

    print('\n=== Building JS ===')
    js_block = build_js(search_index)
    print(f'JS block size: {len(js_block):,} chars')

    print(f'\n=== Injecting into {len(FILES)} files ===')
    for filename in FILES:
        fp = BASE / filename
        if not fp.exists():
            print(f'  SKIP (missing): {filename}')
            continue

        print(f'\n{filename}:')
        html = fp.read_text(encoding='utf-8')

        if filename == 'samaysaar-index.html':
            html = fix_index_nav(html)
            html = add_search_css(html)

        html = remove_existing_search_js(html)
        html = inject_js(html, js_block)

        fp.write_text(html, encoding='utf-8')
        print(f'  ✓ Saved')

    print('\n=== Done ===')


if __name__ == '__main__':
    main()
