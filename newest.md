---
layout: default
title: "Newest Pages"
permalink: /newest/
categories: [Project pages]
description: "Browse the latest website pages added to sunilabraham.in, sorted by creation date with options for filtering and interactive sorting."
created: 2025-11-22
---

Welcome to the Newest Pages index for sunilabraham.in. This page helps you explore the most recently added content across the site, organised neatly by their actual creation date.  

As you continue adding `created:` dates to pages, this list will automatically grow and stay up to date. Use the sorting and month filters below to quickly browse the freshest additions.

## Sort & Filter

<div class="controls-box">
  <div class="sort-section">
    <span class="label">Sort by:</span>
    <button data-sort="newest">Newest</button>
    <button data-sort="oldest">Oldest</button>
    <button data-sort="az">A–Z</button>
    <button data-sort="random">Random</button>
  </div>

  <div class="month-filter">
    <label for="month-select" class="label">Filter by Month:</label>
    <select id="month-select">
      <option value="all">All Months</option>
      {% assign filtered = site.pages | where_exp: "p", "p.created" %}
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
  >
    <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    <span class="created-date"> — {{ page.created | date: "%d %B %Y" }}</span>
  </li>
{% endfor %}
</ol>

<style>
/* Container styling */
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

/* Buttons */
.sort-section button {
  margin-right: 0.5em;
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

/* Month filter */
.month-filter {
  margin-top: 1em;
}

#month-select {
  padding: 0.35em;
  border-radius: 6px;
  border: 1px solid #7a8ea3;
  cursor: pointer;
  transition: 0.25s ease;
}
#month-select:hover {
  border-color: #0645ad;
}

/* Pages list */
.created-pages {
  padding-left: 1.4em;
  line-height: 1.6;
}

/* Animation for items */
.page-item {
  opacity: 0;
  transform: translateY(5px);
  animation: fadeInUp 0.4s ease forwards;
}

.page-item a {
  text-decoration: none;
  color: #0645ad;
}

.page-item a:hover {
  text-decoration: underline;
}

.created-date {
  color: #555;
  font-size: 0.9em;
}

/* Fade-in animation */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const list = document.getElementById('created-pages-list');
  const items = Array.from(list.querySelectorAll('li'));

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

  /* MONTH FILTER */
  const monthSelect = document.getElementById('month-select');
  monthSelect.addEventListener('change', () => {
    const selected = monthSelect.value;
    items.forEach(item => {
      if (selected === "all" || item.dataset.month === selected) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  });

});
</script>
