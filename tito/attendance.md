---
layout: default
title: "Attendance"
description: "A personal daily attendance record for Tito Dutta, with a calendar showing the days marked present."
categories: [Tito Dutta]
authors: [Tito Dutta]
permalink: /tito/attendance/
created: 2026-10-15
attendance_dates: []
---

{% include author.html %}

This is a personal attendance log. Each date marked with a raised hand indicates that attendance was recorded for that day.

## Attendance calendar

<p id="attendance-summary" aria-live="polite">Loading attendance record...</p>

<div id="attendance-calendar" class="attendance-calendar" aria-label="Annual attendance calendar"></div>

## Recorded dates

<ul id="attendance-recorded-dates" class="attendance-recorded-dates"></ul>

<p class="attendance-edit-note">To record attendance, edit this page in the GitHub repository and add the date to the <code>attendance_dates</code> list in the YAML at the top. Add only one entry per day, using the format <code>YYYY-MM-DD</code>. The calendar and total will update after the website rebuilds.</p>

<!--
Recording attendance:
1. Find attendance_dates in the YAML at the top of this file.
2. Replace attendance_dates: [] with a list on the first entry, for example:
   attendance_dates:
     - "2026-10-15"
3. On each later day, add one new line under the list, using that day's date.
4. Do not add the same date more than once.
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
  const attendanceDates = {{ page.attendance_dates | jsonify }};
  const dateSet = new Set(Array.isArray(attendanceDates) ? attendanceDates : []);
  const calendar = document.getElementById('attendance-calendar');
  const summary = document.getElementById('attendance-summary');
  const recordedDates = document.getElementById('attendance-recorded-dates');

  if (!calendar || !summary || !recordedDates) return;

  const today = new Date();
  const year = today.getFullYear();
  const todayString = [
    year,
    String(today.getMonth() + 1).padStart(2, '0'),
    String(today.getDate()).padStart(2, '0')
  ].join('-');

  const sortedDates = Array.from(dateSet).filter(date => /^\d{4}-\d{2}-\d{2}$/.test(date)).sort().reverse();
  summary.textContent = sortedDates.length + (sortedDates.length === 1 ? ' day marked present.' : ' days marked present.') + ' in total.';

  const weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

  for (let month = 0; month < 12; month++) {
    const monthSection = document.createElement('section');
    monthSection.className = 'attendance-month';

    const heading = document.createElement('h3');
    heading.textContent = new Date(year, month, 1).toLocaleDateString('en-GB', { month: 'long', year: 'numeric' });
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

    const firstDay = new Date(year, month, 1);
    const offset = (firstDay.getDay() + 6) % 7;
    for (let blank = 0; blank < offset; blank++) {
      const empty = document.createElement('span');
      empty.className = 'attendance-day';
      empty.setAttribute('aria-hidden', 'true');
      grid.appendChild(empty);
    }

    const daysInMonth = new Date(year, month + 1, 0).getDate();
    for (let day = 1; day <= daysInMonth; day++) {
      const dateString = [
        year,
        String(month + 1).padStart(2, '0'),
        String(day).padStart(2, '0')
      ].join('-');

      const cell = document.createElement('span');
      cell.className = 'attendance-day';
      cell.textContent = String(day);
      cell.setAttribute('aria-label', dateString);

      if (dateSet.has(dateString)) {
        cell.classList.add('is-present');
        cell.textContent = '✋';
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
    sortedDates.forEach(date => {
      const item = document.createElement('li');
      const parsed = new Date(date + 'T12:00:00');
      item.textContent = parsed.toLocaleDateString('en-GB', {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      });
      recordedDates.appendChild(item);
    });
  }
});
</script>
