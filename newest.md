---
layout: default
title: "Newest Pages"
permalink: /newest/
categories: [Project pages]
created: 2025-11-22
---


This page lists website pages ordered by their **creation date**. Only pages with a `created` field will appear here. As we add created dates to more pages, they will automatically show up below.


## Sort Options

<div class="sort-controls" aria-label="Sort options">
  <button data-sort="newest">Newest</button>
  <button data-sort="oldest">Oldest</button>
  <button data-sort="az">A–Z</button>
  <button data-sort="random">Random</button>
</div>

## Pages

<ol id="created-pages-list" class="created-pages">
{% assign filtered = site.pages | where_exp: "p", "p.created" %}
{% assign sorted = filtered | sort: "created" | reverse %}

{% for page in sorted %}
  <li data-title="{{ page.title | downcase }}" data-created="{{ page.created }}">
    <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    <span class="created-date"> — {{ page.created | date: "%d %B %Y" }}</span>
  </li>
{% endfor %}
</ol>

<style>
.created-pages {
  padding-left: 1.4em;
  line-height: 1.6;
  margin-top: 1em;
}

.created-pages li {
  margin: 0.5em 0;
}

.sort-controls {
  margin: 1em 0;
  padding: 0.6em;
  background: #f2f4f5;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.sort-controls button {
  margin-right: 0.5em;
  padding: 0.35em 0.7em;
  border: 1px solid #888;
  border-radius: 6px;
  cursor: pointer;
  background: #fff;
}

.sort-controls button:hover {
  background: #e6eefb;
  border-color: #0645ad;
}

.created-date {
  color: #555;
  font-size: 0.9em;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {

  function sortList(type) {
    const list = document.getElementById('created-pages-list');
    const items = Array.from(list.querySelectorAll('li'));

    if (type === 'newest') {
      items.sort((a, b) => new Date(b.dataset.created) - new Date(a.dataset.created));
    } 
    else if (type === 'oldest') {
      items.sort((a, b) => new Date(a.dataset.created) - new Date(b.dataset.created));
    } 
    else if (type === 'az') {
      items.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
    } 
    else if (type === 'random') {
      items.sort(() => Math.random() - 0.5);
    }

    items.forEach(item => list.appendChild(item));
  }

  document.querySelectorAll('.sort-controls button').forEach(button => {
    button.addEventListener('click', () => {
      sortList(button.dataset.sort);
    });
  });

});
</script>
