---
layout: default
title: "Press Clippings"
description: "A visual archive of newspaper and magazine clippings featuring Sunil Abraham and the Centre for Internet and Society, including print media references that may not be available online."
categories: [Media mentions]
permalink: /media/clippings/
created: 2026-03-21
---

**Press Clippings** is a collection of newspaper and magazine coverage featuring [Sunil Abraham](/sunil/) in print media. These clippings span coverage across Indian and international publications on topics including internet governance, privacy law, digital rights, and technology policy.

<div class="clippings-grid">

  <article class="clipping-card">
    <button class="clipping-thumb" onclick="openLightbox('/media/images/civil-society-pushes-for-privacy-panel.jpg', 'Civil Society Pushes for Privacy Panel — The Times of India, 6 May 2014')" aria-label="View full clipping: Civil Society Pushes for Privacy Panel">
      <img
        src="/media/images/civil-society-pushes-for-privacy-panel.jpg"
        alt="The Times of India clipping dated 6 May 2014 titled Civil Society Pushes for Privacy Panel"
        loading="lazy"
      >
      <span class="zoom-hint" aria-hidden="true">🔍 Click to enlarge</span>
    </button>
    <div class="clipping-caption">
      <span class="clipping-source">The Times of India</span>
      <span class="clipping-date">6 May 2014</span>
      <a href="/media/civil-society-pushes-for-privacy-panel/" class="clipping-link">Civil Society Pushes for Privacy Panel</a>
    </div>
  </article>

</div>

<!-- Lightbox -->
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Clipping viewer" tabindex="-1">
  <div class="lightbox-backdrop" onclick="closeLightbox()"></div>
  <div class="lightbox-content">
    <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close viewer">✕</button>
    <img id="lightbox-img" src="" alt="" class="lightbox-image">
    <p id="lightbox-caption" class="lightbox-caption"></p>
  </div>
</div>

<style>
/* --- Grid --- */
.clippings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.8rem;
  margin: 2rem 0;
}

/* --- Card --- */
.clipping-card {
  background: #fff;
  border: 1px solid #dde5f0;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  transition: box-shadow 0.25s ease, transform 0.2s ease;
  display: flex;
  flex-direction: column;
}

.clipping-card:hover {
  box-shadow: 0 6px 20px rgba(0,0,0,0.13);
  transform: translateY(-2px);
}

/* --- Thumbnail button --- */
.clipping-thumb {
  all: unset;
  cursor: zoom-in;
  display: block;
  position: relative;
  overflow: hidden;
  background: #f4f6fa;
  line-height: 0;
}

.clipping-thumb img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  object-position: top;
  display: block;
  transition: transform 0.3s ease, filter 0.3s ease;
}

.clipping-thumb:hover img {
  transform: scale(1.03);
  filter: brightness(0.88);
}

.zoom-hint {
  position: absolute;
  bottom: 0.6rem;
  right: 0.6rem;
  background: rgba(0,0,0,0.55);
  color: #fff;
  font-size: 0.75rem;
  padding: 0.25rem 0.55rem;
  border-radius: 20px;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.clipping-thumb:hover .zoom-hint,
.clipping-thumb:focus .zoom-hint {
  opacity: 1;
}

.clipping-thumb:focus-visible {
  outline: 3px solid #1a5fb4;
  outline-offset: 2px;
}

/* --- Caption --- */
.clipping-caption {
  padding: 0.85rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  border-top: 1px solid #eef1f7;
}

.clipping-source {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #1b2a49;
}

.clipping-date {
  font-size: 0.8rem;
  color: #888;
}

.clipping-link {
  font-size: 0.88rem;
  color: #1a5fb4;
  text-decoration: none;
  line-height: 1.45;
  margin-top: 0.3rem;
  font-weight: 500;
}

.clipping-link:hover {
  text-decoration: underline;
}

/* --- Lightbox --- */
.lightbox {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 1000;
  align-items: center;
  justify-content: center;
}

.lightbox.active {
  display: flex;
}

.lightbox-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.82);
}

.lightbox-content {
  position: relative;
  z-index: 1001;
  max-width: min(92vw, 860px);
  max-height: 92vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.lightbox-close {
  align-self: flex-end;
  background: rgba(255,255,255,0.15);
  border: none;
  color: #fff;
  font-size: 1.2rem;
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 50%;
  cursor: pointer;
  transition: background 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-close:hover {
  background: rgba(255,255,255,0.3);
}

.lightbox-close:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

.lightbox-image {
  max-width: 100%;
  max-height: 78vh;
  object-fit: contain;
  border-radius: 6px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.5);
}

.lightbox-caption {
  color: rgba(255,255,255,0.8);
  font-size: 0.85rem;
  text-align: center;
  margin: 0;
  padding: 0 1rem;
}

/* --- Reduced motion --- */
@media (prefers-reduced-motion: reduce) {
  .clipping-card,
  .clipping-thumb img,
  .zoom-hint {
    transition: none;
  }
}

/* --- Mobile --- */
@media (max-width: 500px) {
  .clippings-grid {
    grid-template-columns: 1fr;
  }
  .clipping-thumb img {
    height: 260px;
  }
}
</style>

<script>
function openLightbox(src, caption) {
  const lb = document.getElementById('lightbox');
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-img').alt = caption;
  document.getElementById('lightbox-caption').textContent = caption;
  lb.classList.add('active');
  lb.focus();
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
  document.getElementById('lightbox-img').src = '';
  document.body.style.overflow = 'auto';
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeLightbox();
});
</script>
