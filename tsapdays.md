---
layout: default
title: "TSAPDays"
permalink: /tsapdays/
categories: [Project pages]
created: 2026-01-21
---
<div id="streak-page">
<section class="lead">
  <p>
    <strong>TSAPDays</strong> celebrates daily article creation on <strong>The Sunil Abraham Project</strong> (TSAP). The name combines "TSAP" with "Days," inspired by collaborative documentation challenges like #100WikiDays—a global initiative where contributors create or improve 100 Wikipedia articles over 100 days—and #100HappyDays, a social media movement encouraging daily gratitude through photo sharing. TSAPDays adapts this spirit of consistent creative output to track new page creation streaks and publishing momentum.
  </p>
  <p>
    <strong>Caveat lector:</strong> Some days in October and November 2025 show no activity, which does not indicate the absence of work—only that no new pages were created on those dates. This visualization focuses exclusively on new page creation and does not capture other vital contributions such as content expansion, article improvements, maintenance edits, or structural refinements, all of which are equally important to the project's growth and quality.
  </p>
</section>

<div class="streak-card">
  <h2>Current Creation Streak</h2>
  <p id="streak-summary" class="streak-summary"></p>
  
  <div class="garland" id="garland"></div>
  
  <div class="legend">
    <div class="legend-item">
      <div class="legend-flower rose"></div>
      <span>5+ pages</span>
    </div>
    <div class="legend-item">
      <div class="legend-flower sunflower"></div>
      <span>3-4 pages</span>
    </div>
    <div class="legend-item">
      <div class="legend-flower lotus"></div>
      <span>2 pages</span>
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
    <strong>Scroll down to see all entries</strong> organized by month.
  </p>
  <div id="log-by-month"></div>
</div>

<style>
/* ========== BASE STYLES ========== */
* {
  box-sizing: border-box;
}

#streak-page {
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 50%, #fcd34d 100%);
  padding: clamp(12px, 3vw, 24px);
  border-radius: 16px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.lead {
  background: linear-gradient(135deg, #ffffff 0%, #fef3c7 100%);
  padding: clamp(16px, 4vw, 24px);
  border-radius: 16px;
  margin-bottom: clamp(16px, 4vw, 24px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.lead h1 {
  margin: 0 0 12px 0;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: #065f46;
  font-weight: 700;
}

.lead p {
  margin: 0 0 12px 0;
  line-height: 1.6;
  color: #064e3b;
  font-size: clamp(0.9rem, 2.5vw, 1rem);
}

.lead p:last-child {
  margin-bottom: 0;
}

/* ========== CARDS ========== */
.streak-card, .timeline-card {
  background: white;
  border-radius: 16px;
  padding: clamp(16px, 4vw, 28px);
  margin-bottom: clamp(16px, 4vw, 24px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
  overflow: hidden;
}

.streak-card h2, .timeline-card h2 {
  margin: 0 0 16px 0;
  font-size: clamp(1.3rem, 4vw, 1.75rem);
  color: #065f46;
  font-weight: 600;
}

.streak-summary {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  padding: 12px 16px;
  border-radius: 12px;
  margin: 0 0 20px 0;
  font-size: clamp(0.95rem, 2.5vw, 1.1rem);
  font-weight: 500;
  color: #065f46;
  border-left: 4px solid #10b981;
}

.timeline-note {
  background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
  padding: 12px 16px;
  border-radius: 10px;
  margin: 0 0 16px 0;
  font-size: clamp(0.9rem, 2.5vw, 0.95rem);
  line-height: 1.5;
  color: #075985;
  border-left: 4px solid #0ea5e9;
}

/* ========== GARLAND ========== */
.garland {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(16px, 4vw, 24px);
  padding: clamp(16px, 4vw, 24px) 0;
  min-height: 80px;
  overflow: hidden;
}

.flower-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.3s ease;
}

.flower-container:hover {
  transform: translateY(-8px);
}

.flower {
  position: relative;
  width: clamp(50px, 12vw, 70px);
  height: clamp(50px, 12vw, 70px);
  cursor: pointer;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15));
  flex-shrink: 0;
}

.flower.animate {
  animation: gentle-sway 4s ease-in-out infinite;
}

/* ========== ROSE (5+ pages) ========== */
.rose .petal {
  position: absolute;
  width: 45%;
  height: 50%;
  background: linear-gradient(135deg, #fb7185 0%, #f43f5e 50%, #e11d48 100%);
  border-radius: 50% 50% 45% 55%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 80%;
  box-shadow: inset 0 -2px 4px rgba(0,0,0,0.2);
}

.rose .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-12px); }
.rose .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(60deg) translateY(-12px); }
.rose .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(120deg) translateY(-12px); }
.rose .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(180deg) translateY(-12px); }
.rose .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(240deg) translateY(-12px); }
.rose .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(300deg) translateY(-12px); }

.rose .center {
  position: absolute;
  width: 12px;
  height: 12px;
  background: radial-gradient(circle, #fef08a, #fde047);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  box-shadow: 0 0 4px rgba(253,224,71,0.6);
  z-index: 1;
}

/* ========== SUNFLOWER (3-4 pages) ========== */
.sunflower .petal {
  position: absolute;
  width: 30%;
  height: 35%;
  background: linear-gradient(135deg, #fde047 0%, #facc15 50%, #eab308 100%);
  border-radius: 45% 55% 40% 60%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 90%;
}

.sunflower .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-10px); }
.sunflower .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(45deg) translateY(-10px); }
.sunflower .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(90deg) translateY(-10px); }
.sunflower .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(135deg) translateY(-10px); }
.sunflower .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(180deg) translateY(-10px); }
.sunflower .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(225deg) translateY(-10px); }
.sunflower .petal:nth-child(7) { transform: translate(-50%,-50%) rotate(270deg) translateY(-10px); }
.sunflower .petal:nth-child(8) { transform: translate(-50%,-50%) rotate(315deg) translateY(-10px); }

.sunflower .center {
  position: absolute;
  width: 16px;
  height: 16px;
  background: radial-gradient(circle, #78350f, #92400e);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  z-index: 1;
}

/* ========== LOTUS (2 pages) ========== */
.lotus .petal {
  position: absolute;
  width: 38%;
  height: 48%;
  background: linear-gradient(135deg, #f9a8d4 0%, #f472b6 50%, #ec4899 100%);
  border-radius: 50% 50% 48% 52%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 85%;
}

.lotus .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-11px); }
.lotus .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(72deg) translateY(-11px); }
.lotus .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(144deg) translateY(-11px); }
.lotus .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(216deg) translateY(-11px); }
.lotus .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(288deg) translateY(-11px); }

.lotus .center {
  position: absolute;
  width: 11px;
  height: 11px;
  background: radial-gradient(circle, #fde68a, #fbbf24);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  z-index: 1;
}

/* ========== DAISY (1 page) ========== */
.daisy .petal {
  position: absolute;
  width: 25%;
  height: 32%;
  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform-origin: 50% 90%;
  border: 1px solid #e5e7eb;
}

.daisy .petal:nth-child(1) { transform: translate(-50%,-50%) rotate(0deg) translateY(-9px); }
.daisy .petal:nth-child(2) { transform: translate(-50%,-50%) rotate(45deg) translateY(-9px); }
.daisy .petal:nth-child(3) { transform: translate(-50%,-50%) rotate(90deg) translateY(-9px); }
.daisy .petal:nth-child(4) { transform: translate(-50%,-50%) rotate(135deg) translateY(-9px); }
.daisy .petal:nth-child(5) { transform: translate(-50%,-50%) rotate(180deg) translateY(-9px); }
.daisy .petal:nth-child(6) { transform: translate(-50%,-50%) rotate(225deg) translateY(-9px); }
.daisy .petal:nth-child(7) { transform: translate(-50%,-50%) rotate(270deg) translateY(-9px); }
.daisy .petal:nth-child(8) { transform: translate(-50%,-50%) rotate(315deg) translateY(-9px); }

.daisy .center {
  position: absolute;
  width: 14px;
  height: 14px;
  background: radial-gradient(circle, #fde047, #facc15);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  z-index: 1;
}

/* ========== FLOWER INFO ========== */
.info {
  margin-top: 8px;
  text-align: center;
  font-size: clamp(0.7rem, 2vw, 0.85rem);
  color: #065f46;
  font-weight: 500;
  background: #f0fdf4;
  padding: 4px 8px;
  border-radius: 6px;
  white-space: nowrap;
}

/* ========== LEGEND ========== */
.legend {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(12px, 3vw, 20px);
  margin-top: clamp(16px, 4vw, 24px);
  padding-top: clamp(16px, 4vw, 20px);
  border-top: 2px dashed #d1fae5;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: clamp(0.8rem, 2vw, 0.9rem);
  color: #065f46;
}

.legend-flower {
  width: clamp(24px, 6vw, 32px);
  height: clamp(24px, 6vw, 32px);
  position: relative;
  flex-shrink: 0;
}

.legend-flower.rose { background: linear-gradient(135deg, #fb7185, #e11d48); border-radius: 50%; }
.legend-flower.sunflower { background: linear-gradient(135deg, #fde047, #eab308); border-radius: 50%; }
.legend-flower.lotus { background: linear-gradient(135deg, #f9a8d4, #ec4899); border-radius: 50%; }
.legend-flower.daisy { background: linear-gradient(135deg, #ffffff, #f3f4f6); border-radius: 50%; border: 2px solid #e5e7eb; }

/* ========== ANIMATIONS ========== */
@keyframes gentle-sway {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  25% { transform: translateY(-3px) rotate(1deg); }
  50% { transform: translateY(-6px) rotate(-1deg); }
  75% { transform: translateY(-3px) rotate(1deg); }
}

/* ========== TIMELINE LOG ========== */
#log-by-month {
  max-height: 700px;
  overflow-y: auto;
  padding-right: 8px;
}

#log-by-month::-webkit-scrollbar {
  width: 8px;
}

#log-by-month::-webkit-scrollbar-track {
  background: #f0fdf4;
  border-radius: 4px;
}

#log-by-month::-webkit-scrollbar-thumb {
  background: #86efac;
  border-radius: 4px;
}

#log-by-month::-webkit-scrollbar-thumb:hover {
  background: #4ade80;
}

#log-by-month h3 {
  margin: 20px 0 12px 0;
  padding: 8px 12px;
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  border-radius: 8px;
  font-size: clamp(1rem, 3vw, 1.2rem);
  color: #065f46;
  font-weight: 600;
  position: sticky;
  top: 0;
  z-index: 1;
}

#log-by-month h3:first-child {
  margin-top: 0;
}

#log-by-month ol {
  margin: 0 0 16px 20px;
  padding: 0;
  list-style: none;
  counter-reset: day-counter;
}

#log-by-month li {
  counter-increment: day-counter;
  padding: 8px 12px;
  margin-bottom: 6px;
  background: #f9fafb;
  border-radius: 8px;
  font-size: clamp(0.85rem, 2.5vw, 0.95rem);
  color: #064e3b;
  border-left: 3px solid #e5e7eb;
  transition: all 0.2s ease;
  position: relative;
  padding-left: 40px;
}

#log-by-month li::before {
  content: counter(day-counter);
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: #e5e7eb;
  color: #6b7280;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 600;
}

#log-by-month li:hover {
  background: #f0fdf4;
  border-left-color: #10b981;
  transform: translateX(4px);
}

#log-by-month li.active-day {
  background: #d1fae5;
  border-left-color: #10b981;
  font-weight: 500;
}

#log-by-month li.active-day::before {
  background: #10b981;
  color: white;
}

/* ========== RESPONSIVE ========== */
@media (max-width: 640px) {
  .garland {
    gap: 12px;
  }
  
  .legend {
    flex-direction: column;
    align-items: flex-start;
  }
  
  #log-by-month {
    max-height: 500px;
  }
}

@media (max-width: 480px) {
  .flower {
    width: 50px;
    height: 50px;
  }
}
</style>

<script>
/* ========== DATA FROM JEKYLL ========== */
const pages = [
  {% for page in site.pages %}
    {% unless page.published == false or page.url contains '/sandbox/' %}
      {% if page.created %}
        { created: "{{ page.created }}" },
      {% endif %}
    {% endunless %}
  {% endfor %}
];

/* ========== COUNT PER DAY ========== */
const counts = {};
pages.forEach(p => {
  if (p.created) {
    counts[p.created] = (counts[p.created] || 0) + 1;
  }
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
  const monthName = date.toLocaleString("en-IN", { month: "long", timeZone: "UTC" });
  return `${day} ${monthName} ${y}`;
}

function monthLabel(d) {
  const [y, m] = d.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, 1));
  return date.toLocaleString("en-IN", { month: "long", year: "numeric", timeZone: "UTC" });
}

const today = new Date().toISOString().slice(0, 10);

/* ========== FLOWER TYPE SELECTOR ========== */
function getFlowerType(count) {
  if (count >= 5) return { type: 'rose', petals: 6 };
  if (count >= 3) return { type: 'sunflower', petals: 8 };
  if (count === 2) return { type: 'lotus', petals: 5 };
  return { type: 'daisy', petals: 8 };
}

/* ========== STREAK CALCULATION ========== */
let streakDates = [];
let cursor = today;

while ((counts[cursor] || 0) > 0) {
  streakDates.unshift({ date: cursor, count: counts[cursor] });
  cursor = prevDate(cursor);
}

/* ========== RENDER STREAK SUMMARY ========== */
const summary = document.getElementById("streak-summary");
if (streakDates.length === 0) {
  summary.textContent = "🌱 No active streak. Start creating today to begin your garden!";
  summary.style.background = "linear-gradient(135deg, #fef3c7, #fde68a)";
  summary.style.borderLeftColor = "#f59e0b";
} else {
  const totalPages = streakDates.reduce((sum, d) => sum + d.count, 0);
  summary.textContent = 
    `🔥 ${streakDates.length} day${streakDates.length === 1 ? "" : "s"} streak • ` +
    `${totalPages} page${totalPages === 1 ? "" : "s"} created • ` +
    `Started ${formatLongDate(streakDates[0].date)}`;
}

/* ========== RENDER FLOWERS ========== */
const garland = document.getElementById("garland");

if (streakDates.length === 0) {
  const emptyMsg = document.createElement("p");
  emptyMsg.textContent = "Your garden awaits... 🌱";
  emptyMsg.style.cssText = "color: #6b7280; font-style: italic; padding: 20px;";
  garland.appendChild(emptyMsg);
} else {
  streakDates.forEach((d, i) => {
    const wrap = document.createElement("div");
    wrap.className = "flower-container";

    const flowerInfo = getFlowerType(d.count);
    const flower = document.createElement("div");
    flower.className = `flower ${flowerInfo.type} animate`;
    flower.style.animationDelay = `${(i * 0.15) % 4}s`;
    flower.setAttribute('role', 'img');
    flower.setAttribute('aria-label', `${formatLongDate(d.date)}: ${d.count} page${d.count === 1 ? '' : 's'} created`);

    for (let j = 0; j < flowerInfo.petals; j++) {
      flower.appendChild(document.createElement("div")).className = "petal";
    }
    flower.appendChild(document.createElement("div")).className = "center";

    const info = document.createElement("div");
    info.className = "info";
    info.textContent = `${formatLongDate(d.date)}: ${d.count}`;

    wrap.appendChild(flower);
    wrap.appendChild(info);
    garland.appendChild(wrap);
  });
}

/* ========== DAILY LOG ========== */
const log = document.getElementById("log-by-month");
const allDates = Object.keys(counts).sort();
const startDate = allDates.length > 0 ? allDates[0] : today;

let currentMonth = null;
let list;

for (let d = startDate; d <= today; d = nextDate(d)) {
  const m = monthLabel(d);
  if (m !== currentMonth) {
    const h3 = document.createElement("h3");
    h3.textContent = m;
    log.appendChild(h3);
    list = document.createElement("ol");
    log.appendChild(list);
    currentMonth = m;
  }
  
  const c = counts[d] || 0;
  const li = document.createElement("li");
  li.textContent = `${formatLongDate(d)}: ${c} ${c === 1 ? "page" : "pages"}`;
  
  if (c > 0) {
    li.classList.add('active-day');
  }
  
  list.appendChild(li);
}
</script>
</div>
