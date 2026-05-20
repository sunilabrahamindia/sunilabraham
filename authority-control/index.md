---
layout: default
title: "Authority Control"
description: "Authority control records and metadata systems used across The Sunil Abraham Project."
permalink: /authority-control/
categories: [Authority control]
created: 2026-05-20
---

**Authority control** is a method used by libraries, archives, research institutions, and digital knowledge projects to organise information about people, organisations, publications, and subjects in a consistent and reliable manner. It helps ensure that different names, spellings, transliterations, and references connected to the same entity are brought together under a stable identity record. Systems such as VIAF, ISNI, ORCID, Library of Congress authority files, Wikidata, and OpenAlex are examples of authority-control frameworks used internationally across catalogues, databases, and scholarly infrastructures. On **The Sunil Abraham Project** (TSAP), selected authority-control entries are maintained for people and institutions closely connected to the project's archival and research focus. TSAP is not intended to function as a dedicated metadata or authority-records project, but authority-control pages are included where they improve context, discoverability, and long-term reference value.

In practice, authority control makes knowledge systems easier to navigate, search, preserve, and cite. It allows readers and researchers to distinguish between entities with similar names, trace relationships across collections, and connect records distributed across multiple repositories or institutions. Authority records also support interoperability between digital archives, academic databases, library catalogues, and search systems, helping information remain discoverable over long periods of time.

For The Sunil Abraham Project (TSAP), authority control is important because the project functions not only as a website, but also as a growing digital archive and research infrastructure. Many individuals, organisations, publications, and historical materials documented within TSAP appear across scattered institutional records, academic references, media archives, and online repositories. By maintaining structured authority-control pages, TSAP improves long-term discoverability, strengthens citation reliability, supports archival preservation, and helps connect the project's materials with wider public knowledge systems.

## Current authority-control entries {#entries}

{% assign authority_pages = site.pages
  | where_exp: "page", "page.title contains 'Authority Control:'"
  | sort: "title" %}

<ul class="authority-entry-list">

{% for page in authority_pages %}
  {% assign clean_title = page.title | remove: "Authority Control: " %}
  <li>
    <a href="{{ page.url }}">
      {{ clean_title }}
    </a>
  </li>
  
{% endfor %}

</ul>

## External links
- [Authority control](https://en.wikipedia.org/wiki/Authority_control) article on Wikipedia
- [Authority control FAQ](https://www.loc.gov/aba/pcc/naco/documents/PCC-SCT-Authority-Control-FAQs-Authors-Creators.pdf) (PDF) at The Library of Congress

<style>
.authority-entry-list {
  margin: 1rem 0 2rem 1.2rem;
  padding: 0;
}

.authority-entry-list li {
  margin-bottom: 0.45rem;
}

.authority-entry-list a {
  color: #0645ad;
  text-decoration: none;
}

.authority-entry-list a:hover {
  color: #2f6f6f;
  text-decoration: underline;
}

.authority-entry-list a:visited {
  color: #0b0080;
}

.authority-entry-list a:focus-visible {
  outline: 2px solid #2f6f6f;
  outline-offset: 2px;
}
</style>
