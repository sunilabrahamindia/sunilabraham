---
layout: default
title: "Authors Directory"
description: "Browse all authors contributing to publications within the Sunil Abraham Project."
categories: [Project pages]
---

## Authors Directory

This page allows you to browse all publications by author.  
Select an author from the dropdown below to view their associated works.

<select id="author-select" aria-label="Select Author">
  <option value="">-- Select an Author --</option>
  {% assign all_authors = "" | split: "" %}
  {% for page in site.pages %}
    {% if page.categories contains "Publications" and page.authors %}
      {% for author in page.authors %}
        {% unless all_authors contains author %}
          {% assign all_authors = all_authors | push: author %}
        {% endunless %}
      {% endfor %}
    {% endif %}
  {% endfor %}
  {% assign sorted_authors = all_authors | sort %}
  {% for author in sorted_authors %}
    <option value="{{ author | slugify }}">{{ author }}</option>
  {% endfor %}
</select>

<div id="author-publications" aria-live="polite"></div>

<script>
  const publications = [
    {% for page in site.pages %}
      {% if page.categories contains "Publications" and page.authors %}
        {
          title: "{{ page.title | escape }}",
          url: "{{ page.url }}",
          authors: [{% for author in page.authors %}"{{ author | slugify }}"{% unless forloop.last %}, {% endunless %}{% endfor %}]
        }{% unless forloop.last %},{% endunless %}
      {% endif %}
    {% endfor %}
  ];

  const dropdown = document.getElementById('author-select');
  const output = document.getElementById('author-publications');

  dropdown.addEventListener('change', function() {
    const selected = this.value;
    output.innerHTML = "";

    if (!selected) return;

    const matches = publications.filter(pub => pub.authors.includes(selected));

    if (matches.length > 0) {
      const list = document.createElement('ul');
      matches.forEach(pub => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="${pub.url}">${pub.title}</a>`;
        list.appendChild(li);
      });
      output.appendChild(list);
    } else {
      output.innerHTML = "<p>No publications found for this author.</p>";
    }
  });
</script>

<style>
/* --- Author Directory Styling --- */
#author-select {
  width: 100%;
  max-width: 400px;
  padding: 0.6em;
  margin: 1em 0;
  font-size: 1em;
  border-radius: 8px;
  border: 1px solid #ccc;
  background-color: #fff;
  color: #222;
}

#author-publications {
  margin-top: 1.5em;
  font-size: 1rem;
}

#author-publications ul {
  list-style-type: disc;
  margin-left: 1.5em;
  padding-left: 0.5em;
}

#author-publications a {
  text-decoration: none;
  color: #0056b3;
}

#author-publications a:hover,
#author-publications a:focus {
  text-decoration: underline;
}

@media (max-width: 600px) {
  #author-select {
    width: 100%;
    font-size: 0.95em;
  }

  #author-publications ul {
    margin-left: 1em;
  }

  #author-publications a {
    font-size: 1em;
  }
}
</style>
