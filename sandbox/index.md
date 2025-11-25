---
layout: default
title: Home
description: "Knowledge sharing and documentation portal of Sunil Abraham: notes, essays, and research on internet policy, technology and digital rights."
image: /assets/images/sunil-abraham-colour-nature.jpg
categories: [Project pages]
created: 2025-10-19
---

<style>
  /* ===========================
     Variables & global reset
     Mobile-first
     =========================== */
  :root{
    --tsap-primary: #0a2e57;
    --tsap-accent: #005cc5;
    --tsap-bg: #f4f6f8;
    --tsap-card-bg: #ffffff;
    --tsap-text: #2d3748;
    --tsap-text-light: #4a5568;
    --radius: 12px;
    --shadow: 0 6px 18px rgba(12, 16, 23, 0.06);
    --reading-max: 920px; /* inner readable width */
  }

  *,*::before,*::after{ box-sizing: border-box; }

  html,body{ margin:0; padding:0; font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
              color:var(--tsap-text); background: #fff; -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale; overflow-x:hidden; }

  /* Page wrapper: full width sections but inner constrained for readability */
  .tsap-section {
    width:100%;
    background:transparent;
    padding: 1rem 1rem;
  }

  .tsap-inner {
    margin: 0 auto;
    width:100%;
    max-width: var(--reading-max);
  }

  /* Hide theme title and breadcrumb on homepage only (preserve other pages) */
  main h1, main nav.breadcrumb { display:none !important; }

  /* ===========================
     Banner
     =========================== */
  .tsap-banner {
    width:100%;
    position:relative;
    overflow:hidden;
    background:#e6e9ec;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
  }
  .tsap-banner img.tsap-image { width:100%; height:auto; display:block; object-fit:cover; }
  .tsap-banner-hover-text{
    position:absolute;
    left:50%;
    top:50%;
    transform: translate(-50%,-50%);
    padding:6px 12px;
    font-size:1rem;
    background: rgba(0,0,0,0.62);
    color:#fff;
    border-radius:6px;
    opacity:0;
    transition:opacity .22s ease;
    pointer-events:none;
    z-index:2;
    white-space:nowrap;
  }
  .tsap-banner:hover .tsap-banner-hover-text{ opacity:1; }

  /* Responsive banner heights */
  @media (min-width: 900px){
    .tsap-banner img.tsap-image{ height:160px; }
  }
  @media (max-width: 899px){
    .tsap-banner img.tsap-image{ height:88px; }
    .tsap-banner-hover-text{ font-size:0.85rem; padding:5px 10px; }
  }

  /* ===========================
     Card style blocks
     =========================== */
  .tsap-card {
    background: var(--tsap-card-bg);
    border-radius: var(--radius);
    padding: 1.2rem;
    margin: 1rem 0;
    box-shadow: 0 2px 8px rgba(10, 20, 30, 0.04);
    border-left: 4px solid var(--tsap-primary);
  }

  .tsap-card h2{
    margin: 0 0 0.6rem 0;
    color: var(--tsap-primary);
    font-size:1.35rem;
  }

  .tsap-card p{ color: var(--tsap-text-light); margin-top:0.6rem; margin-bottom:0.75rem; line-height:1.6; }

  a { color: var(--tsap-accent); text-decoration:none; }
  a:hover{ text-decoration:underline; color: var(--tsap-primary); }

  /* Button */
  .tsap-btn{
    display:inline-block;
    background: var(--tsap-primary);
    color: #fff;
    padding: 0.5rem 0.9rem;
    border-radius: 6px;
    text-decoration:none;
    font-weight:600;
    margin-top:0.6rem;
  }
  .tsap-btn:hover{ background: var(--tsap-accent); box-shadow: 0 6px 18px rgba(0,92,197,0.14); }

  /* ===========================
     Intro / Nav grid
     =========================== */
  .tsap-intro { margin-bottom: 0.6rem; }
  .tsap-intro p { margin:0 0 0.9rem 0; color:var(--tsap-text-light); font-size:1.05rem; }
  .tsap-nav-grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap:0.6rem;
    margin-top:0.9rem;
  }
  .tsap-nav-item{
    display:block;
    background: #fff;
    border-radius:8px;
    padding:0.7rem;
    text-align:center;
    border:1px solid #e6e9ee;
    font-weight:600;
    color:var(--tsap-primary);
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    text-decoration:none;
  }
  .tsap-nav-item:hover{ background:var(--tsap-primary); color:#fff; transform:translateY(-2px); }

  /* ===========================
     Bio
     =========================== */
  .tsap-bio {
    display:flex;
    flex-direction:column;
    gap:1rem;
    align-items:center;
  }
  .tsap-bio-figure { width:100%; text-align:center; margin:0; }
  .tsap-bio-img { width:100%; max-width:520px; border-radius:8px; display:block; }

  /* ===========================
     Media / responsive iframe
     =========================== */
  .tsap-media {
    width:100%;
  }
  .tsap-media-embed {
    position:relative;
    width:100%;
    padding-bottom:56.25%;
    background:#000;
    border-radius:8px;
    overflow:hidden;
  }
  .tsap-media-embed iframe{ position:absolute; left:0; top:0; width:100%; height:100%; border:0; }

  .tsap-media-caption{
    margin-top:0.65rem;
    background:#fbfcfd;
    padding:0.6rem;
    border-radius:6px;
    border-left:4px solid var(--tsap-accent);
    color:var(--tsap-text-light);
    line-height:1.55;
  }

  /* ===========================
     Did you know list
     =========================== */
  .tsap-facts { list-style:none; padding:0; margin:0; }
  .tsap-facts li{ padding:0.6rem 0 0.8rem 2rem; border-bottom:1px solid #f1f3f5; position:relative; color:var(--tsap-text-light); }
  .tsap-facts li::before{ content:"💡"; position:absolute; left:0; top:0; font-size:1.1rem; }

  /* ===========================
     About / Licence
     =========================== */
  .tsap-about { background: linear-gradient(180deg, #f7f9fc, #ffffff); border-left:5px solid var(--tsap-primary); }

  /* ===========================
     Small screens tweaks
     =========================== */
  @media (max-width: 767px) {
    .tsap-inner{ padding:0 0.5rem; }
    .tsap-card{ padding:1rem; }
    .tsap-banner img.tsap-image{ height:84px; object-fit:cover; }
    .tsap-bio-img{ max-width:360px; }
    .tsap-btn{ width:100%; text-align:center; }
    .tsap-nav-grid{ grid-template-columns: repeat(2, 1fr); }
  }

  /* Desktop minor layout polish */
  @media (min-width: 900px){
    .tsap-inner{ padding:0 1.25rem; }
    .tsap-intro p{ font-size:1.08rem; }
    .tsap-card{ margin:1.25rem 0; }
    .tsap-nav-grid{ gap:1rem; }
  }

  /* ensure no overflow anywhere */
  img, iframe { max-width:100%; height:auto; display:block; }
  html,body{ -webkit-overflow-scrolling:touch; }
  a:focus, button:focus { outline:3px solid rgba(0,92,197,0.12); outline-offset:3px; }
</style>

<!-- ===========================
     PAGE START (single column)
     =========================== -->

<!-- Full width banner (section spans full width; inner content constrained) -->
<section class="tsap-section">
  <div class="tsap-inner">
    <div class="tsap-banner" role="img" aria-label="Graffiti-style banner for the Sunil Abraham Project showing colourful 1990s India technology icons like a rotary phone, wireless device, pendrive, laptop and communication tower on a brick wall.">
      <span class="tsap-banner-hover-text" aria-hidden="true"></span>
      <img class="tsap-image" src="/assets/images/tsap-welcome-banner.png" alt="Graffiti mural banner for the Sunil Abraham Project showing colourful 1990s India technology icons painted on a brick wall.">
    </div>
  </div>
</section>

<!-- Intro + navigation grid -->
<section class="tsap-section">
  <div class="tsap-inner">
    <div class="tsap-intro">
      <p><strong>Welcome</strong> to the knowledge sharing and documentation portal of <strong>Sunil Abraham</strong>. This space brings together notes, essays, research, and reflections on technology, policy, and society. It aims to make knowledge freely accessible, encourage collaborative learning, and preserve insights that might otherwise remain scattered or unpublished.</p>

      <p>The project reflects years of engagement with digital rights, open technology, and social research in India and beyond. It seeks to connect individual thought with public understanding, bridging ideas across disciplines and communities. Each page is designed for clarity, readability, and reuse, keeping the focus on substance rather than design.</p>

      <p>Whether you are a researcher, student, practitioner, or reader exploring questions of openness, equity, and digital transformation, this documentation offers a growing archive of material to study, share, and build upon.</p>
    </div>

    <nav class="tsap-nav-grid" aria-label="Quick links">
      <a class="tsap-nav-item" href="#featured-article">Featured Article</a>
      <a class="tsap-nav-item" href="#featured-media">Featured Media</a>
      <a class="tsap-nav-item" href="#sunil-abraham">Biography</a>
      <a class="tsap-nav-item" href="#did-you-know">Did you know?</a>
      <a class="tsap-nav-item" href="#about">About</a>
      <a class="tsap-nav-item" href="#licence">Licence</a>
    </nav>
  </div>
</section>

<!-- Featured article -->
<section id="featured-article" class="tsap-section">
  <div class="tsap-inner">
    <article class="tsap-card" aria-labelledby="fa-heading">
      <h2 id="fa-heading">Featured article</h2>

      <p><strong>Rev. Athanasius Mathen Abraham Ayrookuzhiel</strong> (1933–1996) was an Indian theologian, priest, and scholar whose work bridged faith, culture, and social justice. Educated in philosophy and theology in Pune, Rome, and Oxford, he combined pastoral life with a deep interest in the moral and social struggles of ordinary people. His ministry reflected a conviction that religion must respond to the realities of oppression and inequality.</p>

      <p>After returning to India, he joined the <a href="https://cisrs.in/">Christian Institute for the Study of Religion and Society</a> in Bangalore, where he became Associate Director. Working closely with theologian M. M. Thomas, he explored how Christian thought could engage with caste and class through the lived experiences of Dalit communities.</p>

      <p>Among his major works are <em>The Sacred in Popular Hinduism</em>, <em>Swami Anand Thirth: Untouchability, Gandhian Solution on Trial</em>, and <em>Essays on Dalits, Religion, and Liberation</em>.</p>

      <a class="tsap-btn" href="https://sunilabraham.in/amaa/">Read full article...</a>

      {% include back-to-top.html %}
    </article>
  </div>
</section>

<!-- Sunil biography -->
<section id="sunil-abraham" class="tsap-section">
  <div class="tsap-inner">
    <section class="tsap-card tsap-bio" aria-labelledby="bio-heading">
      <h2 id="bio-heading">Sunil Abraham</h2>

      <figure class="tsap-bio-figure">
        <img class="tsap-bio-img" src="https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/sunil-abraham-colour-nature.jpg?raw=true" alt="Illustration of Sunil Abraham in a grey shirt pointing upward, set against a colourful landscape.">
      </figure>

      <div>
        <p><strong>Sunil Abraham</strong> (IAST: Sunīl Ābrahām; born 17 June 1973) is an Indian internet researcher, public policy advocate, and social entrepreneur known for his work on digital rights, technology governance, and openness. He co-founded the Centre for Internet and Society (CIS) and Mahiti Infotech, and has advised governments and civil society on open standards and policy.</p>

        <a class="tsap-btn" href="https://sunilabraham.in/sunil/">Read full biography...</a>
      </div>

      {% include back-to-top.html %}
    </section>
  </div>
</section>

<!-- Featured media -->
<section id="featured-media" class="tsap-section">
  <div class="tsap-inner">
    <article class="tsap-card" aria-labelledby="fm-heading">
      <h2 id="fm-heading">Featured media</h2>

      <div class="tsap-media">
        <div class="tsap-media-embed" role="group" aria-label="Video: Aadhaar by Numbers — Sunil Abraham">
          <iframe src="https://www.youtube.com/embed/Y9uOBAqjIMg" title="Aadhaar by Numbers — Sunil Abraham" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>

        <div class="tsap-media-caption">
          <strong>Aadhaar by Numbers — Sunil Abraham</strong><br>
          This talk examines Aadhaar from a technical viewpoint: how biometrics function as identification and authentication tools, the UIDAI's openness claims, and alternative identity designs that aim to deliver the benefits of digital identity without the risks of centralised biometric databases.<br><br>
          Sunil <a href="https://x.com/sunil_abraham/status/788018356209197058">posted this video on 𝕏</a> (then known as Twitter) on 17 October 2016 with the note: "Dear <span style="color:var(--tsap-accent);">#FriendWithoutAadhaar</span> — If you have an hour to waste. Please watch this:". The tweet has remained pinned as the debate around Aadhaar continues to be important.
        </div>
      </div>

      {% include back-to-top.html %}
    </article>
  </div>
</section>

<!-- Did you know -->
<section id="did-you-know" class="tsap-section">
  <div class="tsap-inner">
    <article class="tsap-card" aria-labelledby="dyk-heading">
      <h2 id="dyk-heading">Did you know?</h2>

      <ul class="tsap-facts">
        <li>the concept of <a href="/amaa/edrl/">religious colonisation</a> was used by A. M. A. Ayrookuzhiel to describe how Dalit gods and myths were absorbed into a Brahmanical order.</li>
        <li>the movement <a href="/articles/students-for-peace/">Students for Peace</a> (1993) brought 5,000 students together on Bangalore's M. G. Road for a candlelight protest.</li>
        <li><a href="/publications/surveillance-project/">Aadhaar reverses the logic of transparency</a>, making citizens visible while keeping the state opaque.</li>
        <li>India's 2011 Intermediaries Guidelines require platforms to remove content within 36 hours of a complaint, creating a culture of over-compliance and silent censorship.</li>
        <li><a href="/publications/shreya-singhal-and-66a/">Shreya Singhal</a> (2015) shifted Indian doctrine from a 'tendency' test to an 'imminence' test for speech that incites violence.</li>
        <li><a href="/publications/intermediary-liability-law-needs-updating/">Intermediary liability</a> has been described as 'private censorship' because platforms decide what stays online without clear legal transparency.</li>
        <li><a href="/publications/artificial-intelligence-full-spectrum/">Artificial Intelligence: A Full-Spectrum Regulatory Challenge</a> (2019) rejects one-size-fits-all AI ethics and recommends context-specific regulation.</li>
      </ul>

      {% include back-to-top.html %}
    </article>
  </div>
</section>

<!-- About + Licence -->
<section id="about" class="tsap-section">
  <div class="tsap-inner">
    <aside class="tsap-card tsap-about" aria-labelledby="about-heading">
      <h2 id="about-heading">About</h2>

      <p>This project is a living documentation space for research, writing, and reflection. It is built to create, organise, and publish documentation in a structured yet flexible manner, encouraging open learning and collaboration.</p>

      <ul>
        <li>Create and maintain documentation — capture insights, notes, essays, and drafts across themes and disciplines.</li>
        <li>Make ideas accessible, referenceable and remixable.</li>
        <li>Support learning, synthesis and critical reflection.</li>
        <li>Enable collaboration and iterative development of ideas.</li>
      </ul>

      <hr style="border:0;border-top:1px solid #e9eef3;margin:1.25rem 0;">
      <h2 id="licence">Licence</h2>
      <p>All content is released under the <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution–ShareAlike 4.0 International</a> (CC BY-SA 4.0) licence, unless otherwise stated. You are free to share and adapt this material with proper attribution.</p>

      {% include back-to-top.html %}
    </aside>
  </div>
</section>

<!-- ===========================
     Banner greetings script (restored, safe)
     =========================== -->
<script>
document.addEventListener("DOMContentLoaded", () => {
  const firstGreeting = "[kn] ನಮಸ್ಕಾರ";
  const otherGreetings = [
    "[ar] السلام عليكم","[as] নমস্কাৰ","[bn] নমস্কার","[de] Hallo","[en] Hello",
    "[es] Hola","[fr] Bonjour","[gu] નમસ્તે","[he] שלום","[hi] नमस्ते",
    "[id] Halo","[it] Ciao","[ja] こんにちは","[ko] 안녕하세요","[ml] നമസ്കാരം",
    "[mr] नमस्कार","[pa] ਸਤ ਸ੍ਰੀ ਅਕਾਲ","[pt] Olá","[ru] Привет","[sa] स्वागतम्",
    "[ta] நமஸ்காரம்","[te] నమస్కారం","[tr] Merhaba","[ur] السلام عليكم","[zh] 你好"
  ];

  const banner = document.querySelector(".tsap-banner");
  const textEl = banner ? banner.querySelector(".tsap-banner-hover-text") : null;
  if (!banner || !textEl) return;

  textEl.textContent = firstGreeting;
  let interval, mobileTimer;

  function shuffle(arr){ let a = arr.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]];} return a; }

  function randomisePosition(){
    const rect = banner.getBoundingClientRect();
    const textW = textEl.offsetWidth;
    const textH = textEl.offsetHeight;
    const margin = 6;
    const maxX = Math.max(0, rect.width - textW - margin);
    const maxY = Math.max(0, rect.height - textH - margin);
    const x = Math.random() * Math.max(0, maxX) + margin/2;
    const y = Math.random() * Math.max(0, maxY) + margin/2;
    textEl.style.left = x + "px";
    textEl.style.top = y + "px";
    textEl.style.position = "absolute";
  }

  function startRotation(){
    textEl.style.opacity = "1";
    randomisePosition();
    const seq = [firstGreeting, ...shuffle(otherGreetings)];
    let i=0;
    interval = setInterval(()=>{ i=(i+1)%seq.length; textEl.textContent = seq[i]; randomisePosition(); }, 1400);
  }

  function stopRotation(){
    clearInterval(interval);
    textEl.textContent = firstGreeting;
    textEl.style.opacity = "0";
  }

  banner.addEventListener("mouseenter", startRotation);
  banner.addEventListener("mouseleave", stopRotation);

  banner.addEventListener("click", ()=>{
    stopRotation();
    startRotation();
    clearTimeout(mobileTimer);
    mobileTimer = setTimeout(stopRotation, 14000);
  });
});
</script>
