---
layout: default
title: "On This Day"
description: "Discover Sunil Abraham's publications, media articles, and media mentions from history organised by date—explore what happened today, this week, and beyond."
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

.otd-intro {
  color: #495057;
  margin-bottom: 1rem;
  font-style: italic;
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

.otd-week-label {
  display: inline-block;
  background: #007bff;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.85rem;
  margin-left: 1rem;
  font-weight: normal;
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
  
  .otd-week-label {
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
  
  .otd-intro {
    font-size: 0.9rem;
  }
}
</style>

<div class="otd-container">
  <h2 class="otd-date-header" id="today-date"></h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro">Sunil Abraham published the following articles on this day in history.</p>
    <ul class="otd-list" id="today-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro">Sunil Abraham was mentioned or quoted in the following articles on this day in history.</p>
    <ul class="otd-list" id="today-mentions"></ul>
  </div>

  <h2 class="otd-date-header">
    This Week <span class="otd-week-label" id="current-week-range"></span>
  </h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro">Sunil Abraham published the following articles during this week across different years.</p>
    <ul class="otd-list" id="week-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro">Sunil Abraham was mentioned or quoted in the following articles during this week across different years.</p>
    <ul class="otd-list" id="week-mentions"></ul>
  </div>

  <h2 class="otd-date-header">
    Previous Week <span class="otd-week-label" id="prev-week-range"></span>
  </h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro">Sunil Abraham published the following articles during the previous week across different years.</p>
    <ul class="otd-list" id="prev-week-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro">Sunil Abraham was mentioned or quoted in the following articles during the previous week across different years.</p>
    <ul class="otd-list" id="prev-week-mentions"></ul>
  </div>

  <h2 class="otd-date-header">
    Next Week <span class="otd-week-label" id="next-week-range"></span>
  </h2>
  
  <div class="otd-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro">Sunil Abraham published the following articles during the next week across different years.</p>
    <ul class="otd-list" id="next-week-publications"></ul>
  </div>
  
  <div class="otd-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro">Sunil Abraham was mentioned or quoted in the following articles during the next week across different years.</p>
    <ul class="otd-list" id="next-week-mentions"></ul>
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
        url: {{ page.url | jsonify }}
      });
    {% endif %}
    
    {% if is_mention %}
      SITE_DATA.mentions.push({
        title: {{ page.title | jsonify }},
        date: "{{ page.date }}",
        description: {{ page.description | default: "" | jsonify }},
        url: {{ page.url | jsonify }}
      });
    {% endif %}
  {% endif %}
{% endfor %}

// Also check posts
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
        url: {{ post.url | jsonify }}
      });
    {% endif %}
    
    {% if is_mention %}
      SITE_DATA.mentions.push({
        title: {{ post.title | jsonify }},
        date: "{{ post.date | date: '%Y-%m-%d' }}",
        description: {{ post.description | default: "" | jsonify }},
        url: {{ post.url | jsonify }}
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

function formatDateRange(startDate, endDate) {
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  
  if (startDate.getMonth() === endDate.getMonth() && startDate.getFullYear() === endDate.getFullYear()) {
    return `${startDate.getDate()}–${endDate.getDate()} ${months[startDate.getMonth()]} ${startDate.getFullYear()}`;
  } else if (startDate.getFullYear() === endDate.getFullYear()) {
    return `${startDate.getDate()} ${months[startDate.getMonth()]}–${endDate.getDate()} ${months[endDate.getMonth()]} ${startDate.getFullYear()}`;
  } else {
    return `${startDate.getDate()} ${months[startDate.getMonth()]} ${startDate.getFullYear()}–${endDate.getDate()} ${months[endDate.getMonth()]} ${endDate.getFullYear()}`;
  }
}

function parseDate(dateString) {
  if (dateString.includes('T')) {
    return new Date(dateString);
  }
  const parts = dateString.split('-');
  return new Date(parts[0], parts[1] - 1, parts[2]);
}

function getWeekBounds(date, weekOffset = 0) {
  const targetDate = new Date(date);
  targetDate.setDate(targetDate.getDate() + (weekOffset * 7));
  
  const dayOfWeek = targetDate.getDay();
  const sunday = new Date(targetDate);
  sunday.setDate(targetDate.getDate() - dayOfWeek);
  sunday.setHours(0, 0, 0, 0);
  
  const saturday = new Date(sunday);
  saturday.setDate(sunday.getDate() + 6);
  saturday.setHours(23, 59, 59, 999);
  
  return { start: sunday, end: saturday };
}

function matchesMonthDay(itemDate, targetDate) {
  const item = parseDate(itemDate);
  return item.getMonth() === targetDate.getMonth() && 
         item.getDate() === targetDate.getDate();
}

function isInWeek(itemDate, weekStart, weekEnd) {
  const item = parseDate(itemDate);
  const startMD = weekStart.getMonth() * 100 + weekStart.getDate();
  const endMD = weekEnd.getMonth() * 100 + weekEnd.getDate();
  const itemMD = item.getMonth() * 100 + item.getDate();
  
  // Handle year wrap-around (e.g., week spanning December-January)
  if (weekStart.getMonth() > weekEnd.getMonth()) {
    return itemMD >= startMD || itemMD <= endMD;
  } else {
    return itemMD >= startMD && itemMD <= endMD;
  }
}

function renderItems(items, containerId) {
  const container = document.getElementById(containerId);
  
  if (items.length === 0) {
    container.innerHTML = '<li class="otd-empty">No items found for this period</li>';
    return;
  }
  
  // Sort by oldest year first
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
  
  // Set today's date header
  document.getElementById('today-date').textContent = formatDateDMY(today);
  
  // Get week bounds
  const currentWeek = getWeekBounds(today, 0);
  const prevWeek = getWeekBounds(today, -1);
  const nextWeek = getWeekBounds(today, 1);
  
  // Set week range labels
  document.getElementById('current-week-range').textContent = formatDateRange(currentWeek.start, currentWeek.end);
  document.getElementById('prev-week-range').textContent = formatDateRange(prevWeek.start, prevWeek.end);
  document.getElementById('next-week-range').textContent = formatDateRange(nextWeek.start, nextWeek.end);
  
  // Filter and render today's items (matching ONLY month and day, ANY year)
  const todayPubs = SITE_DATA.publications.filter(item => matchesMonthDay(item.date, today));
  const todayMentions = SITE_DATA.mentions.filter(item => matchesMonthDay(item.date, today));
  
  renderItems(todayPubs, 'today-publications');
  renderItems(todayMentions, 'today-mentions');
  
  // Filter and render this week's items (excluding today)
  const weekPubs = SITE_DATA.publications.filter(item => 
    isInWeek(item.date, currentWeek.start, currentWeek.end) && !matchesMonthDay(item.date, today)
  );
  const weekMentions = SITE_DATA.mentions.filter(item => 
    isInWeek(item.date, currentWeek.start, currentWeek.end) && !matchesMonthDay(item.date, today)
  );
  
  renderItems(weekPubs, 'week-publications');
  renderItems(weekMentions, 'week-mentions');
  
  // Filter and render previous week's items
  const prevWeekPubs = SITE_DATA.publications.filter(item => 
    isInWeek(item.date, prevWeek.start, prevWeek.end)
  );
  const prevWeekMentions = SITE_DATA.mentions.filter(item => 
    isInWeek(item.date, prevWeek.start, prevWeek.end)
  );
  
  renderItems(prevWeekPubs, 'prev-week-publications');
  renderItems(prevWeekMentions, 'prev-week-mentions');
  
  // Filter and render next week's items
  const nextWeekPubs = SITE_DATA.publications.filter(item => 
    isInWeek(item.date, nextWeek.start, nextWeek.end)
  );
  const nextWeekMentions = SITE_DATA.mentions.filter(item => 
    isInWeek(item.date, nextWeek.start, nextWeek.end)
  );
  
  renderItems(nextWeekPubs, 'next-week-publications');
  renderItems(nextWeekMentions, 'next-week-mentions');
}

// Run on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
</script>
