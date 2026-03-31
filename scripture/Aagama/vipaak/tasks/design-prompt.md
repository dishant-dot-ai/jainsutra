# Prompt Template: Vipaak Sutra Chapter Page

Use this prompt when asking any LLM coding tool (Cursor, Copilot, GPT-4, etc.) to build a new chapter page for JainAwaken.org.

> **IMPORTANT — Content Style:** The Vipaak Sutra is **prose narrative**, not verse. Each chapter is a complete story. Sutras are long prose sentences (not two-line couplets). The structure is: narrative frame → question → past-life story → karma revelation → future trajectory. This is fundamentally different from the Uttaradhyana design — treat each "sutra" as a story beat, not a philosophical aphorism.

---

## THE PROMPT (copy, fill in the brackets, paste)

---

Build an HTML page for Chapter [NUMBER] of the Vipaak Sutra ([VOLUME]: [Duhkha Vipaak / Sukha Vipaak]) for the site JainAwaken.org.

**File to create:** `vipak-ch[NUMBER].html`

---

### TECH STACK

- Tailwind CSS via CDN: `https://cdn.tailwindcss.com?plugins=forms,container-queries`
- Fonts via Google Fonts: Noto Serif (400, 700, italic) + Inter (300, 400, 500, 600) + Material Symbols Outlined
- No build step. Pure static HTML.

---

### TAILWIND CONFIG

Paste this inside a `<script id="tailwind-config">` tag:

```js
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "on-tertiary-fixed-variant": "#35437e","on-secondary-fixed-variant": "#4a4642","secondary-container": "#e6ded9","primary-fixed-dim": "#e6c364","surface-bright": "#fef9f1","tertiary-fixed": "#dde1ff","surface": "#fef9f1","primary-fixed": "#ffe08f","surface-container-low": "#f8f3eb","secondary-fixed": "#e9e1dc","outline-variant": "#d0c5b2","outline": "#7e7665","inverse-on-surface": "#f5f0e8","on-background": "#1d1c17","on-secondary": "#ffffff","on-tertiary-container": "#2e3b77","error": "#ba1a1a","on-error": "#ffffff","on-primary-fixed-variant": "#584400","surface-dim": "#ded9d2","surface-container-high": "#ece8e0","primary": "#755b00","on-primary-container": "#503d00","inverse-surface": "#32302b","secondary": "#625d59","error-container": "#ffdad6","tertiary-fixed-dim": "#b9c3ff","on-secondary-container": "#67625e","on-primary": "#ffffff","on-primary-fixed": "#241a00","on-error-container": "#93000a","surface-tint": "#755b00","secondary-fixed-dim": "#ccc5c0","surface-variant": "#e7e2da","surface-container-lowest": "#ffffff","on-tertiary-fixed": "#041451","surface-container-highest": "#e7e2da","primary-container": "#c9a84c","inverse-primary": "#e6c364","on-surface-variant": "#4d4637","tertiary": "#4d5a98","background": "#fef9f1","on-tertiary": "#ffffff","on-surface": "#1d1c17","tertiary-container": "#9ba8eb","surface-container": "#f2ede5","on-secondary-fixed": "#1e1b18"
      },
      fontFamily: {
        "headline": ["Noto Serif", "serif"],
        "body": ["Inter", "sans-serif"],
        "label": ["Inter", "sans-serif"]
      },
      borderRadius: {
        "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"
      },
    },
  },
}
```

---

### CUSTOM CSS CLASSES

Add these inside a `<style>` tag:

```css
html { scroll-behavior: smooth; }
.burnished-gradient { background: radial-gradient(circle at center, #755b00, #c9a84c); }
.sutra-card { border: 1px solid rgba(201,168,76,0.25); border-left: 3px solid #c9a84c; background: white; }
.sutra-number { font-size: 0.75rem; font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 0.15em; color: #755b00; font-weight: 600; margin-bottom: 0.5rem; }
.sutra-prose { font-size: 1.05rem; line-height: 1.85; color: #1d1c17; font-family: 'Inter', sans-serif; }
.sutra-prakrit { font-size: 1.1rem; line-height: 1.9; color: #503d00; font-family: 'Noto Serif', serif; font-style: italic; border-left: 2px solid rgba(201,168,76,0.4); padding-left: 1rem; margin: 0.75rem 0; }
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
.karma-banner { background: linear-gradient(135deg, #fef9f1 0%, #f2ede5 100%); border: 1px solid rgba(201,168,76,0.2); border-radius: 0.5rem; padding: 1.5rem 2rem; margin: 2rem 0; }
@media (max-width: 768px) { .nav-button { bottom: 16px; } .nav-button.left-btn { left: 12px !important; } .nav-button.right-btn { right: 12px !important; } }
```

---

### PAGE STRUCTURE (in order)

Build these sections in this exact order:

**1. Fixed Top Nav**
- Logo: `JainAwaken.org` (links to `../../../../index-v4.html#hero`)
- Nav links: Fundamentals, Navkar, Meditations, Sacred Texts (same relative paths as Uttaradhyana pages)
- Donate button (`.burnished-gradient`, links to `../../../../fundamentals/donate-v4.html`)
- Class: `glass-nav fixed top-0 w-full z-50`

**2. Hero Section** (`pt-40`, 12-column grid)
- Left col (5/12):
  - Volume label: e.g. `Vipaak Sutra · Duhkha Vipaak · Chapter [N]`
  - H1 with English story title + Gujarati name in `<span class="block text-primary font-normal">`
  - H2 subtitle: one-line karma theme (e.g. "The story of a man whose cruelty as a tax collector returns as a lifetime of suffering")
  - 2–3 sentence story overview paragraph
  - 3-stat row: Narrator / Questioner / Compiled By
- Right col (7/12): Hero image (`assets/ch9-hero.jpg`), and below it a "Karma Theme" banner:
```html
<div class="karma-banner">
  <p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-2">[Duhkha Vipaak / Sukha Vipaak] — The Fruit of [Sin / Virtue]</p>
  <p class="font-headline text-lg text-on-surface">[One-sentence moral of the chapter — what sin/virtue caused what result]</p>
</div>
```

**3. About Section** (`bg-[#f2f1f0]`)
- Left: "About This Chapter" label + story name as H3
- Right:
  - Para 1: Story background — who is the protagonist, what city, what sin/virtue
  - Para 2: Karma theme — what they did in a past life, what fruit they received in this life
  - Stat row: Number of sutras | Protagonist | Past Life

**4. Story Section** (the sutras)
- Header: `Pratham Shrutaskandha — [Duhkha/Sukha] Vipaak · Chapter [N]` label, story name as H3, brief intro
- Use `.section-divider` to mark the four natural acts of every Vipaak chapter:

```html
<div class="section-divider" id="act-1"><span>Act I — The Setting &amp; Arrival</span></div>
<div class="section-divider" id="act-2"><span>Act II — The Question &amp; The Story</span></div>
<div class="section-divider" id="act-3"><span>Act III — The Past Life Revealed</span></div>
<div class="section-divider" id="act-4"><span>Act IV — The Karma's Fruit &amp; Future Destiny</span></div>
```

- For each sutra, use this card structure:

```html
<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-[N]">
  <div class="space-y-4">
    <p class="sutra-number">Sutra [CHAPTER].[N]</p>
    <!-- If the sutra contains Prakrit text (formulaic openings, verse quotes): -->
    <p class="sutra-prakrit">[PRAKRIT TEXT if present]</p>
    <!-- The narrative prose translation — this is the main content -->
    <p class="sutra-prose">[ENGLISH TRANSLATION — full prose narrative sentence(s). This can be 2–5 sentences for long sutras. Do not summarize. Translate fully.]</p>
    <!-- Commentary: what is happening in the story + why it matters -->
    <p class="text-base text-on-surface-variant leading-relaxed">[COMMENTARY — 2–4 sentences explaining the narrative moment, its karmic significance, and what it reveals about Jain teaching]</p>
    <p class="simple-explanation"><b>The simple version:</b> [1–2 plain sentences. No Jain terms. What is happening and why does it matter?]</p>
    <div class="concept-tags">
      <span class="concept-tag">[TAG 1]</span>
      <span class="concept-tag">[TAG 2]</span>
      <!-- 2–4 tags: e.g. "Karmic Fruit", "Past Life", "Suffering", "Compassion", "Animal Cruelty" -->
    </div>
  </div>
</article>
```

> **Note on Prakrit text in Vipaak:** Unlike Uttaradhyana, not every Vipaak sutra has its own Prakrit verse. Most sutras are prose narrative with "vaṇṇao" abbreviation formulas. Include Prakrit only where the text explicitly has it (formulaic openings like "teṇaṃ kāleṇaṃ…", or verse quotations). Do not fabricate Prakrit for sutras that are pure prose.

**5. Karma Summary Panel** (after all sutras)

Add a highlighted summary panel before the footer:

```html
<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-16">
  <div class="karma-banner">
    <h3 class="text-2xl font-headline font-bold text-on-surface mb-4">The Karmic Lesson of This Chapter</h3>
    <p class="text-lg text-on-surface-variant leading-relaxed mb-4">[2–3 sentences summarizing the sin or virtue, the life it produced, and the teaching it conveys]</p>
    <p class="text-base text-primary font-semibold font-headline">[Short memorable closing statement — one line]</p>
  </div>
</section>
```

**6. Footer**
- Same footer as all other pages: copyright, links to index, sacred texts, meditations, navkar

**7. Fixed Nav Buttons** (bottom corners, appear on scroll)
```html
<a href="vipak-ch[PREV].html" class="nav-button left-btn" style="left:24px">← Ch [PREV]</a>
<a href="vipak-ch[NEXT].html" class="nav-button right-btn" style="right:24px">Ch [NEXT] →</a>
```
With this JS to show them on scroll:
```js
window.addEventListener('scroll', () => {
  const visible = window.scrollY > 300;
  document.querySelectorAll('.nav-button').forEach(b => b.classList.toggle('visible', visible));
});
```

---

### CONTENT TO FILL IN

Replace all bracketed values below:

| Field | Value |
|---|---|
| Chapter number | [NUMBER] |
| Volume | Duhkha Vipaak (chapters 1–10) or Sukha Vipaak (chapters 1–10) |
| English story title | [PROTAGONIST'S NAME + brief descriptor, e.g. "The Fisherman's Agony"] |
| Gujarati story name | [NAME IN GUJARATI/DEVANAGARI] |
| H2 subtitle | [One line: what sin/virtue caused what suffering/happiness] |
| Hero paragraph | [2–3 sentence story overview: who, what they did, what happened] |
| Narrator | Lord Mahavira (always) |
| Questioner | Gautam Swami (usually) or Sudharmashvami (who transmits to Jambushvami) |
| Karma theme banner | [What sin/virtue → what fruit] |
| About para 1 | [Protagonist's current life — city, status, present suffering/happiness] |
| About para 2 | [Past life — who they were, what sin/virtue they performed, karmic link] |
| Number of sutras | [N] |
| Protagonist | [Name] |
| Past life | [Brief: "royal cook who slaughtered animals" / "merchant who gave charity"] |
| Act I sutras | [Setting the scene, the arrival, the question asked] |
| Act II sutras | [Mahavir begins the story, past life narration] |
| Act III sutras | [The sin/virtue committed, in detail] |
| Act IV sutras | [Present suffering/happiness explained, future destiny, liberation or continued cycle] |
| Karma lesson | [The summary moral of the chapter] |
| Prev chapter number | [NUMBER - 1] |
| Next chapter number | [NUMBER + 1] |

---

### UNDERSTANDING THE VIPAAK SUTRA STRUCTURE

Every chapter of the Vipaak Sutra follows the same narrative arc:

1. **Setting** — "At that time, in that period, there was a city called [X]…" (formulaic Prakrit opening, abbreviated with "vaṇṇao")
2. **Arrival** — Gautam Swami (or Sudharmashvami) arrives with monks, gives teachings, assembly disperses
3. **The Question** — Gautam or a disciple sees something that prompts a question to Mahavir (a suffering person, a blessed person, an unusual situation)
4. **Past Life Revelation** — Mahavir uses his omniscience to reveal the protagonist's previous birth and the specific sin or virtue they performed
5. **Karmic Fruit** — How that exact sin or virtue produced their current state of suffering or happiness
6. **Future Trajectory** — Where the soul will go next: more hell births, animal births, or eventual liberation through righteous living

Duhkha Vipaak (chapters 1–10): all protagonists suffer due to sins in past lives
Sukha Vipaak (chapters 1–10): all protagonists are happy/blessed due to virtue in past lives

---

### RULES FOR CONTENT QUALITY

- **Prakrit text**: only include where explicitly present in the translation source (formulaic openings, embedded verse quotations). Never fabricate.

- **No truncation — ever.** This is sacred religious scripture. Every word of the Prakrit and every word of the translation must appear in full. Do not shorten, ellipsize, paraphrase, or cut any part of the Prakrit text or its translation. A truncated sacred verse is a disrespect to the scripture. If the card feels long, that is correct — let it be long.

- **Translation**: full prose narrative — do not summarize long sutras into one line. If a sutra narrates 5 events, all 5 must appear in the translation, in order, without omission.

- **Commentary**: This is the most important explanatory layer on the page. Write it comprehensively so that a 15-year-old with no background in Jainism can fully understand what is happening and why it matters. Use plain everyday English — no Jain terminology, no Sanskrit or Prakrit words. Use analogies and real-world comparisons where helpful. Explain the narrative moment, the karmic law at work, and what it means for how we live. Do not artificially limit the length — write as much as it takes for the teaching to land clearly.

- **Visual aid flag**: At the end of the commentary for any sutra whose content would benefit from a picture (e.g. a scene of suffering, a description of a hell realm, a vivid past-life moment, a karmic transformation), add this note on its own line:
  `📷 Visual Aid: [One sentence describing what image would best illustrate this sutra]`
  This flags it for the design team to commission or source an illustration. Not every sutra needs this — only where a picture would genuinely help the viewer understand.

- **Simple version**: Condense the single most important idea or focal point of the sutra into one or two plain sentences. Not a summary of everything — just the core teaching or the central moment. No Jain jargon. Write it as if explaining to a curious teenager who has never heard of karma.

- **Concept tags**: 2–4 per sutra. Story-oriented: "Animal Cruelty", "Karmic Fruit", "Past Life", "Suffering", "Compassion", "Liberation", "Hellish Birth", "Virtue", "Charity", "Non-violence"
- **Section dividers**: use the four-act structure (Setting, Question & Story, Past Life, Karma's Fruit). Add sub-dividers within acts for long chapters if needed.
- **"vaṇṇao" formula**: when the source says "[description follows from Aupapatika Sutra]," write a brief note in the commentary explaining this is a canonical abbreviation, and render the translated sentence without it.

---

### WHAT NOT TO DO

- Do not add any JavaScript beyond the scroll listener for nav buttons
- Do not add dark mode toggles, search, or modals
- Do not use any CSS framework other than Tailwind
- Do not change the color palette
- Do not add external images other than `assets/ch9-hero.jpg`
- Do not fabricate Prakrit text for prose-only sutras
- Do not treat Vipaak sutras like Uttaradhyana verses — they are story beats, not philosophical aphorisms
- Do not compress multiple sutras into one card — keep each sutra as its own card even if they feel like parts of one sentence
- Do not truncate or shorten any Prakrit text or translation — ever

---

*Template version: March 2026 — JainAwaken.org Vipaak Sutra series*

---

## Visual Flag System — All Chapters

For every chapter, read the full content and identify where a visual
would help a user understand a concept faster — not decoration, not
literal illustration of every metaphor. Only where a visual genuinely
accelerates comprehension.

At each such spot, insert:
<span style="color: red;">[VISUAL FLAG #[chapter].[flag] — one sentence describing what kind of image is needed]</span>

Example: Chapter 4, third flag = #4.3

Rules:
- Flag numbering resets to 1 at every new chapter
- When an image is provided, Dishant will dictate placement
- Remove the flag once image is placed
- Never auto-source or generate images
