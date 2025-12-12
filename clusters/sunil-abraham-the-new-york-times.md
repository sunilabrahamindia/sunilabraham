---
layout: default
title: "Sunil Abraham and The New York Times"
description: "A curated cluster of New York Times reporting that features commentary from Sunil Abraham across issues of technology policy, digital rights, online speech and internet governance."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-the-new-york-times/
created: 2025-12-12
---

***The New York Times*** has, over the years, covered many of the debates that define India's digital landscape — questions of online speech, privacy, regulation, platform power, civic mobilisation and technology governance. Across this reporting, **Sunil Abraham** appears as a frequent voice who helps contextualise how law, policy and society intersect in the digital sphere.

This cluster brings together all **media mentions** connected to *The New York Times*, making it easier for researchers, students and policy audiences to trace recurring themes and follow the evolution of Abraham’s public commentary.

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","The New York Times"
%}
{% assign media_sorted = media_items | sort:"title" %}

<ol id="media-list" class="cluster-list">
{% for item in media_sorted %}
  <li data-title="{{ item.title | downcase }}"
      data-date="{{ item.date | date: '%Y-%m-%d' }}">
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%d %b %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## External links
<a href="https://www.nytimes.com/search?query=%22Sunil%20Abraham%22">"Sunil Abraham" on *The New York Times*</a>

<style>

/* ---------------------------------------------------------
   LIST DESIGN (matching your ET cluster style)
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

    /* Default: alphabetical */
    sortList("alpha");

    buttons.forEach(btn => {
      btn.addEventListener("click", () => sortList(btn.dataset.sort));
    });
  }

  attachSort("media-list");
});
</script>
