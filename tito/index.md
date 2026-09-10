---
layout: default
title: Tito Dutta (Zone)
categories: [Project pages, Tito Dutta]
description: Writings, essays, articles, papers, and other works by Tito Dutta.
permalink: /tito/
page_id: TSAP-1216
created: 2026-08-16
---

{% include under-construction.html %}

The **Tito Dutta** zone is a dedicated space for his writings and other works. The content presented here is related to The Sunil Abraham Project, either directly or through the project's broader scope and areas of interest.

Gradually, content and subpages will be added here, and this page will serve as the index (main) page.

**Note:** As I will be writing this content myself, unlike the rest of the website, many of the writings in this zone will use a first-person narrative.

## Works

### The Witness

An interactive visual meditation on the idea of the Witness — awareness that remains still while the cosmos moves.

[Explore The Witness](/tito/witness/)

### Simulations

#### Simulation #1

An artificial-life experiment exploring autonomous organisms, ecology, evolution, resource competition, and emergent behaviour.

[Explore Simulation #1](/tito/s1/)

### TSPA

An original comic strip created as part of The Sunil Abraham Project. TSPA is a rearrangement of TSAP, the short form of The Sunil Abraham Project.

[Explore TSPA](/tspa/)

## Essays by Tito Dutta

{% assign tito_essays = site.pages | where_exp: "p", "p.categories contains 'Essays by Tito Dutta'" | sort: "created" | reverse %}

<div class="tito-essays-controls" role="group" aria-label="Essay sorting">
  <span class="tito-essays-label">Sort by:</span>
  <button type="button" data-tito-sort="newest" class="active">Newest</button>
  <button type="button" data-tito-sort="oldest">Oldest</button>
  <button type="button" data-tito-sort="az">A–Z</button>
</div>

<ol id="tito-essays-list" class="tito-essays-list">
{% for page in tito_essays %}
  <li class="tito-essay-item"
      data-title="{{ page.title | downcase | escape }}"
      data-created="{{ page.created }}">
    <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    {% if page.created %}<span class="tito-essay-date"> — {{ page.created | date: "%d %B %Y" }}</span>{% endif %}
  </li>
{% endfor %}
</ol>

{% if tito_essays.size == 0 %}
<p>No essays have been added yet.</p>
{% endif %}

<style>
.tito-essays-controls {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5em;
  margin: 0.75em 0 1em;
}

.tito-essays-label {
  font-weight: bold;
  margin-right: 0.25em;
}

.tito-essays-controls button {
  padding: 0.4em 0.75em;
  background: #fff;
  color: #222;
  border: 1px solid #7a8ea3;
  border-radius: 6px;
  cursor: pointer;
  font: inherit;
  line-height: 1.3;
}

.tito-essays-controls button:hover,
.tito-essays-controls button:focus-visible,
.tito-essays-controls button.active {
  background: #dce7f9;
  border-color: #0645ad;
  color: #111;
}

.tito-essays-controls button:focus-visible {
  outline: 3px solid #0645ad;
  outline-offset: 2px;
}

.tito-essays-list {
  padding-left: 2.8em;
  line-height: 1.6;
}

.tito-essay-item a {
  color: #0645ad;
  text-decoration: none;
}

.tito-essay-item a:hover,
.tito-essay-item a:focus-visible {
  text-decoration: underline;
}

.tito-essay-item a:focus-visible {
  outline: 3px solid #0645ad;
  outline-offset: 2px;
}

.tito-essay-date {
  color: #555;
  font-size: 0.9em;
}

/* =========================================================
   Dark Mode - follows the audited Newest Pages treatment
   ========================================================= */

body.tsap-dark-mode .tito-essays-controls button {
  background: #374151;
  color: #e5e7eb;
  border-color: #4b5563;
}

body.tsap-dark-mode .tito-essays-controls button:hover,
body.tsap-dark-mode .tito-essays-controls button:focus-visible,
body.tsap-dark-mode .tito-essays-controls button.active {
  background: #1f5fbf;
  color: #ffffff;
  border-color: #1f5fbf;
}

body.tsap-dark-mode .tito-essays-controls button:focus-visible {
  outline-color: #93c5fd;
}

body.tsap-dark-mode .tito-essay-item a {
  color: #93c5fd;
}

body.tsap-dark-mode .tito-essay-item a:hover,
body.tsap-dark-mode .tito-essay-item a:focus-visible {
  color: #bfdbfe;
}

body.tsap-dark-mode .tito-essay-item a:focus-visible {
  outline-color: #93c5fd;
}

body.tsap-dark-mode .tito-essay-date {
  color: #94a3b8;
}

@media (max-width: 600px) {
  .tito-essays-controls {
    align-items: stretch;
  }

  .tito-essays-label {
    flex-basis: 100%;
  }

  .tito-essays-controls button {
    flex: 1 1 auto;
    min-width: 0;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const list = document.getElementById('tito-essays-list');
  if (!list) return;

  const items = Array.from(list.querySelectorAll('.tito-essay-item'));
  const buttons = Array.from(document.querySelectorAll('[data-tito-sort]'));

  function sortEssays(type) {
    const sorted = [...items];

    if (type === 'newest') {
      sorted.sort((a, b) => new Date(b.dataset.created) - new Date(a.dataset.created));
    } else if (type === 'oldest') {
      sorted.sort((a, b) => new Date(a.dataset.created) - new Date(b.dataset.created));
    } else if (type === 'az') {
      sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
    }

    list.replaceChildren(...sorted);
    buttons.forEach(button => {
      button.classList.toggle('active', button.dataset.titoSort === type);
    });
  }

  buttons.forEach(button => {
    button.addEventListener('click', () => sortEssays(button.dataset.titoSort));
  });

  sortEssays('newest');
});
</script>
