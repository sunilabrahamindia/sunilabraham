---
layout: default
title: "Time & Date Converter"
description: "Convert a meeting or event time between timezones, including your own, with a shareable link."
permalink: /tools/timeanddate/
categories: [Tools]
page_id: TSAP-1221
created: 2026-08-19
---

<div id="tsaptz-intro">

Convert a call or meeting time into any timezone. Enter a date and time and pick the timezone it belongs to; the tool shows the same instant in your own timezone (detected automatically from your browser) and in about twenty-five major cities worldwide.

Daylight-saving changes are handled automatically using your browser's built-in timezone rules, so results stay correct even when the date falls on a different side of a DST change. You can also generate a shareable link that carries the date, time, timezone and an optional event name/location, so anyone who opens it immediately sees the time converted into their own timezone.

</div>

<section class="tsaptz" id="tsaptz-root" aria-label="Timezone converter">

  <div class="tsaptz-result-view" id="tsaptz-result-view" hidden>

    <div class="tsaptz-event" id="tsaptz-event" hidden>
      <p class="tsaptz-event-what" id="tsaptz-event-what"></p>
      <p class="tsaptz-event-when" id="tsaptz-event-when"></p>
      <p class="tsaptz-event-where" id="tsaptz-event-where"></p>
    </div>

    <h2 class="tsaptz-results-heading" id="tsaptz-results-heading" tabindex="-1">Converted times</h2>

    <div class="tsaptz-results" id="tsaptz-results" aria-live="polite">
      <p class="tsaptz-results-empty" id="tsaptz-results-empty" hidden>Choose a date, time and timezone above, then select Convert to see results here.</p>
      <ul class="tsaptz-list" id="tsaptz-list" hidden></ul>
    </div>

    <div class="tsaptz-result-actions" id="tsaptz-result-actions">
      <button type="button" class="tsaptz-btn tsaptz-btn-primary" id="tsaptz-new-conversion">
        Start a New Conversion
      </button>
    </div>

  </div>

  <div class="tsaptz-form-wrap" id="tsaptz-form-wrap">

    <form class="tsaptz-form" id="tsaptz-form">

      <fieldset class="tsaptz-fieldset">
        <legend class="tsaptz-legend" tabindex="-1">Event details (optional)</legend>

        <div class="tsaptz-field">
          <label for="tsaptz-what">What or topic</label>
          <input type="text" id="tsaptz-what" name="what" maxlength="120"
                 placeholder="e.g. ResolveQ Meeting" autocomplete="off">
        </div>

        <div class="tsaptz-field">
          <label for="tsaptz-where">Where</label>
          <input type="text" id="tsaptz-where" name="where" maxlength="200"
                 placeholder="e.g. https://meet.google.com/abc-defg-hij" autocomplete="off">
        </div>
      </fieldset>

      <fieldset class="tsaptz-fieldset">
        <legend class="tsaptz-legend">Date</legend>
        <div class="tsaptz-row tsaptz-row-date">
          <div class="tsaptz-field tsaptz-field-narrow">
            <label for="tsaptz-day">Day</label>
            <select id="tsaptz-day" name="day"></select>
          </div>
          <div class="tsaptz-field">
            <label for="tsaptz-month">Month</label>
            <select id="tsaptz-month" name="month">
              <option value="1">January</option>
              <option value="2">February</option>
              <option value="3">March</option>
              <option value="4">April</option>
              <option value="5">May</option>
              <option value="6">June</option>
              <option value="7">July</option>
              <option value="8">August</option>
              <option value="9">September</option>
              <option value="10">October</option>
              <option value="11">November</option>
              <option value="12">December</option>
            </select>
          </div>
          <div class="tsaptz-field tsaptz-field-narrow">
            <label for="tsaptz-year">Year</label>
            <select id="tsaptz-year" name="year"></select>
          </div>
        </div>
      </fieldset>

      <fieldset class="tsaptz-fieldset">
        <legend class="tsaptz-legend">Time</legend>
        <div class="tsaptz-row tsaptz-row-time">
          <div class="tsaptz-field tsaptz-field-narrow">
            <label for="tsaptz-hour">Hour</label>
            <select id="tsaptz-hour" name="hour"></select>
          </div>
          <div class="tsaptz-field tsaptz-field-narrow">
            <label for="tsaptz-minute">Minute</label>
            <select id="tsaptz-minute" name="minute"></select>
          </div>
          <div class="tsaptz-field tsaptz-field-narrow">
            <label for="tsaptz-ampm">AM/PM</label>
            <select id="tsaptz-ampm" name="ampm">
              <option value="AM">AM</option>
              <option value="PM">PM</option>
            </select>
          </div>
        </div>
      </fieldset>

      <fieldset class="tsaptz-fieldset">
        <legend class="tsaptz-legend">Source timezone</legend>
        <div class="tsaptz-field">
          <label for="tsaptz-source-tz">This date/time is in</label>
          <select id="tsaptz-source-tz" name="sourcetz"></select>
        </div>
      </fieldset>

      <p class="tsaptz-error" id="tsaptz-error" role="alert" hidden></p>

      <div class="tsaptz-actions">
        <button type="submit" class="tsaptz-btn tsaptz-btn-primary" id="tsaptz-convert">Convert</button>
        <button type="button" class="tsaptz-btn" id="tsaptz-share">Get shareable link</button>
      </div>

      <div class="tsaptz-share-box" id="tsaptz-share-box" hidden>
        <label for="tsaptz-share-url">Shareable link</label>
        <div class="tsaptz-share-row">
          <input type="text" id="tsaptz-share-url" readonly>
          <button type="button" class="tsaptz-btn" id="tsaptz-copy">Copy</button>
        </div>
        <p class="tsaptz-share-note" id="tsaptz-copy-note" aria-live="polite"></p>
      </div>

    </form>

  </div>

</section>

<script>
  window.TSAP_TZ_CITIES = [
    {% for c in site.data.timezones.cities %}
    {
      name: {{ c.name | jsonify }},
      country: {{ c.country | default: "" | jsonify }},
      region: {{ c.region | default: "" | jsonify }},
      timezone: {{ c.timezone | jsonify }}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];
</script>

<style>
/* ===== Scoped styles for the Time & Date converter (#tsaptz-root) ===== */

.tsaptz [hidden] {
  display: none !important;
}

.tsaptz {
  max-width: 100%;
  margin: 1.5rem 0;
  font-size: 1rem;
  line-height: 1.5;
}

.tsaptz-event {
  border: 1px solid currentColor;
  border-left-width: 4px;
  border-radius: 4px;
  padding: 0.9rem 1rem;
  margin-bottom: 1.25rem;
  background: rgba(127, 127, 127, 0.08);
}

.tsaptz-event-what {
  font-weight: 700;
  font-size: 1.1rem;
  margin: 0 0 0.35rem;
}

.tsaptz-event-when,
.tsaptz-event-where {
  margin: 0.15rem 0;
}

.tsaptz-event-where a {
  word-break: break-all;
}

.tsaptz-results-heading {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0.2rem 0 0.75rem;
  outline: none;
}

.tsaptz-results-heading:focus {
  outline: none !important;
  box-shadow: none !important;
}

.tsaptz-result-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 1.25rem;
}

.tsaptz-result-actions .tsaptz-btn {
  flex: 1 1 14rem;
  max-width: 22rem;
}

.tsaptz-fieldset {
  border: 1px solid rgba(127, 127, 127, 0.4);
  border-radius: 6px;
  padding: 0.85rem 1rem 1rem;
  margin: 0 0 1rem;
}

.tsaptz-legend {
  font-weight: 700;
  padding: 0 0.35rem;
}

.tsaptz-field {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  margin-bottom: 0.75rem;
  min-width: 0;
}

.tsaptz-field label {
  font-weight: 600;
  font-size: 0.92rem;
}

.tsaptz-field input[type="text"],
.tsaptz-field select {
  font-size: 1rem;
  padding: 0.55rem 0.6rem;
  min-height: 2.6rem;
  border-radius: 5px;
  border: 1px solid rgba(127, 127, 127, 0.6);
  background: transparent;
  color: inherit;
  width: 100%;
  box-sizing: border-box;
}

.tsaptz-field input[type="text"]:focus,
.tsaptz-field select:focus,
.tsaptz-btn:focus {
  outline: 2px solid Highlight;
  outline: 2px solid -webkit-focus-ring-color;
  outline-offset: 2px;
}

.tsaptz-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.tsaptz-row > .tsaptz-field {
  flex: 1 1 8rem;
}

.tsaptz-field-narrow {
  flex: 1 1 6rem;
}

.tsaptz-error {
  color: #b3261e;
  font-weight: 600;
  border: 1px solid #b3261e;
  border-radius: 4px;
  padding: 0.5rem 0.75rem;
  margin: 0 0 1rem;
}

.tsaptz-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-bottom: 1rem;
}

.tsaptz-btn {
  font-size: 1rem;
  padding: 0.6rem 1.1rem;
  min-height: 2.7rem;
  border-radius: 6px;
  border: 1px solid rgba(127, 127, 127, 0.6);
  background: transparent;
  color: inherit;
  cursor: pointer;
  transition: background-color 0.2s ease, border-color 0.2s ease;
}

.tsaptz-btn-primary {
  font-weight: 700;
  border-color: #2a4b8d;
  background: #2a4b8d;
  color: #fff;
}

.tsaptz-btn:hover {
  filter: brightness(1.08);
}

.tsaptz-share-box {
  border: 1px solid rgba(127, 127, 127, 0.4);
  border-radius: 6px;
  padding: 0.85rem 1rem;
  margin-bottom: 1.25rem;
}

.tsaptz-share-box label {
  font-weight: 600;
  display: block;
  margin-bottom: 0.4rem;
}

.tsaptz-share-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tsaptz-share-row input[type="text"] {
  flex: 1 1 14rem;
  font-size: 0.95rem;
  padding: 0.5rem 0.6rem;
  min-height: 2.6rem;
  border-radius: 5px;
  border: 1px solid rgba(127, 127, 127, 0.6);
  background: transparent;
  color: inherit;
}

.tsaptz-share-note {
  margin: 0.4rem 0 0;
  font-size: 0.9rem;
}

.tsaptz-results-empty {
  font-style: italic;
  opacity: 0.85;
}

.tsaptz-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.tsaptz-item {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.75rem;
  border: 1px solid rgba(127, 127, 127, 0.35);
  border-radius: 6px;
  padding: 0.65rem 0.9rem;
  flex-wrap: wrap;
}

.tsaptz-item-you {
  border-color: rgba(127, 127, 127, 0.6);
  border-left-width: 4px;
  background: rgba(255, 214, 89, 0.32);
}

.tsaptz-you-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  border: 1px solid currentColor;
  border-radius: 3px;
  padding: 0.1rem 0.4rem;
  margin-right: 0.5rem;
  vertical-align: middle;
}

.tsaptz-item-name {
  font-weight: 600;
}

.tsaptz-item-meta {
  font-size: 0.85rem;
  opacity: 0.8;
  display: block;
}

.tsaptz-item-time {
  text-align: right;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.tsaptz-item-daybadge {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 700;
  border-radius: 4px;
  padding: 0.05rem 0.4rem;
  margin-left: 0.4rem;
  border: 1px solid currentColor;
}

@media (max-width: 480px) {
  .tsaptz-item {
    flex-direction: column;
    align-items: flex-start;
  }
  .tsaptz-item-time {
    text-align: left;
  }
}

/* =========================================================
   Active Class Architecture Dark Mode Overrides
   ========================================================= */

body.tsap-dark-mode .tsaptz-event {
  background: #1e293b !important;
  border-color: var(--border-main, #374151) !important;
  border-left-color: #38bdf8 !important;
  color: var(--text-main, #e5e7eb) !important;
}

body.tsap-dark-mode .tsaptz-event-where a {
  color: #38bdf8 !important;
}

body.tsap-dark-mode .tsaptz-fieldset,
body.tsap-dark-mode .tsaptz-share-box {
  border-color: var(--border-main, #374151) !important;
  background: rgba(30, 41, 59, 0.4) !important;
}

body.tsap-dark-mode .tsaptz-legend,
body.tsap-dark-mode .tsaptz-field label,
body.tsap-dark-mode .tsaptz-share-box label {
  color: #f3f4f6 !important;
}

body.tsap-dark-mode .tsaptz-field input[type="text"],
body.tsap-dark-mode .tsaptz-field select,
body.tsap-dark-mode .tsaptz-share-row input[type="text"] {
  background: #1e293b !important;
  border-color: var(--border-main, #374151) !important;
  color: #f1f5f9 !important;
}

body.tsap-dark-mode .tsaptz-field input[type="text"]:focus,
body.tsap-dark-mode .tsaptz-field select:focus,
body.tsap-dark-mode .tsaptz-share-row input[type="text"]:focus {
  border-color: #38bdf8 !important;
  outline-color: #38bdf8 !important;
}

body.tsap-dark-mode .tsaptz-btn {
  background: #1e293b !important;
  border-color: var(--border-main, #4b5563) !important;
  color: #f3f4f6 !important;
}

body.tsap-dark-mode .tsaptz-btn:hover {
  background: #334155 !important;
  border-color: #64748b !important;
}

body.tsap-dark-mode .tsaptz-btn-primary {
  background: #1e5fbf !important;
  border-color: #1e5fbf !important;
  color: #ffffff !important;
}

body.tsap-dark-mode .tsaptz-btn-primary:hover {
  background: #38bdf8 !important;
  border-color: #38bdf8 !important;
  color: #0f172a !important;
}

body.tsap-dark-mode .tsaptz-item {
  border-color: var(--border-main, #374151) !important;
  background: #1e293b !important;
  color: #e5e7eb !important;
}

body.tsap-dark-mode .tsaptz-item-you {
  background: #2a3424 !important;
  border-color: #4d7c0f !important;
  border-left-color: #a3e635 !important;
}

body.tsap-dark-mode .tsaptz-you-badge {
  border-color: #a3e635 !important;
  color: #a3e635 !important;
}

body.tsap-dark-mode .tsaptz-item-meta {
  color: var(--text-muted, #94a3b8) !important;
}

body.tsap-dark-mode .tsaptz-item-daybadge {
  border-color: #38bdf8 !important;
  color: #38bdf8 !important;
}

body.tsap-dark-mode .tsaptz-error {
  background: rgba(179, 38, 30, 0.15) !important;
  border-color: #f87171 !important;
  color: #fca5a5 !important;
}
</style>

<script>
(function () {
  "use strict";

  var CITIES = window.TSAP_TZ_CITIES || [];
  var DEFAULT_TITLE_TEXT = "Time & Date Converter";
  var DEFAULT_DOCUMENT_TITLE = document.title;

  var pageHeadingEl = document.querySelector("#maincontent h1") || document.querySelector("main h1");

  var TZ_ALIASES = {
    "asia/calcutta": "Asia/Kolkata",
    "asia/katmandu": "Asia/Kathmandu",
    "asia/saigon": "Asia/Ho_Chi_Minh",
    "asia/rangoon": "Asia/Yangon",
    "america/buenos_aires": "America/Argentina/Buenos_Aires",
    "us/pacific": "America/Los_Angeles",
    "us/eastern": "America/New_York",
    "us/central": "America/Chicago",
    "europe/kiev": "Europe/Kyiv"
  };

  var els = {
    root: document.getElementById("tsaptz-root"),
    intro: document.getElementById("tsaptz-intro"),
    form: document.getElementById("tsaptz-form"),
    what: document.getElementById("tsaptz-what"),
    where: document.getElementById("tsaptz-where"),
    day: document.getElementById("tsaptz-day"),
    month: document.getElementById("tsaptz-month"),
    year: document.getElementById("tsaptz-year"),
    hour: document.getElementById("tsaptz-hour"),
    minute: document.getElementById("tsaptz-minute"),
    ampm: document.getElementById("tsaptz-ampm"),
    sourceTz: document.getElementById("tsaptz-source-tz"),
    error: document.getElementById("tsaptz-error"),
    share: document.getElementById("tsaptz-share"),
    shareBox: document.getElementById("tsaptz-share-box"),
    shareUrl: document.getElementById("tsaptz-share-url"),
    copy: document.getElementById("tsaptz-copy"),
    copyNote: document.getElementById("tsaptz-copy-note"),
    resultsEmpty: document.getElementById("tsaptz-results-empty"),
    list: document.getElementById("tsaptz-list"),
    eventBox: document.getElementById("tsaptz-event"),
    eventWhat: document.getElementById("tsaptz-event-what"),
    eventWhen: document.getElementById("tsaptz-event-when"),
    eventWhere: document.getElementById("tsaptz-event-where"),
    resultView: document.getElementById("tsaptz-result-view"),
    resultActions: document.getElementById("tsaptz-result-actions"),
    newBtn: document.getElementById("tsaptz-new-conversion"),
    formWrap: document.getElementById("tsaptz-form-wrap"),
    resultsHeading: document.getElementById("tsaptz-results-heading")
  };

  function pad(n) { return String(n).length < 2 ? "0" + n : String(n); }

  function normaliseAlias(tz) {
    if (!tz) return tz;
    var lower = String(tz).toLowerCase();
    return TZ_ALIASES[lower] || tz;
  }

  function getVisitorTimeZone() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
      tz = normaliseAlias(tz);
      if (tz && isValidTimeZone(tz)) return tz;
    } catch (e) {}
    return "UTC";
  }

  function isValidTimeZone(tz) {
    try {
      new Intl.DateTimeFormat("en-US", { timeZone: tz });
      return true;
    } catch (e) {
      return false;
    }
  }

  function findCanonicalTimeZone(input) {
    if (!input) return null;
    var aliasResolved = normaliseAlias(input);
    var lower = String(aliasResolved).toLowerCase();
    for (var i = 0; i < CITIES.length; i++) {
      if (CITIES[i].timezone.toLowerCase() === lower) return CITIES[i].timezone;
    }
    if (lower === "utc") return "UTC";
    if (isValidTimeZone(aliasResolved)) return aliasResolved;
    var attempt = aliasResolved.replace(/(^|\/)([a-z])/g, function (m, sep, c) {
      return sep + c.toUpperCase();
    });
    if (isValidTimeZone(attempt)) return attempt;
    return null;
  }

  function populateSelect(select, start, end, formatter) {
    var frag = document.createDocumentFragment();
    for (var i = start; i <= end; i++) {
      var opt = document.createElement("option");
      opt.value = String(i);
      opt.textContent = formatter ? formatter(i) : pad(i);
      frag.appendChild(opt);
    }
    select.appendChild(frag);
  }

  function buildSourceTimezoneOptions() {
    var frag = document.createDocumentFragment();
    var groups = {};
    var order = [];

    CITIES.forEach(function (c) {
      var key = c.country + "|" + c.timezone;

      if (!groups[key]) {
        groups[key] = {
          country: c.country,
          timezone: c.timezone,
          cities: []
        };
        order.push(key);
      }

      groups[key].cities.push(c.name);
    });

    order.forEach(function (key) {
      var group = groups[key];
      var opt = document.createElement("option");

      opt.value = group.timezone;

      var countryLabel = group.country || "Global";
      var cityLabel = group.cities.join(" / ");

      opt.textContent = countryLabel + " \u2014 " + cityLabel;

      frag.appendChild(opt);
    });

    els.sourceTz.appendChild(frag);

    var visitorTz = getVisitorTimeZone();
    var visitorAlreadyListed = order.some(function (key) {
      return groups[key].timezone === visitorTz;
    });

    if (!visitorAlreadyListed) {
      var own = document.createElement("option");
      own.value = visitorTz;
      own.textContent = "Your browser timezone \u2014 " + visitorTz;
      els.sourceTz.insertBefore(own, els.sourceTz.firstChild);
    }
  }

  function buildStaticSelects() {
    populateSelect(els.day, 1, 31);
    populateSelect(els.hour, 1, 12);
    populateSelect(els.minute, 0, 59, function (i) { return pad(i); });

    var thisYear = new Date().getFullYear();
    populateSelect(els.year, thisYear - 2, thisYear + 5);

    buildSourceTimezoneOptions();
  }

  function setDefaultsToNow(tz) {
    var now = new Date();
    var parts = getPartsInZone(now, tz);
    els.day.value = String(parts.day);
    els.month.value = String(parts.month);
    els.year.value = String(parts.year);
    var h12 = parts.hour % 12;
    if (h12 === 0) h12 = 12;
    els.hour.value = String(h12);
    els.minute.value = String(parts.minute);
    els.ampm.value = parts.hour >= 12 ? "PM" : "AM";
    els.sourceTz.value = tz;
  }

  function getPartsInZone(date, timeZone) {
    var dtf = new Intl.DateTimeFormat("en-US", {
      timeZone: timeZone,
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hourCycle: "h23"
    });
    var partsArr = dtf.formatToParts(date);
    var out = {};
    partsArr.forEach(function (p) {
      if (p.type !== "literal") out[p.type] = parseInt(p.value, 10);
    });
    return {
      year: out.year,
      month: out.month,
      day: out.day,
      hour: out.hour,
      minute: out.minute,
      second: out.second || 0
    };
  }

  function offsetMinutesFor(utcMs, timeZone) {
    var rendered = getPartsInZone(new Date(utcMs), timeZone);
    var renderedAsUtc = Date.UTC(
      rendered.year, rendered.month - 1, rendered.day,
      rendered.hour, rendered.minute, rendered.second
    );
    return (renderedAsUtc - utcMs) / 60000;
  }

  function zonedTimeToUtc(year, month, day, hour, minute, timeZone) {
    var naiveUtc = Date.UTC(year, month - 1, day, hour, minute, 0);
    var offset1 = offsetMinutesFor(naiveUtc, timeZone);
    var candidate = naiveUtc - offset1 * 60000;
    var offset2 = offsetMinutesFor(candidate, timeZone);

    var result = candidate;
    var flag = null;

    if (offset2 !== offset1) {
      var candidate2 = naiveUtc - offset2 * 60000;
      var offset3 = offsetMinutesFor(candidate2, timeZone);
      if (offset3 === offset2) {
        result = candidate2;
        flag = "shifted";
      } else {
        result = candidate2;
        flag = "ambiguous";
      }
    }

    var verify = getPartsInZone(new Date(result), timeZone);
    var requestedMinutesOfDay = hour * 60 + minute;
    var verifyMinutesOfDay = verify.hour * 60 + verify.minute;
    var sameDate = verify.year === year && verify.month === month && verify.day === day;

    if (!sameDate || requestedMinutesOfDay !== verifyMinutesOfDay) {
      if (!flag) flag = "nonexistent";
    }

    return { utcMs: result, flag: flag };
  }

  function isValidCalendarDate(year, month, day) {
    if (!year || !month || !day) return false;
    var d = new Date(Date.UTC(year, month - 1, day));
    return (
      d.getUTCFullYear() === year &&
      d.getUTCMonth() === month - 1 &&
      d.getUTCDate() === day
    );
  }

  var WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  var MONTHS = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];

  function formatResultRow(epochMs, timeZone) {
    var parts = getPartsInZone(new Date(epochMs), timeZone);
    var dObj = new Date(Date.UTC(parts.year, parts.month - 1, parts.day));
    var weekday = WEEKDAYS[dObj.getUTCDay()];
    var h12 = parts.hour % 12;
    if (h12 === 0) h12 = 12;
    var ampm = parts.hour >= 12 ? "PM" : "AM";
    return {
      dateLabel: weekday + ", " + parts.day + " " + MONTHS[parts.month - 1] + " " + parts.year,
      timeLabel: h12 + ":" + pad(parts.minute) + " " + ampm,
      dayKey: parts.year * 10000 + parts.month * 100 + parts.day
    };
  }

  function looksLikeUrl(str) {
    return /^https?:\/\/\S+$/i.test(str.trim());
  }

  function labelForTimeZone(tz) {
    var group = CITIES.filter(function (c) { return c.timezone === tz; });
    if (group.length) return group.map(function (c) { return c.name; }).join(" / ");
    return tz;
  }

  function countryForTimeZone(tz) {
    var group = CITIES.filter(function (c) { return c.timezone === tz; });
    if (group.length && group[0].country) return group[0].country;
    return "";
  }

  function setPageHeading(text) {
    if (pageHeadingEl) pageHeadingEl.textContent = text;
    document.title = (text === DEFAULT_TITLE_TEXT) ? DEFAULT_DOCUMENT_TITLE : text;
  }

  function renderEventBanner(what, where, epochMs, sourceTzCanonical) {
    var hasWhat = what && what.trim().length > 0;
    var hasWhere = where && where.trim().length > 0;
    var hasTime = typeof epochMs === "number" && !isNaN(epochMs);

    if (!hasWhat && !hasWhere && !hasTime) {
      els.eventBox.hidden = true;
      return;
    }

    els.eventBox.hidden = false;

    if (hasWhat) {
      els.eventWhat.textContent = what;
      els.eventWhat.hidden = false;
    } else {
      els.eventWhat.hidden = true;
    }

    if (hasTime) {
      var row = formatResultRow(epochMs, sourceTzCanonical);
      var cityLabel = labelForTimeZone(sourceTzCanonical);
      els.eventWhen.textContent = row.dateLabel + " \u2013 " + row.timeLabel + " (" + cityLabel + " time)";
      els.eventWhen.hidden = false;
    } else {
      els.eventWhen.hidden = true;
    }

    if (hasWhere) {
      els.eventWhere.innerHTML = "";
      els.eventWhere.appendChild(document.createTextNode("Where: "));
      if (looksLikeUrl(where)) {
        var a = document.createElement("a");
        a.href = where.trim();
        a.textContent = where.trim();
        a.rel = "noopener noreferrer";
        els.eventWhere.appendChild(a);
      } else {
        els.eventWhere.appendChild(document.createTextNode(where));
      }
      els.eventWhere.hidden = false;
    } else {
      els.eventWhere.hidden = true;
    }
  }

  function renderResults(epochMs, sourceTzCanonical) {
    els.list.innerHTML = "";
    var visitorTz = getVisitorTimeZone();
    var sourceRow = formatResultRow(epochMs, sourceTzCanonical);

    var rows = [];
    rows.push({ label: null, timezone: visitorTz, isYou: true });

    var seen = {};
    CITIES.forEach(function (c) {
      if (c.timezone === visitorTz) return;
      if (seen[c.timezone]) return;
      seen[c.timezone] = true;
      var group = CITIES.filter(function (x) { return x.timezone === c.timezone; });
      rows.push({
        label: group.map(function (x) { return x.name; }).join(" / "),
        country: c.country,
        timezone: c.timezone,
        isYou: false
      });
    });

    rows.forEach(function (r) {
      var row = formatResultRow(epochMs, r.timezone);
      var li = document.createElement("li");
      li.className = "tsaptz-item" + (r.isYou ? " tsaptz-item-you" : "");

      var left = document.createElement("div");

      if (r.isYou) {
        var badgeText = document.createElement("span");
        badgeText.className = "tsaptz-you-badge";
        badgeText.textContent = "Your timezone";
        left.appendChild(badgeText);
      }

      var nameEl = document.createElement("span");
      nameEl.className = "tsaptz-item-name";
      nameEl.textContent = r.isYou ? labelForTimeZone(visitorTz) : r.label;
      left.appendChild(nameEl);

      var metaEl = document.createElement("span");
      metaEl.className = "tsaptz-item-meta";
      var metaCountry = r.isYou ? countryForTimeZone(visitorTz) : r.country;
      metaEl.textContent = (metaCountry ? metaCountry + " \u2013 " : "") + (r.isYou ? visitorTz : r.timezone);
      left.appendChild(metaEl);

      var right = document.createElement("div");
      right.className = "tsaptz-item-time";
      right.appendChild(document.createTextNode(row.timeLabel + ", " + row.dateLabel + " "));

      if (row.dayKey !== sourceRow.dayKey) {
        var badge = document.createElement("span");
        badge.className = "tsaptz-item-daybadge";
        badge.textContent = row.dayKey < sourceRow.dayKey ? "Previous day" : "Next day";
        right.appendChild(badge);
      }

      li.appendChild(left);
      li.appendChild(right);
      els.list.appendChild(li);
    });

    els.list.hidden = false;
    els.resultsEmpty.hidden = true;
  }

  function showError(msg) {
    els.error.textContent = msg;
    els.error.hidden = false;
  }

  function clearError() {
    els.error.hidden = true;
    els.error.textContent = "";
  }

  function readFormState() {
    var day = parseInt(els.day.value, 10);
    var month = parseInt(els.month.value, 10);
    var year = parseInt(els.year.value, 10);
    var hour12 = parseInt(els.hour.value, 10);
    var minute = parseInt(els.minute.value, 10);
    var ampm = els.ampm.value;
    var tz = els.sourceTz.value;

    if (!isValidCalendarDate(year, month, day)) {
      return { error: "That date does not exist. Please check the day, month and year (for example, February 29 only exists in leap years)." };
    }

    var hour24 = hour12 % 12;
    if (ampm === "PM") hour24 += 12;

    var canonicalTz = findCanonicalTimeZone(tz);
    if (!canonicalTz) {
      return { error: "That timezone is not recognised by your browser." };
    }

    var conversion = zonedTimeToUtc(year, month, day, hour24, minute, canonicalTz);

    return {
      epochMs: conversion.utcMs,
      flag: conversion.flag,
      timezone: canonicalTz,
      day: day, month: month, year: year,
      hour24: hour24, minute: minute
    };
  }

  function buildShareHash(state, what, where) {
    var ts = state.year + pad(state.month) + pad(state.day) + pad(state.hour24) + pad(state.minute);
    var tz = state.timezone.toLowerCase();
    var hash = "ts=" + ts + "&tz=" + encodeURIComponent(tz);
    if (what && what.trim()) hash += "&what=" + encodeURIComponent(what.trim());
    if (where && where.trim()) hash += "&where=" + encodeURIComponent(where.trim());
    return hash;
  }

  function parseUrlHash() {
    var hash = window.location.hash;
    if (!hash || hash.length < 2) return null;
    hash = hash.substring(1);
    var params = {};
    hash.split("&").forEach(function (pair) {
      var idx = pair.indexOf("=");
      if (idx === -1) return;
      var key = decodeURIComponent(pair.substring(0, idx));
      var val = decodeURIComponent(pair.substring(idx + 1));
      params[key] = val;
    });

    var ts = params.ts;
    var tz = params.tz;
    if (!ts || !tz) return null;

    var match = /^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})$/.exec(ts);
    if (!match) return null;

    var year = parseInt(match[1], 10);
    var month = parseInt(match[2], 10);
    var day = parseInt(match[3], 10);
    var hour24 = parseInt(match[4], 10);
    var minute = parseInt(match[5], 10);

    if (!isValidCalendarDate(year, month, day)) return null;
    if (hour24 < 0 || hour24 > 23 || minute < 0 || minute > 59) return null;

    var canonicalTz = findCanonicalTimeZone(tz);
    if (!canonicalTz) return null;

    var what = (params.what || "").slice(0, 120);
    var where = (params.where || "").slice(0, 200);

    return {
      year: year, month: month, day: day,
      hour24: hour24, minute: minute,
      timezone: canonicalTz,
      what: what, where: where
    };
  }

  function applyStateToForm(state) {
    els.day.value = String(state.day);
    els.month.value = String(state.month);
    els.year.value = String(state.year);
    var h12 = state.hour24 % 12;
    if (h12 === 0) h12 = 12;
    els.hour.value = String(h12);
    els.minute.value = String(state.minute);
    els.ampm.value = state.hour24 >= 12 ? "PM" : "AM";
    els.sourceTz.value = state.timezone;
    els.what.value = state.what || "";
    els.where.value = state.where || "";
  }

  function focusElement(el) {
    if (!el) return;
    if (!el.hasAttribute("tabindex")) el.setAttribute("tabindex", "-1");
    el.focus();
  }

  function enterResultView(epochMs, sourceTzCanonical, what, where) {
    renderResults(epochMs, sourceTzCanonical);
    renderEventBanner(what, where, epochMs, sourceTzCanonical);

    var trimmedWhat = what && what.trim();
    setPageHeading(trimmedWhat ? trimmedWhat : DEFAULT_TITLE_TEXT);

    if (els.intro) els.intro.hidden = true;
    if (els.formWrap) els.formWrap.hidden = true;
    if (els.resultView) els.resultView.hidden = false;
    if (els.resultActions) els.resultActions.hidden = false;

    focusElement(els.resultsHeading || els.eventBox || els.list);
  }

  function enterFormView() {
    if (els.intro) els.intro.hidden = false;
    if (els.formWrap) els.formWrap.hidden = false;
    if (els.resultView) els.resultView.hidden = true;
    if (els.resultActions) els.resultActions.hidden = true;

    setPageHeading(DEFAULT_TITLE_TEXT);
  }

  function doConvert() {
    clearError();
    var state = readFormState();
    if (state.error) {
      showError(state.error);
      return null;
    }
    if (state.flag === "nonexistent") {
      showError("That local time does not exist in this timezone on this date, because clocks move forward for daylight saving at that point. Showing the nearest equivalent instant instead \u2014 please double-check the time.");
    } else if (state.flag === "ambiguous") {
      showError("That local time occurs twice in this timezone on this date, because clocks move back for daylight saving at that point. Showing one of the two possible instants \u2014 please double-check the time.");
    }
    return state;
  }

  els.form.addEventListener("submit", function (e) {
    e.preventDefault();
    var state = doConvert();
    if (!state) return;

    var hash = buildShareHash(state, els.what.value, els.where.value);
    var url = window.location.pathname + "#" + hash;
    history.pushState({ tsaptzResult: true }, "", url);

    enterResultView(state.epochMs, state.timezone, els.what.value, els.where.value);
  });

  els.share.addEventListener("click", function () {
    clearError();
    var state = readFormState();
    if (state.error) {
      showError(state.error);
      return;
    }
    var hash = buildShareHash(state, els.what.value, els.where.value);
    var url = window.location.origin + window.location.pathname + "#" + hash;
    els.shareUrl.value = url;
    els.shareBox.hidden = false;
    els.copyNote.textContent = "";
    history.replaceState(null, "", "#" + hash);
  });

  els.copy.addEventListener("click", function () {
    els.shareUrl.select();
    try {
      var ok = document.execCommand && document.execCommand("copy");
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(els.shareUrl.value).then(function () {
          els.copyNote.textContent = "Link copied.";
        }, function () {
          els.copyNote.textContent = ok ? "Link copied." : "Could not copy automatically; please copy the text manually.";
        });
      } else {
        els.copyNote.textContent = ok ? "Link copied." : "Could not copy automatically; please copy the text manually.";
      }
    } catch (e) {
      els.copyNote.textContent = "Could not copy automatically; please copy the text manually.";
    }
  });

  if (els.newBtn) {
    els.newBtn.addEventListener("click", function () {
      window.location.href = window.location.pathname;
    });
  }

  function loadFromCurrentHash() {
    var urlState = parseUrlHash();
    if (urlState) {
      applyStateToForm(urlState);
      var conversion = zonedTimeToUtc(
        urlState.year, urlState.month, urlState.day,
        urlState.hour24, urlState.minute, urlState.timezone
      );
      if (conversion.flag === "nonexistent") {
        showError("That local time does not exist in this timezone on this date, because clocks move forward for daylight saving at that point. Showing the nearest equivalent instant instead \u2014 please double-check the time.");
      } else if (conversion.flag === "ambiguous") {
        showError("That local time occurs twice in this timezone on this date, because clocks move back for daylight saving at that point. Showing one of the two possible instants \u2014 please double-check the time.");
      }
      enterResultView(conversion.utcMs, urlState.timezone, urlState.what, urlState.where);
    } else {
      var visitorTz = getVisitorTimeZone();
      setDefaultsToNow(visitorTz);
      els.eventBox.hidden = true;
      enterFormView();
    }
  }

  window.addEventListener("popstate", function () {
    loadFromCurrentHash();
  });

  function init() {
    buildStaticSelects();
    loadFromCurrentHash();
  }

  init();
})();
</script>
