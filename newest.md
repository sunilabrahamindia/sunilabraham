---
layout: default
title: "Newest Pages"
permalink: /newest/
categories: [Project pages]
description: "Browse the latest website pages added to sunilabraham.in, sorted by creation date with options for filtering, searching, and interactive sorting."
created: 2025-11-22
---

Welcome to the Newest Pages index for the **Sunil Abraham Project** This page helps you explore the most recently added content across the site, organised neatly by their actual creation date.

Please use the sorting, category/month filters, and search box to browse the freshest content.

## Sort & Filter

<div class="controls-box">

  <!-- SEARCH -->
  <div class="search-box">
    <label class="label" for="search-input">Search:</label>
    <input id="search-input" type="text" placeholder="Type to filter pages…" />
  </div>

  <!-- SORT -->
  <div class="sort-section">
    <span class="label">Sort by:</span>
    <button data-sort="newest">Newest</button>
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

</div>

## Pages

<ol id="created-pages-list" class="created-pages">
{% assign sorted = filtered | sort: "created" | reverse %}
{% for page in sorted %}
<li 
  class="page-item"
  data-title="{{ page.title | downcase }}"
  data-created="{{ page.created }}"
  data-month="{{ page.created | date: "%Y-%m" }}"
  data-cats="{{ page.categories | join: ',' | downcase }}"
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
  margin-bottom: 1.5em;
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

.created-pages {
  padding-left: 1.4em;
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
  to { opacity: 1; transform: translateY(0); }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const list = document.getElementById('created-pages-list');
  const items = Array.from(list.querySelectorAll('li'));

  const catSelect = document.getElementById('cat-select');
  const monthSelect = document.getElementById('month-select');
  const searchInput = document.getElementById('search-input');

  /* UNIFIED FILTER FUNCTION */
  function applyFilters() {
    const selectedCat = catSelect.value;
    const selectedMonth = monthSelect.value;
    const searchText = searchInput.value.toLowerCase();

    items.forEach(item => {
      const cats = item.dataset.cats.split(',');
      const itemMonth = item.dataset.month;
      const title = item.dataset.title;

      const catMatch = (selectedCat === "all" || cats.includes(selectedCat));
      const monthMatch = (selectedMonth === "all" || itemMonth === selectedMonth);
      const searchMatch = title.includes(searchText);

      if (catMatch && monthMatch && searchMatch) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }

  /* Apply filter on change */
  catSelect.addEventListener('change', applyFilters);
  monthSelect.addEventListener('change', applyFilters);
  searchInput.addEventListener('input', applyFilters);

  /* SORTING */
  function sortList(type) {
    let sorted = [...items];

    if (type === 'newest') {
      sorted.sort((a, b) => new Date(b.dataset.created) - new Date(a.dataset.created));
    }
    else if (type === 'oldest') {
      sorted.sort((a, b) => new Date(a.dataset.created) - new Date(b.dataset.created));
    }
    else if (type === 'az') {
      sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
    }
    else if (type === 'random') {
      sorted.sort(() => Math.random() - 0.5);
    }

    list.innerHTML = "";
    sorted.forEach(item => list.appendChild(item));
  }

  document.querySelectorAll('.sort-section button').forEach(btn => {
    btn.addEventListener('click', () => sortList(btn.dataset.sort));
  });

});
</script>
