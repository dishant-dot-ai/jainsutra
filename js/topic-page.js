/* ============================================
   JainSutra — Topic Page JS
   "The Digital Alchemist" Edition
   ============================================ */

(function () {
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');

  if (!id || typeof TOPICS === 'undefined') {
    window.location.href = 'index.html';
    return;
  }

  const topic = TOPICS.find(t => t.id === id);
  if (!topic) {
    window.location.href = 'index.html';
    return;
  }

  document.title = `${topic.title} — JainSutra`;

  // Image mappings
  const TOPIC_IMAGES = {
    'navkar-mantra': 'assets/card-navkar.jpg',
    'samyaktva': 'assets/card-samyaktva.jpg',
    'ratnatraya': 'assets/card-ratnatraya.jpg',
    'jiva': 'assets/card-jiva.jpg',
    'ajiva': 'assets/card-ajiva.jpg',
    'six-dravyas': 'assets/card-six-dravyas.jpg',
    'gati': 'assets/card-gati.jpg',
    'nav-tattvas': 'assets/golden-orb-2.jpg',
    'karma': 'assets/abstract-dark-2.jpg',
    'ghati-aghati': 'assets/golden-orb-3.jpg',
    'kashaya': 'assets/cosmic-soul.jpg',
    'asrav-samvar-nirjara': 'assets/card-asrav.jpg',
    'leshya': 'assets/lamp-glow.jpg',
    'charitra': 'assets/card-charitra.jpg',
    'bhavnas': 'assets/golden-orb-3.jpg',
    'pratikraman': 'assets/abstract-dark-1.jpg',
    'gunsthanaks': 'assets/card-gunsthanaks-new.jpg',
    'anekantavada': 'assets/card-anekantavada-new.jpg'
  };

  const HERO_IMAGES = {
    'samyaktva': 'assets/hero-samyaktva.jpg',
    'jiva': 'assets/jiva-nebula.jpg'
  };

  const heroImg = HERO_IMAGES[topic.id] || TOPIC_IMAGES[topic.id] || 'assets/abstract-dark-2.jpg';

  // ---- Hero ----
  document.getElementById('topicLabel').textContent = topic.category.toUpperCase();
  document.getElementById('topicTitle').textContent = topic.title;
  document.getElementById('topicSanskrit').textContent = topic.sanskrit;
  document.getElementById('topicTagline').textContent = topic.tagline;

  const heroBg = document.getElementById('heroBg');
  heroBg.src = heroImg;
  heroBg.alt = topic.title;

  // ---- Deep Dive ----
  const paragraphs = topic.full_content.split('\n\n');

  // Lead: first paragraph
  document.getElementById('deepLead').textContent = paragraphs[0] || '';

  // Sidebar TOC: extract key concepts from key_terms (first 3)
  const tocEl = document.getElementById('deepToc');
  const tocItems = topic.key_terms.slice(0, 3);
  tocEl.innerHTML = tocItems.map((t, i) => `
    <div class="tp-deep__toc-item">
      <span class="tp-deep__toc-num">0${i + 1}</span>
      <p class="tp-deep__toc-text">${t.term}</p>
    </div>
  `).join('');

  // Body: paragraphs 1+
  const bodyParagraphs = paragraphs.slice(1);
  document.getElementById('deepBody').innerHTML =
    bodyParagraphs.map(p => '<p>' + p + '</p>').join('');

  // ---- CTA ----
  const ctaBtn = document.getElementById('ctaBtn');
  if (topic.connected_topics && topic.connected_topics.length > 0) {
    ctaBtn.href = 'topic.html?id=' + topic.connected_topics[0];
    const next = TOPICS.find(t => t.id === topic.connected_topics[0]);
    if (next) {
      ctaBtn.querySelector('span:first-child').textContent =
        'Explore ' + next.title;
    }
  } else {
    ctaBtn.href = 'index.html';
  }

  // ---- Key Terms ----
  document.getElementById('termsHeading').textContent = topic.title;
  document.getElementById('termsSub').textContent =
    'The essential vocabulary of ' + topic.title + '.';

  const termsEl = document.getElementById('keyTerms');
  termsEl.innerHTML = topic.key_terms.map((t, i) => `
    <div class="tp-term">
      <span class="tp-term__num">0${i + 1}</span>
      <div class="tp-term__word">${t.term}</div>
      <div class="tp-term__meaning">${t.meaning}</div>
    </div>
  `).join('');

  // ---- Quote ----
  let quoteText = topic.summary;
  if (paragraphs.length > 2) {
    const match = paragraphs[2].match(/^[^.!?]+[.!?]/);
    if (match) {
      let cleaned = match[0].replace(/^[A-Z][a-z\s]{0,25}:\s*/, '');
      cleaned = cleaned.charAt(0).toUpperCase() + cleaned.slice(1);
      quoteText = cleaned;
    }
  }
  document.getElementById('quoteText').textContent = quoteText;

  // ---- Connected Topics ----
  const connGrid = document.getElementById('connectedGrid');
  const connected = topic.connected_topics
    .map(cid => TOPICS.find(t => t.id === cid))
    .filter(Boolean)
    .slice(0, 3);

  connGrid.innerHTML = connected.map(t => {
    return `
    <a href="topic.html?id=${t.id}" class="tp-conn-card">
      <div>
        <h4 class="tp-conn-card__title">${t.title}</h4>
        <p class="tp-conn-card__desc">${t.tagline}</p>
      </div>
      <span class="tp-conn-card__link">Explore Path</span>
    </a>`;
  }).join('');

  // ---- Reading Progress ----
  const progressBar = document.getElementById('progressBar');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    });
  }

  initFadeIn();
})();
