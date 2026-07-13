---
layout: default
title: "TSAP Documentation"
description: "Documentation hub for The Sunil Abraham Project, including architecture, workflows, and editorial standards."
categories: [TSAP Documentation]
permalink: /tsap/
page_id: TSAP-0727
created: 2026-03-18
---

{% include documentation-notice.html %}

Welcome to the **documentation hub** for **The Sunil Abraham Project** (TSAP). This section documents how the site is structured, how content is created, and how systems evolve over time.

<h2 id="documentation-pages">Documentation Pages</h2>

<p>
The following pages form the documentation corpus of The Sunil Abraham Project (TSAP). This list is generated automatically from pages categorised as "TSAP Documentation".
</p>

{% assign docs = site.pages | concat: site.documents | sort: "created" | reverse %}

{% assign doc_count = 0 %}
{% for page in docs %}
  {% if page.categories contains "TSAP Documentation" and page.url != "/tsap/" %}
    {% assign doc_count = doc_count | plus: 1 %}
  {% endif %}
{% endfor %}

<p class="doc-count">
  {{ doc_count }} documentation page{% unless doc_count == 1 %}s{% endunless %}.
</p>

<div class="doc-controls">
  <label for="doc-sort">Sort by:</label>
  <select id="doc-sort" aria-label="Sort documentation pages">
    <option value="created-desc">Created (newest)</option>
    <option value="created-asc">Created (oldest)</option>
    <option value="title-asc">A–Z</option>
    <option value="title-desc">Z–A</option>
  </select>
</div>

<div id="doc-pages-list">

  {% for page in docs %}
    {% if page.categories contains "TSAP Documentation" and page.url != "/tsap/" %}

    <article
      class="doc-card"
      data-title="{{ page.title | downcase }}"
      data-created="{{ page.created }}">

      <h3 class="doc-card-title">
        <a href="{{ page.url }}">{{ page.title }}</a>
      </h3>

      {% if page.description %}
      <p class="doc-card-description">
        {{ page.description }}
      </p>
      {% endif %}

      {% if page.created %}
      <p class="doc-card-meta">
        Created: {{ page.created | date: "%-d %B %Y" }}
      </p>
      {% endif %}

    </article>

    {% endif %}
  {% endfor %}

</div>

<style>
.doc-count {
  color: #444;
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

.doc-controls {
  margin: 1rem 0 1.5rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.6rem;
}

.doc-controls label {
  font-weight: 600;
}

.doc-controls select {
  padding: 0.45rem 0.7rem;
  border: 1px solid #888;
  border-radius: 6px;
  font-size: 0.95rem;
  background: #fff;
  color: #222;
}

#doc-pages-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.doc-card {
  padding: 1rem 1.25rem;
  border-left: 4px solid #1f5fbf;
  background: #f8faff;
  border-radius: 8px;
}

.doc-card-title {
  margin: 0 0 0.4rem;
  font-size: 1.05rem;
}

.doc-card-title a {
  color: #003f8a;
  text-decoration: none;
}

.doc-card-title a:hover,
.doc-card-title a:focus {
  text-decoration: underline;
}

.doc-card-title a:focus {
  outline: 2px solid #1f5fbf;
  outline-offset: 2px;
}

.doc-card-description {
  margin: 0 0 0.5rem;
  color: #444;
  line-height: 1.6;
}

.doc-card-meta {
  margin: 0;
  font-size: 0.9rem;
  color: #444;
}

@media (max-width: 768px) {
  .doc-controls {
    flex-direction: column;
    align-items: stretch;
  }

  .doc-controls select {
    width: 100%;
  }

  .doc-card {
    padding: 0.9rem 1rem;
  }
}

/* =========================================================
   Active Class Architecture Dark Mode Overrides
   ========================================================= */

body.tsap-dark-mode .doc-count {
  color: var(--text-muted, #cbd5e1) !important;
}

body.tsap-dark-mode .doc-controls select {
  background-color: #1e293b !important;
  color: #f3f4f6 !important;
  border-color: #4b5563 !important;
}

body.tsap-dark-mode .doc-card {
  background-color: #1e293b !important;
  border-left-color: #38bdf8 !important;
}

body.tsap-dark-mode .doc-card-title a {
  color: #38bdf8 !important;
}

body.tsap-dark-mode .doc-card-title a:hover {
  color: #7dd3fc !important;
}

body.tsap-dark-mode .doc-card-description {
  color: #cbd5e1 !important;
}

body.tsap-dark-mode .doc-card-meta {
  color: #94a3b8 !important;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {

  const select = document.getElementById('doc-sort');
  const container = document.getElementById('doc-pages-list');

  if (!select || !container) return;

  function sortCards() {

    const cards = Array.from(
      container.querySelectorAll('.doc-card')
    );

    const mode = select.value;

    cards.sort((a, b) => {

      const titleA = a.dataset.title;
      const titleB = b.dataset.title;

      const dateA = a.dataset.created || '';
      const dateB = b.dataset.created || '';

      switch (mode) {

        case 'title-asc':
          return titleA.localeCompare(titleB);

        case 'title-desc':
          return titleB.localeCompare(titleA);

        case 'created-asc':
          return dateA.localeCompare(dateB);

        default:
          return dateB.localeCompare(dateA);

      }
    });

    cards.forEach(card => container.appendChild(card));
  }

  select.addEventListener('change', sortCards);

  sortCards();

});
</script>
