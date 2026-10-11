---
layout: default
title: "Recent Changes"
description: "Track recent updates and edits across The Sunil Abraham Project."
permalink: /recent-changes/
categories: [Project pages]
page_id: TSAP-0787
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

function formatDate(dateString) {
  return new Date(dateString).toLocaleString('en-IN', {
    dateStyle: 'medium',
    timeStyle: 'short'
  });
}

function extractFilename(message) {
  if (!message) return null;
  const parts = message.trim().split(' ');
  const last = parts[parts.length - 1];
  return last.endsWith('.md') ? last : null;
}

function detectAction(message) {
  if (!message) return 'Updated';
  message = message.toLowerCase();
  if (message.includes('create') || message.includes('add')) return 'Created';
  return 'Updated';
}

function formatAuthor(author) {
  const map = {
    'sunilabrahamindia': 'Tito (TSAP moderator)',
    'sunilabrahamayrookhuziel': 'Sunil Abraham (Owner)'
  };
  return map[author] || author;
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

      const variantIndex = (colorIndex % 6) + 1;
      colorIndex++;

      const item = document.createElement('div');
      item.className = `rc-item rc-card-variant-${variantIndex}`;

      // Title logic
      let titleHTML;
      if (filename) {
        titleHTML = `📄 File: ${filename}`;
      } else {
        titleHTML = `📝 Change: ${message}`;
      }

      let articleLink = '';

      item.innerHTML = `
        <div class="rc-title">${titleHTML}</div>

        <div class="rc-meta">
          ${action === 'Created' ? '🟢 Created' : '✏️ Updated'} • 
          <time datetime="${date}">${formatDate(date)}</time>
        </div>

        <div class="rc-author">
          👤 ${authorName}
        </div>

        <div class="rc-links">
          ${articleLink}
          🔗 <a href="${commitUrl}" rel="nofollow noopener noreferrer" target="_blank">View commit</a>
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
  margin: 16px 0 20px; 
  font-size: 0.95rem; 
}

.rc-controls label {
  font-weight: 500;
}

.rc-controls select { 
  margin-left: 6px; 
  padding: 6px 10px; 
  border: 1px solid #ccc; 
  border-radius: 6px; 
  background: #fff; 
  font-size: 0.9rem;
}

.rc-item { 
  border: 1px solid #e2e8f0; 
  border-radius: 10px; 
  padding: 16px; 
  margin-bottom: 16px; 
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  transition: background-color 0.2s ease, border-color 0.2s ease;
}

/* Light Mode Card Color Variants */
.rc-card-variant-1 { background-color: #f9fbff; }
.rc-card-variant-2 { background-color: #f6fff9; }
.rc-card-variant-3 { background-color: #fffaf6; }
.rc-card-variant-4 { background-color: #f8f6ff; }
.rc-card-variant-5 { background-color: #f6ffff; }
.rc-card-variant-6 { background-color: #fff6fa; }

.rc-title { 
  font-size: 1.05rem; 
  font-weight: 600; 
  color: #1e293b;
  margin-bottom: 6px;
  line-height: 1.4;
}

.rc-meta,
.rc-author { 
  font-size: 0.88rem; 
  color: #555; 
  margin-bottom: 4px;
}

.rc-links { 
  margin-top: 10px; 
  font-size: 0.88rem; 
}

.rc-links a { 
  color: #1f5fbf; 
  text-decoration: none;
  font-weight: 500;
}

.rc-links a:hover {
  text-decoration: underline;
}

.rc-more-wrap { 
  text-align: center; 
  margin: 24px 0 30px; 
}

.rc-more-btn {
  padding: 9px 18px;
  border: 1px solid #cbd5e1;
  background: #ffffff;
  color: #334155;
  border-radius: 6px;
  font-size: 0.92rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease;
}

.rc-more-btn:hover { 
  background: #f1f5f9; 
  border-color: #94a3b8;
}

.rc-loading {
  font-style: italic;
  color: #64748b;
  margin: 16px 0;
}

@media (max-width: 600px) {
  .rc-controls { 
    flex-direction: column; 
    gap: 10px;
  }
}

/* =========================================================
   Active Class Architecture Dark Mode Overrides
   ========================================================= */

body.tsap-dark-mode .rc-controls select {
  background: #1e293b !important;
  color: #f3f4f6 !important;
  border-color: #374151 !important;
}

body.tsap-dark-mode .rc-item {
  border-color: #374151 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
}

/* Dark Mode Card Variations */
body.tsap-dark-mode .rc-card-variant-1 { background-color: #1e293b !important; }
body.tsap-dark-mode .rc-card-variant-2 { background-color: #1b2e2b !important; }
body.tsap-dark-mode .rc-card-variant-3 { background-color: #2b281f !important; }
body.tsap-dark-mode .rc-card-variant-4 { background-color: #252238 !important; }
body.tsap-dark-mode .rc-card-variant-5 { background-color: #1b2d38 !important; }
body.tsap-dark-mode .rc-card-variant-6 { background-color: #2d1f28 !important; }

body.tsap-dark-mode .rc-title {
  color: #f3f4f6 !important;
}

body.tsap-dark-mode .rc-meta,
body.tsap-dark-mode .rc-author {
  color: #cbd5e1 !important;
}

body.tsap-dark-mode .rc-links a {
  color: #38bdf8 !important;
}

body.tsap-dark-mode .rc-more-btn {
  background: #1e293b !important;
  color: #f3f4f6 !important;
  border-color: #374151 !important;
}

body.tsap-dark-mode .rc-more-btn:hover {
  background: #334155 !important;
  border-color: #4b5563 !important;
}

body.tsap-dark-mode .rc-loading {
  color: #cbd5e1 !important;
}
</style>
