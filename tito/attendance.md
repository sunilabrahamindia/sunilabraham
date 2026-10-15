---
layout: default
title: "Attendance"
description: "A personal daily attendance record for Tito Dutta, with a calendar showing the days marked present."
categories: [Tito Dutta]
authors: [Tito Dutta]
permalink: /tito/attendance/
created: 2026-10-15
attendance_log:
  "2026-10-15": "yes"
  "2026-10-16": ""
  "2026-10-17": ""
  "2026-10-18": ""
  "2026-10-19": ""
  "2026-10-20": ""
  "2026-10-21": ""
  "2026-10-22": ""
  "2026-10-23": ""
  "2026-10-24": ""
  "2026-10-25": ""
  "2026-10-26": ""
  "2026-10-27": ""
  "2026-10-28": ""
  "2026-10-29": ""
  "2026-10-30": ""
  "2026-10-31": ""
  "2026-11-01": ""
  "2026-11-02": ""
  "2026-11-03": ""
  "2026-11-04": ""
  "2026-11-05": ""
  "2026-11-06": ""
  "2026-11-07": ""
  "2026-11-08": ""
  "2026-11-09": ""
  "2026-11-10": ""
  "2026-11-11": ""
  "2026-11-12": ""
  "2026-11-13": ""
  "2026-11-14": ""
  "2026-11-15": ""
  "2026-11-16": ""
  "2026-11-17": ""
  "2026-11-18": ""
  "2026-11-19": ""
  "2026-11-20": ""
  "2026-11-21": ""
  "2026-11-22": ""
  "2026-11-23": ""
  "2026-11-24": ""
  "2026-11-25": ""
  "2026-11-26": ""
  "2026-11-27": ""
  "2026-11-28": ""
  "2026-11-29": ""
  "2026-11-30": ""
  "2026-12-01": ""
  "2026-12-02": ""
  "2026-12-03": ""
  "2026-12-04": ""
  "2026-12-05": ""
  "2026-12-06": ""
  "2026-12-07": ""
  "2026-12-08": ""
  "2026-12-09": ""
  "2026-12-10": ""
  "2026-12-11": ""
  "2026-12-12": ""
  "2026-12-13": ""
  "2026-12-14": ""
  "2026-12-15": ""
  "2026-12-16": ""
  "2026-12-17": ""
  "2026-12-18": ""
  "2026-12-19": ""
  "2026-12-20": ""
  "2026-12-21": ""
  "2026-12-22": ""
  "2026-12-23": ""
  "2026-12-24": ""
  "2026-12-25": ""
  "2026-12-26": ""
  "2026-12-27": ""
  "2026-12-28": ""
  "2026-12-29": ""
  "2026-12-30": ""
  "2026-12-31": ""
---

{% include author.html %}

This is a personal attendance log. Each date marked with a raised hand indicates that attendance was recorded for that day. Each date marked with a raised hand indicates that attendance was recorded for that day. The calendar only displays a mark when a date has a non-empty value in the attendance log. Enter "yes" for attendance or "no" for an absence; leave unrecorded dates blank. This is not merely an attendance record for TSAP; it is mainly a practice of contemplation.

## Attendance calendar

<p id="attendance-summary" aria-live="polite">Loading attendance record...</p>

<div id="attendance-calendar" class="attendance-calendar" aria-label="Annual attendance calendar"></div>

## Recorded dates

<ul id="attendance-recorded-dates" class="attendance-recorded-dates"></ul>

<p class="attendance-edit-note">To record attendance, edit this page in GitHub and find today's date under <code>attendance_log</code> in the YAML at the top. Replace the empty quotes with <code>"yes"</code> if present or <code>"no"</code> if absent. Leave other dates blank. The calendar and totals update after the website rebuilds.</p>

<!--
Recording attendance:
Find today's date under attendance_log in the YAML above and replace its empty value:
  "2026-10-15": "yes"
Use "no" for an absence. Leave unrecorded dates as empty quotes. Date entries are prepared through 31 December 2026.
-->

<style>
.attendance-calendar {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin: 1.25rem 0 2rem;
}

.attendance-month {
  min-width: 0;
  padding: 0.85rem;
  border: 1px solid var(--border-main, #cbd5e1);
  border-radius: 8px;
  background: var(--bg-surface, #fff);
  color: var(--text-main, #1f2937);
}

.attendance-month h3 {
  margin: 0 0 0.7rem;
  color: var(--text-heading, #163b65);
  font-size: 1rem;
}

.attendance-month-grid {
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  gap: 0.2rem;
}

.attendance-weekday,
.attendance-day {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 0;
  min-height: 2rem;
  font-size: 0.82rem;
  text-align: center;
}

.attendance-weekday {
  color: var(--text-muted, #444);
  font-weight: 700;
}

.attendance-day {
  border-radius: 4px;
  gap: 0.1rem;
}

.attendance-day.is-present {
  flex-direction: column;
  line-height: 1.05;
}

.attendance-day-number {
  font-size: 0.78rem;
}

.attendance-hand {
  font-size: 0.78rem;
  line-height: 1;
}

.attendance-day.is-present {
  background: #d9f0e2;
  color: #174b2d;
  font-weight: 700;
}

.attendance-day.is-today {
  outline: 2px solid #1f5fbf;
  outline-offset: -2px;
}

.attendance-legend {
  margin: 0.5rem 0;
  color: var(--text-muted, #444);
  font-size: 0.95rem;
}

.attendance-recorded-dates {
  padding-left: 1.5rem;
  line-height: 1.8;
}

.attendance-edit-note {
  margin-top: 1.5rem;
  padding: 0.9rem 1rem;
  border-left: 4px solid #1f5fbf;
  background: var(--bg-surface, #f3f6fa);
  color: var(--text-main, #1f2937);
  line-height: 1.6;
}

body.tsap-dark-mode .attendance-month {
  background: var(--bg-surface, #1f2937);
  border-color: var(--border-sub, #4b5563);
  color: var(--text-main, #e5e7eb);
}

body.tsap-dark-mode .attendance-month h3 {
  color: var(--text-heading, #f3f4f6);
}

body.tsap-dark-mode .attendance-weekday,
body.tsap-dark-mode .attendance-legend {
  color: var(--text-muted, #cbd5e1);
}

body.tsap-dark-mode .attendance-day.is-present {
  background: #17452b;
  color: #d1fae5;
}

body.tsap-dark-mode .attendance-day.is-today {
  outline-color: #93c5fd;
}

body.tsap-dark-mode .attendance-edit-note {
  background: var(--bg-surface, #1e293b);
  color: var(--text-main, #e5e7eb);
  border-left-color: #60a5fa;
}

@media (max-width: 900px) {
  .attendance-calendar {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 560px) {
  .attendance-calendar {
    grid-template-columns: minmax(0, 1fr);
  }

  .attendance-month {
    padding: 1rem;
  }

  .attendance-day,
  .attendance-weekday {
    min-height: 2.25rem;
    font-size: 0.9rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  const attendanceLog = {{ page.attendance_log | jsonify }};
  const log = attendanceLog && typeof attendanceLog === "object" ? attendanceLog : {};
  const recordedLog = Object.entries(log).filter(([date, value]) => /^\d{4}-\d{2}-\d{2}$/.test(date) && String(value).trim().length > 0).sort(([a], [b]) => b.localeCompare(a));
  const dateSet = new Set(recordedLog.filter(([date, value]) => String(value).trim().toLowerCase() === "yes").map(([date]) => date));
  const calendar = document.getElementById('attendance-calendar');
  const summary = document.getElementById('attendance-summary');
  const recordedDates = document.getElementById('attendance-recorded-dates');

  if (!calendar || !summary || !recordedDates) return;

  const today = new Date();
  const todayYear = today.getFullYear();
  const calendarYear = 2026;
  const todayString = [
    todayYear,
    String(today.getMonth() + 1).padStart(2, '0'),
    String(today.getDate()).padStart(2, '0')
  ].join('-');

  const sortedDates = Array.from(dateSet).sort().reverse();
  const absentCount = recordedLog.filter(([, value]) => String(value).trim().toLowerCase() === "no").length;
  summary.textContent = sortedDates.length + (sortedDates.length === 1 ? ' day marked present' : ' days marked present') + ' and ' + absentCount + (absentCount === 1 ? ' day marked absent.' : ' days marked absent.');

  const weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

  // Show the months covered by this attendance record, starting in October 2026.
  for (let month = 9; month < 12; month++) {
    const monthSection = document.createElement('section');
    monthSection.className = 'attendance-month';

    const heading = document.createElement('h3');
    heading.textContent = new Date(calendarYear, month, 1).toLocaleDateString('en-GB', { month: 'long', year: 'numeric' });
    monthSection.appendChild(heading);

    const grid = document.createElement('div');
    grid.className = 'attendance-month-grid';

    weekdays.forEach(day => {
      const weekday = document.createElement('span');
      weekday.className = 'attendance-weekday';
      weekday.textContent = day;
      weekday.setAttribute('aria-hidden', 'true');
      grid.appendChild(weekday);
    });

    const firstDay = new Date(calendarYear, month, 1);
    const offset = (firstDay.getDay() + 6) % 7;
    for (let blank = 0; blank < offset; blank++) {
      const empty = document.createElement('span');
      empty.className = 'attendance-day';
      empty.setAttribute('aria-hidden', 'true');
      grid.appendChild(empty);
    }

    const daysInMonth = new Date(calendarYear, month + 1, 0).getDate();
    for (let day = 1; day <= daysInMonth; day++) {
      const dateString = [
        calendarYear,
        String(month + 1).padStart(2, '0'),
        String(day).padStart(2, '0')
      ].join('-');

      const cell = document.createElement('span');
      cell.className = 'attendance-day';
      cell.textContent = String(day);
      cell.setAttribute('aria-label', dateString);

      if (dateSet.has(dateString)) {
        cell.classList.add('is-present');

        const dayNumber = document.createElement('span');
        dayNumber.className = 'attendance-day-number';
        dayNumber.textContent = String(day);

        const hand = document.createElement('span');
        hand.className = 'attendance-hand';
        hand.textContent = '✋';
        hand.setAttribute('aria-hidden', 'true');

        cell.replaceChildren(dayNumber, hand);
        cell.setAttribute('aria-label', dateString + ': attendance marked');
        cell.setAttribute('title', dateString + ': attendance marked');
      }

      if (dateString === todayString) {
        cell.classList.add('is-today');
        if (!dateSet.has(dateString)) {
          cell.setAttribute('aria-label', dateString + ': today, not yet marked');
        }
      }

      grid.appendChild(cell);
    }

    monthSection.appendChild(grid);
    calendar.appendChild(monthSection);
  }

  if (sortedDates.length === 0) {
    const item = document.createElement('li');
    item.textContent = 'No attendance dates have been recorded yet.';
    recordedDates.appendChild(item);
  } else {
    recordedLog.forEach(([date, value]) => {
      const item = document.createElement('li');
      const parsed = new Date(date + 'T12:00:00');
      const status = String(value).trim().toLowerCase();
      const label = parsed.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
      item.textContent = label + (status === 'yes' ? ' — Present (raised hand)' : status === 'no' ? ' — Absent' : ' — ' + String(value).trim());
      recordedDates.appendChild(item);
    });
  }
});
</script>

## See also

- [The Mind](/tito/mind/) — A visual exploration of the human mind.

{% include navbox-tito.html %}
