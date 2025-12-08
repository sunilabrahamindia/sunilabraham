---
layout: default
title: "Sunil Abraham and The Economic Times"
description: "A consolidated archive of Sunil Abraham's writings for The Economic Times and media coverage featuring his commentary."
categories: [Clusters]
permalink: /clusters/sunil-abraham-economic-times/
created: 2025-12-08
---

***The Economic Times*** is one of India's largest financial newspapers, reporting on policy, markets, technology, industry regulation, and economic governance. Over the years, **Sunil Abraham** has engaged with the publication in multiple ways. He has written opinion pieces, contributed analysis on technology policy, and has also been quoted across a range of stories covering digital rights, privacy, platform governance, and emerging technologies.

This cluster brings together all **published writings** and **media mentions** connected to *The Economic Times*. It serves as a single, easy-to-use reference point for researchers, students, and readers following Sunil Abraham's work on technology and public policy.

## Publications
Articles authored by Sunil Abraham in *The Economic Times*.

<div class="cluster-sort">
  Sort by:
  <a href="#" class="sort-btn" data-sort="alpha">Alphabetical</a> |
  <a href="#" class="sort-btn" data-sort="newest">Newest</a> |
  <a href="#" class="sort-btn" data-sort="oldest">Oldest</a>
</div>

<ol class="cluster-list" id="pub-list">
{% assign pub_items = site.publications | where: "source", "The Economic Times" %}
{% assign pub_sorted = pub_items | sort: "title" %}
{% for item in pub_sorted %}
  <li>
    <strong><a href="{{ item.permalink }}">{{ item.title }}</a></strong>  
    <span class="cluster-date">({{ item.date | date: "%Y-%m-%d" }})</span>
  </li>
{% endfor %}
</ol>

---

## Media mentions
Media reports in *The Economic Times* quoting or featuring Sunil Abraham.

<div class="cluster-sort">
  Sort by:
  <a href="#" class="sort-btn" data-sort="alpha">Alphabetical</a> |
  <a href="#" class="sort-btn" data-sort="newest">Newest</a> |
  <a href="#" class="sort-btn" data-sort="oldest">Oldest</a>
</div>

<ol class="cluster-list" id="media-list">
{% assign media_items = site.pages | where: "categories", "Media mentions" | where: "source", "The Economic Times" %}
{% assign media_sorted = media_items | sort: "title" %}
{% for item in media_sorted %}
  <li>
    <strong><a href="{{ item.permalink }}">{{ item.title }}</a></strong>  
    <span class="cluster-date">({{ item.date | date: "%Y-%m-%d" }})</span>
  </li>
{% endfor %}
</ol>

{% include back-to-top.html %}

<a href="/media/" class="btn" style="margin-top: 1rem;">← Back to Media Index</a>

<style>
.cluster-list {
  margin: 1rem 0;
  padding-left: 1rem;
  max-width: 760px;
}

.cluster-list li {
  margin-bottom: 0.6rem;
}

.cluster-list a {
  text-decoration: none;
  color: #0b66d1;
}

.cluster-list a:hover {
  text-decoration: underline;
}

.cluster-date {
  color: #556072;
  font-size: 0.85rem;
}

.cluster-sort {
  margin: 0.6rem 0 0.4rem 0;
  font-size: 0.9rem;
}

.cluster-sort a {
  color: #0b66d1;
  text-decoration: none;
  margin-right: 0.4rem;
}

.cluster-sort a:hover {
  text-decoration: underline;
}

.btn {
  display: inline-block;
  background: #3278d6;
  color: #fff !important;
  padding: 0.45rem 0.85rem;
  border-radius: 6px;
  font-size: 0.9rem;
  text-decoration: none;
}

.btn:hover {
  background: #255ea9;
}
</style>

<script>
// Generic cluster sorting for Publications and Media sections
function sortList(listId, mode) {
  const list = document.getElementById(listId);
  const items = Array.from(list.querySelectorAll("li"));

  items.sort((a, b) => {
    const titleA = a.querySelector("a").innerText.trim().toLowerCase();
    const titleB = b.querySelector("a").innerText.trim().toLowerCase();
    const dateA = new Date(a.querySelector(".cluster-date").innerText.replace(/\(|\)/g, ""));
    const dateB = new Date(b.querySelector(".cluster-date").innerText.replace(/\(|\)/g, ""));

    if (mode === "alpha") return titleA.localeCompare(titleB);
    if (mode === "newest") return dateB - dateA;
    if (mode === "oldest") return dateA - dateB;
    return 0;
  });

  list.innerHTML = "";
  items.forEach(i => list.appendChild(i));
}

document.querySelectorAll(".sort-btn").forEach(btn => {
  btn.addEventListener("click", function(e) {
    e.preventDefault();
    const mode = this.dataset.sort;
    const section = this.closest("div").nextElementSibling.id;
    sortList(section, mode);
  });
});
</script>
