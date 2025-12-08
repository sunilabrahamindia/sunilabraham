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

## Media Mentions

### Sort by:
<div class="sort-controls">
  <button data-sort="year_desc">Newest First</button>
  <button data-sort="year_asc">Oldest First</button>
  <button data-sort="alpha">Alphabetical</button>
</div>

{% comment %}
Collect media pages
{% endcomment %}
{% assign media_list = site.pages 
     | where_exp: "p", "p.path contains 'media/'" 
     | where_exp: "p", "p.path != 'media/index.md'" 
%}

<ol id="media-list">
{% for page in media_list %}
  <li data-title="{{ page.title | downcase }}"
      data-year="{{ page.date | date: '%Y' }}">
    <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    <br>
    <span class="meta">{{ page.source }} • {{ page.date | date: "%Y" }}</span>
  </li>
{% endfor %}
</ol>

<style>
.sort-controls {
  margin: 0.8rem 0 1.2rem 0;
}
.sort-controls button {
  background: #eef3fa;
  border: 1px solid #cdd7e5;
  padding: 0.45rem 0.85rem;
  margin-right: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.2s ease;
}
.sort-controls button:hover {
  background: #dbe6f5;
}
.sort-controls button.active-sort {
  background: #3278d6;
  color: #fff;
  border-color: #3278d6;
}
.meta {
  font-size: 0.9rem;
  color: #555;
}
#media-list li {
  margin-bottom: 0.8rem;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const list = document.getElementById('media-list');
  const items = Array.from(list.querySelectorAll('li'));
  const buttons = document.querySelectorAll('.sort-controls button');

  function sortList(type) {
    let sorted = [...items];

    if (type === 'alpha') {
      sorted.sort((a, b) =>
        a.dataset.title.localeCompare(b.dataset.title)
      );
    } else if (type === 'year_asc') {
      sorted.sort((a, b) =>
        a.dataset.year.localeCompare(b.dataset.year)
      );
    } else {
      sorted.sort((a, b) =>
        b.dataset.year.localeCompare(a.dataset.year)
      );
    }

    list.innerHTML = '';
    sorted.forEach(li => list.appendChild(li));

    buttons.forEach(btn => btn.classList.remove('active-sort'));
    document.querySelector(`[data-sort="${type}"]`).classList.add('active-sort');
  }

  // Default sort: newest first
  sortList('year_desc');

  // Add click handlers
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      sortList(btn.dataset.sort);
    });
  });
});
</script>
