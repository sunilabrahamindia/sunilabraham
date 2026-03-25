---
layout: default
title: "Recent Changes"
description: "Track recent updates and edits across The Sunil Abraham Project."
permalink: /recent-changes/
categories: [Project pages]
created: 2026-03-25
---

**Recent Changes** lists recent edits and updates across The Sunil Abraham Project based on repository activity. Times are shown in your local timezone.

<div class="rc-controls">
  <label>
    Show
    <select id="rc-limit">
      <option value="20">20</option>
      <option value="50" selected>50</option>
      <option value="100">100</option>
    </select>
  </label>

  <label>
    Time
    <select id="rc-days">
      <option value="1">1 day</option>
      <option value="7" selected>7 days</option>
      <option value="30">30 days</option>
      <option value="all">All</option>
    </select>
  </label>
</div>

<div id="recent-changes" aria-live="polite">
  <p class="rc-loading">Loading recent changes…</p>
</div>

<div class="rc-more-wrap">
  <button id="rc-load-more" class="rc-more-btn">Load more</button>
</div>

<script>
const container = document.getElementById('recent-changes');
const loadMoreBtn = document.getElementById('rc-load-more');
const limitSelect = document.getElementById('rc-limit');
const daysSelect = document.getElementById('rc-days');

let currentPage = 1;
let isLoading = false;

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleString('en-IN', {
    dateStyle: 'medium',
    timeStyle: 'short'
  });
}

function cleanMessage(message) {
  if (!message) return 'Updated page';
  message = message.split('\n')[0];
  message = message.replace(/\.md/gi, '');
  message = message.replace(/_/g, ' ');
  return message;
}

function passesTimeFilter(dateString) {
  const days = daysSelect.value;
  if (days === 'all') return true;

  const cutoff = new Date();
  cutoff.setDate(cutoff.getDate() - parseInt(days));

  return new Date(dateString) >= cutoff;
}

async function fetchCommits(reset = false) {
  if (isLoading) return;

  isLoading = true;

  if (reset) {
    container.innerHTML = '';
    currentPage = 1;
  }

  const limit = limitSelect.value;

  try {
    const response = await fetch(
      `https://api.github.com/repos/sunilabrahamindia/sunilabraham/commits?per_page=${limit}&page=${currentPage}`
    );

    const commits = await response.json();

    if (!commits.length && currentPage === 1) {
      container.innerHTML = '<p>No recent changes found.</p>';
      return;
    }

    let shown = 0;

    commits.forEach(commit => {
      const date = commit.commit.author.date;

      if (!passesTimeFilter(date)) return;

      shown++;

      const message = cleanMessage(commit.commit.message);
      const author = commit.author ? commit.author.login : 'Unknown';
      const commitUrl = commit.html_url;

      const item = document.createElement('div');
      item.className = 'rc-item';

      item.innerHTML = `
        <div class="rc-top">
          <time class="rc-date" datetime="${date}">
            ${formatDate(date)}
          </time>
        </div>

        <div class="rc-message">
          ${message}
        </div>

        <div class="rc-author">
          Edited by ${author}
        </div>

        <div class="rc-links">
          <a href="${commitUrl}">View commit</a>
        </div>
      `;

      container.appendChild(item);
    });

    if (shown === 0 && currentPage === 1) {
      container.innerHTML = '<p>No changes found for selected time range.</p>';
    }

    currentPage++;

  } catch (error) {
    container.innerHTML = '<p>Unable to load recent changes at the moment.</p>';
    console.error(error);
  }

  isLoading = false;
}

limitSelect.addEventListener('change', () => fetchCommits(true));
daysSelect.addEventListener('change', () => fetchCommits(true));
loadMoreBtn.addEventListener('click', () => fetchCommits());

fetchCommits(true);
</script>

<style>
/* Controls */
.rc-controls {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin: 12px 0;
  font-size: 0.9rem;
}

.rc-controls select {
  margin-left: 6px;
  padding: 4px;
}

/* Container */
#recent-changes {
  margin-top: 1rem;
}

/* Card */
.rc-item {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 14px;
  margin-bottom: 14px;
  background: #fafafa;
}

/* Date */
.rc-date {
  font-size: 0.85rem;
  color: #666;
}

/* Message */
.rc-message {
  font-size: 1rem;
  font-weight: 600;
  color: #111;
  margin: 6px 0;
}

/* Author */
.rc-author {
  font-size: 0.9rem;
  color: #444;
}

/* Links */
.rc-links {
  margin-top: 8px;
}

.rc-links a {
  font-size: 0.85rem;
  color: #0645ad;
}

/* Load more */
.rc-more-wrap {
  text-align: centre;
  margin: 20px 0;
}

.rc-more-btn {
  padding: 8px 14px;
  border: 1px solid #ccc;
  background: #fff;
  border-radius: 6px;
  cursor: pointer;
}

.rc-more-btn:hover {
  background: #f5f5f5;
}

/* Mobile */
@media (max-width: 600px) {
  .rc-controls {
    flex-direction: column;
    gap: 8px;
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .rc-item {
    transition: none;
  }
}
</style>
