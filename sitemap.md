---
layout: default
title: Sitemap
categories: [Project pages]
permalink: /sitemap/
description: "Complete list of all public pages, categories, and posts on sunilabraham.in, organised and linked for easy navigation and reference."
created: 2025-10-21
---

Below is the complete sitemap of the <strong>Sunil Abraham Project</strong>, divided into <em>Pages</em>, <em>Categories</em>, and <em>Posts</em> for easy browsing.

As of {{ site.time | date: "%-d %B %Y" }}, the site contains {{ site.pages | size }} pages and {{ site.posts | size }} blog posts. This does not include support files such as PDFs, images, scripts.

To explore the newest pages on the site, please visit the [Newest Pages](/newest/){: .btn } list.

# Pages

<!-- =========================================================
     FILTER + SORT + SEARCH CONTROLS (Pages only)
     ========================================================= -->
<div class="sitemap-controls">

  <div class="control-row">
    <label for="page-search">Search:</label>
    <input id="page-search" type="text" placeholder="Type to filter pages…" />
  </div>

  <div class="control-row">
    <label for="page-sort">Sort:</label>
    <select id="page-sort">
      <option value="az">A–Z</option>
      <option value="za">Z–A</option>
      <option value="random">Random</option>
    </select>
  </div>

  <div class="control-row">
    <label for="page-cat-filter">Filter by Category:</label>
    <select id="page-cat-filter">
      <option value="all">All Categories</option>

      {% assign allpages = site.pages | where_exp: "p", "p.title" %}
      {% assign catset = "" | split: "," %}
      {% for p in allpages %}
        {% for c in p.categories %}
          {% unless catset contains c %}
            {% assign catset = catset | push: c %}
          {% endunless %}
        {% endfor %}
      {% endfor %}

      {% assign sortedcats = catset | sort %}
      {% for c in sortedcats %}
        <option value="{{ c | downcase }}">{{ c }}</option>
      {% endfor %}
    </select>
  </div>

</div>

<!-- =========================================================
     Pages (interactive list)
     ========================================================= -->
<ol id="pages-list" class="sitemap-list">
{% assign sorted_pages = site.pages | sort: "title" %}
{% for page in sorted_pages %}
{% unless page.url == '/' 
      or page.url == '/random/'
      or page.path contains 'categories/' 
      or page.path contains '_layouts' 
      or page.path contains '_includes' 
      or page.path contains '_templates' 
      or page.path contains '_short/' 
      or page.path contains '404' 
      or page.path contains 'sitemap' 
      or page.path contains 'sandbox/' %}
    {% if page.title %}
      <li 
        class="page-item"
        data-title="{{ page.title | downcase }}"
        data-cats="{{ page.categories | join: ',' | downcase }}"
      >
        <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
        {% if page.description %}
          <br><small>{{ page.description }}</small>
        {% endif %}
      </li>
    {% endif %}
  {% endunless %}
{% endfor %}
</ol>


# Categories

<ol class="sitemap-list">
{% assign category_pages = site.pages | where_exp: "p", "p.path contains 'categories/'" | sort: "title" %}
{% for cat in category_pages %}
  {% if cat.title %}
    {% assign cat_name = cat.title | remove: 'Category:' | strip %}
    {% assign cat_count = site.pages | where_exp: "p", "p.categories contains cat_name" | size %}

    {% if cat_count == 0 and cat.url == '/categories/' %}
      {% assign cat_count = category_pages.size %}
    {% endif %}

    <li>
      <a href="{{ cat.url | relative_url }}">{{ cat_name }}</a>
      <span class="count">({{ cat_count }})</span>
      {% if cat.description %}
        <br><small>{{ cat.description }}</small>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ol>


# Posts

<ol class="sitemap-list">
{% assign sorted_posts = site.posts | sort: "title" %}
{% for post in sorted_posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="date"> — {{ post.date | date: "%B %Y" }}</span>
    {% if post.description %}
      <br><small>{{ post.description }}</small>
    {% endif %}
  </li>
{% endfor %}
</ol>

<style>
/* Existing sitemap styles remain unchanged */
.sitemap-list {
  padding-left: 1.5em;
  margin-top: 0.8em;
  margin-bottom: 1.5em;
}
.sitemap-list li { margin: 0.4em 0; line-height: 1.6; }
.sitemap-list a { color: #0645ad; text-decoration: none; }
.sitemap-list a:hover { text-decoration: underline; }
.sitemap-list small { color: #555; font-size: 0.9em; }
.count { color: #444; font-size: 0.9em; margin-left: 0.3em; }
.date { color: #666; font-size: 0.9em; }

/* NEW lightweight control box */
.sitemap-controls {
  background: #f5f7fa;
  border: 1px solid #d7dde5;
  padding: 0.8em;
  border-radius: 8px;
  margin-bottom: 1.2em;
  font-size: 0.9em;
}

.control-row {
  margin-bottom: 0.6em;
}

.control-row label {
  font-weight: 600;
  margin-right: 0.4em;
}

.control-row input,
.control-row select {
  padding: 0.3em 0.5em;
  border: 1px solid #9aacc0;
  border-radius: 6px;
}

.control-row input:focus,
.control-row select:focus {
  border-color: #0645ad;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  const list = document.getElementById('pages-list');
  const items = Array.from(list.querySelectorAll('li'));

  const searchInput = document.getElementById('page-search');
  const sortSelect = document.getElementById('page-sort');
  const catSelect = document.getElementById('page-cat-filter');

  /* Combined filters */
  function applyFilters() {
    const searchText = searchInput.value.toLowerCase();
    const selectedCat = catSelect.value;

    items.forEach(item => {
      const title = item.dataset.title;
      const cats = item.dataset.cats.split(',');

      const searchMatch = title.includes(searchText);
      const catMatch = (selectedCat === "all" || cats.includes(selectedCat));

      if (searchMatch && catMatch) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }

  searchInput.addEventListener('input', applyFilters);
  catSelect.addEventListener('change', applyFilters);

  /* Sorting */
  function sortList() {
    let sorted = [...items];

    const type = sortSelect.value;

    if (type === "az") {
      sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
    }
    else if (type === "za") {
      sorted.sort((a, b) => b.dataset.title.localeCompare(a.dataset.title));
    }
    else if (type === "random") {
      sorted.sort(() => Math.random() - 0.5);
    }

    list.innerHTML = "";
    sorted.forEach(item => list.appendChild(item));
  }

  sortSelect.addEventListener('change', sortList);

});
</script>
