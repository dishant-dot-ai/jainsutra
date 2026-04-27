# Prompt Template: Uttaradhyayana Chapter Page

Use this prompt when asking any LLM coding tool (Cursor, Copilot, GPT-4, etc.) to build a new chapter page for JainSutra.org.

---

## THE PROMPT (copy, fill in the brackets, paste)

---

Build an HTML page for Chapter [NUMBER] of the Uttaradhyayana Sutra for the site JainSutra.org.

**File to create:** `uttaradhyana-ch[NUMBER].html`

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
.sutra-sanskrit { font-size: 1.35rem; line-height: 2; color: #503d00; }
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
@media (max-width: 768px) { .nav-button { bottom: 16px; } .nav-button.left-btn { left: 12px !important; } .nav-button.right-btn { right: 12px !important; } .sutra-sanskrit { font-size: 1.15rem; } }
```

---

### PAGE STRUCTURE (in order)

Build these sections in this exact order:

**1. Fixed Top Nav**
- Logo: `JainSutra.org` (links to `index-v4.html#hero`)
- Nav links: Fundamentals (`index-v4.html#foundations`), Navkar (`navkar-mantra-v4.html`), Meditations (`meditations.html`), Sacred Texts (`tattvartha-index-v4.html`)
- Donate button (`.burnished-gradient`, links to `donate-v4.html`)
- Class: `glass-nav fixed top-0 w-full z-50`

**2. Hero Section** (`pt-40`, 12-column grid)
- Left col (5/12): Chapter label, H1 with English title + Gujarati/Sanskrit subtitle in `<span class="block text-primary font-normal">`, H2 subtitle (what the chapter is about), paragraph description, 3-stat row (Imparted By / Compiled By / Translated By)
- Right col (7/12): Hero image (`assets/ch9-hero.jpg`), featured quote in Prakrit below image, English translation of quote in italics

**3. About Section** (grey background `bg-[#f2f1f0]`)
- Left: "About This Chapter" label + chapter name as H3
- Right: 2 paragraphs of chapter description, stat row: number of sutras | addressed to | number of sections

**4. Sutras Section**
- Header: "Adhyayana [NUMBER]" label, "The [N] Sutras" H3, brief intro line
- For each logical group of sutras, add a `.section-divider` with label: `<div class="section-divider" id="section-[slug]"><span>Part [N] — [Title]</span></div>`
- For each sutra, use this card structure:

```html
<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-[N]">
  <div class="flex items-start gap-6">
    <span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">[CHAPTER].[SUTRA]</span>
    <div class="space-y-4 flex-1">
      <p class="sutra-sanskrit font-headline">[PRAKRIT TEXT]</p>
      <p class="text-lg font-semibold text-on-surface leading-relaxed">[ENGLISH TRANSLATION — full sentence, no shortcuts]</p>
      <p class="text-base text-on-surface-variant leading-relaxed">[COMMENTARY — 3–5 sentences, explain what is happening in the story and why it matters philosophically]</p>
      <p class="simple-explanation"><b>The simple version:</b> [1–2 plain English sentences, no jargon]</p>
      <div class="concept-tags">
        <span class="concept-tag">[TAG 1]</span>
        <span class="concept-tag">[TAG 2]</span>
        <!-- 2–5 tags total -->
      </div>
    </div>
  </div>
</article>
```

**5. Footer**
- Same footer as all other pages: copyright line, links to index, sacred texts, meditations, navkar

**6. Fixed Nav Buttons** (bottom corners, appear on scroll)
```html
<a href="uttaradhyana-ch[PREV].html" class="nav-button left-btn" style="left:24px">← Ch [PREV]</a>
<a href="uttaradhyana-ch[NEXT].html" class="nav-button right-btn" style="right:24px">Ch [NEXT] →</a>
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
| English title | [ENGLISH TITLE] |
| Gujarati/Sanskrit title | [GUJARATI TITLE] |
| H2 subtitle | [ONE-LINE DESCRIPTION OF THE CHAPTER'S STORY] |
| Hero paragraph | [2–3 sentence story overview] |
| Featured quote (Prakrit) | [SUTRA TEXT — typically the most philosophical sutra] |
| Featured quote (English) | [TRANSLATION OF ABOVE] |
| About paragraph 1 | [Chapter name + position in canon + what the chapter narrates] |
| About paragraph 2 | [Philosophical significance and how it ends] |
| Number of sutras | [N] |
| Addressed To | [WHO RECEIVES THE TEACHING] |
| Number of sections | [N] |
| Sections | [LIST: Part I — Title (sutras X–Y), Part II — Title, ...] |
| All sutras | [PRAKRIT + TRANSLATION + COMMENTARY + SIMPLE + TAGS for each] |
| Prev chapter number | [NUMBER - 1] |
| Next chapter number | [NUMBER + 1] |

---

### RULES FOR CONTENT QUALITY

- Prakrit text: copy exactly from the source — no modifications
- Translation: complete sentences, not summaries. Translate the meaning, not word-for-word.
- Commentary: explain what is happening in the story AND what the philosophical point is. Minimum 3 sentences.
- Simple version: no Prakrit terms, no Jain jargon. One or two sentences maximum.
- Concept tags: 2–5 per sutra. Title case. Keep them tight (e.g. "Renunciation", "Karma", "Non-attachment", "Dharma").
- Section dividers: use natural story breaks (dialogue shifts, scene changes, topic shifts).
- The last sutra of the chapter always ends with `— iti bemi` ("Thus I say") — note this in the translation.

---

### WHAT NOT TO DO

- Do not add any JavaScript beyond the scroll listener for nav buttons
- Do not add dark mode toggles, search, or modals
- Do not use any CSS framework other than Tailwind
- Do not change the color palette
- Do not add external images other than `assets/ch9-hero.jpg`
- Do not summarize sutras in the translation field — translate them fully

---

*Template version: March 2026 — JainSutra.org Uttaradhyayana series*

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
