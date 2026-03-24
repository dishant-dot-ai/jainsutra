import re

with open('tattvartha-ch4-v4.html', 'r') as f:
    content = f.read()

css = """
      .sutra-sanskrit { font-size: 1.35rem; line-height: 2; color: #503d00; }
      /* Pondering Over Section Styling */
      .pondering-section {
        display: flex;
        align-items: flex-start;
        gap: 1.5rem; /* Gap-6 matching sutra-card */
        margin-top: 4rem;
        margin-bottom: 6rem;
        padding: 0 2rem;
      }
      .pondering-star {
        font-variation-settings: 'FILL' 1, 'wght' 700, 'GRAD' 0, 'opsz' 48;
        color: #c9a84c;
        font-size: 2rem;
        flex-shrink: 0;
        padding-top: 0.25rem;
      }
      .pondering-content {
        flex: 1;
      }
      .pondering-title {
        font-family: 'Noto Serif', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #755b00;
        margin-bottom: 1rem;
        display: block;
      }
      .pondering-recap {
        font-family: 'Inter', sans-serif;
        font-size: 1.125rem;
        font-weight: 600;
        color: #1d1c17;
        line-height: 1.625;
        margin-bottom: 1.5rem;
        display: block;
      }
      .pondering-questions {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #4d4637;
        line-height: 1.625;
        font-style: italic;
        padding: 1.5rem;
        background: rgba(201,168,76,0.05);
        border-left: 2px solid #c9a84c;
        display: block;
      }
"""

if "pondering-section" not in content:
    content = content.replace('.sutra-sanskrit { font-size: 1.35rem; line-height: 2; color: #503d00; }', css)


replacements = [
    (
        "<!-- Divider: Pleasures of Celestial Beings -->",
        """</article>

<!-- Pondering Over: Classes and Hierarchy -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: Classes and Hierarchy</span>
        <span class="pondering-recap">We've learned that celestial beings are categorized into four classes (4.1), with varying thought-colorations (4.2) and subclasses (4.3). Despite their divine status, they still operate within strict social hierarchies featuring lords, ministers, bodyguards, and servants (4.4-4.6).</span>
        <span class="pondering-questions">If even the "gods" are bound by strict hierarchies, ranks, and roles, does heaven sound like a place of true freedom, or just a more comfortable version of worldly life?</span>
    </div>
</div>

<!-- Divider: Pleasures of Celestial Beings -->""",
        True # Remove closing </article> before this if it exists. Actually the regex will handle the </article> before the divider.
    ),
    (
        "<!-- Divider: Subclasses of the Four Nikaya -->",
        """</article>

<!-- Pondering Over: Celestial Pleasures -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: Celestial Pleasures</span>
        <span class="pondering-recap">Celestial pleasures range from physical contact in the lower heavens (4.7) to merely looking, hearing, or thinking about companions in the higher heavens (4.8). The most advanced devas experience constant bliss without any need for sensory stimulation at all (4.9).</span>
        <span class="pondering-questions">Think of a time you felt deeply happy just by remembering a beautiful moment. If your mind can create joy without needing anything physical, how much "stuff" do you really need to be happy?</span>
    </div>
</div>

<!-- Divider: Subclasses of the Four Nikaya -->"""
    ),
    (
        "<!-- Divider: The Stellar Devas and Time -->",
        """</article>

<!-- Pondering Over: Subclasses of the Devas -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: Subclasses of the Devas</span>
        <span class="pondering-recap">The sutras detail the specific subclasses of the Residential (4.10) and Peripatetic (4.11) devas, showcasing a vast array of beings like Asurakumaras, Kinnaras, and Gandharvas, each inhabiting different parts of the cosmos (4.12).</span>
        <span class="pondering-questions">Ancient texts populate every corner of the universe with diverse, living consciousness. How does imagining a universe teeming with invisible life change the way you walk through an empty forest or sit in a quiet room?</span>
    </div>
</div>

<!-- Divider: The Stellar Devas and Time -->"""
    ),
    (
        "<!-- Divider: The Heavenly Devas and the Kalpas -->",
        """</article>

<!-- Pondering Over: The Stellar Devas and Time -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: The Stellar Devas and Time</span>
        <span class="pondering-recap">We explored the Stellar devas—suns, moons, planets, constellations, and scattered stars (4.13). Their continuous movement creates the concept of time for us humans (4.14), while they remain stationary outside the human region (4.15).</span>
        <span class="pondering-questions">If our entire concept of "time" (days, years, rushing, waiting) is just created by the mechanical movement of stars and planets, why do we let time cause us so much stress?</span>
    </div>
</div>

<!-- Divider: The Heavenly Devas and the Kalpas -->"""
    ),
    (
        "<!-- Divider: Qualities of Higher and Lower Devas -->",
        """</article>

<!-- Pondering Over: The Heavenly Kalpas -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: The Heavenly Kalpas</span>
        <span class="pondering-recap">The heavenly devas are divided into those born in the structured kalpas (4.16) and those born in the higher, structureless realms like the Graiveyakas and Anuttaras (4.17-4.19). At the very top lives the Sarvarthasiddhi, just below the liberated souls (4.20).</span>
        <span class="pondering-questions">As the devas get higher, their societies lose their "structure" and hierarchy. Do you think true spiritual advancement requires letting go of our need for rules, ranks, and social status?</span>
    </div>
</div>

<!-- Divider: Qualities of Higher and Lower Devas -->"""
    ),
    (
        "<!-- Divider: Lifetimes of Celestial Beings -->",
        """</article>

<!-- Pondering Over: Ascending Qualities -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: Ascending Qualities</span>
        <span class="pondering-recap">As you move higher through the heavens, the devas experience increased lifespan, power, happiness, and purity of thought (4.21). Yet, they have less physical movement, smaller bodies, and less attachment to objects (4.22-4.23), utilizing purer thought-colors (4.24) and experiencing less frequent breathing and hunger (4.25-4.27).</span>
        <span class="pondering-questions">The highest beings have the most power and joy, but the smallest bodies and the least need to consume or travel. If "having less" naturally correlates with "being more," what is one thing you can minimize today to feel lighter?</span>
    </div>
</div>

<!-- Divider: Lifetimes of Celestial Beings -->"""
    ),
    (
        "<!-- Chapter End -->",
        """</article>

<!-- Pondering Over: Lifetimes and Liberation -->
<div class="pondering-section">
    <span class="material-symbols-outlined pondering-star">star</span>
    <div class="pondering-content">
        <span class="pondering-title">Pondering over: Lifetimes and Liberation</span>
        <span class="pondering-recap">The final sutras map out the massive, almost incomprehensible lifespans of the celestial beings across all the different heavens (4.28-4.42). Yet, no matter how many 'sagaropamas' a deva lives, their time eventually runs out, and they must be reborn to continue their journey toward ultimate liberation.</span>
        <span class="pondering-questions">If a million-year vacation in a celestial paradise still ends in having to come back and do the hard work of spiritual growth, is it better to seek a temporary paradise or permanent freedom?</span>
    </div>
</div>

<!-- Chapter End -->"""
    )
]

for target, replacement in replacements:
    # Need to replace `</article>\n\n<!-- Divider...` with the replacement
    pattern = r'</article>\s*' + re.escape(target)
    content = re.sub(pattern, replacement, content)

with open('tattvartha-ch4-v4.html', 'w') as f:
    f.write(content)
