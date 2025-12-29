---
layout: default
title: "Media Mentions"
categories: [Media mentions]
description: "Index of media coverage featuring Sunil Abraham, including interviews, quotations, profiles, and reporting across newspapers, magazines, and digital platforms."
permalink: /media/
created: 2025-12-06
---

Over the years, Sunil Abraham's work in technology policy, digital rights, internet governance, and institutional leadership has been covered by a wide range of media outlets. These pieces — whether they are interviews, quotations, profiles, or news reports — form a valuable part of the public record. They help trace how ideas have travelled, how debates have shifted, and how organisations, policymakers and journalists have engaged with questions of openness, privacy, platforms and technology governance.

To keep the site organised, all media-related material is stored inside the **`/media/`** directory. This includes coverage from newspapers, magazines, online newsrooms, and specialist technology publications. Each article reproduced here follows a consistent archival format: contextual introduction, publication details, and the full text from the original source, whenever available.

## List

### Search and sort

<div class="media-controls">
  <input
    type="search"
    id="media-search"
    placeholder="Search titles or sources…"
    aria-label="Search media mentions"
  >

  <div class="sort-controls">
    <button data-sort="date_desc">Newest First</button>
    <button data-sort="date_asc">Oldest First</button>
    <button data-sort="alpha">Alphabetical</button>
  </div>

  <div id="media-count" class="media-count"></div>
</div>

{% comment %}
Collect media pages
{% endcomment %}
{% assign media_list = site.pages
     | where_exp: "p", "p.path contains 'media/'"
     | where_exp: "p", "p.path != 'media/index.md'"
     | sort: "date"
     | reverse
%}

<div id="media-container">
{% assign current_year = "" %}
{% for page in media_list %}
  {% assign page_year = page.date | date: "%Y" %}

  {% if page_year != current_year %}
    {% unless forloop.first %}
      </ol>
    </div>
    {% endunless %}

    <div class="year-group" data-year="{{ page_year }}">
      <button class="year-toggle" aria-expanded="true">
        {{ page_year }}
      </button>
      <ol class="media-list">
    {% assign current_year = page_year %}
  {% endif %}

    <li
      data-title="{{ page.title | downcase }}"
      data-source="{{ page.source | downcase }}"
      data-date="{{ page.date | date: '%Y-%m-%d' }}"
    >
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a><br>
      <span class="meta">
        {{ page.source }} • {{ page.date | date: "%-d %B %Y" }}
      </span>
    </li>

{% endfor %}
      </ol>
    </div>
</div>

## See also
- [Clusters](/clusters), thematic groupings that bring together related pieces of writing or coverage

<style>
.media-controls {
  margin: 1rem 0 1.4rem 0;
}

#media-search {
  width: 100%;
  max-width: 420px;
  padding: 0.55rem 0.7rem;
  margin-bottom: 0.7rem;
  border: 1px solid #cdd7e5;
  border-radius: 6px;
  font-size: 0.95rem;
}

#media-search:focus {
  outline: 2px solid #3278d6;
  outline-offset: 2px;
}

.sort-controls {
  margin-bottom: 0.4rem;
}

.sort-controls button {
  background: #eef3fa;
  border: 1px solid #cdd7e5;
  padding: 0.45rem 0.85rem;
  margin-right: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
}

.sort-controls button:hover {
  background: #dbe6f5;
}

.sort-controls button.active-sort {
  background: #3278d6;
  color: #fff;
  border-color: #3278d6;
}

.media-count {
  font-size: 0.9rem;
  color: #555;
  margin-top: 0.2rem;
}

.year-group {
  margin-bottom: 1.4rem;
}

.year-toggle {
  background: none;
  border: none;
  font-size: 1.15rem;
  font-weight: 600;
  padding: 0;
  cursor: pointer;
  margin-bottom: 0.4rem;
}

.year-toggle:focus {
  outline: 2px solid #3278d6;
  outline-offset: 2px;
}

.media-list li {
  margin-bottom: 0.85rem;
}

.meta {
  font-size: 0.9rem;
  color: #555;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('media-search');
  const countBox = document.getElementById('media-count');
  const sortButtons = document.querySelectorAll('.sort-controls button');
  const yearGroups = Array.from(document.querySelectorAll('.year-group'));

  let currentSort = localStorage.getItem('mediaSort') || 'date_desc';

  function getAllItems() {
    return Array.from(document.querySelectorAll('.media-list li'));
  }

  function updateCount() {
    const visible = getAllItems().filter(li => li.style.display !== 'none').length;
    countBox.textContent = `Showing ${visible} articles`;
  }

  function applySearch() {
    const query = searchInput.value.toLowerCase();

    yearGroups.forEach(group => {
      let groupVisible = false;
      const items = group.querySelectorAll('li');

      items.forEach(li => {
        const text = li.dataset.title + ' ' + li.dataset.source;
        const match = text.includes(query);
        li.style.display = match ? '' : 'none';
        if (match) groupVisible = true;
      });

      group.style.display = groupVisible ? '' : 'none';
    });

    updateCount();
  }

  function sortWithinYears(type) {
    yearGroups.forEach(group => {
      const list = group.querySelector('.media-list');
      const items = Array.from(list.querySelectorAll('li'));

      let sorted = [...items];

      if (type === 'alpha') {
        sorted.sort((a, b) =>
          a.dataset.title.localeCompare(b.dataset.title)
        );
      } else if (type === 'date_asc') {
        sorted.sort((a, b) =>
          a.dataset.date.localeCompare(b.dataset.date)
        );
      } else {
        sorted.sort((a, b) =>
          b.dataset.date.localeCompare(a.dataset.date)
        );
      }

      list.innerHTML = '';
      sorted.forEach(li => list.appendChild(li));
    });

    sortButtons.forEach(btn => btn.classList.remove('active-sort'));
    document.querySelector(`[data-sort="${type}"]`).classList.add('active-sort');
    localStorage.setItem('mediaSort', type);
  }

  // Year toggle behaviour
  document.querySelectorAll('.year-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const list = btn.nextElementSibling;
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', !expanded);
      list.style.display = expanded ? 'none' : '';
    });
  });

  // Initial state
  sortWithinYears(currentSort);
  updateCount();

  // Events
  sortButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      sortWithinYears(btn.dataset.sort);
    });
  });

  searchInput.addEventListener('input', applySearch);
});
</script>
