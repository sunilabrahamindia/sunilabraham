---
layout: default
title: "Currently Reading (Tito Dutta)"
categories: [Tito Dutta]
description: "A personal reading log documenting books being read and books completed."
permalink: /tito/reading/
created: 2026-10-11
authors: [Tito Dutta]
---

{% include author.html %}

This page is a personal reading log. Each book has its own entry, and new entries are added at the top. When a book is finished, its status and completion date can be updated while the entry remains in the log.

<div class="reading-log">

  <article class="reading-entry" aria-labelledby="book-papers-title">
    <p class="reading-status reading-status-finished">Finished reading</p>
    <h2 id="book-papers-title"><span lang="bn">পাপের সন্ধানে</span> <span class="reading-transliteration" lang="en">(Pāper Sandhāne)</span></h2>
    <p class="reading-author">By <span lang="en">Pracheta Gupta</span> (<span lang="bn">প্রচেত গুপ্ত</span>)</p>

    <dl class="reading-details">
      <div>
        <dt>Genre</dt>
        <dd>Fiction</dd>
      </div>
      <div>
        <dt>Language</dt>
        <dd>Bengali (বাংলা)</dd>
      </div>
      <div>
        <dt>Publication</dt>
        <dd><span lang="bn">আনন্দবাজার পত্রিকা</span> (Anandabazar Patrika), Sharadiya 2026</dd>
      </div>
      <div>
        <dt>Started reading</dt>
        <dd>Sunday, 11 October 2026</dd>
      </div>
      <div>
        <dt>Finished reading</dt>
        <dd>Wednesday, 14 October 2026</dd>
      </div>
      <div>
        <dt>Rating</dt>
        <dd><span class="reading-stars" role="img" aria-label="1 out of 5 stars">★<span class="reading-empty-stars">★★★★</span></span> (1/5)</dd>
      </div>
      <div>
        <dt>Recommended</dt>
        <dd>No</dd>
      </div>
    </dl>
  </article>

</div>

<style>
.reading-log {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
  margin: 1.25rem 0;
}

.reading-entry {
  min-width: 0;
  padding: 1.25rem;
  border: 1px solid var(--border-main, #d8dee4);
  border-radius: 12px;
  background: var(--bg-surface, #fff);
  color: var(--text-main, #1a1a1a);
  overflow-wrap: anywhere;
}

.reading-entry h2 {
  margin: 0.6rem 0 0.35rem;
  color: var(--text-heading, #0a2e57);
  line-height: 1.45;
}

.reading-transliteration {
  font-size: 0.78em;
  font-weight: 400;
}

.reading-status {
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

.reading-author {
  margin: 0 0 1rem;
  color: var(--text-muted, #444);
}

.reading-details {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.9rem 1.25rem;
  margin: 0;
}

.reading-details div {
  min-width: 0;
}

.reading-details dt {
  margin-bottom: 0.2rem;
  color: var(--text-muted, #444);
  font-size: 0.9rem;
  font-weight: 700;
}

.reading-details dd {
  margin: 0;
  line-height: 1.55;
}

body.tsap-dark-mode .reading-entry {
  background: var(--bg-surface, #1f2937);
  border-color: var(--border-sub, #374151);
  color: var(--text-main, #e5e7eb);
}

body.tsap-dark-mode .reading-entry h2 {
  color: var(--text-heading, #f3f4f6);
}

body.tsap-dark-mode .reading-author,
body.tsap-dark-mode .reading-details dt {
  color: var(--text-muted, #cbd5e1);
}

.reading-status-finished {
  background: #e8f0ff;
  color: #173b70;
  border-color: #2859a8;
}

.reading-stars {
  color: #8a5a00;
  letter-spacing: 0.08em;
  white-space: nowrap;
}

.reading-empty-stars {
  color: #767676;
}

body.tsap-dark-mode .reading-stars {
  color: #ffd166;
}

body.tsap-dark-mode .reading-empty-stars {
  color: #9ca3af;
}

body.tsap-dark-mode .reading-status-finished {
  background: #1e3a5f;
  color: #dbeafe;
  border-color: #60a5fa;
}

body.tsap-dark-mode .reading-status {
  background: #173b2a;
  color: #d1fae5;
  border-color: #4ade80;
}

@media (max-width: 600px) {
  .reading-entry {
    padding: 1rem;
  }

  .reading-details {
    grid-template-columns: minmax(0, 1fr);
    gap: 0.8rem;
  }
}
</style>

<!--
Adding another book:
1. Copy the <article class="reading-entry">...</article> block for a book.
2. Add the new book above the existing entries so the newest entry appears first.
3. Give each heading a unique id and update its aria-labelledby value.
4. When finished, change the status to "Finished reading" and add a completion date.
5. Keep this page free of page_id metadata, as requested.
-->
