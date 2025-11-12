---
layout: default
title: "Media Outlets Directory"
description: "Browse all media outlets featuring opinion pieces, essays, and commentaries by Sunil Abraham."
categories: [Project pages]
---

This directory groups **media articles and commentaries** by **Sunil Abraham** according to the **newspaper or media outlet** where they appeared.  
- Each outlet below includes articles authored or co-authored by Sunil Abraham.  
- Only works categorised under [Media Articles and Commentaries](/categories/media-articles/) are included.  
- Select an outlet from the list below to view his published articles in that publication.

<div class="media-directory">

<select id="media-select" aria-label="Select Media Outlet">
  <option value="">-- Select a Media Outlet --</option>
  {% assign all_outlets = "" | split: "" %}
  {% for page in site.pages %}
    {% if page.categories contains "Media Articles" and page.outlet %}
      {% unless all_outlets contains page.outlet %}
        {% assign all_outlets = all_outlets | push: page.outlet %}
      {% endunless %}
    {% endif %}
  {% endfor %}
  {% assign sorted_outlets = all_outlets | sort %}
  {% for outlet in sorted_outlets %}
  <option value="{{ outlet | slugify }}">{{ outlet }}</option>
  {% endfor %}
</select>

<div id="media-articles" aria-live="polite"></div>

</div>

<script>
  const mediaArticles = [
    {% for page in site.pages %}
      {% if page.categories contains "Media Articles" and page.outlet %}
        {
          title: "{{ page.title | escape }}",
          url: "{{ page.url }}",
          description: "{{ page.description | escape }}",
          date: "{{ page.date | date: '%-d %B %Y' }}",
          year: "{{ page.date | date: '%Y' }}",
          outlet: "{{ page.outlet | slugify }}"
        }{% unless forloop.last %},{% endunless %}
      {% endif %}
    {% endfor %}
  ];

  const dropdown = document.getElementById('media-select');
  const output = document.getElementById('media-articles');

  dropdown.addEventListener('change', function() {
    const selected = this.value;
    const selectedText = this.options[this.selectedIndex].text;
    output.innerHTML = "";

    if (!selected) return;

    const matches = mediaArticles.filter(pub => pub.outlet === selected);

    const intro = document.createElement('p');
    intro.innerHTML = `<strong>Articles by Sunil Abraham published in ${selectedText}:</strong>`;
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
      output.innerHTML += "<p>No articles found for this outlet.</p>";
    }
  });
</script>

<style>
/* --- Media Directory Styling --- */
.media-directory {
  margin-top: 1em;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1em;
}

#media-select {
  width: 100%;
  max-width: 420px;
  padding: 0.6em;
  font-size: 1em;
  border-radius: 8px;
  border: 1px solid #ccc;
  background-color: #fff;
  color: #222;
}

#media-articles {
  width: 100%;
  margin-top: 1.5em;
