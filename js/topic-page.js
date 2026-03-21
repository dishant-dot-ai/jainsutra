/* ============================================
   JainAwaken — Topic Page JS
   ============================================ */

(function () {
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');

  if (!id || typeof TOPICS === 'undefined') {
    window.location.href = 'concepts.html';
    return;
  }

  const topic = TOPICS.find(t => t.id === id);
  if (!topic) {
    window.location.href = 'concepts.html';
    return;
  }

  // Set page title
  document.title = `${topic.title} — JainAwaken`;

  // Map categories to images
  const categoryImages = {
    'Foundation': 'assets/hero-meditation.jpg',
    'Soul & Reality': 'assets/cosmic-soul.jpg',
    'Karma System': 'assets/golden-orb-1.jpg',
    'The Path': 'assets/lamp-glow.jpg',
    'Philosophy': 'assets/abstract-dark-1.jpg'
  };

  // Fill hero
  document.getElementById('topicCategory').textContent = topic.category;
  document.getElementById('topicSanskrit').textContent = topic.sanskrit;
  document.getElementById('topicTitle').textContent = topic.title;
  document.getElementById('topicTagline').textContent = topic.tagline;

  // Add hero image
  const heroImageEl = document.getElementById('topicHeroImage');
  if (heroImageEl) {
    const imgSrc = categoryImages[topic.category] || 'assets/abstract-dark-2.jpg';
    heroImageEl.innerHTML = `<img src="${imgSrc}" alt="${topic.title}" loading="lazy">`;
  }

  // Fill key terms
  const termsEl = document.getElementById('keyTerms');
  termsEl.innerHTML = topic.key_terms.map(t => `
    <div class="term-pill">
      <div class="term-pill__word">${t.term}</div>
      <div class="term-pill__meaning">${t.meaning}</div>
    </div>
  `).join('');

  // Fill content
  const contentEl = document.getElementById('topicContent');
  const paragraphs = topic.full_content.split('\n\n');
  contentEl.innerHTML = paragraphs.map(p => `<p>${p}</p>`).join('');

  // Fill connected topics
  const connGrid = document.getElementById('connectedGrid');
  const connected = topic.connected_topics
    .map(cid => TOPICS.find(t => t.id === cid))
    .filter(Boolean)
    .slice(0, 3);

  connGrid.innerHTML = connected.map(t => `
    <a href="topic.html?id=${t.id}" class="card fade-in">
      <div class="card__category">
        <span class="card__dot"></span>
        <span class="category-tag">${t.category}</span>
      </div>
      <div class="card__sanskrit">${t.sanskrit}</div>
      <h3 class="card__title">${t.title}</h3>
      <p class="card__tagline">${t.tagline}</p>
      <span class="card__link">Explore</span>
    </a>
  `).join('');

  // Reading progress bar
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
