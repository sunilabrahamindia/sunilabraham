---
layout: default
title: "On This Day"
description: "Discover Sunil Abraham's publications, media articles, and media mentions from history organised by date—explore what happened today, this week, and beyond."
categories: [Project pages]
permalink: /otd/
created: 2026-01-26
---

The Sunil Abraham Project archives a substantial body of work spanning publications, media articles, and media mentions. This chronological view surfaces historical content by date, allowing you to discover contributions that might otherwise remain buried in the archives. Whether you're researching Sunil's evolving perspectives on a topic or tracking media coverage over time, this timeline offers a unique lens into his intellectual journey and public influence.

**Please note:** Whilst publications and media content are integrated here, **events (conducted and participated) await sufficient standalone coverage and necessary metadata**. Those will be added gradually as documentation standards are met.

<style>
.otd-container {
  max-width: 100%;
  margin: 0 auto;
}

.otd-nav-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 2rem 0;
  padding: 0;
  list-style: none;
  border-bottom: 3px solid #dee2e6;
  position: relative;
  justify-content: center;
}

.otd-nav-tab {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 8px 8px 0 0;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  color: white;
  font-weight: 600;
  position: relative;
  overflow: hidden;
  transform: translateY(0);
}

.otd-nav-tab::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  transition: left 0.3s ease;
  z-index: -1;
}

.otd-nav-tab:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.otd-nav-tab:hover::before {
  left: 0;
}

.otd-nav-tab:active {
  transform: translateY(-1px);
}

.otd-nav-tab.active {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  box-shadow: 0 6px 16px rgba(240, 147, 251, 0.5);
  transform: translateY(-2px);
}

.otd-custom-range-panel {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  display: none;
}

.otd-custom-range-panel.active {
  display: block;
  animation: slideDown 0.3s ease;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.otd-date-selectors {
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  gap: 1rem;
  align-items: end;
  margin-bottom: 1rem;
}

.otd-date-group {
  display: flex;
  flex-direction: column;
}

.otd-date-group label {
  font-weight: 600;
  color: #495057;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.otd-date-input {
  display: flex;
  gap: 0.5rem;
}

.otd-date-input select {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 0.95rem;
  background: white;
  cursor: pointer;
  transition: border-color 0.2s;
}

.otd-date-input select:hover {
  border-color: #667eea;
}

.otd-date-input select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.otd-show-btn {
  padding: 0.5rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.otd-show-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.otd-show-btn:active {
  transform: translateY(0);
}

.otd-section {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-left: 4px solid #667eea;
  border-radius: 4px;
  animation: fadeIn 0.4s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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
  position: relative;
}

.otd-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.otd-item-badge {
  display: inline-block;
  background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 3px;
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
  font-weight: 600;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.85rem;
  margin-left: 1rem;
  font-weight: normal;
}

.otd-today-intro {
  color: #495057;
  margin: 1rem 0;
  font-size: 1rem;
  line-height: 1.6;
}

.otd-placeholder {
  padding: 3rem;
  text-align: center;
  color: #6c757d;
  font-style: italic;
  background: #f8f9fa;
  border-radius: 8px;
  border: 2px dashed #dee2e6;
}

/* Mobile optimisation */
@media (max-width: 768px) {
  .otd-nav-tabs {
    gap: 0.25rem;
  }
  
  .otd-nav-tab {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
    flex: 1 1 calc(50% - 0.25rem);
    text-align: center;
  }
  
  .otd-date-selectors {
    grid-template-columns: 1fr;
  }
  
  .otd-show-btn {
    width: 100%;
  }
  
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
  .otd-nav-tab {
    padding: 0.5rem 0.75rem;
    font-size: 0.85rem;
  }
  
  .otd-custom-range-panel {
    padding: 1rem;
  }
  
  .otd-date-input {
    flex-direction: column;
  }
  
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
  
  .otd-item-badge {
    font-size: 0.75rem;
  }
}
</style>

<nav class="otd-nav-tabs">
  <a href="#today" class="otd-nav-tab" data-tab="today">Today</a>
  <a href="#this-week" class="otd-nav-tab" data-tab="this-week">This Week</a>
  <a href="#previous-week" class="otd-nav-tab" data-tab="previous-week">Previous Week</a>
  <a href="#next-week" class="otd-nav-tab" data-tab="next-week">Next Week</a>
  <a href="#custom-range" class="otd-nav-tab" data-tab="custom-range">Custom Range</a>
</nav>

<div id="custom-range" class="otd-custom-range-panel">
  <div class="otd-date-selectors">
    <div class="otd-date-group">
      <label>From Date</label>
      <div class="otd-date-input">
        <select id="from-day">
          <option value="">Day</option>
        </select>
        <select id="from-month">
          <option value="">Month</option>
        </select>
      </div>
    </div>
    
    <div class="otd-date-group">
      <label>To Date</label>
      <div class="otd-date-input">
        <select id="to-day">
          <option value="">Day</option>
        </select>
        <select id="to-month">
          <option value="">Month</option>
        </select>
      </div>
    </div>
    
    <button class="otd-show-btn" onclick="showCustomRange()">Show Results</button>
  </div>
  
  <div id="custom-results" style="display: none;">
    <h2 class="otd-date-header">
      Custom Range <span class="otd-week-label" id="custom-range-label"></span>
    </h2>
    
    <div class="otd-section">
      <h3>📝 Publications & Media Articles</h3>
      <p class="otd-intro" id="custom-publications-intro">Sunil Abraham published the following articles during this period across different years.</p>
      <ul class="otd-list" id="custom-publications"></ul>
    </div>
    
    <div class="otd-section">
      <h3>📰 Media Mentions</h3>
      <p class="otd-intro" id="custom-mentions-intro">Sunil Abraham was mentioned or quoted in the following articles during this period across different years.</p>
      <ul class="otd-list" id="custom-mentions"></ul>
    </div>
  </div>
  
  <div class="otd-placeholder" id="custom-placeholder">
    Please select a date range and click "Show Results" to view historical content.
  </div>
</div>

<div class="otd-container">
  <h2 class="otd-date-header" id="today">Today</h2>
  <p class="otd-today-intro" id="today-intro"></p>
  
  <div class="otd-section" id="today-publications-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro" id="today-publications-intro">Sunil Abraham published the following articles on this day in history.</p>
    <ul class="otd-list" id="today-publications"></ul>
  </div>
  
  <div class="otd-section" id="today-mentions-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro" id="today-mentions-intro">Sunil Abraham was mentioned or quoted in the following articles on this day in history.</p>
    <ul class="otd-list" id="today-mentions"></ul>
  </div>

  <h2 class="otd-date-header" id="this-week">
    This Week <span class="otd-week-label" id="current-week-range"></span>
  </h2>
  
  <div class="otd-section" id="week-publications-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro" id="week-publications-intro">Sunil Abraham published the following articles during this week across different years.</p>
    <ul class="otd-list" id="week-publications"></ul>
  </div>
  
  <div class="otd-section" id="week-mentions-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro" id="week-mentions-intro">Sunil Abraham was mentioned or quoted in the following articles during this week across different years.</p>
    <ul class="otd-list" id="week-mentions"></ul>
  </div>

  <h2 class="otd-date-header" id="previous-week">
    Previous Week <span class="otd-week-label" id="prev-week-range"></span>
  </h2>
  
  <div class="otd-section" id="prev-week-publications-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro" id="prev-week-publications-intro">Sunil Abraham published the following articles during the previous week across different years.</p>
    <ul class="otd-list" id="prev-week-publications"></ul>
  </div>
  
  <div class="otd-section" id="prev-week-mentions-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro" id="prev-week-mentions-intro">Sunil Abraham was mentioned or quoted in the following articles during the previous week across different years.</p>
    <ul class="otd-list" id="prev-week-mentions"></ul>
  </div>

  <h2 class="otd-date-header" id="next-week">
    Next Week <span class="otd-week-label" id="next-week-range"></span>
  </h2>
  
  <div class="otd-section" id="next-week-publications-section">
    <h3>📝 Publications & Media Articles</h3>
    <p class="otd-intro" id="next-week-publications-intro">Sunil Abraham published the following articles during the next week across different years.</p>
    <ul class="otd-list" id="next-week-publications"></ul>
  </div>
  
  <div class="otd-section" id="next-week-mentions-section">
    <h3>📰 Media Mentions</h3>
    <p class="otd-intro" id="next-week-mentions-intro">Sunil Abraham was mentioned or quoted in the following articles during the next week across different years.</p>
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

// Populate date dropdowns
function populateDateDropdowns() {
  const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December'];
  
  const fromMonth = document.getElementById('from-month');
  const toMonth = document.getElementById('to-month');
  
  months.forEach((month, index) => {
    fromMonth.innerHTML += `<option value="${index}">${month}</option>`;
    toMonth.innerHTML += `<option value="${index}">${month}</option>`;
  });
  
  const fromDay = document.getElementById('from-day');
  const toDay = document.getElementById('to-day');
  
  for (let i = 1; i <= 31; i++) {
    fromDay.innerHTML += `<option value="${i}">${i}</option>`;
    toDay.innerHTML += `<option value="${i}">${i}</option>`;
  }
}

// Tab functionality
document.querySelectorAll('.otd-nav-tab').forEach(tab => {
  tab.addEventListener('click', function(e) {
    e.preventDefault();
    
    // Remove active class from all tabs
    document.querySelectorAll('.otd-nav-tab').forEach(t => t.classList.remove('active'));
    
    // Add active class to clicked tab
    this.classList.add('active');
    
    // Handle custom range panel
    const customPanel = document.querySelector('.otd-custom-range-panel');
    if (this.dataset.tab === 'custom-range') {
      customPanel.classList.add('active');
      customPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      customPanel.classList.remove('active');
      
      // Scroll to section
      const targetId = this.getAttribute('href');
      const targetSection = document.querySelector(targetId);
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });
});

// Custom range functionality
function showCustomRange() {
  const fromDay = parseInt(document.getElementById('from-day').value);
  const fromMonth = parseInt(document.getElementById('from-month').value);
  const toDay = parseInt(document.getElementById('to-day').value);
  const toMonth = parseInt(document.getElementById('to-month').value);
  
  if (isNaN(fromDay) || isNaN(fromMonth) || isNaN(toDay) || isNaN(toMonth)) {
    alert('Please select both From and To dates');
    return;
  }
  
  const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December'];
  
  const rangeLabel = `${fromDay} ${months[fromMonth]} – ${toDay} ${months[toMonth]}`;
  document.getElementById('custom-range-label').textContent = rangeLabel;
  
  const today = new Date();
  
  // Filter items in custom range
  const customPubs = SITE_DATA.publications.filter(item => 
    isInCustomRange(item.date, fromMonth, fromDay, toMonth, toDay)
  );
  const customMentions = SITE_DATA.mentions.filter(item => 
    isInCustomRange(item.date, fromMonth, fromDay, toMonth, toDay)
  );
  
  renderItems(customPubs, 'custom-publications', 'custom-publications-intro', today);
  renderItems(customMentions, 'custom-mentions', 'custom-mentions-intro', today);
  
  // Show results, hide placeholder
  document.getElementById('custom-placeholder').style.display = 'none';
  document.getElementById('custom-results').style.display = 'block';
  
  // Scroll to results
  document.getElementById('custom-results').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function isInCustomRange(itemDate, fromMonth, fromDay, toMonth, toDay) {
  const item = parseDate(itemDate);
  const itemMonth = item.getMonth();
  const itemDay = item.getDate();
  
  const fromValue = fromMonth * 100 + fromDay;
  const toValue = toMonth * 100 + toDay;
  const itemValue = itemMonth * 100 + itemDay;
  
  // Handle range spanning year boundary
  if (fromValue > toValue) {
    return itemValue >= fromValue || itemValue <= toValue;
  } else {
    return itemValue >= fromValue && itemValue <= toValue;
  }
}

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

function getYearsDifference(itemDate, referenceDate) {
  const item = parseDate(itemDate);
  const years = referenceDate.getFullYear() - item.getFullYear();
  return years;
}

function getTimeDifferenceText(itemDate, referenceDate) {
  const years = getYearsDifference(itemDate, referenceDate);
  
  if (years === 0) {
    return "This year";
  } else if (years === 1) {
    return "1 year ago";
  } else {
    return `${years} years ago`;
  }
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
  
  // Handle year wrap-around
  if (weekStart.getMonth() > weekEnd.getMonth()) {
    return itemMD >= startMD || itemMD <= endMD;
  } else {
    return itemMD >= startMD && itemMD <= endMD;
  }
}

function renderItems(items, containerId, introId, referenceDate) {
  const container = document.getElementById(containerId);
  const intro = document.getElementById(introId);
  
  if (items.length === 0) {
    container.innerHTML = '<li class="otd-empty">No items found for this period</li>';
    if (intro) intro.style.display = 'none';
    return;
  }
  
  if (intro) intro.style.display = 'block';
  
  // Sort by oldest year first
  items.sort((a, b) => parseDate(a.date) - parseDate(b.date));
  
  const html = items.map(item => {
    const itemDate = parseDate(item.date);
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    const formattedDate = `${itemDate.getDate()} ${months[itemDate.getMonth()]} ${itemDate.getFullYear()}`;
    const timeDiff = getTimeDifferenceText(item.date, referenceDate);
    
    return `
      <li class="otd-item">
        <div class="otd-item-badge">${timeDiff}</div>
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
  
  // Populate date dropdowns
  populateDateDropdowns();
  
  // Set today's intro text
  const todayIntro = document.getElementById('today-intro');
  todayIntro.textContent = `Today is ${formatDateDMY(today)}. In the past, Sunil Abraham has published content and been featured in media on this day.`;
  
  // Get week bounds
  const currentWeek = getWeekBounds(today, 0);
  const prevWeek = getWeekBounds(today, -1);
  const nextWeek = getWeekBounds(today, 1);
  
  // Set week range labels
  document.getElementById('current-week-range').textContent = formatDateRange(currentWeek.start, currentWeek.end);
  document.getElementById('prev-week-range').textContent = formatDateRange(prevWeek.start, prevWeek.end);
  document.getElementById('next-week-range').textContent = formatDateRange(nextWeek.start, nextWeek.end);
  
  // Filter and render today's items
  const todayPubs = SITE_DATA.publications.filter(item => matchesMonthDay(item.date, today));
  const todayMentions = SITE_DATA.mentions.filter(item => matchesMonthDay(item.date, today));
  
  renderItems(todayPubs, 'today-publications', 'today-publications-intro', today);
  renderItems(todayMentions, 'today-mentions', 'today-mentions-intro', today);
  
  // Filter and render this week's items (excluding today)
  const weekPubs = SITE_DATA.publications.filter(item => 
    isInWeek(item.date, currentWeek.start, currentWeek.end) && !matchesMonthDay(item.date, today)
  );
  const weekMentions = SITE_DATA.mentions.filter(item => 
    isInWeek(item.date, currentWeek.start, currentWeek.end) && !matchesMonthDay(item.date, today)
  );
  
  renderItems(weekPubs, 'week-publications', 'week-publications-intro', today);
  renderItems(weekMentions, 'week-mentions', 'week-mentions-intro', today);
  
  // Filter and render previous week's items
  const prevWeekPubs = SITE_DATA.publications.filter(item => 
    isInWeek(item.date, prevWeek.start, prevWeek.end)
  );
  const prevWeekMentions = SITE_DATA.mentions.filter(item => 
    isInWeek(item.date, prevWeek.start, prevWeek.end)
  );
  
  renderItems(prevWeekPubs, 'prev-week-publications', 'prev-week-publications-intro', today);
  renderItems(prevWeekMentions, 'prev-week-mentions', 'prev-week-mentions-intro', today);
  
  // Filter and render next week's items
  const nextWeekPubs = SITE_DATA.publications.filter(item => 
    isInWeek(item.date, nextWeek.start, nextWeek.end)
  );
  const nextWeekMentions = SITE_DATA.mentions.filter(item => 
    isInWeek(item.date, nextWeek.start, nextWeek.end)
  );
  
  renderItems(nextWeekPubs, 'next-week-publications', 'next-week-publications-intro', today);
  renderItems(nextWeekMentions, 'next-week-mentions', 'next-week-mentions-intro', today);
}

// Run on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
</script>
