---
layout: default
title: "Recent Changes"
description: "Track recent updates and edits across The Sunil Abraham Project."
permalink: /recent-changes/
categories: [Project pages]
created: 2026-03-25
---

**Recent Changes** lists recent edits and updates across **The Sunil Abraham Project** (TSAP) based on repository activity.  

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
let colorIndex = 0;

const bgColors = [
  '#f9fbff',
  '#f6fff9',
  '#fffaf6',
  '#f8f6ff',
  '#f6ffff',
  '#fff6fa'
];

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleString('en-IN', {
    dateStyle: 'medium',
    timeStyle: 'short'
  });
}

function extractFilename(message) {
  if (!message) return 'unknown';

  const parts = message.trim().split(' ');
  return parts[parts.length - 1];
}

function detectAction(message) {
  if (!message) return 'Updated';
  message = message.toLowerCase();

  if (message.includes('create') || message.includes('add')) {
    return 'Created';
  }
  return 'Updated';
}

function formatAuthor(author) {
  const map = {
    'sunilabrahamindia': 'Tito (TSAP moderator)',
    'sunilabrahamayrookhuziel': 'Sunil Abraham (Owner)'
  };
  return map[author] || author;
}

function isMarkdownFile(filename) {
  return filename && filename.endsWith('.md');
}

function fileToPageUrl(filename) {
  if (!isMarkdownFile(filename)) return null;

  return '/' + filename.replace('.md', '/');
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
    colorIndex = 0;
  }

  const limit = limitSelect.value;

  try {
    const response = await fetch(
      `https://api.github.com/repos/sunilabrahamindia/sunilabraham/commits?per_page=${limit}&page=${currentPage}`
    );

    const commits = await response.json();

    let shown = 0;

    commits.forEach(commit => {
      const date = commit.commit.author.date;

      if (!passesTimeFilter(date)) return;

      shown++;

      const message = commit.commit.message;
      const filename = extractFilename(message);
      const action = detectAction(message);
      const author = commit.author ? commit.author.login : 'Unknown';
      const authorName = formatAuthor(author);
      const commitUrl = commit.html_url;
      const pageUrl = fileToPageUrl(filename);

      const bg = bgColors[colorIndex % bgColors.length];
      colorIndex++;

      const item = document.createElement('div');
      item.className = 'rc-item';
      item.style.background = bg;

      item.innerHTML = `
        <div class="rc-title">📄 File: ${filename}</div>

        <div class="rc-meta">
          ${action === 'Created' ? '🟢 Created' : '✏️ Updated'} • 
          <time datetime="${date}">${formatDate(date)}</time>
        </div>

        <div class="rc-author">
          👤 ${authorName}
        </div>

        <div class="rc-links">
          ${pageUrl ? `📖 <a href="${pageUrl}">View article</a>` : ''}
          🔗 <a href="${commitUrl}" rel="nofollow noopener noreferrer">View commit</a>
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

.rc-item {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 14px;
  margin-bottom: 14px;
}

.rc-title {
  font-size: 1.05rem;
  font-weight: 600;
}

.rc-meta {
  font-size: 0.85rem;
  color: #555;
}

.rc-author {
  font-size: 0.85rem;
  color: #444;
}

.rc-links {
  margin-top: 6px;
  font-size: 0.85rem;
}

.rc-links a {
  color: #0645ad;
}

.rc-more-wrap {
  text-align: center;
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

@media (max-width: 600px) {
  .rc-controls {
    flex-direction: column;
  }
}
</style>
