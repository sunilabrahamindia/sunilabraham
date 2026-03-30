---
layout: default
title: "Sunil Abraham and Bangalore Mirror"
description: "A consolidated archive of Sunil Abraham's writings for Bangalore Mirror and media coverage featuring his commentary on technology, privacy, social media, and digital culture in India."
categories: [Clusters]
permalink: /clusters/sunil-abraham-bangalore-mirror/
created: 2025-12-20
---

***Bangalore Mirror*** is an Indian daily newspaper known for its city-focused reporting, opinion writing, and long-form weekend features that explore urban life, culture, and social change. Alongside local news and commentary, the paper has regularly published reflective pieces on how technology and digital platforms shape everyday experiences in India.

Over the years, **Sunil Abraham** has contributed opinion writing to *Bangalore Mirror* and has also appeared as a quoted source across its reporting and Sunday Read features. His presence in the paper often connects questions of technology policy and digital rights with the lived experiences of internet users, particularly in urban contexts.

This cluster brings together all **publications** and **media mentions** connected to *Bangalore Mirror*, providing a single reference point for readers tracing how issues such as online privacy, social media behaviour, digital exit, and platform power were discussed in mainstream city journalism.


## ✍️ Publications

<ol class="cluster-list">
{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Bangalore Mirror"
     | sort:"date" | reverse
%}

{% for item in pub_items %}
  <li>
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## 📣 Media Mentions

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

<ol id="media-list" class="cluster-list">
{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Bangalore Mirror"
%}
{% assign media_sorted = media_items | sort:"title" %}

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

<style>
/* ---------------------------------------------------------
   Bangalore Mirror Cluster – Minimal Styling
--------------------------------------------------------- */

.cluster-list {
  margin: 1rem 0 2rem 0;
  padding-left: 1.1rem;
}

.cluster-list li {
  margin-bottom: 0.8rem;
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
  font-size: 0.95rem;
  color: #444;
  margin-top: 0.2rem;
}

/* Sort buttons */
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
}

.cluster-sort button.active-sort {
  background: #3278d6;
  color: #fff;
  border-color: #3278d6;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {

  const list = document.getElementById("media-list");
  const items = Array.from(list.querySelectorAll("li"));
  const buttons = document.querySelectorAll(".cluster-sort button");

  function sortList(type) {
    let sorted = [...items];

    if (type === "alpha") {
      sorted.sort((a, b) =>
        a.dataset.title.localeCompare(b.dataset.title)
      );
    } 
    else if (type === "newest") {
      sorted.sort((a, b) =>
        b.dataset.date.localeCompare(a.dataset.date)
      );
    } 
    else if (type === "oldest") {
      sorted.sort((a, b) =>
        a.dataset.date.localeCompare(b.dataset.date)
      );
    }

    list.innerHTML = "";
    sorted.forEach(li => list.appendChild(li));

    buttons.forEach(btn => btn.classList.remove("active-sort"));
    document.querySelector(`[data-sort="${type}"]`)
      .classList.add("active-sort");
  }

  sortList("alpha");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => sortList(btn.dataset.sort));
  });

});
</script>
