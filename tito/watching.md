---
layout: default
title: "Currently Watching (Tito Dutta)"
categories: [Tito Dutta]
description: "A personal viewing log documenting films and series watched or currently being watched."
permalink: /tito/watching/
created: 2026-10-30
authors: [Tito Dutta]
---

{% include author.html %}

This page is a personal viewing log for films and series. Each title has its own entry, and new entries are added at the top. The log can include release details, cast, viewing date, status and an IMDb reference.

This list includes films and series watched from 29 October 2026 onwards. Titles watched before that date have not been added, so this is not a complete record of everything I have watched.

I may also be lazy about maintaining this list and might not add every film or series I watch.

<div class="watching-log">

  <article class="watching-entry" aria-labelledby="project-hail-mary" markdown="1">
    <p class="watching-status watching-status-watched">Watched</p>

    ### Project Hail Mary {#project-hail-mary}

    <dl class="watching-details">
      <div>
        <dt>Release year</dt>
        <dd>2026</dd>
      </div>
      <div>
        <dt>Director</dt>
        <dd>Phil Lord and Christopher Miller</dd>
      </div>
      <div>
        <dt>Cast</dt>
        <dd>Ryan Gosling, Sandra Hüller, James Ortiz, Lionel Boyce, Ken Leung, Milana Vayntrub and Priya Kansara</dd>
      </div>
      <div>
        <dt>Genre</dt>
        <dd>Science fiction, adventure</dd>
      </div>
      <div>
        <dt>Runtime</dt>
        <dd>2 hours 36 minutes</dd>
      </div>
      <div>
        <dt>Language</dt>
        <dd>English</dd>
      </div>
      <div>
        <dt>Date watched</dt>
        <dd>Friday, 30 October 2026</dd>
      </div>
      <div>
        <dt>Rating</dt>
        <dd><span class="watching-stars" role="img" aria-label="4 out of 5 stars">★★★★<span class="watching-empty-stars">★</span></span> (4/5)</dd>
      </div>
      <div>
        <dt>IMDb</dt>
        <dd><a href="https://www.imdb.com/title/tt12042730/">Project Hail Mary on IMDb</a></dd>
      </div>
    </dl>
  </article>

</div>

{% include navbox-tito.html %}

<style>
.watching-log {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
  margin: 1.25rem 0;
}

.watching-entry {
  min-width: 0;
  padding: 1.25rem;
  border: 1px solid var(--border-main, #d8dee4);
  border-radius: 12px;
  background: var(--bg-surface, #fff);
  color: var(--text-main, #1a1a1a);
  overflow-wrap: anywhere;
}

.watching-entry h3 {
  margin: 0.6rem 0 1rem;
  color: var(--text-heading, #0a2e57);
  line-height: 1.45;
}

.watching-status {
  display: inline-block;
  margin: 0;
  padding: 0.3rem 0.65rem;
  border: 1px solid #1f5f3b;
  border-radius: 999px;
  background: #e8f5ec;
  color: #17452b;
  font-size: 0.9rem;
  font-weight: 700;
}

.watching-details {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.9rem 1.25rem;
  margin: 0;
}

.watching-details div {
  min-width: 0;
}

.watching-details dt {
  margin-bottom: 0.2rem;
  color: var(--text-muted, #444);
  font-size: 0.9rem;
  font-weight: 700;
}

.watching-details dd {
  margin: 0;
  line-height: 1.55;
}

.watching-stars {
  color: #8a5a00;
  letter-spacing: 0.08em;
  white-space: nowrap;
}

.watching-empty-stars {
  color: #767676;
}

body.tsap-dark-mode .watching-stars {
  color: #ffd166;
}

body.tsap-dark-mode .watching-empty-stars {
  color: #9ca3af;
}

.watching-entry a {
  color: #184c99;
  text-decoration: underline;
  text-underline-offset: 0.15em;
}

.watching-entry a:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}

body.tsap-dark-mode .watching-entry {
  background: var(--bg-surface, #1f2937);
  border-color: var(--border-sub, #374151);
  color: var(--text-main, #e5e7eb);
}

body.tsap-dark-mode .watching-entry h3 {
  color: var(--text-heading, #f3f4f6);
}

body.tsap-dark-mode .watching-details dt {
  color: var(--text-muted, #cbd5e1);
}

body.tsap-dark-mode .watching-entry a {
  color: #9ec5ff;
}

body.tsap-dark-mode .watching-status {
  background: #173b2a;
  color: #d1fae5;
  border-color: #4ade80;
}

@media (max-width: 600px) {
  .watching-entry {
    padding: 1rem;
  }

  .watching-details {
    grid-template-columns: minmax(0, 1fr);
    gap: 0.8rem;
  }
}
</style>

<!--
Adding another film or series:
1. Copy the <article class="watching-entry">...</article> block for a title.
2. Add the new entry above existing entries so the newest appears first.
3. Give each heading a unique anchor and keep its aria-labelledby value in sync.
4. Include the release year, director or creator, cast, genre, runtime, language, date watched and IMDb link when known.
5. Change the status to "Currently watching" for a title still in progress.
6. Keep this page free of page_id metadata, as requested.
-->
