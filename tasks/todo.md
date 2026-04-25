# Prakrit Verse Number Fix

## Goal
Make sure Prakrit verse numbers (`॥X॥` or `॥X.Y॥`) appear on the same line as the verse text. Where missing, add the verse number.

## Survey Findings

**Issue A — `<br/>` before verse number (puts it on a new line):**
6 files in `Aagama/vipaak/` only — total 130 occurrences.
- vipaak-ch2.html (25), ch3.html (32), ch4.html (13), ch7.html (17), ch8.html (14), ch9.html (29)

**Issue B — No Prakrit verse number at end of sutra:**
51 files across multiple scriptures with varying formats:
- Samayvang (5 files) — uses single number `1, 2, 3...`
- Sutrakritang (3 files: ch14, ch15, ch16, ch23) — uses `chapter.verse` format
- Nirayavali (10 files) — prose narrative; mostly no traditional verse numbers
- Upasakdashang (8 files) — uses `chapter.verse` format
- Vipaak/Sukhvipak (some) — uses `chapter.verse` format
- Uttaradhyana (some chapters) — uses `chapter.verse` format
- Gyansaar (ch2, ch15) — partial; ch15 uses `।।X।।Y।।` (double-danda not `॥`)
- Samaysaar (most) — already has `॥X॥` (false positive in survey)

## Plan

### Phase 1 — Fix `<br/>` issue (SAFE)
Replace `<br/>॥` with ` ॥` in the 6 vipaak files. This is the exact issue from the screenshot. Pattern is well-defined and reversible.

### Phase 2 — Add missing Prakrit verse numbers (RISKY — needs decision)
Open question: should the format match each scripture's existing convention, or use `chapter.verse` everywhere?
Need to know:
1. Format preference (per-scripture vs uniform `X.Y`)
2. Whether to add to prose narratives that traditionally have no verse numbers (e.g. nirayavali)
3. How to handle Gyansaar ch15's `।।X।।Y।।` double-danda style — leave alone or normalize to `॥`?

## Status
- [ ] Phase 1: Fix vipaak `<br/>` issue (130 occurrences across 6 files)
- [ ] Phase 2: Pending decisions on format/scope before starting
