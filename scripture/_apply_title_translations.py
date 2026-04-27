#!/usr/bin/env python3
"""
Apply concise English + Hindi (Devanagari) titles to chapter heroes.

For each file, updates:
  - H1 inner text (the English title before the inline span)
  - The (...) Hindi text inside the inline text-primary span
  - The H2 quoted content (the chapter prefix's italic part) to match the new English title

Idempotent — second run is a no-op (the OLD strings will no longer match).
"""
from __future__ import annotations
import re
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path("/Users/thefounder/Projects/active/JainSutra/scripture")

# (old_english, new_english, new_hindi)
TRANSLATIONS: Dict[str, Tuple[str, str, str]] = {
    # ========= UPASAKDASHANG (drop redundant "Lay Follower / Shramanopasak" prefix) =========
    "Aagama/upasakdashang/upasakdashang-ch3.html": (
        "Lay Follower Chunilipita", "Chulanipita", "चुलनीपिता",
    ),
    "Aagama/upasakdashang/upasakdashang-ch4.html": (
        "Lay Follower Suradeva", "Suradeva", "सुरादेव",
    ),
    "Aagama/upasakdashang/upasakdashang-ch5.html": (
        "Lay Follower Chullashatak", "Chullashatak", "चुल्लशतक",
    ),
    "Aagama/upasakdashang/upasakdashang-ch6.html": (
        "Lay Follower Kundkolik", "Kundkolik", "कुण्डकोलिक",
    ),
    "Aagama/upasakdashang/upasakdashang-ch9.html": (
        "Shramanopasak Nandinipita", "Nandinipita", "नंदिनीपिता",
    ),
    "Aagama/upasakdashang/upasakdashang-ch10.html": (
        "Shramanopasak Salihipita", "Salihipita", "सालिहीपिता",
    ),

    # ========= UTTARADHYANA (Gujarati → Hindi; mostly already concise) =========
    "Aagama/uttaradhyana/uttaradhyana-ch3.html": (
        "Four Supreme Rarities", "Four Supreme Rarities", "चातुरंगीय",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch14.html": (
        "Arrowmaker", "The Arrowmaker", "इषुकारीय",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch15.html": (
        "Worthy Monk", "The Worthy Monk", "सभिक्षु",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch16.html": (
        "Foundations of Celibacy", "Foundations of Celibacy", "ब्रह्मचर्य समाधिस्थान",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch17.html": (
        "Fallen Monk", "The Fallen Monk", "पापश्रमणीय",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch24.html": (
        "Mothers of the Teaching", "Mothers of the Teaching", "प्रवचन माता",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch29.html": (
        "Right Effort", "Right Effort", "सम्यक् पराक्रम",
    ),
    "Aagama/uttaradhyana/uttaradhyana-ch36.html": (
        "Classification of Living &amp; Non-Living", "Living & Non-Living", "जीव-अजीव विभक्ति",
    ),

    # ========= SUTRAKRITANG (romanized → Devanagari) =========
    "Aagama/sutrakritang/sutrakritang-ch2.html": (
        "Sensation", "Sensation", "वेदनीय",
    ),
    "Aagama/sutrakritang/sutrakritang-ch3.html": (
        "Consciousness", "Consciousness", "चेतना",
    ),
    "Aagama/sutrakritang/sutrakritang-ch4.html": (
        "Rejection of Error", "Rejection of Error", "स्त्रीपरिज्ञा",
    ),
    "Aagama/sutrakritang/sutrakritang-ch5.html": (
        "Equal Seeing", "Equal Seeing", "नपुंसक",
    ),

    # ========= MAHABHARAT =========
    "epics/mahabharat/translations/mahabharat-ch1.html": (
        "Introduction — The Four Anuyogs", "The Four Anuyogs", "चार अनुयोग",
    ),
    "epics/mahabharat/translations/mahabharat-ch2.html": (
        "The Jain Lens on Mahabharata's Era", "Jain View of the Era", "जैन दृष्टि से युग",
    ),

    # ========= RAMAYANA — BACKSTORY =========
    "epics/ramayana/ramayana-backstory-1.html": (
        "The Origins of the Rakshasa Clan", "Rakshasa Clan Origins", "राक्षस वंश की उत्पत्ति",
    ),
    "epics/ramayana/ramayana-backstory-2.html": (
        "Past Lives of Chandanti &amp; Abhayant", "Chandanti & Abhayant's Past", "चंदन्ती-अभयन्त के पूर्वभव",
    ),
    "epics/ramayana/ramayana-backstory-3.html": (
        "Past Lives of Dasharatha, Saumyaprabha &amp; Ram", "Dasharatha & Ram's Past Lives", "दशरथ-राम के पूर्वभव",
    ),
    "epics/ramayana/ramayana-backstory-4.html": (
        "Past Lives of Ravana's Kin", "Ravana's Lineage Past", "रावण वंश के पूर्वभव",
    ),
    "epics/ramayana/ramayana-backstory-5.html": (
        "The Origins of the Vanar Clan", "Vanar Clan Origins", "वानर वंश की उत्पत्ति",
    ),
    "epics/ramayana/ramayana-backstory-6.html": (
        "Past Lives of Bharat &amp; Suvarankanta", "Bharat & Suvarankanta's Past", "भरत-सुवर्णकान्ता के पूर्वभव",
    ),
    "epics/ramayana/ramayana-backstory-7.html": (
        "The Elephant Bhuvnalankara's Past Lives", "Bhuvnalankara's Past", "भुवनालंकार के पूर्वभव",
    ),
    "epics/ramayana/ramayana-backstory-8.html": (
        "Past Lives of the Principal Souls", "Principal Souls' Past", "प्रमुख आत्माओं के पूर्वभव",
    ),

    # ========= RAMAYANA — MAIN CHAPTERS =========
    "epics/ramayana/ramayana-ch4.html": (
        "Vibhishana &mdash; On the Path to Liberation", "Vibhishana Bound for Moksha", "मोक्षगामी विभीषण",
    ),
    "epics/ramayana/ramayana-ch5.html": (
        "Kaikeyi's Swayamvar", "Kaikeyi's Swayamvar", "कैकेयी का स्वयंवर",
    ),
    "epics/ramayana/ramayana-ch7.html": (
        "King Janaka's Concern", "King Janaka's Concern", "जनक राजा की चिंता",
    ),
    "epics/ramayana/ramayana-ch8.html": (
        "Janakpur's Gift &mdash; The Bow of Shiva", "Janakpur's Bow", "जनकपुर का धनुष",
    ),
    "epics/ramayana/ramayana-ch9.html": (
        "Sita's Swayamvar", "Sita's Swayamvar", "सीता का स्वयंवर",
    ),
    "epics/ramayana/ramayana-ch10.html": (
        "The Sacred Trust of Character", "Sacred Trust of Character", "चरित्र की दिव्य अमानत",
    ),
    "epics/ramayana/ramayana-ch11.html": (
        "King Dasharatha's Boon to Kaikeyi", "Dasharatha's Boon to Kaikeyi", "दशरथ का कैकेयी को वरदान",
    ),
    "epics/ramayana/ramayana-ch12.html": (
        "Ram and Sita's Journey into the Forest", "Ram & Sita's Vanvas", "राम-सीता का वनवास",
    ),
    "epics/ramayana/ramayana-ch13.html": (
        "Kaikeyi's Followers and Bharat's Coronation", "Bharat's Coronation", "भरत का राज्याभिषेक",
    ),
    "epics/ramayana/ramayana-ch14.html": (
        "Ayodhya's King in Grief", "King's Grief in Ayodhya", "अयोध्यापति की चिंता",
    ),
    "epics/ramayana/ramayana-ch15.html": (
        "Gokiran's Service to Sages", "Gokiran's Service", "गोकिरण की सेवा",
    ),
    "epics/ramayana/ramayana-ch16.html": (
        "Meeting Jatayu", "Meeting Jatayu", "जटायु से भेंट",
    ),
    "epics/ramayana/ramayana-ch17.html": (
        "Sita's Abduction", "Sita's Abduction", "सीता का अपहरण",
    ),
    "epics/ramayana/ramayana-ch19.html": (
        "Hanuman Carries the Message to Sita", "Hanuman's Message to Sita", "हनुमान का सीता को संदेश",
    ),
}


# Match the parens span content; replace just the inner WORD
SPAN_PAREN_RE = re.compile(
    r'(<span\s+class="[^"]*\btext-primary\b[^"]*"[^>]*>)\(([^)]+)\)(</span>)',
    re.IGNORECASE,
)
H2_QUOTE_RE = re.compile(
    r'(<span class="not-italic">Chapter[^<]*— </span>“)([^”]+)(”)',
)
H2_QUOTE_VARGA_RE = re.compile(
    r'(<span class="not-italic">[^<]*— </span>“)([^”]+)(”)',
)


def apply(path: Path, old_eng: str, new_eng: str, new_hindi: str) -> bool:
    src = path.read_text(encoding="utf-8")
    new = src
    changed = False

    # 1) Replace English title in H1 (the text before the span)
    # Idempotency guard: skip if the file already contains new_eng in an H1 context
    h1_has_new = bool(re.search(rf'<h1[^>]*>[^<]*{re.escape(new_eng)}\s*<span', new, re.IGNORECASE))
    if old_eng in new and not h1_has_new:
        new = new.replace(old_eng, new_eng, 1)
        changed = True

    # 2) Replace the Hindi parens content in the span (first occurrence only)
    m = SPAN_PAREN_RE.search(new)
    if m:
        replacement = f'{m.group(1)}({new_hindi}){m.group(3)}'
        new = new[:m.start()] + replacement + new[m.end():]
        changed = True

    # 3) Replace H2 quoted text (first occurrence only) — try Chapter form, then varga form
    h2_old_text = old_eng.replace('&amp;', '&').replace('&mdash;', '—')
    m = H2_QUOTE_RE.search(new)
    if m and h2_old_text in m.group(2):
        replacement = m.group(1) + new_eng.replace('&amp;', '&').replace('&mdash;', '—') + m.group(3)
        new = new[:m.start()] + replacement + new[m.end():]
        changed = True

    if changed:
        path.write_text(new, encoding="utf-8")
    return changed


def main():
    modified = 0
    for rel, (old_eng, new_eng, new_hindi) in TRANSLATIONS.items():
        f = ROOT / rel
        if not f.exists():
            print(f"  ! MISSING: {rel}")
            continue
        if apply(f, old_eng, new_eng, new_hindi):
            modified += 1
            print(f"  ✓ {rel}")
            print(f"      EN: {old_eng}  →  {new_eng}")
            print(f"      HI: ({new_hindi})")
        else:
            print(f"  - {rel} (no change)")
    print(f"\nUpdated {modified}/{len(TRANSLATIONS)} files.")


if __name__ == "__main__":
    main()
