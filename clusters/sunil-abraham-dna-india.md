---
layout: default
title: "Sunil Abraham and DNA India"
description: "A consolidated archive of Sunil Abraham’s contributions to DNA India and related news coverage that references his analysis of technology, internet governance, digital rights, and public policy in the Indian context."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-dna-india/
created: 2026-02-05
---

***DNA India*** (short for *Daily News and Analysis*) is a national English-language newspaper known for its reportage on politics, public policy, urban affairs, and technology. Its coverage has often explored how digital platforms, state regulation, and emerging technologies intersect with questions of rights, governance, and civic life.

This cluster brings together all **publications** and **media mentions** associated with *DNA India*, providing a single reference point for readers tracing how technology policy and digital rights debates have been reflected in mainstream Indian journalism over time.

## ✍️ Publications {#publications}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign pub_items = site.pages
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","DNA India"
%}
{% assign pub_sorted = pub_items | sort:"title" %}

<ol id="pub-list" class="cluster-list">
{% for item in pub_sorted %}
  <li data-title="{{ item.title | downcase }}"
      data-date="{{ item.date | date: '%Y-%m-%d' }}">
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","DNA India"
%}
{% assign media_sorted = media_items | sort:"title" %}

<ol id="media-list" class="cluster-list">
{% for item in media_sorted %}
  <li data-title="{{ item.title | downcase }}"
      data-date="{{ item.date | date: '%Y-%m-%d' }}">
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## External links
- [Official website](https://www.dnaindia.com/)

<style>

/* ---------------------------------------------------------
   LIST DESIGN (consistent with other clusters)
--------------------------------------------------------- */
.cluster-list {
  margin: 0.8rem 0 1.6rem 0;
  padding-left: 1.1rem;
}

.cluster-list li {
  margin-bottom: 0.75rem;
  animation: fadeUp 0.25s ease;
}

.cluster-list a {
  text-decoration: none;
}

.cluster-list a:hover {
  text-decoration: underline;
}

.meta {
  font-size: 0.9rem;
  color: #555;
}

.desc {
  font-size: 0.92rem;
  color: #444;
  margin-top: 0.2rem;
}

/* ---------------------------------------------------------
   SORT BUTTONS
--------------------------------------------------------- */
.cluster-sort {
  margin: 0.6rem 0 1rem 0;
}

.cluster-sort button {
  background: #eef3fa;
  border: 1px solid #cdd7e5;
  padding: 0.4rem 0.8rem;
  margin-right: 0.45rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.88rem;
  transition: background 0.2s ease, border-color 0.2s ease;
}

.cluster-sort button:hover {
  background: #dbe6f5;
}

.cluster-sort button.active-sort {
  background: #3278d6;
  color: #fff;
  border-color: #3278d6;
}

/* ---------------------------------------------------------
   Fade animation
--------------------------------------------------------- */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(3px); }
  to   { opacity: 1; transform: translateY(0); }
}

</style>

<script>
document.addEventListener("DOMContentLoaded", () => {

  function attachSort(sectionId) {
    const list = document.getElementById(sectionId);
    const items = Array.from(list.querySelectorAll("li"));
    const buttons = list.previousElementSibling.querySelectorAll("button");

    function sortList(type) {
      const sorted = [...items];

      if (type === "alpha") {
        sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
      } else if (type === "newest") {
        sorted.sort((a, b) => b.dataset.date.localeCompare(a.dataset.date));
      } else if (type === "oldest") {
        sorted.sort((a, b) => a.dataset.date.localeCompare(b.dataset.date));
      }

      list.innerHTML = "";
      sorted.forEach(li => list.appendChild(li));

      buttons.forEach(btn => btn.classList.remove("active-sort"));
      document.querySelector(`#${sectionId}`)
        .previousElementSibling
        .querySelector(`[data-sort="${type}"]`)
        .classList.add("active-sort");
    }

    /* Default sort */
    sortList("alpha");

    buttons.forEach(btn => {
      btn.addEventListener("click", () => sortList(btn.dataset.sort));
    });
  }

  attachSort("pub-list");
  attachSort("media-list");
});
</script>
