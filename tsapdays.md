---
layout: default
title: "TSAP Days"
permalink: /tsapdays/
categories: [Project pages, TSAP Events and Rituals]
created: 2026-01-21
---
<div id="streak-page-wrapper">
<div id="streak-page">
<section class="lead">
  <p>
    <strong>TSAP Days</strong> celebrates daily article creation on <strong>The Sunil Abraham Project</strong> (TSAP). The name combines "TSAP" with "Days," inspired by collaborative documentation challenges like #100WikiDays, a global initiative where contributors create or improve 100 Wikipedia articles over 100 days, and #100HappyDays, a social media movement encouraging daily gratitude through photo sharing. TSAP Days adapts this spirit of consistent creative output to track new page creation streaks and publishing momentum.
  </p>
  <p>
    <strong><em>Caveat lector</em></strong> 
<ol>
<li>Some days in October and November 2025 show no activity, which does not indicate the absence of work, only that no new pages were created on those dates.</li>
  <li>This visualisation focuses exclusively on new page creation and does not capture other vital contributions such as content expansion, article improvements, maintenance edits, or structural refinements, all of which are equally important to the project's growth and quality.</li>
</ol>
  </p>
</section>

<div class="streak-card">
  <h2>🌸 Current TSAP Days Streak</h2>
  <p id="streak-summary" class="streak-summary"></p>
  
  <div class="garland" id="garland"></div>
  
  <div class="legend">
    <div class="legend-item">
      <div class="legend-flower rose"></div>
      <span>10+ pages</span>
    </div>
    <div class="legend-item">
      <div class="legend-flower sunflower"></div>
      <span>6–9 pages</span>
    </div>
    <div class="legend-item">
      <div class="legend-flower lotus"></div>
      <span>2–5 pages</span>
    </div>
    <div class="legend-item">
      <div class="legend-flower daisy"></div>
      <span>1 page</span>
    </div>
  </div>
</div>

<div class="timeline-card">
  <h2>📅 Publishing Timeline</h2>
  <p class="timeline-note">
    Below you'll find the number of pages created per day since the site began tracking.
    <strong>Click any flower above to jump to its date.</strong> Scroll down to see all entries organised by month.
  </p>
  <div id="log-by-month"></div>
</div>

<style>
/* ========== BASE STYLES ========== */
* {
  box-sizing: border-box;
}

#streak-page-wrapper {
  width: 100%;
  margin: 0;
  padding: 0;
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 30%, #fcd34d 70%, #fbbf24 100%);
  min-height: 100vh;
}

#streak-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: clamp(16px, 4vw, 32px);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.lead {
  background: linear-gradient(135deg, #ffffff 0%, #fffbeb 50%, #fef3c7 100%);
  padding: clamp(20px, 5vw, 32px);
  border-radius: 20px;
  margin-bottom: clamp(20px, 5vw, 32px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12), 0 2px 8px rgba(0,0,0,0.08);
  border: 2px solid rgba(251, 191, 36, 0.3);
}

.lead p {
  margin: 0 0 16px 0;
  line-height: 1.7;
  color: #064e3b;
  font-size: clamp(0.95rem, 2.5vw, 1.05rem);
}

.lead p:last-child {
  margin-bottom: 0;
}

.lead ol {
  margin: 8px 0 0 0;
  padding-left: 24px;
}

.lead li {
  margin-bottom: 8px;
  line-height: 1.6;
}

/* ========== CARDS ========== */
.streak-card, .timeline-card {
  background: linear-gradient(135deg, #ffffff 0%, #fefefe 100%);
  border-radius: 20px;
  padding: clamp(20px, 5vw, 36px);
  margin-bottom: clamp(20px, 5vw, 32px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.15), 0 4px 12px rgba(0,0,0,0.1);
  border: 2px solid rgba(251, 191, 36, 0.2);
  position: relative;
  overflow: hidden;
}

.streak-card::before, .timeline-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #f43f5e, #eab308, #ec4899, #60a5fa);
  background-size: 300% 100%;
  animation: gradient-shift 6s ease infinite;
}

@keyframes gradient-shift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.streak-card h2, .timeline-card h2 {
  margin: 0 0 20px 0;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: #065f46;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.streak-summary {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 50%, #86efac 100%);
  padding: 16px 20px;
  border-radius: 14px;
  margin: 0 0 28px 0;
  font-size: clamp(1rem, 2.8vw, 1.15rem);
  font-weight: 600;
  color: #065f46;
  border-left: 5px solid #10b981;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
  line-height: 1.6;
}

.timeline-note {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 50%, #93c5fd 100%);
  padding: 16px 20px;
  border-radius: 14px;
  margin: 0 0 24px 0;
  font-size: clamp(0.95rem, 2.5vw, 1rem);
  line-height: 1.6;
  color: #075985;
  border-left: 5px solid #0ea5e9;
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.2);
}

/* ========== GARLAND ========== */
.garland {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  gap: clamp(20px, 5vw, 32px);
  padding: clamp(20px, 5vw, 32px) 0;
  min-height: 100px;
}

.flower-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  flex: 0 0 auto;
  max-width: 90px;
}

.flower-container:hover {
  transform: translateY(-12px) scale(1.05);
}

.flower {
  position: relative;
  width: clamp(60px, 15vw, 80px);
  height: clamp(60px, 15vw, 80px);
  cursor: pointer;
  filter: drop-shadow(0 6px 12px rgba(0,0,0,0.2));
  flex-shrink: 0;
  transition: filter 0.4s ease, transform 0.4s ease;
}

.flower:hover {
  filter: drop-shadow(0 8px 20px rgba(0,0,0,0.3));
  transform: rotate(5deg);
}

.flower.animate {
  animation: gentle-sway 5s ease-in-out infinite;
}

/* ========== ROSE (10+ pages) ========== */
.rose .petal {
  position: absolute;
  width: 48%;
  height: 52%;
  background: linear-gradient(135deg, #fb7185 0%, #f43f5e 40%, #e11d48 80%, #be123c 100%);
  border-radius: 50% 50% 45% 55%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 80%;
  box-shadow: inset 0 -3px 6px rgba(0,0,0,0.25), 0 2px 4px rgba(0,0,0,0.15);
}

.rose .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-14px); }
.rose .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(45deg) translateY(-14px); }
.rose .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(90deg) translateY(-14px); }
.rose .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(135deg) translateY(-14px); }
.rose .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(180deg) translateY(-14px); }
.rose .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(225deg) translateY(-14px); }
.rose .petal:nth-child(7) { transform: translate(-50%,-50%) rotate(270deg) translateY(-14px); }
.rose .petal:nth-child(8) { transform: translate(-50%,-50%) rotate(315deg) translateY(-14px); }

/* ========== SUNFLOWER (6-9 pages) ========== */
.sunflower .petal {
  position: absolute;
  width: 32%;
  height: 38%;
  background: linear-gradient(135deg, #fde047 0%, #facc15 40%, #eab308 80%, #ca8a04 100%);
  border-radius: 45% 55% 40% 60%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 90%;
  box-shadow: inset 0 -2px 4px rgba(0,0,0,0.2), 0 1px 3px rgba(0,0,0,0.15);
}

.sunflower .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-12px); }
.sunflower .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(30deg) translateY(-12px); }
.sunflower .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(60deg) translateY(-12px); }
.sunflower .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(90deg) translateY(-12px); }
.sunflower .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(120deg) translateY(-12px); }
.sunflower .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(150deg) translateY(-12px); }
.sunflower .petal:nth-child(7) { transform: translate(-50%,-50%) rotate(180deg) translateY(-12px); }
.sunflower .petal:nth-child(8) { transform: translate(-50%,-50%) rotate(210deg) translateY(-12px); }
.sunflower .petal:nth-child(9) { transform: translate(-50%,-50%) rotate(240deg) translateY(-12px); }
.sunflower .petal:nth-child(10) { transform: translate(-50%,-50%) rotate(270deg) translateY(-12px); }
.sunflower .petal:nth-child(11) { transform: translate(-50%,-50%) rotate(300deg) translateY(-12px); }
.sunflower .petal:nth-child(12) { transform: translate(-50%,-50%) rotate(330deg) translateY(-12px); }

/* ========== LOTUS (2-5 pages) ========== */
.lotus .petal {
  position: absolute;
  width: 40%;
  height: 50%;
  background: linear-gradient(135deg, #f9a8d4 0%, #f472b6 40%, #ec4899 80%, #db2777 100%);
  border-radius: 50% 50% 48% 52%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 85%;
  box-shadow: inset 0 -2px 5px rgba(0,0,0,0.22), 0 2px 4px rgba(0,0,0,0.15);
}

.lotus .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-13px); }
.lotus .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(51deg) translateY(-13px); }
.lotus .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(102deg) translateY(-13px); }
.lotus .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(153deg) translateY(-13px); }
.lotus .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(204deg) translateY(-13px); }
.lotus .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(255deg) translateY(-13px); }
.lotus .petal:nth-child(7) { transform: translate(-50%,-50%) rotate(306deg) translateY(-13px); }

/* ========== DAISY (1 page) ========== */
.daisy .petal {
  position: absolute;
  width: 28%;
  height: 35%;
  background: linear-gradient(135deg, #dbeafe 0%, #93c5fd 40%, #60a5fa 80%, #3b82f6 100%);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 90%;
  border: 1.5px solid #2563eb;
  box-shadow: inset 0 -1px 3px rgba(0,0,0,0.2), 0 1px 2px rgba(0,0,0,0.1);
}

.daisy .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-11px); }
.daisy .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(40deg) translateY(-11px); }
.daisy .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(80deg) translateY(-11px); }
.daisy .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(120deg) translateY(-11px); }
.daisy .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(160deg) translateY(-11px); }
.daisy .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(200deg) translateY(-11px); }
.daisy .petal:nth-child(7) { transform: translate(-50%,-50%) rotate(240deg) translateY(-11px); }
.daisy .petal:nth-child(8) { transform: translate(-50%,-50%) rotate(280deg) translateY(-11px); }
.daisy .petal:nth-child(9) { transform: translate(-50%,-50%) rotate(320deg) translateY(-11px); }

/* ========== FLOWER INFO ========== */
.info {
  margin-top: 10px;
  text-align: center;
  font-size: clamp(0.75rem, 2.2vw, 0.9rem);
  color: #065f46;
  font-weight: 600;
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  padding: 6px 10px;
  border-radius: 8px;
  max-width: 100%;
  overflow-wrap: break-word;
  word-wrap: break-word;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  border: 1px solid #bbf7d0;
  line-height: 1.4;
}

/* ========== LEGEND ========== */
.legend {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(16px, 4vw, 28px);
  margin-top: clamp(20px, 5vw, 32px);
  padding-top: clamp(20px, 5vw, 28px);
  border-top: 3px dashed rgba(16, 185, 129, 0.3);
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: clamp(0.9rem, 2.3vw, 1rem);
  color: #065f46;
  font-weight: 600;
  padding: 8px 14px;
  background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
  border-radius: 12px;
  box-shadow: 0 3px 8px rgba(0,0,0,0.1);
  border: 1.5px solid rgba(16, 185, 129, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.legend-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

.legend-flower {
  width: clamp(32px, 7vw, 40px);
  height: clamp(32px, 7vw, 40px);
  position: relative;
  flex-shrink: 0;
  border-radius: 50%;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}

.legend-flower.rose { 
  background: linear-gradient(135deg, #fb7185 0%, #e11d48 100%); 
}
.legend-flower.sunflower { 
  background: linear-gradient(135deg, #fde047 0%, #eab308 100%); 
}
.legend-flower.lotus { 
  background: linear-gradient(135deg, #f9a8d4 0%, #ec4899 100%); 
}
.legend-flower.daisy { 
  background: linear-gradient(135deg, #bfdbfe 0%, #60a5fa 100%); 
  border: 2px solid #3b82f6; 
}

/* ========== ANIMATIONS ========== */
@keyframes gentle-sway {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  20% { transform: translateY(-4px) rotate(2deg); }
  40% { transform: translateY(-7px) rotate(-2deg); }
  60% { transform: translateY(-5px) rotate(1deg); }
  80% { transform: translateY(-3px) rotate(-1deg); }
}

/* ========== TIMELINE LOG ========== */
#log-by-month {
  max-height: 700px;
  overflow-y: auto;
  padding-right: 10px;
  scroll-behavior: smooth;
}

#log-by-month::-webkit-scrollbar {
  width: 10px;
}

#log-by-month::-webkit-scrollbar-track {
  background: #f0fdf4;
  border-radius: 6px;
}

#log-by-month::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #86efac 0%, #4ade80 100%);
  border-radius: 6px;
}

#log-by-month::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #4ade80 0%, #22c55e 100%);
}

#log-by-month h3 {
  margin: 24px 0 16px 0;
  padding: 12px 16px;
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  border-radius: 12px;
  font-size: clamp(1.1rem, 3.5vw, 1.3rem);
  color: #065f46;
  font-weight: 700;
  position: sticky;
  top: 0;
  z-index: 1;
  box-shadow: 0 4px 10px rgba(16, 185, 129, 0.2);
  border-left: 5px solid #10b981;
}

#log-by-month h3:first-child {
  margin-top: 0;
}

#log-by-month ol {
  margin: 0 0 20px 0;
  padding: 0;
  list-style: none;
  counter-reset: day-counter;
}

#log-by-month li {
  counter-increment: day-counter;
  padding: 10px 14px 10px 48px;
  margin-bottom: 8px;
  background: linear-gradient(135deg, #fafafa 0%, #ffffff 100%);
  border-radius: 10px;
  font-size: clamp(0.9rem, 2.5vw, 1rem);
  color: #064e3b;
  border-left: 4px solid #e5e7eb;
  transition: all 0.3s ease;
  position: relative;
  scroll-margin-top: 70px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

#log-by-month li::before {
  content: counter(day-counter);
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  background: linear-gradient(135deg, #e5e7eb 0%, #d1d5db 100%);
  color: #6b7280;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#log-by-month li:hover {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  border-left-color: #10b981;
  transform: translateX(6px);
  box-shadow: 0 4px 10px rgba(16, 185, 129, 0.15);
}

#log-by-month li.active-day {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  border-left-color: #10b981;
  font-weight: 600;
  box-shadow: 0 3px 8px rgba(16, 185, 129, 0.2);
}

#log-by-month li.active-day::before {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
}

#log-by-month li.highlight {
  animation: highlight-flash 1.2s ease;
}

@keyframes highlight-flash {
  0%, 100% { 
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
    transform: translateX(6px) scale(1);
  }
  50% { 
    background: linear-gradient(135deg, #6ee7b7 0%, #34d399 100%);
    transform: translateX(6px) scale(1.02);
  }
}

.page-links {
  display: inline;
  color: #059669;
  font-size: 0.92em;
  font-weight: 500;
}

.page-links a {
  color: #059669;
  text-decoration: none;
  transition: color 0.3s ease;
  border-bottom: 1px dotted #059669;
}

.page-links a:hover {
  color: #047857;
  text-decoration: none;
  border-bottom: 1px solid #047857;
}

.page-links .more-count {
  font-style: italic;
  color: #6b7280;
  font-weight: 500;
}

/* ========== RESPONSIVE IMPROVEMENTS ========== */
@media (max-width: 768px) {
  .garland {
    gap: 18px;
    padding: 20px 0;
  }
  
  .flower-container {
    max-width: 80px;
  }
  
  .legend {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
  }
  
  .legend-item {
    justify-content: flex-start;
  }
  
  #log-by-month {
    max-height: 600px;
  }
}

@media (max-width: 480px) {
  #streak-page-wrapper {
    padding: 0;
  }
  
  #streak-page {
    padding: clamp(12px, 3vw, 16px);
  }
  
  .garland {
    gap: 16px;
    padding: 16px 0;
  }
  
  .flower {
    width: 60px;
    height: 60px;
  }
  
  .flower-container {
    max-width: 70px;
  }
  
  #log-by-month {
    max-height: 500px;
  }
}

@media (min-width: 1400px) {
  #streak-page {
    max-width: 1400px;
  }
}
</style>

<script>
/* ========== DATA FROM JEKYLL ========== */
const pagesData = [
  {% for page in site.pages %}
    {% unless page.published == false or page.url contains '/sandbox/' %}
      {% if page.created %}
        { 
          created: "{{ page.created }}",
          title: {{ page.title | jsonify }},
          url: "{{ page.url }}"
        },
      {% endif %}
    {% endunless %}
  {% endfor %}
];

/* ========== CONFIGURATION ========== */
const MAX_ARTICLES_DISPLAY = 3;

/* ========== ORGANISE DATA BY DATE ========== */
const pagesByDate = {};
pagesData.forEach(p => {
  if (!pagesByDate[p.created]) {
    pagesByDate[p.created] = [];
  }
  pagesByDate[p.created].push(p);
});

const counts = {};
Object.keys(pagesByDate).forEach(date => {
  counts[date] = pagesByDate[date].length;
});

/* ========== DATE HELPERS ========== */
function nextDate(d) {
  const [y, m, day] = d.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, day + 1));
  return date.toISOString().slice(0, 10);
}

function prevDate(d) {
  const [y, m, day] = d.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, day - 1));
  return date.toISOString().slice(0, 10);
}

function formatLongDate(d) {
  const [y, m, day] = d.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, day));
  
  const weekday = date.toLocaleString('en-IN', { weekday: 'long', timeZone: 'UTC' });
  const monthName = date.toLocaleString('en-IN', { month: 'long', timeZone: 'UTC' });
  
  return `${weekday}, ${day} ${monthName} ${y}`;
}

function monthLabel(d) {
  const [y, m] = d.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, 1));
  return date.toLocaleString('en-IN', { month: 'long', year: 'numeric', timeZone: 'UTC' });
}

/* ========== FORMAT ARTICLE LINKS WITH TRUNCATION ========== */
function formatArticleLinks(articles) {
  const total = articles.length;
  
  if (total <= MAX_ARTICLES_DISPLAY) {
    const links = articles.map(p => `<a href="${p.url}">${p.title}</a>`).join(', ');
    return links;
  } else {
    const visible = articles.slice(0, MAX_ARTICLES_DISPLAY);
    const links = visible.map(p => `<a href="${p.url}">${p.title}</a>`).join(', ');
    const remaining = total - MAX_ARTICLES_DISPLAY;
    return `${links}, <span class="more-count">… +${remaining} more</span>`;
  }
}

const today = new Date().toLocaleString('sv-SE', { 
  timeZone: 'Asia/Kolkata' 
}).slice(0, 10);

/* ========== FLOWER TYPE SELECTOR (UPDATED CATEGORIES) ========== */
function getFlowerType(count) {
  if (count >= 10) return { type: 'rose', petals: 8 };
  if (count >= 6) return { type: 'sunflower', petals: 12 };
  if (count >= 2) return { type: 'lotus', petals: 7 };
  return { type: 'daisy', petals: 9 };
}

/* ========== SCROLL TO DATE FUNCTION ========== */
function scrollToDate(date) {
  const targetLi = document.querySelector(`li[data-date="${date}"]`);
  if (targetLi) {
    targetLi.scrollIntoView({ behavior: 'smooth', block: 'center' });
    targetLi.classList.add('highlight');
    setTimeout(() => targetLi.classList.remove('highlight'), 1200);
  }
}

/* ========== STREAK CALCULATION ========== */
let streakDates = [];
let cursor = today;

while ((counts[cursor] || 0) > 0) {
  streakDates.unshift({ date: cursor, count: counts[cursor] });
  cursor = prevDate(cursor);
}

/* ========== RENDER STREAK SUMMARY ========== */
const summary = document.getElementById('streak-summary');
if (streakDates.length === 0) {
  summary.textContent = '🌱 No active streak. We need to restart article creation to begin the garden!';
  summary.style.background = 'linear-gradient(135deg, #fef3c7, #fde68a)';
  summary.style.borderLeftColor = '#f59e0b';
} else {
  const totalPages = streakDates.reduce((sum, d) => sum + d.count, 0);
  summary.textContent = 
    `🔥 ${streakDates.length} day${streakDates.length === 1 ? '' : 's'} streak • ` +
    `${totalPages} page${totalPages === 1 ? '' : 's'} created • ` +
    `Started ${formatLongDate(streakDates[0].date)}`;
}

/* ========== RENDER FLOWERS (NO LAZY LOAD) ========== */
const garland = document.getElementById('garland');

if (streakDates.length === 0) {
  const emptyMsg = document.createElement('p');
  emptyMsg.textContent = 'The garden awaits... 🌱';
  emptyMsg.style.cssText = 'color: #6b7280; font-style: italic; padding: 24px; font-size: 1.1rem;';
  garland.appendChild(emptyMsg);
} else {
  streakDates.forEach((d, i) => {
    const wrap = document.createElement('div');
    wrap.className = 'flower-container';

    const flowerInfo = getFlowerType(d.count);
    const flower = document.createElement('div');
    flower.className = `flower ${flowerInfo.type} animate`;
    flower.style.animationDelay = `${(i * 0.2) % 5}s`;
    flower.setAttribute('role', 'button');
    flower.setAttribute('aria-label', `${formatLongDate(d.date)}: ${d.count} page${d.count === 1 ? '' : 's'} created. Click to view details.`);
    flower.dataset.date = d.date;
    flower.tabIndex = 0;
    
    flower.addEventListener('click', () => scrollToDate(d.date));
    flower.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        scrollToDate(d.date);
      }
    });

    for (let j = 0; j < flowerInfo.petals; j++) {
      flower.appendChild(document.createElement('div')).className = 'petal';
    }

    const info = document.createElement('div');
    info.className = 'info';
    info.textContent = `${formatLongDate(d.date)}: ${d.count}`;

    wrap.appendChild(flower);
    wrap.appendChild(info);
    garland.appendChild(wrap);
  });
}

/* ========== DAILY LOG ========== */
const log = document.getElementById('log-by-month');
const allDates = Object.keys(counts).sort();
const startDate = allDates.length > 0 ? allDates[0] : today;

let currentMonth = null;
let list;

for (let d = startDate; d <= today; d = nextDate(d)) {
  const m = monthLabel(d);
  if (m !== currentMonth) {
    const h3 = document.createElement('h3');
    h3.textContent = m;
    log.appendChild(h3);
    list = document.createElement('ol');
    log.appendChild(list);
    currentMonth = m;
  }
  
  const c = counts[d] || 0;
  const li = document.createElement('li');
  li.dataset.date = d;
  
  let dateText = `${formatLongDate(d)}: ${c} ${c === 1 ? 'page' : 'pages'}`;
  
  if (c > 0 && pagesByDate[d]) {
    const links = formatArticleLinks(pagesByDate[d]);
    li.innerHTML = `${dateText} <span class="page-links">[${links}]</span>`;
  } else {
    li.textContent = dateText;
  }
  
  if (c > 0) {
    li.classList.add('active-day');
  }
  
  list.appendChild(li);
}
</script>
</div>
