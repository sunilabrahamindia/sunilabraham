---
layout: default
title: "Versions Helper Tool"
description: "A helper tool for generating version reports for The Sunil Abraham Project from any selected date range."
permalink: /versions/helper/
categories: [Project pages, Versions]
created: 2026-08-24
---

**Versions Helper Tool** is a reporting tool for The Sunil Abraham Project that generates a summary of pages, Git activity, and GitHub activity for a selected date range. The tool is mainly created to support report writing for the [Versions](/versions/) and other report pages; however, it can also be used for broader activity summaries.

## Helper tool
Generate a report of pages created, Git commits, and GitHub issues for any date range.

<div id="activity-report-app" class="activity-report-container">
  <section class="report-controls" aria-labelledby="controls-heading">
    <h2 id="controls-heading">Select date range</h2>
    
    <div class="date-inputs">
      <div class="date-field">
        <label for="from-date">From</label>
        <input type="date" id="from-date" name="from" required />
      </div>
      
      <div class="date-field">
        <label for="to-date">To</label>
        <input type="date" id="to-date" name="to" required />
      </div>
    </div>
    
    <div class="date-shortcuts">
      <button type="button" id="prev-week-btn" class="shortcut-btn">Previous week</button>
      <button type="button" id="current-week-btn" class="shortcut-btn">Current week</button>
    </div>
    
    <button type="button" id="generate-btn" class="generate-btn">Generate report</button>
  </section>
  
  <section id="report-output" class="report-output" aria-live="polite" aria-busy="false">
    <p class="loading-msg">Select a date range and click "Generate report" to see activity.</p>
  </section>
  
  <section id="copy-output" class="copy-output" aria-labelledby="copy-heading">
    <h2 id="copy-heading">Copy-ready output</h2>
    <p>Use this text for the Versions page or weekly reports.</p>
    <textarea id="copy-text" rows="12" readonly aria-label="Copy-ready report text"></textarea>
    <button type="button" id="copy-btn" class="copy-btn">Copy to clipboard</button>
    <span id="copy-status" class="copy-status" role="status" aria-live="polite"></span>
  </section>
</div>

{% include versions.html %}

<style>
.activity-report-container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.report-controls {
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

@media (prefers-color-scheme: dark) {
  .report-controls {
    background: #2a2a2a;
    border-color: #444;
  }
}

.date-inputs {
  display: flex;
  gap: 1.5rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.date-field {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.date-field label {
  font-weight: 600;
  font-size: 0.9rem;
}

.date-field input[type="date"] {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  min-width: 180px;
}

@media (prefers-color-scheme: dark) {
  .date-field input[type="date"] {
    background: #333;
    border-color: #555;
    color: #fff;
  }
}

.date-shortcuts {
  display: flex;
  gap: 0.75rem;
  margin: 1rem 0;
}

.shortcut-btn,
.generate-btn,
.copy-btn {
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 4px;
  font-size: 0.95rem;
  cursor: pointer;
  background: #0066cc;
  color: #fff;
  transition: background 0.2s;
}

.shortcut-btn:hover,
.generate-btn:hover,
.copy-btn:hover {
  background: #0052a3;
}

.shortcut-btn:focus,
.generate-btn:focus,
.copy-btn:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

.generate-btn {
  margin-top: 0.5rem;
  font-weight: 600;
}

.report-output {
  margin-bottom: 2rem;
}

.report-section {
  margin-bottom: 2rem;
}

.report-section h3 {
  border-bottom: 2px solid #0066cc;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

@media (prefers-color-scheme: dark) {
  .report-section h3 {
    border-color: #4da3ff;
  }
}

.page-list {
  list-style: none;
  padding: 0;
}

.page-list li {
  margin-bottom: 0.75rem;
  padding: 0.5rem;
  border-left: 3px solid #0066cc;
  background: #fafafa;
}

@media (prefers-color-scheme: dark) {
  .page-list li {
    background: #2a2a2a;
    border-left-color: #4da3ff;
  }
}

.page-list a {
  font-weight: 600;
  text-decoration: none;
}

.page-list a:hover {
  text-decoration: underline;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.stat-card {
  background: #f0f0f0;
  padding: 1rem;
  border-radius: 6px;
  text-align: center;
}

@media (prefers-color-scheme: dark) {
  .stat-card {
    background: #333;
  }
}

.stat-card .stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #0066cc;
}

@media (prefers-color-scheme: dark) {
  .stat-card .stat-number {
    color: #4da3ff;
  }
}

.stat-card .stat-label {
  font-size: 0.9rem;
  color: #666;
}

@media (prefers-color-scheme: dark) {
  .stat-card .stat-label {
    color: #aaa;
  }
}

.issue-list,
.comment-list {
  list-style: none;
  padding: 0;
}

.issue-list li,
.comment-list li {
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  background: #f9f9f9;
  border-radius: 4px;
}

@media (prefers-color-scheme: dark) {
  .issue-list li,
  .comment-list li {
    background: #2a2a2a;
  }
}

.copy-output {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid #ddd;
}

@media (prefers-color-scheme: dark) {
  .copy-output {
    border-top-color: #444;
  }
}

.copy-output textarea {
  width: 100%;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.9rem;
  resize: vertical;
  margin: 1rem 0;
}

@media (prefers-color-scheme: dark) {
  .copy-output textarea {
    background: #2a2a2a;
    border-color: #555;
    color: #fff;
  }
}

.copy-status {
  margin-left: 1rem;
  font-weight: 600;
}

.copy-status.success {
  color: #2e7d32;
}

.copy-status.error {
  color: #c62828;
}

.loading-msg {
  color: #666;
  font-style: italic;
}

.error-msg {
  background: #ffebee;
  border: 1px solid #ef5350;
  color: #c62828;
  padding: 1rem;
  border-radius: 4px;
  margin: 1rem 0;
}

@media (prefers-color-scheme: dark) {
  .error-msg {
    background: #3b1f1f;
    border-color: #ef5350;
  }
}

.warning-msg {
  background: #fff3e0;
  border: 1px solid #ff9800;
  color: #e65100;
  padding: 0.75rem;
  border-radius: 4px;
  margin: 1rem 0;
  font-size: 0.9rem;
}

@media (prefers-color-scheme: dark) {
  .warning-msg {
    background: #3b2f1f;
    border-color: #ff9800;
  }
}

.day-breakdown,
.category-breakdown {
  margin: 1rem 0;
}

.day-breakdown ul,
.category-breakdown ul {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.5rem;
}

.day-breakdown li,
.category-breakdown li {
  background: #f0f0f0;
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
}

@media (prefers-color-scheme: dark) {
  .day-breakdown li,
  .category-breakdown li {
    background: #333;
  }
}
</style>

<script>
(function() {
  'use strict';
  
  const PAGES_JSON_URL = '/pages.json';
  const GITHUB_API_BASE = 'https://api.github.com/repos/sunilabrahamindia/sunilabraham';
  
  const fromInput = document.getElementById('from-date');
  const toInput = document.getElementById('to-date');
  const prevWeekBtn = document.getElementById('prev-week-btn');
  const currentWeekBtn = document.getElementById('current-week-btn');
  const generateBtn = document.getElementById('generate-btn');
  const reportOutput = document.getElementById('report-output');
  const copyText = document.getElementById('copy-text');
  const copyBtn = document.getElementById('copy-btn');
  const copyStatus = document.getElementById('copy-status');
  
  let cachedPages = null;
  let copyReadyText = '';
  
  function formatDateDMY(date) {
    const d = date.getDate();
    const m = date.toLocaleString('en-GB', { month: 'long' });
    const y = date.getFullYear();
    return `${d} ${m} ${y}`;
  }
  
  function formatDateISO(date) {
    return date.toISOString().split('T')[0];
  }
  
  function getDayName(date) {
    return date.toLocaleString('en-GB', { weekday: 'long' });
  }
  
  function getPreviousSundaySaturday() {
    const today = new Date();
    const dayOfWeek = today.getDay();
    const daysSinceSaturday = (dayOfWeek + 1) % 7;
    const saturday = new Date(today);
    saturday.setDate(today.getDate() - daysSinceSaturday);
    saturday.setHours(0, 0, 0, 0);
    const sunday = new Date(saturday);
    sunday.setDate(saturday.getDate() - 6);
    return { from: sunday, to: saturday };
  }
  
  function getCurrentWeekSundaySaturday() {
    const today = new Date();
    const dayOfWeek = today.getDay();
    const daysSinceSunday = dayOfWeek;
    const sunday = new Date(today);
    sunday.setDate(today.getDate() - daysSinceSunday);
    sunday.setHours(0, 0, 0, 0);
    const saturday = new Date(sunday);
    saturday.setDate(sunday.getDate() + 6);
    return { from: sunday, to: saturday };
  }
  
  function setDates(fromDate, toDate) {
    fromInput.value = formatDateISO(fromDate);
    toInput.value = formatDateISO(toDate);
    updateURL(fromDate, toDate);
  }
  
  function updateURL(fromDate, toDate) {
    const params = new URLSearchParams();
    params.set('from', formatDateISO(fromDate));
    params.set('to', formatDateISO(toDate));
    const newURL = `${window.location.pathname}?${params.toString()}`;
    window.history.replaceState({}, '', newURL);
  }
  
  function parseDateFromInput(input) {
    const val = input.value;
    if (!val) return null;
    const d = new Date(val + 'T00:00:00');
    return isNaN(d.getTime()) ? null : d;
  }
  
  function isInDateRange(date, from, to) {
    return date >= from && date <= to;
  }
  
  async function fetchPages() {
    if (cachedPages) return cachedPages;
    try {
      const resp = await fetch(PAGES_JSON_URL);
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const data = await resp.json();
      cachedPages = Array.isArray(data) ? data : [];
      return cachedPages;
    } catch (err) {
      console.error('Failed to fetch pages.json:', err);
      throw new Error('Could not load page index. Please refresh the page.');
    }
  }
  
  async function fetchCommits(since, until) {
    const commits = [];
    let page = 1;
    const perPage = 100;
    
    while (true) {
      const url = `${GITHUB_API_BASE}/commits?since=${formatDateISO(since)}T00:00:00Z&until=${formatDateISO(until)}T23:59:59Z&per_page=${perPage}&page=${page}`;
      const resp = await fetch(url);
      if (!resp.ok) {
        if (resp.status === 403) throw new Error('GitHub API rate limit exceeded for commits.');
        throw new Error(`GitHub API error ${resp.status} for commits.`);
      }
      const data = await resp.json();
      if (!Array.isArray(data) || data.length === 0) break;
      commits.push(...data);
      if (data.length < perPage) break;
      page++;
    }
    return commits;
  }
  
  async function fetchIssues(since, until) {
    const issues = [];
    let page = 1;
    const perPage = 100;
    
    while (true) {
      const url = `${GITHUB_API_BASE}/issues?state=all&since=${formatDateISO(since)}T00:00:00Z&until=${formatDateISO(until)}T23:59:59Z&per_page=${perPage}&page=${page}`;
      const resp = await fetch(url);
      if (!resp.ok) {
        if (resp.status === 403) throw new Error('GitHub API rate limit exceeded for issues.');
        throw new Error(`GitHub API error ${resp.status} for issues.`);
      }
      const data = await resp.json();
      if (!Array.isArray(data) || data.length === 0) break;
      issues.push(...data);
      if (data.length < perPage) break;
      page++;
    }
    return issues.filter(i => !i.pull_request);
  }
  
  async function fetchIssueComments(issueNumber, since, until) {
    const comments = [];
    let page = 1;
    const perPage = 100;
    
    while (true) {
      const url = `${GITHUB_API_BASE}/issues/${issueNumber}/comments?since=${formatDateISO(since)}T00:00:00Z&until=${formatDateISO(until)}T23:59:59Z&per_page=${perPage}&page=${page}`;
      const resp = await fetch(url);
      if (!resp.ok) {
        if (resp.status === 403) return { error: 'rate_limit' };
        return { error: `HTTP ${resp.status}` };
      }
      const data = await resp.json();
      if (!Array.isArray(data) || data.length === 0) break;
      comments.push(...data);
      if (data.length < perPage) break;
      page++;
    }
    return comments;
  }
  
  async function fetchIssuesWithComments(since, until, allIssues) {
    const issuesWithComments = [];
    let rateLimitHit = false;
    
    for (const issue of allIssues) {
      if (rateLimitHit) {
        issuesWithComments.push({
          issue,
          comments: [],
          error: 'Rate limit hit'
        });
        continue;
      }
      
      try {
        const comments = await fetchIssueComments(issue.number, since, until);
        if (comments.error === 'rate_limit') {
          rateLimitHit = true;
          issuesWithComments.push({
            issue,
            comments: [],
            error: 'Rate limit hit'
          });
        } else if (comments.error) {
          issuesWithComments.push({
            issue,
            comments: [],
            error: comments.error
          });
        } else if (comments.length > 0) {
          issuesWithComments.push({
            issue,
            comments,
            error: null
          });
        }
      } catch (err) {
        issuesWithComments.push({
          issue,
          comments: [],
          error: err.message
        });
      }
    }
    
    return { issuesWithComments, rateLimitHit };
  }
  
  function filterPagesByDate(pages, from, to) {
    return pages.filter(p => {
      if (!p.created) return false;
      const createdDate = new Date(p.created + 'T00:00:00');
      return isInDateRange(createdDate, from, to);
    });
  }
  
  function groupPagesByDay(pages) {
    const groups = {};
    for (const p of pages) {
      const day = p.created;
      groups[day] = (groups[day] || 0) + 1;
    }
    return groups;
  }
  
  function groupPagesByCategory(pages) {
    const groups = {};
    for (const p of pages) {
      const cats = p.categories || [];
      for (const c of cats) {
        groups[c] = (groups[c] || 0) + 1;
      }
    }
    return groups;
  }
  
  function renderReport(pages, commits, issuesCreated, issuesWithCommentsData, from, to) {
    const fromDayName = getDayName(from);
    const toDayName = getDayName(to);
    const fromStr = formatDateDMY(from);
    const toStr = formatDateDMY(to);
    
    const pagesByDay = groupPagesByDay(pages);
    const pagesByCategory = groupPagesByCategory(pages);
    
    let html = '';
    
    html += `<div class="report-section">`;
    html += `<h3>Pages created</h3>`;
    html += `<p><strong>From ${fromDayName} ${fromStr} to ${toDayName} ${toStr}, ${pages.length} page${pages.length !== 1 ? 's' : ''} were created.</strong></p>`;
    
    if (pages.length === 0) {
      html += `<p class="warning-msg">No pages were created during this period.</p>`;
    } else {
      html += `<div class="stats-grid">`;
      html += `<div class="stat-card"><div class="stat-number">${pages.length}</div><div class="stat-label">Total pages</div></div>`;
      html += `</div>`;
      
      html += `<div class="day-breakdown"><h4>Pages per day</h4><ul>`;
      const sortedDays = Object.keys(pagesByDay).sort();
      for (const day of sortedDays) {
        const d = new Date(day + 'T00:00:00');
        const dayName = getDayName(d);
        const dayDate = formatDateDMY(d);
        html += `<li>${dayName} ${dayDate}: ${pagesByDay[day]}</li>`;
      }
      html += `</ul></div>`;
      
      html += `<div class="category-breakdown"><h4>Pages by category</h4><ul>`;
      const sortedCats = Object.keys(pagesByCategory).sort();
      for (const cat of sortedCats) {
        html += `<li>${cat}: ${pagesByCategory[cat]}</li>`;
      }
      html += `</ul></div>`;
      
      html += `<ul class="page-list">`;
      const sortedPages = [...pages].sort((a, b) => a.created.localeCompare(b.created));
      for (const p of sortedPages) {
        const d = new Date(p.created + 'T00:00:00');
        const createdStr = formatDateDMY(d);
        const title = p.title || 'Untitled';
        const permalink = p.permalink || '#';
        const desc = p.description || '';
        html += `<li><a href="${permalink}">${title}</a>, created on ${createdStr} – ${desc}</li>`;
      }
      html += `</ul>`;
    }
    html += `</div>`;
    
    html += `<div class="report-section">`;
    html += `<h3>Git activity</h3>`;
    html += `<p><strong>${commits.length} commit${commits.length !== 1 ? 's' : ''}</strong> were made during this period.</p>`;
    html += `</div>`;
    
    html += `<div class="report-section">`;
    html += `<h3>GitHub issues created</h3>`;
    if (issuesCreated.length === 0) {
      html += `<p class="warning-msg">No issues were created during this period.</p>`;
    } else {
      html += `<ul class="issue-list">`;
      const sortedIssues = [...issuesCreated].sort((a, b) => a.created_at.localeCompare(b.created_at));
      for (const issue of sortedIssues) {
        const d = new Date(issue.created_at);
        const createdStr = formatDateDMY(d);
        html += `<li>#${issue.number} <a href="${issue.html_url}" rel="noopener">${issue.title}</a>, created on ${createdStr}</li>`;
      }
      html += `</ul>`;
    }
    html += `</div>`;
    
    html += `<div class="report-section">`;
    html += `<h3>GitHub issues with new comments</h3>`;
    const { issuesWithComments, rateLimitHit } = issuesWithCommentsData;
    const issuesWithNewComments = issuesWithComments.filter(i => i.comments && i.comments.length > 0);
    
    if (issuesWithNewComments.length === 0) {
      html += `<p class="warning-msg">No existing issues received new comments during this period.</p>`;
    } else {
      html += `<ul class="comment-list">`;
      for (const item of issuesWithNewComments) {
        const issue = item.issue;
        const comments = item.comments;
        const firstComment = comments[0];
        const d = new Date(firstComment.created_at);
        const commentStr = formatDateDMY(d);
        html += `<li>#${issue.number} <a href="${issue.html_url}" rel="noopener">${issue.title}</a>, ${comments.length} new comment${comments.length !== 1 ? 's' : ''} (first on ${commentStr})</li>`;
      }
      html += `</ul>`;
    }
    
    if (rateLimitHit) {
      html += `<p class="warning-msg">Note: GitHub API rate limit was reached. Some issue comment data may be incomplete.</p>`;
    }
    html += `</div>`;
    
    reportOutput.innerHTML = html;
    
    const openingSentence = `From ${fromDayName} ${fromStr} to ${toDayName} ${toStr}, ${pages.length} page${pages.length !== 1 ? 's' : ''} were created.`;
    let copyTextContent = openingSentence + '\n\n';
    
    if (pages.length > 0) {
      const sortedPages = [...pages].sort((a, b) => a.created.localeCompare(b.created));
      for (const p of sortedPages) {
        const d = new Date(p.created + 'T00:00:00');
        const createdStr = formatDateDMY(d);
        const title = p.title || 'Untitled';
        const permalink = p.permalink || '#';
        const desc = p.description || '';
        copyTextContent += `**[${title}](${permalink})**, created on ${createdStr} – ${desc}\n`;
      }
      copyTextContent += '\n';
    }
    
    copyTextContent += `\n**Git activity:** ${commits.length} commit${commits.length !== 1 ? 's' : ''}.\n`;
    copyTextContent += `\n**GitHub issues created:** ${issuesCreated.length}.\n`;
    if (issuesCreated.length > 0) {
      const sortedIssues = [...issuesCreated].sort((a, b) => a.created_at.localeCompare(b.created_at));
      for (const issue of sortedIssues) {
        const d = new Date(issue.created_at);
        const createdStr = formatDateDMY(d);
        copyTextContent += `- #${issue.number} [${issue.title}](${issue.html_url}), created on ${createdStr}\n`;
      }
    }
    
    copyReadyText = copyTextContent;
    copyText.value = copyReadyText;
  }
  
  async function generateReport() {
    const from = parseDateFromInput(fromInput);
    const to = parseDateFromInput(toInput);
    
    if (!from || !to) {
      reportOutput.innerHTML = `<p class="error-msg">Please select both From and To dates.</p>`;
      return;
    }
    
    if (from > to) {
      reportOutput.innerHTML = `<p class="error-msg">The From date must be before or equal to the To date.</p>`;
      return;
    }
    
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    if (to > today) {
      reportOutput.innerHTML = `<p class="error-msg">The To date cannot be in the future.</p>`;
      return;
    }
    
    reportOutput.setAttribute('aria-busy', 'true');
    reportOutput.innerHTML = `<p class="loading-msg">Loading data…</p>`;
    copyText.value = '';
    copyReadyText = '';
    
    try {
      const pages = await fetchPages();
      const filteredPages = filterPagesByDate(pages, from, to);
      
      let commits = [];
      let commitsError = null;
      try {
        commits = await fetchCommits(from, to);
      } catch (err) {
        commitsError = err.message;
      }
      
      let issuesCreated = [];
      let issuesCreatedError = null;
      try {
        issuesCreated = await fetchIssues(from, to);
      } catch (err) {
        issuesCreatedError = err.message;
      }
      
      let issuesWithCommentsData = { issuesWithComments: [], rateLimitHit: false };
      if (issuesCreated.length > 0 || true) {
        try {
          const allIssuesForComments = await fetchIssues(new Date(from.getTime() - 30 * 24 * 60 * 60 * 1000), to);
          issuesWithCommentsData = await fetchIssuesWithComments(from, to, allIssuesForComments);
        } catch (err) {
          issuesWithCommentsData = { issuesWithComments: [], rateLimitHit: true };
        }
      }
      
      renderReport(filteredPages, commits, issuesCreated, issuesWithCommentsData, from, to);
      
      if (commitsError) {
        const warning = document.createElement('p');
        warning.className = 'warning-msg';
        warning.textContent = `Note: ${commitsError}`;
        reportOutput.insertBefore(warning, reportOutput.firstChild);
      }
      
      if (issuesCreatedError) {
        const warning = document.createElement('p');
        warning.className = 'warning-msg';
        warning.textContent = `Note: ${issuesCreatedError}`;
        reportOutput.insertBefore(warning, reportOutput.firstChild);
      }
      
    } catch (err) {
      reportOutput.innerHTML = `<p class="error-msg">Error: ${err.message}</p>`;
    } finally {
      reportOutput.setAttribute('aria-busy', 'false');
    }
  }
  
  function copyToClipboard() {
    if (!copyReadyText) {
      copyStatus.textContent = 'Generate a report first.';
      copyStatus.className = 'copy-status error';
      return;
    }
    
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    
    navigator.clipboard.writeText(copyReadyText).then(() => {
      copyStatus.textContent = 'Copied!';
      copyStatus.className = 'copy-status success';
      setTimeout(() => {
        copyStatus.textContent = '';
        copyStatus.className = 'copy-status';
      }, 2000);
    }).catch(() => {
      copyStatus.textContent = 'Copy failed. Select and copy manually.';
      copyStatus.className = 'copy-status error';
    });
  }
  
  prevWeekBtn.addEventListener('click', () => {
    const { from, to } = getPreviousSundaySaturday();
    setDates(from, to);
  });
  
  currentWeekBtn.addEventListener('click', () => {
    const { from, to } = getCurrentWeekSundaySaturday();
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    if (to > today) {
      toInput.max = formatDateISO(today);
    }
    setDates(from, to);
  });
  
  generateBtn.addEventListener('click', generateReport);
  copyBtn.addEventListener('click', copyToClipboard);
  
  const params = new URLSearchParams(window.location.search);
  const fromParam = params.get('from');
  const toParam = params.get('to');
  
  if (fromParam && toParam) {
    const from = new Date(fromParam + 'T00:00:00');
    const to = new Date(toParam + 'T00:00:00');
    if (!isNaN(from.getTime()) && !isNaN(to.getTime())) {
      fromInput.value = fromParam;
      toInput.value = toParam;
    } else {
      const { from, to } = getPreviousSundaySaturday();
      setDates(from, to);
    }
  } else {
    const { from, to } = getPreviousSundaySaturday();
    setDates(from, to);
  }
  
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  toInput.max = formatDateISO(today);
  
})();
</script>
