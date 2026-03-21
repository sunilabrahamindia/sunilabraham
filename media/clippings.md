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
    <a href="/media/civil-society-pushes-for-privacy-panel/" aria-label="Read full article: Civil Society Pushes for Privacy Panel">
      <img
        src="/media/images/civil-society-pushes-for-privacy-panel.jpg"
        alt="The Times of India clipping dated 6 May 2014 titled Civil Society Pushes for Privacy Panel"
        loading="lazy"
      >
    </a>
    <div class="clipping-caption">
      <span class="clipping-source">The Times of India</span>
      <span class="clipping-date">6 May 2014</span>
      <a href="/media/civil-society-pushes-for-privacy-panel/" class="clipping-link">Civil Society Pushes for Privacy Panel</a>
    </div>
  </article>

</div>

<style>
.clippings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.clipping-card {
  background: #fff;
  border: 1px solid #e0e6f0;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  transition: box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
}

.clipping-card:hover {
  box-shadow: 0 4px 14px rgba(0,0,0,0.12);
}

.clipping-card a img {
  width: 100%;
  height: auto;
  display: block;
  border-bottom: 1px solid #e8eef6;
}

.clipping-caption {
  padding: 0.75rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.clipping-source {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #1b2a49;
}

.clipping-date {
  font-size: 0.8rem;
  color: #777;
}

.clipping-link {
  font-size: 0.9rem;
  color: #3278d6;
  text-decoration: none;
  line-height: 1.4;
  margin-top: 0.2rem;
}

.clipping-link:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .clippings-grid {
    grid-template-columns: 1fr;
  }
}
</style>
