---
layout: default
title: Home
description: "Knowledge sharing and documentation portal of Sunil Abraham: notes, essays, and research on internet policy, technology and digital rights."
image: /assets/images/sunil-abraham-colour-nature.jpg
categories: [Project pages]
page_id: TSAP-0002
created: 2025-10-19
---

<div class="hero-intro">
  <p><strong>Welcome</strong> to the <strong>Sunil Abraham Project</strong> (TSAP). This space brings together notes, essays, research, and reflections on technology, policy, and society. It aims to make knowledge freely accessible, encourage collaborative learning, and preserve insights.</p>
  
  <p>The project reflects years of engagement with digital rights, open technology, and social research in India and beyond. It seeks to connect individual thought with public understanding, bridging ideas across disciplines and communities.</p>
</div>

<nav class="tsap-contents">
  <h2>Contents</h2>
  <div class="contents-grid">
    <a href="#featured-article" class="content-link">
      <span class="link-icon">📄</span>
      <span>Featured article</span>
    </a>
    <a href="#sunil-abraham" class="content-link">
      <span class="link-icon">👤</span>
      <span>Sunil Abraham</span>
    </a>
    <a href="#featured-media" class="content-link">
      <span class="link-icon">🎥</span>
      <span>Featured media</span>
    </a>
    <a href="#newest-pages" class="content-link">
      <span class="link-icon">🆕</span>
      <span>Newest pages</span>
    </a>
    
    <a href="#about" class="content-link">
      <span class="link-icon">ℹ️</span>
      <span>About</span>
    </a>
    <a href="#licence" class="content-link">
      <span class="link-icon">⚖️</span>
      <span>Licence</span>
    </a>
  </div>
</nav>

{% include featured-article.html %}

{% include back-to-top.html %}

{% include sunil-bio.html %}

{% include back-to-top.html %}

{% include featured-media.html %}

{% include back-to-top.html %}

{% include newest-section.html %}

{% include back-to-top.html %}

{% comment %}
{% include dyk.html %}
{% include back-to-top.html %}
{% endcomment %}

<section class="content-section" id="about">
  <h2 class="section-title">About</h2>
  <div class="about-card">
    <p>This project serves as a living documentation space for research, writing, and reflection. This is built to create, organise, and publish documentation in a structured yet flexible manner, enabling continuous learning and open exchange of ideas.</p>

    <p><strong>It aims to:</strong></p>

    <ul>
      <li>Create and maintain documentation — capture insights, notes, essays, and drafts across themes and disciplines.</li>
      <li>Encourage knowledge sharing — make ideas accessible, referenceable, and adaptable for wider audiences.</li>
      <li>Support learning and reflection — develop patterns of learning, synthesis, and critical thought through open writing.</li>
      <li>Enable collaboration and contribution — allow others to engage with, remix, and build upon existing materials.</li>
      <li>Host brainstorming and ideation — serve as a space for developing and refining emerging ideas and projects.</li>
    </ul>

    <p>This documentation evolves over time, not as a static archive, but as a continuous process of thinking, writing, and sharing.</p>

    <p>Whether you are a researcher, student, practitioner, or reader exploring questions of openness, equity, and digital transformation, this documentation offers a growing archive of material to study, share, and build upon.</p>

    <a href="https://sunilabraham.in/articles/sunil-abraham-project/" class="btn-primary">Read more...</a>
  </div>
</section>

{% include back-to-top.html %}

<section class="content-section" id="licence">
  <h2 class="section-title">Licence</h2>
  <div class="licence-card">
    <p>Content are released under the <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution–ShareAlike 4.0 International</a> (CC BY-SA 4.0) licence, unless otherwise stated. You are free to share and adapt this material with proper attribution.</p>
  </div>
</section>

<style>
/* ========================================
   MODERN REDESIGN
   ======================================== */

/* Hide title and breadcrumb */
main h1,
main nav.breadcrumb {
  display: none !important;
}

/* Hero intro section */
.hero-intro {
  background: #fff;
  color: #0a2e57;
  padding: 0.5rem 2.5rem;
  border-radius: 16px;
  margin-bottom: 3rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

.hero-intro p {
  font-size: 1rem;
  line-height: 1.65;
  margin-bottom: 1rem;
  color: #333;
}

.hero-intro strong {
  font-weight: 600;
  color: #0a2e57;
}

/* Navigation grid */
.tsap-contents {
  padding: 0;
  border: none;
  background: transparent;
  border-radius: 0;
  box-shadow: none;
  max-width: 100%;
  margin: 3rem 0;
}

.tsap-contents h2 {
  font-size: 2rem;
  color: #0a2e57;
  margin-bottom: 1.5rem;
  font-weight: 700;
  border-bottom: 3px solid #005cc5;
  padding-bottom: 0.5rem;
}

.contents-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 0;
}

.content-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem 1.5rem;
  border: 2px solid transparent;
  border-radius: 12px;
  text-decoration: none;
  color: #0a2e57;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.content-link:hover {
  transform: translateY(-2px);
  border-color: #005cc5;
  box-shadow: 0 4px 16px rgba(0,92,197,0.2);
  background: linear-gradient(135deg, #e8f0fe 0%, #d6e7ff 100%);
}

.link-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

/* Content sections */
.content-section {
  margin: 0 0 1.25rem 0;
}

.section-title {
  font-size: 2.2rem;
  color: #0a2e57;
  margin-bottom: 1.5rem;
  font-weight: 700;
  border-bottom: 3px solid #005cc5;
  padding-bottom: 0.5rem;
}

/* Card styles */
.article-card,
.about-card,
.licence-card {
  background: #fff;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  border-left: 5px solid #005cc5;
}

.article-card p,
.about-card p,
.licence-card p {
  margin-bottom: 1rem;
  line-height: 1.7;
  color: #333;
}

/* Button styles */
.btn-primary {
  display: inline-block;
  padding: 0.85rem 2rem;
  background: linear-gradient(135deg, #005cc5 0%, #0a2e57 100%);
  color: #fff;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0,92,197,0.3);
  margin-top: 1rem;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,92,197,0.4);
  background: linear-gradient(135deg, #0047a0 0%, #051d3b 100%);
}

a.btn-primary,
a.btn-primary:hover,
a.btn-primary:focus,
a.btn-primary:active {
  color: #ffffff !important;
  text-decoration: none !important;
}

/* Links */
a {
  color: #005cc5;
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: #0a2e57;
  text-decoration: underline;
}

/* Mobile optimizations */
@media (max-width: 768px) {
  .hero-intro {
    padding: 1.5rem;
    margin-bottom: 2rem;
  }

  .section-title {
    font-size: 1.75rem;
  }

  .tsap-contents h2 {
    font-size: 1.6rem;
  }

  .contents-grid {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }

  .content-link {
    padding: 1rem 1.25rem;
  }

  .article-card,
  .about-card,
  .licence-card {
    padding: 1.5rem;
  }
}

@media (max-width: 480px) {
  .hero-intro {
    padding: 1.25rem;
  }

  .section-title {
    font-size: 1.5rem;
  }

  .article-card,
  .about-card,
  .licence-card {
    padding: 1.25rem;
  }

  .content-link {
    padding: 0.85rem 1rem;
    font-size: 0.95rem;
  }

  .link-icon {
    font-size: 1.25rem;
  }
}
  /* ========================================
   DARK MODE
   ======================================== */

body.tsap-dark-mode .hero-intro,
body.tsap-dark-mode .about-card,
body.tsap-dark-mode .licence-card,
body.tsap-dark-mode .article-card {
  background: #1f2937 !important;
}

body.tsap-dark-mode .hero-intro p,
body.tsap-dark-mode .article-card p,
body.tsap-dark-mode .about-card p,
body.tsap-dark-mode .licence-card p,
body.tsap-dark-mode .about-card li {
  color: #e5e7eb !important;
}

body.tsap-dark-mode .hero-intro strong,
body.tsap-dark-mode .section-title,
body.tsap-dark-mode .tsap-contents h2 {
  color: #f3f4f6 !important;
}

body.tsap-dark-mode .content-link {
  background: #1f2937 !important;
  color: #e5e7eb !important;
  border-color: #374151 !important;
}

body.tsap-dark-mode .content-link:hover {
  background: #2b3a4f !important;
  border-color: #60a5fa !important;
}
</style>
