---
layout: default
title: Portal:A. M. A. Ayrookuzhiel
permalink: /amaa/portal/
categories: [A. M. A. Ayrookuzhiel, Portals, Project pages]
description: Portal page for the life, work, and legacy of Rev. A. M. A. Ayrookuzhiel, bringing together his biography, writings, research contributions, and related materials.
---
{% include under-construction.html %}

<div class="amaa-banner">
  <img 
    src="/amaa/images/amaa-portal-banner.png" 
    alt="Portal banner for A. M. A. Ayrookuzhiel">
  <div class="amaa-banner-text">
    Portal: A. M. A. Ayrookuzhiel
  </div>
</div>

The **A. M. A. Ayrookuzhiel Portal** brings together all material related to the life and work of Rev. A. M. A. Ayrookuzhiel. It serves as a single place to explore his biography, writings, research contributions, and the wider conversations his work shaped. This page links to primary texts, related articles, family archives, and other resources that help readers understand his ideas and the world he engaged with.

## Biography

<!-- Collapsible quick facts -->
<div class="collapse-box" aria-hidden="false">
  <div class="collapse-header" role="button" tabindex="0" aria-expanded="false" aria-controls="bio-facts">
    <span class="collapse-text">Show biography details</span>
    <span class="arrow" aria-hidden="true">▾</span>
  </div>

  <div id="bio-facts" class="collapse-content" aria-hidden="true">
    <dl class="bio-details">
      <dt>🧍 Full name:</dt>
      <dd>Athanasius Mathen Abraham Ayrookuzhiel</dd>

      <dt>📆 Born:</dt>
      <dd>1933, Chengannur, Kerala, India</dd>

      <dt>✝️ Died:</dt>
      <dd>29 November 1996</dd>

      <dt>🎓 Roles:</dt>
      <dd>Theologian, priest, scholar</dd>

      <dt>🏛️ Institutions:</dt>
      <dd>
        <ul>
          <li>CISRS, Bangalore</li>
          <li>St Paul High Anglican Church, Wokingham</li>
          <li>Order of Ordine Imitationis Christi</li>
        </ul>
      </dd>

      <dt>📘 Major publications:</dt>
      <dd>
        <ul>
          <li><em>The Sacred in Popular Hinduism</em> (1983)</li>
          <li><em>Swami Anand Thirth</em> (1987)</li>
          <li><em>The Dalit Desiyata</em> (1990)</li>
          <li><em>Dalit Kavithakal</em> (1992)</li>
          <li><em>Dalit Sahityam</em> (1995)</li>
          <li><em>Essays on Dalits, Religion and Liberation</em> (2006)</li>
        </ul>
      </dd>

      <dt>👰 Spouse:</dt>
      <dd>Ponnamma Thekedath</dd>

      <dt>👥 Children:</dt>
      <dd>
        <ul>
          <li>Sunil Abraham (born 17 June 1973)</li>
          <li>Matthew Abraham</li>
          <li>Jacob Abraham</li>
        </ul>
      </dd>
    </dl>
  </div>
</div>

<!-- Sticky-note summary -->
<div class="bio-note-card" role="region" aria-label="Short biography summary">
  <div class="bio-note-pin" aria-hidden="true">📌</div>
  <p>
    Rev. A. M. A. Ayrookuzhiel (1933–1996) was a theologian who tried to bring faith closer to
    the everyday struggles of marginalised communities. At CISRS in Bangalore he helped shape
    early Dalit Theology by drawing on stories, fieldwork and local practice rather than abstract
    theory. His writing and teaching continue to influence debates on justice, culture and belief.
  </p>
  <a href="/amaa/" class="bio-note-button">Read full biography →</a>
</div>

## Major Works
### Essays on Dalits, Religion and Liberation (2006)

<div class="bio-note-card" role="region" aria-label="Summary of the book 'Essays on Dalits, Religion and Liberation'">
  <div class="bio-note-pin" aria-hidden="true">📌</div>
  <p>
    <strong>Essays on Dalits, Religion and Liberation</strong> gathers A. M. A. Ayrookuzhiel's most important writings on caste, culture and faith. Across these essays he traces how religion has shaped Dalit life — at times as a tool of control, and at other times as a source of resilience and creativity. Drawing on stories, fieldwork and lived experience, the book reflects his lifelong effort to ground theology in the struggles and hopes of the oppressed.
  </p>
  <a href="/amaa/books/essays-on-dalits-religion-and-liberation/" class="bio-note-button">See full entry →</a>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.collapse-header');
  if (!header) return;

  const content = document.getElementById(header.getAttribute('aria-controls'));
  const textSpan = header.querySelector('.collapse-text');
  const arrow = header.querySelector('.arrow');

  function setState(isOpen) {
    header.setAttribute('aria-expanded', String(isOpen));
    content.setAttribute('aria-hidden', String(!isOpen));
    header.classList.toggle('open', isOpen);
    content.classList.toggle('open', isOpen);
    if (isOpen) {
      textSpan.textContent = 'Hide biography details';
      arrow.textContent = '▴';
    } else {
      textSpan.textContent = 'Show biography details';
      arrow.textContent = '▾';
    }
  }

  // initialise (ensure consistent state)
  setState(false);

  function toggle() {
    setState(header.getAttribute('aria-expanded') === 'false');
  }

  header.addEventListener('click', toggle);
  header.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {
      e.preventDefault();
      toggle();
    }
  });
});
</script>

<style>
/* Banner container */
.amaa-banner {
  position: relative;
  width: 100%;
  max-width: 100%;
  margin: 0 auto 1.5rem;
}

/* Banner image */
.amaa-banner img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 6px;
  object-fit: cover;
  border: 2px solid rgba(0,0,0,0.35);
}

/* Banner text */
.amaa-banner-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #fff;
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  padding: 0.5rem 1rem;
  max-width: 90%;
  background: rgba(0,0,0,0.35);
  border-radius: 6px;
  text-shadow: 0 0 10px rgba(0,0,0,0.7);
  white-space: nowrap; 
}

/* Compact height on desktop, without clipping the border */
@media (min-width: 900px) {
  .amaa-banner {
    max-height: 150px;
  }
  .amaa-banner img {
    height: 150px;
    object-fit: cover;
  }
}

/* Keep banner title in a single line on mobile */
@media (max-width: 600px) {
  .amaa-banner-text {
    font-size: 1.25rem;
    padding: 0.35rem 0.6rem;
  }
}
/* Sticky-note biography card */
.bio-note-card {
  background: #fff8dc;
  border: 1px solid #e1d4a8;
  border-radius: 12px;
  padding: 1.2rem 1.4rem;
  max-width: 720px;
  margin: 1.4rem auto;
  box-shadow: 0 3px 6px rgba(0,0,0,0.08);
  position: relative;
  font-size: 0.97rem;
  line-height: 1.55;
  color: #3b3b3b;
}

.bio-note-pin { position: absolute; top: -12px; left: 18px; font-size: 1.4rem; }

.bio-note-card p { margin-bottom: 1rem; }

.bio-note-button {
  display: inline-block;
  margin-top: 0.3rem;
  padding: 0.4rem 0.8rem;
  background: #f4e5a6;
  border: 1px solid #d5c78b;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  color: #4a3f2b;
  transition: background 0.2s ease, box-shadow 0.2s ease;
}
.bio-note-button:hover { background: #f0d98e; box-shadow: 0 2px 4px rgba(0,0,0,0.15); }

/* Collapsible wrapper — match sticky-note card width & feel */
.collapse-box {
  max-width: 720px;
  margin: 1.4rem auto;                 /* same spacing as sticky-note */
  background: #fff;                    /* clean card background */
  border: 1px solid #d8e2f0;           /* light border (same family) */
  border-radius: 12px;                 /* same round corners as sticky-note */
  box-shadow: 0 3px 6px rgba(0,0,0,0.08); /* same soft shadow */
  overflow: hidden;                    /* ensures rounded corners look clean */
}

/* Header */
.collapse-header {
  background: #eef3fa;
  padding: 0.7rem 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #1b2a49;
  user-select: none;
  border-bottom: 1px solid #d8e2f0;   /* clean separation */
  border-radius: 0;                    /* header must not round (wrapper handles it) */
}

.collapse-header:hover { background: #e7edf7; }

.collapse-header:focus {
  outline: 3px solid rgba(50,120,214,0.18);
  outline-offset: 2px;
}

/* Arrow */
.collapse-header .arrow {
  transition: transform 0.25s ease;
}

/* Content panel */
.collapse-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s ease;
  background: #f9fbfe;   /* same soft colour as earlier */
}

/* When opened */
.collapse-content.open {
  max-height: 2000px;
}
  
/* Bio details */
.bio-details {
  background: #f9fbfe;
  padding: 1.2rem 1.4rem;
  font-size: 0.96rem;
  line-height: 1.5;
  color: #333;
}
.bio-details dt { font-weight: 600; color: #1b2a49; margin-top: 0.7rem; }
.bio-details dd { margin: 0 0 0.3rem 0.3rem; color: #555; }
.bio-details ul { margin: 0.2rem 0 0.6rem 0.6rem; padding-left: 0; }
.bio-details ul li { margin-bottom: 0.2rem; }

</style>
