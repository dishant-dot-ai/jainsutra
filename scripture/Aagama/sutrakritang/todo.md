# Sutrakritanga — UI Spec & TODO

## Sutra Card UI Spec (ch1 is the reference — apply to all chapters)

### Card Container
```
.sutra-card
  border: 1px solid rgba(201,168,76,0.25)
  border-left: 3px solid #c9a84c
  background: white
  NO hover effects (removed)
```

### Card Structure (in order, top to bottom)
1. Sutra number (left column, flex layout)
2. Sanskrit verse
3. Translation
4. Banner(s) — only if applicable
5. Commentary
6. Simple version
7. Concept tags

---

### Text Layers

**Sanskrit verse** — `.sutra-sanskrit`
```
font-family: Noto Serif, serif
font-size: 1.35rem  (mobile: 1.15rem)
line-height: 2
color: #503d00
```

**Translation** — `p.text-lg` (class: `text-lg font-semibold text-on-surface leading-relaxed`)
```
font-family: Inter, sans-serif (inherited)
font-size: 1.2rem
line-height: 1.85
color: inherits (text-on-surface = #1d1c17)
font-weight: 600 (font-semibold)
```

**Commentary** — `p.text-base` (class: `text-base text-on-surface-variant leading-relaxed`)
```
font-family: Inter, sans-serif (inherited)
font-size: 1.2rem
line-height: 1.85
color: #4d4637  (from Tailwind text-on-surface-variant — do NOT override with black)
```

**Simple version** — `.simple-explanation`
```
font-family: Inter, sans-serif
font-size: 1.2rem
line-height: 1.85
color: #4d4637
border-top: 1px dashed rgba(201,168,76,0.3)
margin-top: 1rem
padding-top: 1rem

  "The simple version:" bold label:
    color: #1d1c17  (black)
    font-weight: 600
```

**Concept tags** — `.concept-tag`
```
font-family: Inter, sans-serif
font-size: 11px
text-transform: uppercase
letter-spacing: 0.1em
color: #1d1c17
border: 1px solid #C9A84C
border-radius: 100px
padding: 4px 13px
font-weight: 500
```

---

### Banner System (3 colors)

**Structure (in order inside banner):**
1. Header row: badge pill + name
2. Def text (italic description)

**Positioning:** AFTER translation, BEFORE commentary. As standalone `<div>` siblings — NOT inside any `<p>` tag.

#### Wrong View (red) — `.wrong-view-banner`
```
background: rgba(186,26,26,0.04)
border-radius: 6px
padding: 1rem 1.25rem
margin-bottom: 1.5rem
NO border-left

  Badge (.wrong-view-badge):
    font-size: 11px
    font-weight: 700
    color: #9b1515
    background: rgba(186,26,26,0.1)
    border: 1px solid rgba(186,26,26,0.35)
    padding: 3px 11px
    border-radius: 4px
    text-transform: uppercase
    letter-spacing: 0.18em

  Name (.wrong-view-name):
    font-family: Noto Serif, serif
    font-size: 1.0625rem
    font-weight: 700
    color: #1d1c17

  Def (.wrong-view-def):
    font-family: Inter, sans-serif
    font-size: 0.9625rem
    color: #7e7665
    line-height: 1.65
    font-style: italic
```

#### Jain Principle (green) — `.principle-banner`
```
background: rgba(22,101,52,0.04)
border-radius: 6px
(same structure as wrong-view)

  Badge: color #166534, background rgba(22,101,52,0.1), border rgba(22,101,52,0.35)
  Name: same as wrong-view-name
  Def: same as wrong-view-def
```

#### Caution (blue) — `.caution-banner`
```
background: rgba(30,64,175,0.04)
border-radius: 6px
(same structure as wrong-view)

  Badge: color #1e40af, background rgba(30,64,175,0.1), border rgba(30,64,175,0.35)
  Name: same as wrong-view-name
  Def: same as wrong-view-def
```

---

## TODO — Apply ch1 spec to remaining chapters

- [ ] Apply banner CSS + structure to ch2–ch23 of Sutrakritanga
  - CSS block (all 3 banner types) to be copied from ch1
  - Banner repositioning: translation → banner(s) → commentary order
  - Remove hover effects from all chapters
  - Commentary and simple version text: color #1d1c17
  - sutra-card p.text-base and p.text-lg: font-size 1.2rem, line-height 1.85

- [ ] Apply same card CSS fixes to other scriptures:
  - Upasakdashang (ch1, ch7, ch8 done — verify remaining)
  - PrashnaVyakaran (a1–a5 done — verify)
  - Tattvartha ch1–ch10 (done — verify)
  - Vipaak (20 files done — verify)

## Lessons Learned
- Never put banner `<div>` inside a `<p>` tag — browsers auto-close the p, breaking layout
- Use BeautifulSoup (not regex) when restructuring nested HTML with multiple banner types per card
- When bs4 rewrites the file, check that Tailwind color classes still apply (specificity may shift)
- Commit after every file or batch — never batch-commit multiple sessions of work
