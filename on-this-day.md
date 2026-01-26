---
layout: default
title: "On This Day"
description: "Discover Sunil Abraham's publications, media articles, and media mentions from history organised by date—explore what happened today, this month, and beyond."
categories: [Project pages]
permalink: /on-this-day/
created: 2026-01-26
---

The Sunil Abraham Project archives a substantial body of work spanning publications, media articles, and media mentions. This chronological view surfaces historical content by date, allowing you to discover contributions that might otherwise remain buried in the archives. Whether you're researching Sunil's evolving perspectives on a topic or tracking media coverage over time, this timeline offers a unique lens into his intellectual journey and public influence.

Whilst publications and media content are fully integrated here, events (conducted and participated) await sufficient standalone coverage and necessary metadata. Those will be added gradually as documentation standards are met.

<style>
.otd-container {
  max-width: 100%;
  margin: 0 auto;
}

.otd-section {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-left: 4px solid #007bff;
  border-radius: 4px;
}

.otd-section h3 {
  margin-top: 0;
  color: #333;
  font-size: 1.5rem;
}

.otd-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

.otd-item {
  padding: 1rem;
  margin: 0.75rem 0;
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.otd-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.otd-item-title {
  font-weight: 600;
  color: #007bff;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.otd-item-title a {
  color: #007bff;
  text-decoration: none;
}

.otd-item-title a:hover {
  text-decoration: underline;
}

.otd-item-date {
  color: #6c757d;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  font-style: italic;
}

.otd-item-description {
  color: #495057;
  line-height: 1.6;
}

.otd-empty {
  padding: 1rem;
  color: #6c757d;
  font-style: italic;
  text-align: center;
}

.otd-date-header {
  font-size: 1.8rem;
  color: #212529;
  margin: 2rem 0 1rem 0;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #dee2e6;
}

.otd-month-label {
  display: inline-block;
  background: #007bff;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.85rem;
  margin-left: 1rem;
  font-weight: normal;
}

.otd-debug {
  background: #fff3cd;
  border: 1px solid #ffc107;
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.9rem;
}

/* Mobile optimisation */
@media (max-width: 768px) {
  .otd-section {
    padding: 1rem;
    margin: 1rem 0;
  }
  
  .otd-date-header {
    font-size: 1.4rem;
  }
  
  .otd-item {
    padding: 0.75rem;
  }
  
  .otd-item-title {
    font-size: 1rem;
  }
  
  .otd-month-label {
    display: block;
    margin: 0.5rem 0 0 0;
    width: fit-content;
  }
}

@media (max-width: 480px) {
  .otd-section {
    padding: 0.75rem;
    margin: 0.75rem 0;
  }
  
  .otd-date-header {
    font-size: 1.2rem;
  }
  
  .otd-item-title {
    font-size: 0.95rem;
  }
  
  .otd-item-date {
    font-size: 0.85rem;
  }
  
  .otd-item-description {
    font-size: 0.9rem;
  }
}
</style>

<div class="otd-container">
  <!-- Debug information -->
  <div class="otd-debug" id="debug-info">Loading data...</div>
  
  <h2 class="otd-date-header" id="today-date"></h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <ul class="otd-list" id="today-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <ul class="otd-list" id="today-mentions"></ul>
  </div>

  <h2 class="otd-date-header">
    This Month <span class="otd-month-label" id="current-month-label"></span>
  </h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <ul class="otd-list" id="month-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <ul class="otd-list" id="month-mentions"></ul>
  </div>

  <h2 class="otd-date-header">
    Previous Month <span class="otd-month-label" id="prev-month-label"></span>
  </h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <ul class="otd-list" id="prev-month-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <ul class="otd-list" id="prev-month-mentions"></ul>
  </div>

  <h2 class="otd-date-header">
    Next Month <span class="otd-month-label" id="next-month-label"></span>
  </h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <ul class="otd-list" id="next-month-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <ul class="otd-list" id="next-month-mentions"></ul>
  </div>
</div>

<script>
// Configuration
const SITE_DATA = {
  publications: [],
  mentions: []
};

// Populate data from Jekyll
{% for page in site.pages %}
  {% if page.date and page.categories %}
    {% assign is_publication = false %}
    {% assign is_mention = false %}
    
    {% for cat in page.categories %}
      {% assign cat_lower = cat | downcase %}
      {% if cat_lower contains "publication" or cat_lower contains "media article" %}
        {% assign is_publication = true %}
      {% endif %}
      {% if cat_lower contains "media mention" %}
        {% assign is_mention = true %}
      {% endif %}
    {% endfor %}
    
    {% if is_publication %}
      SITE_DATA.publications.push({
        title: {{ page.title | jsonify }},
        date: "{{ page.date }}",
        description: {{ page.description | default: "" | jsonify }},
        url: {{ page.url | jsonify }},
        categories: {{ page.categories | jsonify }}
      });
    {% endif %}
    
    {% if is_mention %}
      SITE_DATA.mentions.push({
        title: {{ page.title | jsonify }},
        date: "{{ page.date }}",
        description: {{ page.description | default: "" | jsonify }},
        url: {{ page.url | jsonify }},
        categories: {{ page.categories | jsonify }}
      });
    {% endif %}
  {% endif %}
{% endfor %}

// Also try posts if they exist
{% for post in site.posts %}
  {% if post.date and post.categories %}
    {% assign is_publication = false %}
    {% assign is_mention = false %}
    
    {% for cat in post.categories %}
      {% assign cat_lower = cat | downcase %}
      {% if cat_lower contains "publication" or cat_lower contains "media article" %}
        {% assign is_publication = true %}
      {% endif %}
      {% if cat_lower contains "media mention" %}
        {% assign is_mention = true %}
      {% endif %}
    {% endfor %}
    
    {% if is_publication %}
      SITE_DATA.publications.push({
        title: {{ post.title | jsonify }},
        date: "{{ post.date | date: '%Y-%m-%d' }}",
        description: {{ post.description | default: "" | jsonify }},
        url: {{ post.url | jsonify }},
        categories: {{ post.categories | jsonify }}
      });
    {% endif %}
    
    {% if is_mention %}
      SITE_DATA.mentions.push({
        title: {{ post.title | jsonify }},
        date: "{{ post.date | date: '%Y-%m-%d' }}",
        description: {{ post.description | default: "" | jsonify }},
        url: {{ post.url | jsonify }},
        categories: {{ post.categories | jsonify }}
      });
    {% endif %}
  {% endif %}
{% endfor %}

// Date utility functions
function formatDateDMY(date) {
  const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December'];
  
  return `${days[date.getDay()]}, ${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}`;
}

function formatMonthYear(date) {
  const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December'];
  return `${months[date.getMonth()]} ${date.getFullYear()}`;
}

function parseDate(dateString) {
  // Handle both YYYY-MM-DD and full ISO date formats
  if (dateString.includes('T')) {
    return new Date(dateString);
  }
  const parts = dateString.split('-');
  return new Date(parts[0], parts[1] - 1, parts[2]);
}

function matchesMonthDay(itemDate, targetDate) {
  const item = parseDate(itemDate);
  return item.getMonth() === targetDate.getMonth() && 
         item.getDate() === targetDate.getDate();
}

function matchesMonth(itemDate, targetMonth) {
  const item = parseDate(itemDate);
  return item.getMonth() === targetMonth;
}

function renderItems(items, containerId) {
  const container = document.getElementById(containerId);
  
  if (items.length === 0) {
    container.innerHTML = '<li class="otd-empty">No items found for this period</li>';
    return;
  }
  
  // Sort by oldest first
  items.sort((a, b) => parseDate(a.date) - parseDate(b.date));
  
  const html = items.map(item => {
    const itemDate = parseDate(item.date);
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    const formattedDate = `${itemDate.getDate()} ${months[itemDate.getMonth()]} ${itemDate.getFullYear()}`;
    
    return `
      <li class="otd-item">
        <div class="otd-item-title"><a href="${item.url}">${item.title}</a></div>
        <div class="otd-item-date">${formattedDate}</div>
        ${item.description ? `<div class="otd-item-description">${item.description}</div>` : ''}
      </li>
    `;
  }).join('');
  
  container.innerHTML = html;
}

// Initialize the page
function init() {
  const today = new Date();
  
  // Debug information
  const debugInfo = document.getElementById('debug-info');
  debugInfo.innerHTML = `
    <strong>Debug Information:</strong><br>
    Total Publications: ${SITE_DATA.publications.length}<br>
    Total Media Mentions: ${SITE_DATA.mentions.length}<br>
    Today's Date: ${today.getDate()}/${today.getMonth() + 1}/${today.getFullYear()}<br>
    <details>
      <summary>Sample Data (click to expand)</summary>
      Publications: ${JSON.stringify(SITE_DATA.publications.slice(0, 3), null, 2)}<br>
      Mentions: ${JSON.stringify(SITE_DATA.mentions.slice(0, 3), null, 2)}
    </details>
  `;
  
  // Set today's date header
  document.getElementById('today-date').textContent = formatDateDMY(today);
  
  // Get month information
  const currentMonth = today.getMonth();
  const currentYear = today.getFullYear();
  
  const prevMonthDate = new Date(currentYear, currentMonth - 1, 1);
  const nextMonthDate = new Date(currentYear, currentMonth + 1, 1);
  
  // Set month labels
  document.getElementById('current-month-label').textContent = formatMonthYear(today);
  document.getElementById('prev-month-label').textContent = formatMonthYear(prevMonthDate);
  document.getElementById('next-month-label').textContent = formatMonthYear(nextMonthDate);
  
  // Filter and render today's items (matching ONLY month and day, ANY year)
  const todayPubs = SITE_DATA.publications.filter(item => matchesMonthDay(item.date, today));
  const todayMentions = SITE_DATA.mentions.filter(item => matchesMonthDay(item.date, today));
  
  console.log('Today filter - Day:', today.getDate(), 'Month:', today.getMonth());
  console.log('Today publications found:', todayPubs.length);
  console.log('Today mentions found:', todayMentions.length);
  
  renderItems(todayPubs, 'today-publications');
  renderItems(todayMentions, 'today-mentions');
  
  // Filter and render this month's items (excluding today)
  const monthPubs = SITE_DATA.publications.filter(item => 
    matchesMonth(item.date, currentMonth) && !matchesMonthDay(item.date, today)
  );
  const monthMentions = SITE_DATA.mentions.filter(item => 
    matchesMonth(item.date, currentMonth) && !matchesMonthDay(item.date, today)
  );
  
  renderItems(monthPubs, 'month-publications');
  renderItems(monthMentions, 'month-mentions');
  
  // Filter and render previous month's items
  const prevMonthPubs = SITE_DATA.publications.filter(item => 
    matchesMonth(item.date, prevMonthDate.getMonth())
  );
  const prevMonthMentions = SITE_DATA.mentions.filter(item => 
    matchesMonth(item.date, prevMonthDate.getMonth())
  );
  
  renderItems(prevMonthPubs, 'prev-month-publications');
  renderItems(prevMonthMentions, 'prev-month-mentions');
  
  // Filter and render next month's items
  const nextMonthPubs = SITE_DATA.publications.filter(item => 
    matchesMonth(item.date, nextMonthDate.getMonth())
  );
  const nextMonthMentions = SITE_DATA.mentions.filter(item => 
    matchesMonth(item.date, nextMonthDate.getMonth())
  );
  
  renderItems(nextMonthPubs, 'next-month-publications');
  renderItems(nextMonthMentions, 'next-month-mentions');
}

// Run on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
</script>
