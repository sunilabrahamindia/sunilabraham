---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

{% include under-construction.html %}

<style>
  :root {
    --amaa-accent: #2a4b7c;       /* Deep Royal Blue */
    --amaa-accent-light: #eef3fa; /* Light Blue wash */
    --amaa-bg-card: #ffffff;
    --amaa-text-main: #2c3e50;
    --amaa-text-muted: #5a6b7c;
    --amaa-border: #dce4ec;
    --amaa-radius: 8px;
  }

  /* Base typography tweaks for this portal */
  .amaa-portal-content {
    color: var(--amaa-text-main);
    line-height: 1.7;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  }
  
  /* --- Banner Section --- */
  .amaa-banner {
    position: relative;
    width: 100%;
    border-radius: var(--amaa-radius);
    overflow: hidden;
    margin-bottom: 2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    background: #000;
  }

  .amaa-banner img {
    width: 100%;
    height: 200px; /* Fixed height for consistency */
    object-fit: cover;
    object-position: center 20%; /* Focus on faces if present */
    display: block;
    opacity: 0.9;
  }

  .amaa-banner-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
    padding: 2rem 1.5rem 1rem;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
  }

  .amaa-banner-title {
    color: #fff;
    font-size: 1.8rem;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    margin: 0;
  }

  /* Flower Trigger in Banner */
  .amaa-flower-btn {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    user-select: none;
  }
  
  .amaa-flower-btn:hover {
    background: rgba(255, 255, 255, 0.4);
    transform: scale(1.1) rotate(15deg);
  }

  /* --- Intro Text --- */
  .amaa-intro {
    font-size: 1.1rem;
    color: var(--amaa-text-main);
    max-width: 800px;
    margin: 0 auto 2rem;
    border-bottom: 1px solid var(--amaa-border);
    padding-bottom: 1.5rem;
  }

  /* --- Feature Cards (Replaces Sticky Notes) --- */
  .feature-card {
    background: var(--amaa-bg-card);
    border: 1px solid var(--amaa-border);
    border-left: 5px solid var(--amaa-accent);
    border-radius: var(--amaa-radius);
    padding: 1.5rem;
    margin: 1.5rem auto;
    max-width: 800px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    transition: transform 0.2s ease;
  }

  .feature-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }

  .feature-card h3 {
    margin-top: 0;
    color: var(--amaa-accent);
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .feature-action {
    display: inline-block;
    margin-top: 1rem;
    font-weight: 600;
    color: var(--amaa-accent);
    text-decoration: none;
    border-bottom: 2px solid transparent;
    transition: border-color 0.2s;
  }
  
  .feature-action:hover {
    border-bottom-color: var(--amaa-accent);
  }

  /* --- Collapsible Bio Section --- */
  .collapse-box {
    max-width: 800px;
    margin: 0 auto 2rem;
    border: 1px solid var(--amaa-border);
    border-radius: var(--amaa-radius);
    overflow: hidden;
    background: #fff;
  }

  .collapse-header {
    background: var(--amaa-accent-light);
    padding: 1rem 1.5rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    color: var(--amaa-accent);
    transition: background 0.2s;
  }

  .collapse-header:hover {
    background: #e2eaf6;
  }

  .collapse-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s cubic-bezier(0, 1, 0, 1);
    background: #fff;
  }

  .collapse-content.open {
    max-height: 2000px; /* Sufficiently large value */
    transition: max-height 0.4s ease-in-out;
  }

  .bio-grid {
    padding: 1.5rem;
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  @media (min-width: 600px) {
    .bio-grid {
      grid-template-columns: 160px 1fr;
    }
  }

  .bio-label {
    font-weight: 600;
    color: var(--amaa-text-muted);
    margin: 0;
  }

  .bio-data {
    margin: 0;
    color: var(--amaa-text-main);
  }

  .bio-data ul {
    margin: 0;
    padding-left: 1.2rem;
  }

  /* --- Gallery --- */
  .gallery-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 800px;
    margin: 2rem auto 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--amaa-border);
  }
  
  .gallery-header h2 {
    margin: 0;
    color: var(--amaa-text-main);
  }

  .amaa-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1rem;
    max-width: 800px;
    margin: 0 auto 3rem;
  }

  .gallery-item {
    background: #fff;
    border: 1px solid var(--amaa-border);
    border-radius: var(--amaa-radius);
    overflow: hidden;
    transition: transform 0.2s;
  }

  .gallery-item:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }

  .gallery-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    object-position: top;
    display: block;
  }

  .gallery-item figcaption {
    padding: 0.8rem;
    font-size: 0.85rem;
    text-align: center;
    background: #fcfcfc;
    border-top: 1px solid var(--amaa-border);
    color: var(--amaa-text-muted);
  }

  /* --- Flower Animation --- */
  .floating-flower {
    position: fixed; /* Fixed so it doesn't affect document flow */
    font-size: 1.8rem;
    pointer-events: none;
    z-index: 9999;
    animation: flowerFloat 6s ease-out forwards;
  }

  @keyframes flowerFloat {
    0% { transform: translate(-50%, -50%) scale(0.5); opacity: 0; }
    10% { opacity: 1; }
    100% {
      transform: translate(
        calc(-50% + var(--rand-x) * 100vw),
        calc(-50% + var(--rand-y) * 100vh)
      ) rotate(720deg) scale(1.5);
      opacity: 0;
    }
  }
</style>

<div class="amaa-portal-content">

  <div class="amaa-banner">
    <img src="/amaa/images/amaa-portal-banner.png" alt="Portal banner for A. M. A. Ayrookuzhiel">
    <div class="amaa-banner-overlay">
      <h1 class="amaa-banner-title">Portal: A. M. A. Ayrookuzhiel</h1>
      <div class="amaa-flower-btn" role="button" tabindex="0" aria-label="Release flowers">
        🌼
      </div>
    </div>
  </div>

  <div class="amaa-intro">
    <p>
      The <strong>A. M. A. Ayrookuzhiel Portal</strong> serves as a comprehensive digital archive dedicated to the life and work of Rev. A. M. A. Ayrookuzhiel. It functions as a central hub for exploring his biography, theological writings, research contributions, and the broader conversations his work influenced. 
    </p>
    <p>
      This page connects readers to primary texts, family archives, and scholarly resources, offering a window into his ideas and the social realities he engaged with throughout his life.
    </p>
  </div>

  <div class="collapse-box" aria-hidden="false">
    <div class="collapse-header" role="button" tabindex="0" aria-expanded="false" aria-controls="bio-facts">
      <span> Biography Details</span>
      <span class="arrow" aria-hidden="true">▾</span>
    </div>

    <div id="bio-facts" class="collapse-content" aria-hidden="true">
      <div class="bio-grid">
        <p class="bio-label">Full Name</p>
        <p class="bio-data">Athanasius Mathen Abraham Ayrookuzhiel</p>

        <p class="bio-label">Born</p>
        <p class="bio-data">1933, Chengannur, Kerala, India</p>

        <p class="bio-label">Died</p>
        <p class="bio-data">29 November 1996</p>

        <p class="bio-label">Roles</p>
        <p class="bio-data">Theologian, Priest, Scholar</p>

        <p class="bio-label">Institutions</p>
        <div class="bio-data">
          <ul>
            <li>CISRS, Bangalore</li>
            <li>St Paul High Anglican Church, Wokingham</li>
            <li>Order of Ordine Imitationis Christi</li>
          </ul>
        </div>

        <p class="bio-label">Key Works</p>
        <div class="bio-data">
          <ul>
            <li><em>The Sacred in Popular Hinduism</em> (1983)</li>
            <li><em>Swami Anand Thirth</em> (1987)</li>
            <li><em>The Dalit Desiyata</em> (1990)</li>
            <li><em>Dalit Kavithakal</em> (1992)</li>
            <li><em>Dalit Sahityam</em> (1995)</li>
            <li><em>Essays on Dalits, Religion and Liberation</em> (2006)</li>
          </ul>
        </div>

        <p class="bio-label">Spouse</p>
        <p class="bio-data">Ponnamma Thekedath</p>

        <p class="bio-label">Children</p>
        <div class="bio-data">
          <ul>
            <li>Sunil Abraham (born 17 June 1973)</li>
            <li>Matthew Abraham</li>
            <li>Jacob Abraham</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="feature-card">
    <h3>Biographical Overview</h3>
    <p>
      Rev. A. M. A. Ayrookuzhiel (1933–1996) was a pioneering theologian who sought to bridge the gap between academic faith and the lived struggles of marginalised communities. During his tenure at CISRS in Bangalore, he was instrumental in shaping early Dalit Theology. He emphasised the importance of oral histories, field research, and local religious practices over abstract theory. His legacy continues to inform contemporary debates regarding justice, culture, and belief in India.
    </p>
    <a href="/amaa/" class="feature-action">Read full biography →</a>
  </div>

  <div class="feature-card">
    <h3>Featured Work: Essays on Dalits, Religion and Liberation</h3>
    <p>
      This volume compiles Ayrookuzhiel's most significant writings on the intersection of caste, culture, and faith. Through these essays, he analyses how religion has historically influenced Dalit life—functioning at times as an instrument of suppression and at others as a wellspring of resilience. Grounded in extensive fieldwork, this book represents his lifelong commitment to a theology rooted in the hopes and hardships of the oppressed.
    </p>
    <a href="/amaa/edrl" class="feature-action">View publication details →</a>
  </div>

  <div class="gallery-header">
    <h2>Gallery</h2>
    <div class="amaa-flower-btn" role="button" tabindex="0" aria-label="Release flowers">
      🌺
    </div>
  </div>

  <div class="amaa-gallery">
    <figure class="gallery-item">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%2004.jpeg" alt="Studio portrait of a young man in a suit, smiling warmly at the camera.">
      <figcaption>Early studio portrait</figcaption>
    </figure>

    <figure class="gallery-item">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%2001.jpeg" alt="A young man in graduation robes and cap, standing formally.">
      <figcaption>Graduation portrait</figcaption>
    </figure>

    <figure class="gallery-item">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%2006.jpeg" alt="A man in a suit standing beside a woman in a wedding sari.">
      <figcaption>Wedding portrait</figcaption>
    </figure>
    
    <figure class="gallery-item">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%2002.jpeg" alt="Indoor scene with a man leaning forward, a woman behind him, and another man with a long beard.">
      <figcaption>Early ministry gathering</figcaption>
    </figure>

    <figure class="gallery-item">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%2005.jpeg" alt="Old family group photograph with adults and children.">
      <figcaption>Family group photograph</figcaption>
    </figure>

    <figure class="gallery-item">
      <img src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%20photo%20low%20resolution.png" alt="Illustration-style black-and-white portrait of a man wearing glasses.">
      <figcaption>Illustrated portrait</figcaption>
    </figure>
  </div>

</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  /* Accordion Logic */
  const header = document.querySelector('.collapse-header');
  const content = document.getElementById('bio-facts');
  const arrow = header.querySelector('.arrow');
  
  // Set initial state
  let isOpen = false;

  function toggleBio() {
    isOpen = !isOpen;
    header.setAttribute('aria-expanded', String(isOpen));
    content.setAttribute('aria-hidden', String(!isOpen));
    
    if (isOpen) {
      content.classList.add('open');
      arrow.textContent = '▴';
      arrow.style.transform = 'rotate(180deg)'; // Smooth rotation via CSS
    } else {
      content.classList.remove('open');
      arrow.textContent = '▾';
      arrow.style.transform = 'rotate(0deg)';
    }
  }

  if (header) {
    header.addEventListener('click', toggleBio);
    header.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleBio();
      }
    });
  }

  /* Flower Logic */
  const triggers = document.querySelectorAll('.amaa-flower-btn');
  const flowers = ["🌸","🌺","🌼","🌷","🌻","💐","🌹","🥀","💮","🌿","🍃"];

  function spawnFlower(x, y) {
    const el = document.createElement('div');
    el.className = 'floating-flower';
    el.textContent = flowers[Math.floor(Math.random() * flowers.length)];
    
    // Start position (relative to viewport)
    el.style.left = x + 'px';
    el.style.top = y + 'px';
    
    // Random trajectory
    el.style.setProperty('--rand-x', (Math.random() - 0.5) * 2); // -1 to 1
    el.style.setProperty('--rand-y', (Math.random() - 0.5) * 2); // -1 to 1
    
    document.body.appendChild(el);
    
    // Cleanup
    setTimeout(() => el.remove(), 6000);
  }

  function burst(e) {
    // Get click coordinates or center of screen if triggered via keyboard
    let startX = window.innerWidth / 2;
    let startY = window.innerHeight / 2;

    if (e.type === 'click') {
      startX = e.clientX;
      startY = e.clientY;
    } else {
      // If keyboard, find the button's position
      const rect = e.target.getBoundingClientRect();
      startX = rect.left + rect.width / 2;
      startY = rect.top + rect.height / 2;
    }

    for (let i = 0; i < 30; i++) {
      setTimeout(() => spawnFlower(startX, startY), i * 50);
    }
  }

  triggers.forEach(btn => {
    btn.addEventListener('click', burst);
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        burst(e);
      }
    });
  });
});
</script>
