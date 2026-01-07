---
layout: default
title: "Sunil Abraham and MediaNama"
description: "A curated cluster of MediaNama reporting that features Sunil Abraham’s perspectives on technology policy, digital regulation, platform governance, and the institutional shaping of India’s internet ecosystem."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-medianama/
created: 2026-01-07
---

***MediaNama*** is a digital publication focused on technology policy, media, telecommunications, and internet governance in India. Its reporting is known for close attention to regulatory processes, institutional decision-making, and the political economy of digital platforms.

Within this coverage, **Sunil Abraham** appears as a referenced analyst offering insight into the policy and governance dimensions of digital technologies. His commentary in *MediaNama* articles typically addresses questions of regulatory design, state power, platform accountability, and the long-term implications of technology policy choices, rather than short-term industry developments.

This cluster brings together all available **media mentions** of Sunil Abraham published on *MediaNama*. Taken together, these articles document how his views have informed policy-oriented journalism at moments of regulatory change and institutional debate in India’s digital landscape.

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","MediaNama"
%}
{% assign media_sorted = media_items | sort:"title" %}

<ol id="media-list" class="cluster-list">
{% for item in media_sorted %}
  <li data-title="{{ item.title | downcase }}"
      data-date="{{ item.date | date: '%Y-%m-%d' }}">
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%-d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## External links
- [Official website](https://www.medianama.com/)

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
  font-size: 0.95rem;
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

    /* Default sort: alphabetical */
    sortList("alpha");

    buttons.forEach(btn => {
      btn.addEventListener("click", () => sortList(btn.dataset.sort));
    });
  }

  attachSort("media-list");
});
</script>
