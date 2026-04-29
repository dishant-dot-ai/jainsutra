# Anuttarovavai Sutra — Translation & Webpage Build

The Anuttarovavai (Anuttaropapātika Daśā) is the 9th Anga of the Jain canon. Three Vargas, 33 Adhyayanas total. The narrative core is Dhanya Anagar's nine-fold abhigraha and his ascent to Sarvarthasiddha — the highest of the five Anuttara realms reachable from human birth.

## Source

- PDF: `Source /Anuttarovavai.pdf` (151 pages — Guru Pran Prakashan, Gujarati edition)
- Extracted text (legacy-encoded, reference only): `Source /anuttarovavai_text.txt`
- Extraction script: `Source /extract_pdf.py`
- PDF page → printed page offset: **PDF = printed + 54**

## Structure

| Varga | Adhyayanas | Detail | PDF pages |
|---|---|---|---|
| 1 | 10 (Jali, Mayali, Upajali, Purisasena, Varisena, Dirghadanta, Lashtadanta, Vehalla, Vehayasa, Abhaya) | Jali full; 2-10 brief | 55–64 |
| 2 | 13 (Dirghasena, Mahasena, Lashtadanta, Gudhadanta, Shuddhadanta, Halla, Druma, Drumasena, Mahadrumasena, Simha, Simhasena, Mahasimhasena, Punyasena) | All brief | 65–67 |
| 3 | 10 (Dhanya, Sunakshatra, Isidasa, Pellaka, Ramaputta, Chandima, Pedhalaputta, Potilla, Padma, Vehallaputta) | Dhanya extensive; Sunakshatra moderate; 3-10 brief | 68–109 |

Appendix at PDF 110+ (skip — not scripture).

## Tasks

- [x] Extract PDF to UTF-8 text
- [x] Map chapter structure
- [x] Translate Varga 1 → `translations/anuttarovavai-ch1-translation.md` (8 sutras, 63 KB)
- [x] Translate Varga 2 → `translations/anuttarovavai-ch2-translation.md` (15 sutras, 56 KB)
- [x] Translate Varga 3 → `translations/anuttarovavai-ch3-translation.md` (33 sutras, 341 KB, 1718 lines)
- [x] Build `anuttarovavai-ch1.html` (372 lines)
- [x] Build `anuttarovavai-ch2.html` (524 lines)
- [x] Build `anuttarovavai-ch3.html` (763 lines)
- [x] Build `anuttarovavai-index.html` (372 lines)
- [x] Wire into Aagama `sacred-sutras-index.html` (book card after Sutrakritanga + footer link)
- [x] Build per-scripture `js/anuttarovavai-search.js` (56 sutras + 3 hero entries)
- [x] Reference `anuttarovavai-search.js` from each chapter HTML
