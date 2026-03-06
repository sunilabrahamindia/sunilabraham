---
layout: default
title: "Categories"
categories: [Project pages]
description: "Index of all content categories on sunilabraham.in, including Videos, Books, Biographies, and more."
permalink: /categories/
created: 2025-10-31
---

{% assign all_pages = site.pages | where_exp: "p", "p.created" %}
{% assign cat_pages = site.pages | where_exp: "p", "p.path contains 'categories/'" | sort: "title" %}

<p>This section is a directory of all content categories on <strong>sunilabraham.in</strong>. Browse {{ cat_pages.size }} categories covering research, documentation, biographies, media, and more.</p>

<div class="controls-box">

  <div class="search-box">
    <label class="label" for="cat-search">Search:</label>
    <input id="cat-search" type="text" placeholder="Type to filter categories…" autocomplete="off" />
  </div>

  <div class="sort-section">
    <span class="label">Sort by:</span>
    <button data-sort="az" class="active">A–Z</button>
    <button data-sort="za">Z–A</button>
    <button data-sort="count">By Count</button>
  </div>

  <div class="clear-section">
    <button id="clear-btn" style="display:none;">✕ Clear</button>
  </div>

</div>

<p id="result-count" aria-live="polite" style="margin: 0.5em 0 0.25em; font-size: 0.92em; color: #444;"></p>
<p id="no-results" style="display:none; color: #a00; font-weight: bold;">No categories match your search.</p>

<ul id="cat-list" class="cat-list">
{% for cat in cat_pages %}
  {% assign cat_name = cat.title | remove: "Category:" | strip %}
  {% assign cat_count = all_pages | where_exp: "p", "p.categories contains cat_name" | size %}
  <li
    class="cat-item"
    data-name="{{ cat_name | downcase }}"
    data-count="{{ cat_count }}"
  >
    <a href="{{ cat.url | relative_url }}">{{ cat_name }}</a>
    <span class="count">({{ cat_count }})</span>
    {% if cat.description %}
      <br><small class="cat-desc">{{ cat.description }}</small>
    {% endif %}
  </li>
{% endfor %}
</ul>

<style>
.controls-box {
  background: #eef2f7;
  border: 1px solid #cad2dd;
  padding: 1em;
  border-radius: 10px;
  margin-bottom: 1em;
}

.label {
  font-weight: bold;
  margin-right: 0.5em;
}

.search-box {
  margin-bottom: 1em;
}

#cat-search {
  padding: 0.35em 0.6em;
  width: 70%;
  max-width: 320px;
  border-radius: 6px;
  border: 1px solid #7a8ea3;
}

.sort-section {
  margin-bottom: 0.5em;
}

.sort-section button {
  margin-right: 0.5em;
  margin-top: 0.3em;
  padding: 0.35em 0.75em;
  background: #fff;
  border: 1px solid #7a8ea3;
  border-radius: 6px;
  cursor: pointer;
  transition: 0.25s ease;
}

.sort-section button:hover {
  background: #dce7f9;
  border-color: #0645ad;
}

.sort-section button.active {
  background: #dce7f9;
  border-color: #0645ad;
  font-weight: bold;
}

#clear-btn {
  padding: 0.35em 0.85em;
  background: #fff3f3;
  border: 1px solid #c0392b;
  border-radius: 6px;
  color: #c0392b;
  cursor: pointer;
  font-weight: bold;
  transition: 0.25s ease;
}

#clear-btn:hover {
  background: #fde8e8;
  border-color: #922b21;
  color: #922b21;
}

.cat-list {
  list-style: disc;
  padding-left: 1.4em;
  margin-top: 0.5em;
  line-height: 1.8;
}

.cat-item a {
  color: #0645ad;
  text-decoration: none;
}

.cat-item a:hover {
  text-decoration: underline;
}

.cat-item .count {
  color: #555;
  font-size: 0.9em;
  margin-left: 0.3em;
}

.cat-item .cat-desc {
  color: #555;
  font-size: 0.88em;
  line-height: 1.5;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const list      = document.getElementById('cat-list');
  const items     = Array.from(list.querySelectorAll('li'));
  const total     = items.length;
  const searchEl  = document.getElementById('cat-search');
  const countEl   = document.getElementById('result-count');
  const noResults = document.getElementById('no-results');
  const clearBtn  = document.getElementById('clear-btn');

  let currentSort = 'az';

  function sortList(type) {
    currentSort = type;
    let sorted = [...items];
    if (type === 'az') {
      sorted.sort((a, b) => a.dataset.name.localeCompare(b.dataset.name));
    } else if (type === 'za') {
      sorted.sort((a, b) => b.dataset.name.localeCompare(a.dataset.name));
    } else if (type === 'count') {
      sorted.sort((a, b) => parseInt(b.dataset.count) - parseInt(a.dataset.count));
    }
    list.innerHTML = '';
    sorted.forEach(i => list.appendChild(i));
    document.querySelectorAll('.sort-section button').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.sort === type);
    });
  }

  function applyFilters() {
    const text = searchEl.value.toLowerCase().trim();
    let visible = 0;
    items.forEach(item => {
      const match = item.dataset.name.includes(text);
      item.style.display = match ? '' : 'none';
      if (match) visible++;
    });
    countEl.textContent = `Showing ${visible} of ${total} categories`;
    noResults.style.display = visible === 0 ? '' : 'none';
    clearBtn.style.display = (text !== '' || currentSort !== 'az') ? '' : 'none';
  }

  clearBtn.addEventListener('click', () => {
    searchEl.value = '';
    currentSort = 'az';
    sortList('az');
    applyFilters();
  });

  searchEl.addEventListener('input', applyFilters);

  document.querySelectorAll('.sort-section button').forEach(btn => {
    btn.addEventListener('click', () => {
      sortList(btn.dataset.sort);
      applyFilters();
    });
  });

  sortList('az');
  applyFilters();

});
</script>
