---
layout: default
title: "Newest Pages"
permalink: /newest/
categories: [Project pages]
description: "Browse the latest website pages added to sunilabraham.in, sorted by creation date with options for filtering, searching, and interactive sorting."
exclude_from_backlinks: true
page_id: TSAP-0111
created: 2025-11-22
---

Welcome to the **Newest Pages** index for the **Sunil Abraham Project** (TSAP). This page helps to explore the most recently added content across the site, organised by their actual **creation date**.

Please use the sorting, category/month filters, and search box to browse the freshest content.

## Sort & Filter

<div class="controls-box">

  <!-- SEARCH -->
  <div class="search-box">
    <label class="label" for="search-input">Search:</label>
    <input id="search-input" type="text" placeholder="Type to filter pages…" autocomplete="off" />
  </div>

  <!-- SORT -->
  <div class="sort-section">
    <span class="label">Sort by:</span>
    <button data-sort="newest" class="active">Newest</button>
    <button data-sort="oldest">Oldest</button>
    <button data-sort="az">A–Z</button>
    <button data-sort="random">Random</button>
  </div>

  <!-- CATEGORY FILTER -->
  <div class="category-filter">
    <label for="cat-select" class="label">Filter by Category:</label>
    <select id="cat-select">
      <option value="all">All Categories</option>

      {% assign filtered = site.pages | where_exp: "p", "p.created" %}
      {% assign catlist = "" | split: "," %}
      {% for page in filtered %}
        {% for c in page.categories %}
          {% unless catlist contains c %}
            {% assign catlist = catlist | push: c %}
          {% endunless %}
        {% endfor %}
      {% endfor %}

      {% assign sorted_cats = catlist | sort %}
      {% for c in sorted_cats %}
        <option value="{{ c | downcase }}">{{ c }}</option>
      {% endfor %}
    </select>
  </div>

  <!-- MONTH FILTER -->
  <div class="month-filter">
    <label for="month-select" class="label">Filter by Month:</label>
    <select id="month-select">
      <option value="all">All Months</option>

      {% assign months = "" | split: "," %}
      {% for page in filtered %}
        {% assign m = page.created | date: "%Y-%m" %}
        {% unless months contains m %}
          {% assign months = months | push: m %}
        {% endunless %}
      {% endfor %}

      {% assign sorted_months = months | sort | reverse %}
      {% for m in sorted_months %}
        <option value="{{ m }}">{{ m | date: "%B %Y" }}</option>
      {% endfor %}
    </select>
  </div>

  <!-- CLEAR FILTERS -->
  <div class="clear-section">
    <button id="clear-btn" style="display:none;">✕ Clear Filters</button>
  </div>

</div>

<p id="result-count" aria-live="polite" style="margin: 0.5em 0 0.25em; font-size: 0.92em; color: #444;"></p>
<p id="no-results" style="display:none; color: #a00; font-weight: bold;">No pages match your filters.</p>

## Pages

<ol id="created-pages-list" class="created-pages">
{% assign sorted = filtered | sort: "created" | reverse %}
{% for page in sorted %}
<li
  class="page-item"
  data-title="{{ page.title | downcase }}"
  data-created="{{ page.created }}"
  data-month="{{ page.created | date: "%Y-%m" }}"
  data-year="{{ page.created | date: "%Y" }}"
  data-cats="{{ page.categories | join: '|' | downcase }}"
>
  <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
  <span class="created-date"> — {{ page.created | date: "%d %B %Y" }}</span>
</li>
{% endfor %}
</ol>

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

#search-input {
  padding: 0.35em 0.6em;
  width: 70%;
  max-width: 320px;
  border-radius: 6px;
  border: 1px solid #7a8ea3;
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

select {
  padding: 0.35em;
  border-radius: 6px;
  border: 1px solid #7a8ea3;
  cursor: pointer;
  transition: 0.25s ease;
}

select:hover {
  border-color: #0645ad;
}

.clear-section {
  margin-top: 0.75em;
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

.created-pages {
  padding-left: 2.8em;
  line-height: 1.6;
}

.page-item {
  opacity: 0;
  transform: translateY(5px);
  animation: fadeInUp 0.4s ease forwards;
}

.page-item a {
  color: #0645ad;
  text-decoration: none;
}

.page-item a:hover {
  text-decoration: underline;
}

.created-date {
  color: #555;
  font-size: 0.9em;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* =========================================================
   Dark Mode
   ========================================================= */

body.tsap-dark-mode .controls-box {
  background: #1f2937;
  border-color: #374151;
}

body.tsap-dark-mode #search-input,
body.tsap-dark-mode select {
  background: #374151;
  color: #f3f4f6;
  border-color: #4b5563;
}

body.tsap-dark-mode #search-input::placeholder {
  color: #94a3b8;
}

body.tsap-dark-mode .sort-section button {
  background: #374151;
  color: #e5e7eb;
  border-color: #4b5563;
}

body.tsap-dark-mode .sort-section button:hover,
body.tsap-dark-mode .sort-section button.active {
  background: #1f5fbf;
  color: #ffffff;
  border-color: #1f5fbf;
}

body.tsap-dark-mode #clear-btn {
  background: #4b1f1f;
  color: #fecaca;
  border-color: #dc2626;
}

body.tsap-dark-mode #clear-btn:hover {
  background: #5f2626;
}

body.tsap-dark-mode #result-count {
  color: #cbd5e1 !important;
}

body.tsap-dark-mode #no-results {
  color: #fca5a5;
}

body.tsap-dark-mode .page-item a {
  color: #93c5fd;
}

body.tsap-dark-mode .page-item a:hover {
  color: #bfdbfe;
}

body.tsap-dark-mode .created-date {
  color: #94a3b8;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const list        = document.getElementById('created-pages-list');
  const items       = Array.from(list.querySelectorAll('li'));
  const totalCount  = items.length;

  const catSelect   = document.getElementById('cat-select');
  const monthSelect = document.getElementById('month-select');
  const searchInput = document.getElementById('search-input');
  const countEl     = document.getElementById('result-count');
  const noResults   = document.getElementById('no-results');
  const clearBtn    = document.getElementById('clear-btn');

  let currentSort  = 'newest';
  let activeYear   = null; // set only via URL ?year=, never by dropdown

  /* ── URL STATE ── */
  function readURL() {
    const params = new URLSearchParams(window.location.search);
    if (params.get('cat'))    catSelect.value   = params.get('cat');
    if (params.get('month'))  monthSelect.value = params.get('month');
    if (params.get('search')) searchInput.value = params.get('search');
    if (params.get('sort'))   currentSort       = params.get('sort');
    if (params.get('year'))   activeYear        = params.get('year');
  }

  function writeURL() {
    // Read the current parameters to find and protect the darkmode flag
    const currentParams = new URLSearchParams(window.location.search);
    const darkmodeValue = currentParams.get('darkmode');

    const params = new URLSearchParams();
    if (catSelect.value   !== 'all') params.set('cat',    catSelect.value);
    if (monthSelect.value !== 'all') params.set('month',  monthSelect.value);
    if (searchInput.value !== '')    params.set('search', searchInput.value);
    if (currentSort !== 'newest')    params.set('sort',   currentSort);
    if (activeYear)                  params.set('year',   activeYear);
    
    // Safely re-inject darkmode back into the history parameters if it was present
    if (darkmodeValue !== null) {
      params.set('darkmode', darkmodeValue);
    }

    const newURL = params.toString()
      ? window.location.pathname + '?' + params.toString()
      : window.location.pathname;
    history.replaceState(null, '', newURL);
  }

  /* ── CLEAR FILTERS VISIBILITY ── */
  function updateClearBtn() {
    const isFiltered = catSelect.value !== 'all'
      || monthSelect.value !== 'all'
      || searchInput.value.trim() !== ''
      || currentSort !== 'newest'
      || activeYear !== null;
    clearBtn.style.display = isFiltered ? '' : 'none';
  }

  /* ── SORT ── */
  function sortList(type) {
    currentSort = type;
    let sorted = [...items];
    if (type === 'newest') {
      sorted.sort((a, b) => new Date(b.dataset.created) - new Date(a.dataset.created));
    } else if (type === 'oldest') {
      sorted.sort((a, b) => new Date(a.dataset.created) - new Date(b.dataset.created));
    } else if (type === 'az') {
      sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
    } else if (type === 'random') {
      sorted.sort(() => Math.random() - 0.5);
    }
    list.innerHTML = '';
    sorted.forEach(item => list.appendChild(item));

    document.querySelectorAll('.sort-section button').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.sort === type);
    });
  }

  /* ── FILTER ── */
  function applyFilters() {
    const selectedCat   = catSelect.value;
    const selectedMonth = monthSelect.value;
    const searchText    = searchInput.value.toLowerCase().trim();

    let visible = 0;
    items.forEach(item => {
      const cats      = item.dataset.cats.split('|');
      const itemMonth = item.dataset.month;
      const itemYear  = item.dataset.year;
      const title     = item.dataset.title;

      const catMatch    = (selectedCat   === 'all' || cats.includes(selectedCat));
      const monthMatch  = (selectedMonth === 'all' || itemMonth === selectedMonth);
      const yearMatch   = (activeYear === null      || itemYear === activeYear);
      const searchMatch = title.includes(searchText);

      if (catMatch && monthMatch && yearMatch && searchMatch) {
        item.style.display = '';
        visible++;
      } else {
        item.style.display = 'none';
      }
    });

    countEl.textContent = `Showing ${visible.toLocaleString()} of ${totalCount.toLocaleString()} pages`;
    noResults.style.display = visible === 0 ? '' : 'none';

    updateClearBtn();
    writeURL();
  }

  /* ── CLEAR ── */
  clearBtn.addEventListener('click', () => {
    catSelect.value   = 'all';
    monthSelect.value = 'all';
    searchInput.value = '';
    currentSort       = 'newest';
    activeYear        = null;
    sortList('newest');
    applyFilters();
  });

  /* ── EVENTS ── */
  catSelect.addEventListener('change',   applyFilters);
  monthSelect.addEventListener('change', applyFilters);
  searchInput.addEventListener('input',  applyFilters);

  document.querySelectorAll('.sort-section button').forEach(btn => {
    btn.addEventListener('click', () => {
      sortList(btn.dataset.sort);
      applyFilters();
    });
  });

  /* ── INIT ── */
  readURL();
  sortList(currentSort);
  applyFilters();

});
</script>
