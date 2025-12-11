---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

Search articles using multiple filters.

<!-- ===========================
     SEARCH CONTROLS
=========================== -->
<div class="search-box" style="background: var(--page-bg); padding: 1rem; border-radius: 8px; border: 1px solid var(--muted);">

  <label>
    Keyword search:
    <input id="q" type="text" placeholder="Search title or description" style="width:100%; margin-bottom:1rem;">
  </label>

  <label>
    Author:
    <select id="author" multiple size="4" style="width:100%; margin-bottom:1rem;">
    </select>
  </label>

  <label>
    Source:
    <select id="source" multiple size="4" style="width:100%; margin-bottom:1rem;">
    </select>
  </label>

  <label>
    Category:
    <select id="category" multiple size="4" style="width:100%; margin-bottom:1rem;">
    </select>
  </label>

  <label>
    Year:
    <select id="year" multiple size="4" style="width:100%; margin-bottom:1rem;">
    </select>
  </label>

</div>

<hr>

<!-- ===========================
     RESULTS AREA
=========================== -->
<div id="results"></div>

<script>
/* Step 1: Build a JSON list of all pages with metadata */
const DATA = [
  {% for p in site.pages %}
    {% if p.title and p.created %}
      {
        "title": {{ p.title | jsonify }},
        "description": {{ p.description | default: "" | jsonify }},
        "source": {{ p.source | default: "" | jsonify }},
        "authors": {{ p.authors | default: "" | jsonify }},
        "categories": {{ p.categories | default: "" | jsonify }},
        "date": {{ p.date | default: "" | jsonify }},
        "created": {{ p.created | jsonify }},
        "url": "{{ p.url }}"
      },
    {% endif %}
  {% endfor %}
];

/* Utility: unique sorted list from a field */
function uniqueValues(field) {
  const values = new Set();
  DATA.forEach(item => {
    if (Array.isArray(item[field])) {
      item[field].forEach(v => v && values.add(v));
    } else if (item[field]) {
      values.add(item[field]);
    }
  });
  return [...values].sort();
}

function populateSelect(id, values) {
  const select = document.getElementById(id);
  values.forEach(v => {
    const opt = document.createElement("option");
    opt.value = v;
    opt.textContent = v;
    select.appendChild(opt);
  });
}

/* Populate multi-select filters */
populateSelect("author", uniqueValues("authors"));
populateSelect("source", uniqueValues("source"));
populateSelect("category", uniqueValues("categories"));
populateSelect("year", [...new Set(DATA.map(x => (x.date ? x.date.substring(0,4) : null)))].filter(Boolean).sort());

/* Filtering */
function getSelectedValues(selectId) {
  return [...document.getElementById(selectId).selectedOptions].map(o => o.value);
}

function matches(item, values, field) {
  if (values.length === 0) return true;
  if (Array.isArray(item[field])) return item[field].some(v => values.includes(v));
  return values.includes(item[field]);
}

/* Main filtering function */
function applyFilters() {
  const q = document.getElementById("q").value.toLowerCase();
  const authors = getSelectedValues("author");
  const sources = getSelectedValues("source");
  const categories = getSelectedValues("category");
  const years = getSelectedValues("year");

  const results = DATA.filter(item => {
    const textMatch =
      (!q) ||
      (item.title && item.title.toLowerCase().includes(q)) ||
      (item.description && item.description.toLowerCase().includes(q));

    const authorMatch = matches(item, authors, "authors");
    const sourceMatch = matches(item, sources, "source");
    const categoryMatch = matches(item, categories, "categories");
    const yearMatch =
      years.length === 0 ||
      (item.date && years.includes(item.date.substring(0, 4)));

    return textMatch && authorMatch && sourceMatch && categoryMatch && yearMatch;
  });

  renderResults(results);
}

/* Render result cards */
function renderResults(items) {
  const box = document.getElementById("results");
  box.innerHTML = "";

  if (items.length === 0) {
    box.innerHTML = "<p>No results found.</p>";
    return;
  }

  items.forEach(item => {
    const div = document.createElement("div");
    div.style.border = "1px solid var(--muted)";
    div.style.padding = "1rem";
    div.style.marginBottom = "1rem";
    div.style.borderRadius = "8px";
    div.style.background = "var(--page-bg)";

    div.innerHTML = `
      <h3><a href="${item.url}">${item.title}</a></h3>
      <p>${item.description || ""}</p>
      <p><strong>Source:</strong> ${item.source || "-"}</p>
      <p><strong>Author(s):</strong> ${Array.isArray(item.authors) ? item.authors.join(", ") : item.authors}</p>
      <p><strong>Date:</strong> ${item.date || "-"}</p>
      <p><strong>Categories:</strong> ${Array.isArray(item.categories) ? item.categories.join(", ") : item.categories}</p>
    `;

    box.appendChild(div);
  });
}

/* Trigger filtering on any change */
["q", "author", "source", "category", "year"].forEach(id => {
  document.getElementById(id).addEventListener("input", applyFilters);
});

/* Initial display */
applyFilters();
</script>
