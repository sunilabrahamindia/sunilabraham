---
layout: default
title: "Sunil Abraham and The Economic Times"
description: "A consolidated archive of Sunil Abraham's writings for The Economic Times and media coverage featuring his commentary."
categories: [Clusters]
permalink: /clusters/sunil-abraham-economic-times/
created: 2025-12-08
---

***The Economic Times*** is one of India's largest financial newspapers, reporting on policy, markets, technology, regulation, and economic governance. Over the years, **Sunil Abraham** has engaged with the publication in many ways. He has contributed opinion pieces, written analytical commentary, and has also been quoted in stories on digital rights, privacy, platform governance, cybersecurity, and emerging technologies.

This cluster brings together all **published writings** and **media mentions** associated with *The Economic Times*. It is intended as a clear, well-organised reference point for readers and researchers following Sunil Abraham's work in technology and public policy.

## Publications
Articles authored by Sunil Abraham in *The Economic Times*.

<div class="cluster-sort">
  <span class="sort-label">Sort by:</span>
  <button class="sort-btn" data-sort="alpha">Alphabetical</button>
  <button class="sort-btn" data-sort="newest">Newest</button>
  <button class="sort-btn" data-sort="oldest">Oldest</button>
</div>

<ol class="cluster-list" id="pub-list">
{% assign pub_items = site.pages 
  | where_exp:"p","p.categories contains 'Publications'" 
  | where:"source","The Economic Times" 
%}
{% assign pub_sorted = pub_items | sort: "title" %}
{% for item in pub_sorted %}
  <li class="cluster-item">
    <a href="{{ item.permalink }}" class="cluster-link">{{ item.title }}</a>
    <span class="cluster-date">{{ item.date | date: "%d %b %Y" }}</span>
  </li>
{% endfor %}
</ol>

## Media mentions
Media reports in *The Economic Times* quoting or featuring Sunil Abraham.

<div class="cluster-sort">
  <span class="sort-label">Sort by:</span>
  <button class="sort-btn" data-sort="alpha">Alphabetical</button>
  <button class="sort-btn" data-sort="newest">Newest</button>
  <button class="sort-btn" data-sort="oldest">Oldest</button>
</div>

<ol class="cluster-list" id="media-list">
{% assign media_items = site.pages 
  | where_exp:"p","p.categories contains 'Media mentions'" 
  | where:"source","The Economic Times" 
%}
{% assign media_sorted = media_items | sort: "title" %}
{% for item in media_sorted %}
  <li class="cluster-item">
    <a href="{{ item.permalink }}" class="cluster-link">{{ item.title }}</a>
    <span class="cluster-date">{{ item.date | date: "%d %b %Y" }}</span>
  </li>
{% endfor %}
</ol>

{% include back-to-top.html %}

<a href="/media/" class="btn" style="margin-top: 1rem;">← Back to Media Index</a>

<style>

/* ---------------------------------------------
   General List Style
---------------------------------------------- */
.cluster-list {
  margin: 1.2rem 0;
  padding-left: 1.2rem;
  max-width: 760px;
}

.cluster-item {
  margin-bottom: 0.75rem;
  padding: 0.25rem 0;
  animation: fadeIn 0.4s ease;
}

.cluster-link {
  text-decoration: none;
  font-weight: 400; /* Not bold */
  color: #0f1720;
}

.cluster-link:hover {
  text-decoration: underline;
  color: #0b66d1;
}

.cluster-date {
  display: inline-block;
  margin-left: 0.4rem;
  font-size: 0.85rem;
  color: #66748a;
}

/* ---------------------------------------------
   Sort Buttons
---------------------------------------------- */
.cluster-sort {
  margin: 0.8rem 0 0.6rem 0;
  display: flex;
  gap: 0.5rem;
  align-items: center;
  flex-wrap: wrap;
}

.sort-label {
  font-size: 0.9rem;
  color: #556072;
}

/* Beautiful pill buttons */
.sort-btn {
  padding: 0.3rem 0.75rem;
  font-size: 0.85rem;
  border: 1px solid #cfd6e3;
  background: #f7f9fc;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.sort-btn:hover {
  background: #e6eef8;
  border-color: #b9c4d6;
}

.sort-btn:focus {
  outline: 2px solid #0b66d1;
  outline-offset: 2px;
}

/* ---------------------------------------------
   Animation
---------------------------------------------- */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

</style>

<script>
// Generic cluster sorting
function sortList(listId, mode) {
  const list = document.getElementById(listId);
  const items = Array.from(list.querySelectorAll("li"));

  items.sort((a, b) => {
    const titleA = a.querySelector(".cluster-link").innerText.trim().toLowerCase();
    const titleB = b.querySelector(".cluster-link").innerText.trim().toLowerCase();
    const dateA = new Date(a.querySelector(".cluster-date").innerText);
    const dateB = new Date(b.querySelector(".cluster-date").innerText);

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

    const section = this.closest(".cluster-sort").nextElementSibling.id;
    sortList(section, mode);
  });
});
</script>
