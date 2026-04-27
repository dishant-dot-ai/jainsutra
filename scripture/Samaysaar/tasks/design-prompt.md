# Design System Prompt: Samaysaar Chapter Pages

Use this prompt when building chapter pages for the Samaysaar scripture on JainSutra.org. This design system is derived from the Sutrakritanga series and must be followed exactly.

---

## TECH STACK

- Tailwind CSS via CDN: `https://cdn.tailwindcss.com?plugins=forms,container-queries`
- Fonts via Google Fonts: Noto Serif (400, 700, italic) + Inter (300, 400, 500, 600) + Material Symbols Outlined
- No build step. Pure static HTML.

---

## TAILWIND CONFIG

Paste this inside a `<script id="tailwind-config">` tag:

```js
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "primary": "#755b00","on-primary": "#ffffff","primary-container": "#c9a84c","on-primary-container": "#503d00",
        "surface": "#fef9f1","on-surface": "#1d1c17","surface-variant": "#e7e2da","on-surface-variant": "#4d4637",
        "outline": "#7e7665","outline-variant": "#d0c5b2","secondary": "#625d59","secondary-container": "#e6ded9",
        "on-secondary-container": "#67625e","surface-container-low": "#f8f3eb","surface-container": "#f2ede5",
        "surface-container-high": "#ece8e0","tertiary": "#4d5a98","tertiary-container": "#9ba8eb",
        "on-tertiary": "#ffffff","on-tertiary-container": "#2e3b77","error": "#ba1a1a","on-error": "#ffffff",
        "inverse-surface": "#32302b","inverse-on-surface": "#f5f0e8","surface-container-highest": "#e7e2da",
        "on-tertiary-fixed-variant": "#35437e","on-secondary-fixed-variant": "#4a4642",
        "primary-fixed-dim": "#e6c364","surface-bright": "#fef9f1","tertiary-fixed": "#dde1ff",
        "primary-fixed": "#ffe08f","secondary-fixed": "#e9e1dc","on-background": "#1d1c17",
        "on-secondary": "#ffffff","surface-dim": "#ded9d2","on-primary-fixed-variant": "#584400",
        "on-primary-fixed": "#241a00","on-error-container": "#93000a","surface-tint": "#755b00",
        "secondary-fixed-dim": "#ccc5c0","surface-container-lowest": "#ffffff",
        "on-tertiary-fixed": "#041451","inverse-primary": "#e6c364","error-container": "#ffdad6",
        "tertiary-fixed-dim": "#b9c3ff","on-secondary-fixed": "#1e1b18"
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

## CUSTOM CSS CLASSES

Add these inside a `<style>` tag:

```css
html { scroll-behavior: smooth; }

/* Core components */
.burnished-gradient { background: radial-gradient(circle at center, #755b00, #c9a84c); }
.glass-nav { background: rgba(248, 247, 246, 0.85); backdrop-filter: blur(20px); }

/* Sutra/Gatha cards */
.sutra-card { border: 1px solid rgba(201,168,76,0.25); border-left: 3px solid #c9a84c; background: white; }
.sutra-sanskrit { font-size: 1.35rem; line-height: 2; color: #503d00; }
.sutra-card p.text-base { font-size: 1.2rem; line-height: 1.85; }
.sutra-card p.text-lg { font-size: 1.2rem; line-height: 1.85; }

/* Simple explanation block */
.simple-explanation { margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed rgba(201,168,76,0.3); font-family: 'Inter', sans-serif; font-size: 1.2rem; line-height: 1.85; color: #4d4637; }
.simple-explanation b { color: #1d1c17; font-weight: 600; }

/* Concept tags */
.concept-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 1rem; }
.concept-tag { display: inline-block; border: 1px solid #C9A84C; background: transparent; color: #1d1c17; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 100px; padding: 4px 13px; font-weight: 500; }

/* Section dividers */
.section-divider { margin: 2.5rem 0 1.5rem; display: flex; align-items: center; gap: 1rem; }
.section-divider span { font-family: 'Noto Serif', serif; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.2em; color: #755b00; font-weight: 600; white-space: nowrap; }
.section-divider::before, .section-divider::after { content: ''; flex: 1; height: 1px; background: rgba(201,168,76,0.3); }

/* Navigation buttons (fixed, bottom corners) */
.nav-button { position: fixed; bottom: 24px; z-index: 100; background: transparent; border: 1px solid rgba(201,168,76,0.35); color: rgba(201,168,76,0.6); transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; transform: translateY(20px); }
.nav-button.visible { opacity: 1; pointer-events: auto; transform: translateY(0); }
.nav-button:hover { border-color: #C9A84C; color: #C9A84C; }

/* Contextual banners — Green: Key Jain Principle */
.principle-banner { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; padding: 1rem 1.25rem; background: rgba(22,101,52,0.04); border-radius: 6px; }
.principle-header { display: inline-flex; align-items: center; gap: 8px; }
.principle-badge { background: rgba(22,101,52,0.1); border: 1px solid rgba(22,101,52,0.35); color: #166534; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 700; padding: 3px 11px; border-radius: 4px; }
.principle-name { font-family: 'Noto Serif', serif; font-size: 1.0625rem; font-weight: 700; color: #1d1c17; }
.principle-def { font-family: 'Inter', sans-serif; font-size: 0.9625rem; color: #7e7665; line-height: 1.65; font-style: italic; }

/* Contextual banners — Red: Wrong View Refuted */
.wrong-view-banner { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; padding: 1rem 1.25rem; background: rgba(186,26,26,0.04); border-radius: 6px; }
.wrong-view-header { display: inline-flex; align-items: center; gap: 8px; }
.wrong-view-badge { background: rgba(186,26,26,0.1); border: 1px solid rgba(186,26,26,0.35); color: #9b1515; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 700; padding: 3px 11px; border-radius: 4px; }
.wrong-view-name { font-family: 'Noto Serif', serif; font-size: 1.0625rem; font-weight: 700; color: #1d1c17; }
.wrong-view-def { font-family: 'Inter', sans-serif; font-size: 0.9625rem; color: #7e7665; line-height: 1.65; font-style: italic; }

/* Contextual banners — Blue: Caution / Warning */
.caution-banner { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; padding: 1rem 1.25rem; background: rgba(30,64,175,0.04); border-radius: 6px; }
.caution-header { display: inline-flex; align-items: center; gap: 8px; }
.caution-badge { background: rgba(30,64,175,0.1); border: 1px solid rgba(30,64,175,0.35); color: #1e40af; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 700; padding: 3px 11px; border-radius: 4px; }
.caution-name { font-family: 'Noto Serif', serif; font-size: 1.0625rem; font-weight: 700; color: #1d1c17; }
.caution-def { font-family: 'Inter', sans-serif; font-size: 0.9625rem; color: #7e7665; line-height: 1.65; font-style: italic; }

/* Breadcrumb transition */
#breadcrumb { transition: opacity 0.4s ease, transform 0.4s ease; }
#main-nav a { text-decoration: none; }
.nav-link { text-decoration: none; }

/* Responsive */
@media (max-width: 768px) {
  .nav-button { bottom: 16px; }
  .nav-button.left-btn { left: 12px !important; }
  .nav-button.right-btn { right: 12px !important; }
  .sutra-sanskrit { font-size: 1.15rem; }
}
```

---

## PAGE STRUCTURE (in order)

Build these sections in this exact order:

### 1. Fixed Top Nav

- Logo: `JainSutra.org` (links to `index-v4.html#hero`)
- Nav links: Fundamentals (`index-v4.html#foundations`), Navkar (`navkar-mantra-v4.html`), Meditations (`meditations.html`), Sacred Texts (`sacred-sutras-index.html`) — Sacred Texts link is highlighted as active
- Donate button (`.burnished-gradient`, links to `donate-v4.html`)
- Class: `glass-nav fixed top-0 w-full z-50`

### 2. Hero Section (`pt-40`, 12-column grid)

- Left col (5/12): Scripture label in italic uppercase, H1 with English title + Sanskrit/Hindi subtitle in `<span class="block text-primary font-normal">`, H2 subtitle (what the chapter covers), paragraph description
- Right col (7/12): Hero image with grayscale hover effect, featured quote in original language below image, English translation in italics

### 3. About Section (grey background `bg-[#f2f1f0]`)

- Left: "About This Chapter" label + chapter name as H3
- Right: 2 paragraphs of chapter description, stat row showing key metadata (number of gathas/verses, sections, source, author)

### 4. Verses/Gathas Section

- Header: Chapter/section label, verse count as H3, brief intro line
- For each logical group of verses, add a `.section-divider`:
  ```html
  <div class="section-divider" id="section-[slug]"><span>Part [N] — [Title]</span></div>
  ```
- For each verse, use this card structure:

```html
<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-[N]">
  <div class="flex items-start gap-6">
    <span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">[CHAPTER].[VERSE]</span>
    <div class="space-y-4 flex-1">
      <p class="sutra-sanskrit font-headline">[ORIGINAL TEXT — Prakrit/Sanskrit/Hindi]</p>
      <p class="text-lg font-semibold text-on-surface leading-relaxed">[ENGLISH TRANSLATION — full sentence, no shortcuts]</p>
      <!-- Optional: contextual banner here if verse states a key principle, refutes a wrong view, or carries a caution -->
      <p class="text-base text-on-surface-variant leading-relaxed">[COMMENTARY — 3–5 sentences, explain meaning and philosophical significance]</p>
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

### 5. Footer

Standard footer across all pages:
- Left: JainSutra branding + tagline + copyright
- Right: 3-column grid with links — Aagama (Sacred Sutras, Sutrakritanga, Uttaradhyayana), Explore (Fundamentals, Navkar Mantra, Meditations), Connect (Contact, Donate)

### 6. Fixed Nav Buttons (bottom corners, appear on scroll)

```html
<a href="[PREV-PAGE].html" class="nav-button left-btn" style="left:24px">← Ch [PREV]</a>
<a href="[NEXT-PAGE].html" class="nav-button right-btn" style="right:24px">Ch [NEXT] →</a>
```

JS to show on scroll:
```js
window.addEventListener('scroll', () => {
  const visible = window.scrollY > 300;
  document.querySelectorAll('.nav-button').forEach(b => b.classList.toggle('visible', visible));
});
```

---

## CONTEXTUAL BANNER SYSTEM

Use banners sparingly — only when a verse introduces a named concept worth highlighting. Three types:

| Banner Type | Class Prefix | Color | Use When |
|---|---|---|---|
| Jain Principle | `.principle-*` | Green | Verse states a core Jain principle (ahimsa, aparigraha, anekantavada, etc.) |
| Wrong View | `.wrong-view-*` | Red | Verse explicitly refutes a named philosophical position |
| Caution | `.caution-*` | Blue | Verse contains a warning or important caveat |

Banner HTML (example — Principle):
```html
<div class="principle-banner">
  <div class="principle-header">
    <span class="principle-badge">Jain Principle</span>
    <span class="principle-name">[Principle Name] · [Sanskrit Term]</span>
  </div>
  <p class="principle-def">[One-sentence definition of the principle in plain English]</p>
</div>
```

Place banners **after the translation** and **before the commentary** within a sutra card.

---

## CONTENT QUALITY RULES

- Original text: copy exactly from the source — no modifications
- Translation: complete sentences, not summaries. Translate the meaning, not word-for-word.
- Commentary: explain what is happening AND what the philosophical point is. Minimum 3 sentences.
- Simple version: no Sanskrit/Prakrit terms, no Jain jargon. One or two sentences maximum.
- Concept tags: 2–5 per verse. Title case. Keep them tight (e.g. "Renunciation", "Karma", "Non-attachment", "Dharma").
- Section dividers: use natural topical breaks.

---

## WHAT NOT TO DO

- Do not add any JavaScript beyond the scroll listener for nav buttons
- Do not add dark mode toggles, search, or modals
- Do not use any CSS framework other than Tailwind
- Do not change the color palette
- Do not summarize verses in the translation field — translate them fully
- Do not over-decorate — the design is intentionally restrained and text-focused

---

## VISUAL FLAG SYSTEM

For every chapter, identify where a visual would help a user understand a concept faster — not decoration, not literal illustration of every metaphor. Only where a visual genuinely accelerates comprehension.

At each such spot, insert:
`<span style="color: red;">[VISUAL FLAG #[chapter].[flag] — one sentence describing what kind of image is needed]</span>`

Rules:
- Flag numbering resets to 1 at every new chapter
- When an image is provided, Dishant will dictate placement
- Remove the flag once image is placed
- Never auto-source or generate images

---

*Design system derived from the Sutrakritanga series — JainSutra.org*
