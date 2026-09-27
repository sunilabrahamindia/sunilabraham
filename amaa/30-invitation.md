---
layout: default
title: "A. M. A. Ayrookuzhiel: 30th Death Anniversary Commemoration"
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration, Events]
permalink: /amaa/30-invitation/
description: Invitation page for the 30th Death Anniversary Commemoration of Rev. Dr. A. M. A. Ayrookuzhiel (1933–1996), to be held on 29 November 2026 in Bengaluru.
created: 2026-09-27
---

<style>
.amaa-poster {
  --ink: #1c1a17;
  --paper: #f7f2e9;
  --paper-deep: #efe6d5;
  --maroon: #6b1f24;
  --maroon-deep: #4a1418;
  --gold: #a9782f;
  --gold-light: #c99a4a;
  --line: rgba(28, 26, 23, 0.16);
  font-family: 'Georgia', 'Iowan Old Style', 'Palatino Linotype', serif;
  color: var(--ink);
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 4px;
  overflow: hidden;
  max-width: 720px;
  margin: 2rem auto;
  box-shadow: 0 18px 40px -20px rgba(28, 20, 10, 0.45);
}

.amaa-poster * { box-sizing: border-box; }

.amaa-band-top {
  background: linear-gradient(135deg, var(--maroon) 0%, var(--maroon-deep) 100%);
  color: #f4ead9;
  text-align: center;
  padding: 1.6rem 1.25rem 1.3rem;
  position: relative;
}

.amaa-band-top::after {
  content: "";
  display: block;
  height: 3px;
  margin: 1rem auto 0;
  width: 72px;
  background: var(--gold-light);
}

.amaa-name {
  font-size: clamp(1.55rem, 5.2vw, 2.25rem);
  line-height: 1.18;
  margin: 0;
  font-weight: 700;
  letter-spacing: 0.01em;
}

.amaa-sub {
  margin: 0.55rem 0 0;
  font-size: clamp(0.95rem, 3vw, 1.1rem);
  font-style: italic;
  color: #ecdfc6;
}

.amaa-portrait-wrap {
  background: var(--paper-deep);
  padding: 1.6rem 1.25rem 1rem;
  display: flex;
  justify-content: center;
}

.amaa-portrait-frame {
  padding: 8px;
  background: #fffdf8;
  border: 1px solid var(--line);
  box-shadow: 0 10px 26px -14px rgba(28, 20, 10, 0.5);
}

.amaa-portrait-frame img {
  display: block;
  width: 190px;
  height: auto;
  filter: grayscale(12%) contrast(1.03);
}

.amaa-portrait-caption {
  text-align: center;
  font-size: 0.85rem;
  font-style: italic;
  color: #5c554a;
  margin: 0;
  padding: 0.7rem 1.25rem 1.4rem;
  background: var(--paper-deep);
}

.amaa-savedate {
  text-align: center;
  padding: 1.5rem 1.25rem 1.6rem;
  border-bottom: 1px solid var(--line);
}

.amaa-savedate-label {
  letter-spacing: 0.3em;
  text-transform: uppercase;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--maroon);
  margin: 0 0 0.6rem;
}

.amaa-date-big {
  font-size: clamp(1.3rem, 4.6vw, 1.75rem);
  font-weight: 700;
  margin: 0;
  color: var(--ink);
}

.amaa-city {
  margin: 0.35rem 0 0;
  font-size: 1rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 600;
}

.amaa-desc {
  text-align: center;
  font-size: 1rem;
  line-height: 1.6;
  padding: 1.4rem 1.5rem;
  color: #3a3630;
  border-bottom: 1px solid var(--line);
}

.amaa-desc strong { color: var(--maroon-deep); }

.amaa-programme-heading {
  text-align: center;
  padding: 1.5rem 1.25rem 0.5rem;
}

.amaa-programme-heading .amaa-eyebrow2 {
  letter-spacing: 0.3em;
  text-transform: uppercase;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--maroon);
  margin: 0;
}

.amaa-timeline {
  padding: 0.5rem 1.25rem 1.6rem;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.amaa-event {
  display: grid;
  grid-template-columns: 90px 1fr;
  gap: 0.9rem;
  padding: 0.95rem 0;
  border-bottom: 1px dashed var(--line);
  align-items: start;
}

.amaa-event:last-child { border-bottom: none; }

.amaa-time {
  font-weight: 700;
  color: var(--maroon);
  font-size: 0.92rem;
  line-height: 1.35;
  padding-top: 0.1rem;
}

.amaa-event-title {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink);
}

.amaa-event-venue {
  margin: 0.2rem 0 0;
  font-size: 0.92rem;
  color: #55503f;
  line-height: 1.5;
}

.amaa-note {
  background: var(--paper-deep);
  padding: 1.4rem 1.5rem;
  font-size: 0.96rem;
  line-height: 1.65;
  color: #3a3630;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.amaa-footer {
  text-align: center;
  padding: 1.5rem 1.25rem 1.8rem;
  background: linear-gradient(135deg, var(--maroon-deep) 0%, var(--maroon) 100%);
  color: #f4ead9;
}

.amaa-footer-label {
  letter-spacing: 0.24em;
  text-transform: uppercase;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--gold-light);
  margin: 0 0 0.5rem;
}

.amaa-footer a {
  color: #fdf6e6;
  font-weight: 700;
  font-size: 1.02rem;
  text-decoration: none;
  border-bottom: 2px solid var(--gold-light);
  padding-bottom: 2px;
}

.amaa-footer a:hover,
.amaa-footer a:focus {
  color: var(--gold-light);
  border-bottom-color: #fdf6e6;
}

@media (max-width: 480px) {
  .amaa-event {
    grid-template-columns: 1fr;
    gap: 0.25rem;
  }

  .amaa-time { padding-top: 0; }

  .amaa-portrait-frame img { width: 160px; }
}
</style>

<div class="amaa-poster" role="region" aria-label="A. M. A. Ayrookuzhiel 30th Death Anniversary Commemoration poster">

  <div class="amaa-band-top">
    <h1 class="amaa-name">A. M. A. Ayrookuzhiel</h1>
    <p class="amaa-sub">30th Death Anniversary Commemoration</p>
  </div>

  <div class="amaa-portrait-wrap">
    <div class="amaa-portrait-frame">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%20photo%20low%20resolution.png" alt="Photograph of Rev. Dr. A. M. A. Ayrookuzhiel" loading="lazy">
    </div>
  </div>
  <p class="amaa-portrait-caption">Rev. Dr. A. M. A. Ayrookuzhiel (1933–1996)</p>

  <div class="amaa-savedate">
    <p class="amaa-savedate-label">Save the Date</p>
    <p class="amaa-date-big">Sunday, 29 November 2026</p>
    <p class="amaa-city">Bengaluru</p>
  </div>

  <div class="amaa-desc">
    A commemoration of the life and work of<br>
    <strong>Rev. Dr. A. M. A. Ayrookuzhiel (1933–1996)</strong>
  </div>

  <div class="amaa-programme-heading">
    <p class="amaa-eyebrow2">Programme</p>
  </div>

  <div class="amaa-timeline">

    <div class="amaa-event">
      <div class="amaa-time">12:00 noon</div>
      <div>
        <p class="amaa-event-title">Memorial Service</p>
        <p class="amaa-event-venue">Wesley English Church, Fraser Town, Bengaluru</p>
      </div>
    </div>

    <div class="amaa-event">
      <div class="amaa-time">1:30 pm</div>
      <div>
        <p class="amaa-event-title">Lunch</p>
        <p class="amaa-event-venue">Wesley English Church, Fraser Town, Bengaluru</p>
      </div>
    </div>

    <div class="amaa-event">
      <div class="amaa-time">6:00 pm–7:30 pm</div>
      <div>
        <p class="amaa-event-title">Evening Commemoration Programme</p>
        <p class="amaa-event-venue">United Theological College<br>63, Millers Road, Benson Town, Bengaluru, Karnataka 560046</p>
      </div>
    </div>

    <div class="amaa-event">
      <div class="amaa-time">7:30 pm onwards</div>
      <div>
        <p class="amaa-event-title">Dinner</p>
        <p class="amaa-event-venue">United Theological College</p>
      </div>
    </div>

  </div>

  <div class="amaa-note">
    The programme will include a commemoration of A. M. A. Ayrookuzhiel's life and work, presentations on his academic, literary and social contributions, and an exhibition of selected works, documents and archival material.
  </div>

  <div class="amaa-footer">
    <p class="amaa-footer-label">More Information</p>
    <a href="https://sunilabraham.in/30/">sunilabraham.in/30</a>
  </div>

</div>
