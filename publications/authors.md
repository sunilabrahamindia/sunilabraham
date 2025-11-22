---
layout: default
title: "Authors Directory"
description: "Browse all authors contributing to publications within the Sunil Abraham Project."
categories: [Project pages]
created: 2025-11-09
---

This directory highlights authors who have collaborated with **Sunil Abraham** on various publications featured within this project.  
- Each author listed below has contributed to one or more works — as co-author, collaborator, or editor.  
- Please note that this directory represents collaborations and not the authors’ complete body of work.  
- You can select a name below to view their shared works with Sunil Abraham.

<div class="authors-directory">

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

</div>

<script>
  const publications = [
    {% for page in site.pages %}
      {% if page.categories contains "Publications" and page.authors %}
        {
          title: "{{ page.title | escape }}",
          url: "{{ page.url }}",
          description: "{{ page.description | escape }}",
          date: "{{ page.date | date: '%-d %B %Y' }}",
          year: "{{ page.date | date: '%Y' }}",
          authors: [{% for author in page.authors %}"{{ author | slugify }}"{% unless forloop.last %}, {% endunless %}{% endfor %}]
        }{% unless forloop.last %},{% endunless %}
      {% endif %}
    {% endfor %}
  ];

  const dropdown = document.getElementById('author-select');
  const output = document.getElementById('author-publications');

  dropdown.addEventListener('change', function() {
    const selected = this.value;
    const selectedText = this.options[this.selectedIndex].text;
    output.innerHTML = "";

    if (!selected) return;

    const matches = publications.filter(pub => pub.authors.includes(selected));

    let introText = "";
    if (selectedText.toLowerCase() === "sunil abraham") {
      introText = `<strong>The following works are authored by Sunil Abraham.</strong>`;
    } else {
      introText = `<strong>Sunil Abraham</strong> and <strong>${selectedText}</strong> have collaborated or co-authored the following works:`;
    }

    const intro = document.createElement('p');
    intro.innerHTML = introText;
    output.appendChild(intro);

    if (matches.length > 0) {
      const list = document.createElement('ol');
      matches.forEach(pub => {
        const li = document.createElement('li');
        li.innerHTML = `
          <div class="pub-entry">
            <a href="${pub.url}">${pub.title}</a>
            ${pub.year ? ` <span class="pub-year">(${pub.year})</span>` : ""}
            ${pub.description ? `<div class="pub-description">• ${pub.description}</div>` : ""}
          </div>
        `;
        list.appendChild(li);
      });
      output.appendChild(list);
    } else {
      output.innerHTML += "<p>No publications found for this author.</p>";
    }
  });
</script>

<style>
/* --- Author Directory Styling --- */
.authors-directory {
  margin-top: 1em;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1em;
}

#author-select {
  width: 100%;
  max-width: 420px;
  padding: 0.6em;
  font-size: 1em;
  border-radius: 8px;
  border: 1px solid #ccc;
  background-color: #fff;
  color: #222;
}

#author-publications {
  width: 100%;
  margin-top: 1.5em;
  font-size: 1rem;
}

#author-publications ol {
  margin-left: 1.5em;
  padding-left: 0.5em;
}

#author-publications ol li {
  margin-bottom: 1em;
}

.pub-entry {
  line-height: 1.4;
}

.pub-year {
  color: #666;
  font-size: 0.9em;
}

.pub-description {
  margin-top: 0.25em;
  margin-left: 0.5em;
  font-size: 0.95em;
  color: #333;
}

#author-publications a {
  text-decoration: none;
  color: #0056b3;
  font-weight: 500;
}

#author-publications a:hover,
#author-publications a:focus {
  text-decoration: underline;
}

/* --- Responsive adjustments --- */
@media (max-width: 600px) {
  .authors-directory {
    align-items: stretch;
  }

  #author-select {
    width: 100%;
    font-size: 0.95em;
  }

  #author-publications ol {
    margin-left: 1em;
  }

  .pub-description {
    margin-left: 0.25em;
    font-size: 0.95em;
  }

  #author-publications a {
    font-size: 1em;
  }
}
</style>
