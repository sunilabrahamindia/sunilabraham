---
layout: default
title: Home
description: "Knowledge sharing and documentation portal of Sunil Abraham: notes, essays, and research on internet policy, technology and digital rights."
image: /assets/images/sunil-abraham-colour-nature.jpg
categories: [Project pages]
created: 2025-10-19
---

<style>
  /* --- GLOBAL LAYOUT & TYPOGRAPHY --- */
  :root {
    --tsap-primary: #0a2e57;
    --tsap-accent: #005cc5;
    --tsap-bg: #f4f6f8;
    --tsap-card-bg: #ffffff;
    --tsap-text: #2d3748;
    --tsap-text-light: #4a5568;
    --radius: 12px;
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
  }

  /* Reset & Base for the container */
  .tsap-container {
    width: 100%;
    max-width: 960px;
    margin: 0 auto;
    padding: 0 1rem;
    color: var(--tsap-text);
    line-height: 1.6;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    box-sizing: border-box;
  }

  /* Hide default Title/Breadcrumb from theme if present */
  main h1, main nav.breadcrumb { display: none !important; }

  /* Typography Overrides */
  .tsap-container h2 {
    color: var(--tsap-primary);
    font-weight: 700;
    font-size: 1.75rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid #edf2f7;
    padding-bottom: 0.5rem;
  }

  .tsap-container p {
    margin-bottom: 1.25rem;
    color: var(--tsap-text-light);
  }

  .tsap-container a {
    color: var(--tsap-accent);
    text-decoration: none;
    transition: color 0.2s;
  }
  
  .tsap-container a:hover {
    text-decoration: underline;
    color: var(--tsap-primary);
  }

  /* --- CARD COMPONENT --- */
  .tsap-card {
    background: var(--tsap-card-bg);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: var(--shadow);
    border: 1px solid #e2e8f0;
  }

  /* --- INTRO SECTION --- */
  .tsap-intro-text {
    font-size: 1.1rem;
    color: var(--tsap-text);
    margin-top: 1rem;
  }
  .tsap-intro-text strong {
    color: var(--tsap-primary);
  }

  /* --- NAVIGATION GRID (Replaces old List) --- */
  .tsap-nav-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 0.8rem;
    margin: 2rem 0;
  }
  
  .tsap-nav-item {
    background: #fff;
    border: 1px solid #cbd5e0;
    padding: 0.8rem;
    border-radius: 8px;
    text-align: center;
    font-weight: 600;
    color: var(--tsap-primary) !important;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    display: block;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }
  
  .tsap-nav-item:hover {
    background: var(--tsap-primary);
    color: #fff !important;
    text-decoration: none;
    transform: translateY(-2px);
  }

  /* --- FEATURED ARTICLE & BUTTONS --- */
  .tsap-btn {
    display: inline-block;
    background: var(--tsap-primary);
    color: #fff !important;
    padding: 0.6rem 1.2rem;
    border-radius: 6px;
    font-weight: 500;
    margin-top: 1rem;
    text-decoration: none !important;
    transition: background 0.2s;
  }
  .tsap-btn:hover {
    background: var(--tsap-accent);
    box-shadow: 0 4px 12px rgba(0, 92, 197, 0.2);
  }

  /* --- BIO SECTION (Flex) --- */
  .tsap-bio-wrapper {
    display: flex;
    flex-direction: row;
    gap: 2rem;
    align-items: flex-start;
  }
  .tsap-bio-img-container {
    flex: 0 0 200px; /* Fixed width on desktop */
  }
  .tsap-bio-img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: var(--shadow);
  }
  .tsap-bio-content {
    flex: 1;
  }

  /* --- MEDIA SECTION --- */
  .tsap-media-container {
    background: #000;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    margin-bottom: 1rem;
  }
  .tsap-media-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }
  .tsap-media-caption {
    font-size: 0.9rem;
    padding: 0.5rem;
    background: #f8f9fa;
    border-radius: 6px;
    border-left: 4px solid var(--tsap-accent);
  }

  /* --- DID YOU KNOW (Styled List) --- */
  .tsap-facts-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .tsap-facts-list li {
    position: relative;
    padding-left: 2rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid #f1f1f1;
    padding-bottom: 1rem;
  }
  .tsap-facts-list li::before {
    content: "💡";
    position: absolute;
    left: 0;
    top: 0;
    font-size: 1.2rem;
  }
  .tsap-facts-list li:last-child {
    border-bottom: none;
  }

  /* --- ABOUT SECTION --- */
  .tsap-about-card {
    background: linear-gradient(to bottom right, #f7f9fc, #ffffff);
    border-left: 5px solid var(--tsap-primary);
  }
  
  /* --- BANNER STYLES (Preserving function, improving container) --- */
  .tsap-banner {
    width: 100%;
    margin: 0 auto 1.5rem;
    border-radius: var(--radius);
    overflow: hidden;
    position: relative;
    box-shadow: var(--shadow);
    background: #ddd; /* Placeholder while loading */
  }
  .tsap-banner img.tsap-image {
    width: 100%;
    height: auto;
    display: block;
    pointer-events: none;
    object-fit: cover;
  }
  .tsap-banner-hover-text {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    padding: 6px 12px;
    font-size: 1rem;
    background: rgba(0, 0, 0, 0.65);
    color: #fff;
    border-radius: 4px;
    opacity: 0;
    transition: opacity 0.25s ease;
    text-align: center;
    white-space: nowrap;
    pointer-events: none;
    z-index: 2;
    backdrop-filter: blur(2px);
  }
  .tsap-banner:hover .tsap-banner-hover-text { opacity: 1; }

  /* --- RESPONSIVE DESIGN (MOBILE) --- */
  @media (min-width: 768px) {
     .tsap-banner img.tsap-image { height: 180px; }
  }

  @media (max-width: 767px) {
    .tsap-bio-wrapper {
      flex-direction: column; /* Stack image and text */
      align-items: center;
    }
    .tsap-bio-img-container {
      width: 100%;
      max-width: 300px;
      margin-bottom: 1.5rem;
    }
    .tsap-btn {
      display: block;
      text-align: center;
      width: 100%; /* Full width button on mobile */
      box-sizing: border-box;
    }
    .tsap-nav-grid {
      grid-template-columns: 1fr 1fr; /* 2 cols on mobile */
    }
    /* Banner height adjustment */
    .tsap-banner img.tsap-image { height: 80px; }
    .tsap-banner-hover-text { font-size: 0.8rem; }
  }
</style>

<div class="tsap-container">

  <div class="tsap-banner"
       role="img"
       aria-label="Graffiti-style banner for the Sunil Abraham Project showing colourful 1990s India technology icons like a rotary phone, wireless device, pendrive, laptop and communication tower on a brick wall.">
  <span class="tsap-banner-hover-text"></span>
    <img class="tsap-image"
         src="/assets/images/tsap-welcome-banner.png"
         alt="Graffiti mural banner for the Sunil Abraham Project showing colourful 1990s India technology icons like a rotary phone, wireless set, USB drive, laptop and communication tower painted on a brick wall background.">
  </div>

  <section class="tsap-intro">
    <div class="tsap-intro-text">
      **Welcome** to the knowledge sharing and documentation portal of **Sunil Abraham**. This space brings together notes, essays, research, and reflections on technology, policy, and society. It aims to make knowledge freely accessible, encourage collaborative learning, and preserve insights that might otherwise remain scattered or unpublished.
      
      <p>The project reflects years of engagement with digital rights, open technology, and social research in India and beyond. It seeks to connect individual thought with public understanding, bridging ideas across disciplines and communities. Each page is designed for clarity, readability, and reuse, keeping the focus on substance rather than design.</p>
      
      <p>Whether you are a researcher, student, practitioner, or reader exploring questions of openness, equity, and digital transformation, this documentation offers a growing archive of material to study, share, and build upon.</p>
    </div>

    <nav class="tsap-nav-grid">
      <a href="#featured-article" class="tsap-nav-item">Featured Article</a>
      <a href="#featured-media" class="tsap-nav-item">Featured Media</a>
      <a href="#sunil-abraham" class="tsap-nav-item">Biography</a>
      <a href="#did-you-know" class="tsap-nav-item">Did You Know?</a>
      <a href="#about" class="tsap-nav-item">About</a>
      <a href="#licence" class="tsap-nav-item">Licence</a>
    </nav>
  </section>

  <section id="featured-article" class="tsap-card">
    <h2>Featured article</h2>
    <div>
      **Rev. Athanasius Mathen Abraham Ayrookuzhiel** (1933–1996) was an Indian theologian, priest, and scholar whose work bridged faith, culture, and social justice. Educated in philosophy and theology in Pune, Rome, and Oxford, he combined pastoral life with a deep interest in the moral and social struggles of ordinary people. His ministry in the Church of England and later in India reflected a conviction that religion must respond to the realities of oppression and inequality.

      <p>After returning to India, he joined the <a href="https://cisrs.in/">Christian Institute for the Study of Religion and Society</a> in Bangalore, where he became Associate Director. Working closely with theologian M. M. Thomas, he explored how Christian thought could engage with caste and class through the lived experiences of Dalit communities. His research on folk religion, ritual, and oral traditions offered new ways of understanding theology as a form of cultural expression and resistance.</p>

      <p>Among his major works are <em>The Sacred in Popular Hinduism</em>, <em>Swami Anand Thirth: Untouchability, Gandhian Solution on Trial</em>, and the posthumous <em>Essays on Dalits, Religion, and Liberation</em>. Until his death in 1996, Ayrookuzhiel remained dedicated to a theology rooted in the struggles of the marginalised—a vision that continues to shape Indian Christian and social thought.</p>
    </div>
    <a href="https://sunilabraham.in/amaa/" class="tsap-btn">Read full article...</a>
    {% include back-to-top.html %}
  </section>

  <section id="sunil-abraham" class="tsap-card">
    <h2>Sunil Abraham</h2>
    <div class="tsap-bio-wrapper">
      
      <div class="tsap-bio-img-container">
        <img 
          src="https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/sunil-abraham-colour-nature.jpg?raw=true" 
          alt="Illustration of Sunil Abraham in a gray shirt pointing upward" 
          class="tsap-bio-img">
      </div>

      <div class="tsap-bio-content">
        **Sunil Abraham** (IAST: Sunīl Ābrahām; IPA: suːˈniːl ˈɑːbrəˌhɑːm, born 17 June 1973) is an Indian internet researcher, public policy advocate, and social entrepreneur known for his work at the intersection of technology, society, and governance.

        <p>Sunil is a co-founder and former executive director of the <a href="https://cis-india.org/">Centre for Internet and Society</a> (CIS), a Bangalore-based non-profit research organisation established in 2008 to explore the relationship between the internet and social change. CIS brings together scholars, technologists, and activists to study issues such as internet governance, privacy, accessibility, and freedom of expression.</p>

        <p>In 1998, he co-founded <a href="https://mahiti.org/">Mahiti Infotech</a>, a social enterprise designed to make technology affordable and effective for the voluntary sector through Free and Open Source Software (FOSS). Under his leadership, Mahiti has supported hundreds of civil society organisations with digital tools, training, and open technology solutions.</p>

        <p>His contributions extend to advising governments, UN agencies, and advocacy groups on open standards, internet policy, and digital rights. A frequent lecturer and writer, Sunil's work highlights issues of openness, equity, and accountability in technology. His lifelong mission remains to ensure that innovation strengthens democracy and social inclusion rather than deepening inequality.</p>

        <a href="https://sunilabraham.in/sunil/" class="tsap-btn">Read full biography...</a>
      </div>
    </div>
    {% include back-to-top.html %}
  </section>

  <section id="featured-media" class="tsap-card">
    <h2>Featured media</h2>
    <div class="tsap-media-container">
      <iframe 
        src="https://www.youtube.com/embed/Y9uOBAqjIMg" 
        title="Aadhaar by Numbers by Sunil Abraham"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
    <div class="tsap-media-caption">
      <strong>Aadhaar by Numbers — Sunil Abraham</strong><br>
      This talk explores Aadhaar from a technical angle. It examines how biometrics work as identification and authentication tools, looks at the UIDAI's claims of openness, and discusses alternative identity system designs that could offer the benefits of digital identity without the risks of centralised biometric databases.<br>
      <br>
      Sunil <a href="https://x.com/sunil_abraham/status/788018356209197058">posted this video on 𝕏</a> (<i>then known as Twitter</i>) on 17 October 2016 with the note: "Dear <span style="color:#005cc5;">#FriendWithoutAadhaar</span> — If you have an hour to waste. Please watch this:". It has remained pinned since then, as the debate around Aadhaar continues to be relevant and important.
    </div>
    {% include back-to-top.html %}
  </section>

  <section id="did-you-know" class="tsap-card">
    <h2>Did you know?</h2>
    <ul class="tsap-facts-list">
      <li>... that the concept of <a href="/amaa/edrl/">religious colonisation</a> was used by theologian <a href="/amaa">A. M. A. Ayrookuzhiel</a> to describe how Dalit gods and myths were absorbed into a Brahmanical order?</li>
      <li>... that the movement <a href="/articles/students-for-peace/">Students for Peace</a> (1993) brought together 5,000 students on Bangalore's M. G. Road for a candlelight protest promoting unity and non-violence after the Ayodhya and Bombay riots?</li>
      <li>... that <a href="/publications/surveillance-project/">Aadhaar reverses the logic of transparency</a> — making citizens visible to the state while keeping the state opaque?</li>
      <li>... that <a href="/publications/eavesdropping-on-the-freedom-of-expression-in-india/">India's 2011 Intermediaries Guidelines</a> require online platforms to remove content within 36 hours of a complaint, creating a culture of over-compliance and silent censorship?</li>
      <li>... that the <a href="/publications/shreya-singhal-and-66a/">Shreya Singhal judgment</a> (2015) marked a significant doctrinal shift in Indian law, moving from a 'tendency' test to an 'imminence' test when judging if speech incites violence?</li>
      <li>... that <a href="/publications/intermediary-liability-law-needs-updating/">intermediary liability law</a> has been described as a form of 'private censorship', since platforms can decide what stays online without clear legal transparency requirements?</li>
      <li>... that the policy brief <a href="/publications/artificial-intelligence-full-spectrum/">Artificial Intelligence: A Full-Spectrum Regulatory Challenge</a> (2019) rejects one-size-fits-all AI ethics and instead proposes context-specific regulation based on who uses the technology and the harm it can cause?</li>
    </ul>
    {% include back-to-top.html %}
  </section>

  <section id="about" class="tsap-card tsap-about-card">
    <h2>About</h2>
    <p>This project serves as a living documentation space for research, writing, and reflection.<br>
    This is built to create, organise, and publish documentation in a structured yet flexible manner, enabling continuous learning and open exchange of ideas.</p>
    
    <p>It aims to:</p>
    <ul>
      <li>Create and maintain documentation — capture insights, notes, essays, and drafts across themes and disciplines.</li>
      <li>Encourage knowledge sharing — make ideas accessible, referenceable, and adaptable for wider audiences.</li>
      <li>Support learning and reflection — develop patterns of learning, synthesis, and critical thought through open writing.</li>
      <li>Enable collaboration and contribution — allow others to engage with, remix, and build upon existing materials.</li>
      <li>Host brainstorming and ideation — serve as a space for developing and refining emerging ideas and projects.</li>
    </ul>
    <p>This documentation evolves over time, not as a static archive, but as a continuous process of thinking, writing, and sharing.</p>

    <hr style="border: 0; border-top: 1px solid #ddd; margin: 2rem 0;">

    <h2 id="licence" style="margin-top:0;">Licence</h2>
    <p>All content are released under the <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution–ShareAlike 4.0 International</a> (CC BY-SA 4.0) licence, unless otherwise stated. You are free to share and adapt this material with proper attribution.</p>
    
    {% include back-to-top.html %}
  </section>

</div> <script>
document.addEventListener("DOMContentLoaded", () => {

  /* 1) Fixed first entry + remaining greetings */
  const firstGreeting = "[kn] ನಮಸ್ಕಾರ";  // always first

  const otherGreetings = [
    "[ar] السلام عليكم",
    "[as] নমস্কাৰ",
    "[bn] নমস্কার",
    "[de] Hallo",
    "[en] Hello",
    "[es] Hola",
    "[fr] Bonjour",
    "[gu] નમસ્તે",
    "[he] שלום",
    "[hi] नमस्ते",
    "[id] Halo",
    "[it] Ciao",
    "[ja] こんにちは",
    "[ko] 안녕하세요",
    "[ml] നമസ്കാരം",
    "[mr] नमस्कार",
    "[pa] ਸਤ ਸ੍ਰੀ ਅਕਾਲ",
    "[pt] Olá",
    "[ru] Привет",
    "[sa] स्वागतम्",
    "[ta] நமஸ்காரம்",
    "[te] నమస్కారం",
    "[tr] Merhaba",
    "[ur] السلام عليكم",
    "[zh] 你好"
  ];

  const banner = document.querySelector(".tsap-banner");
  const textEl = document.querySelector(".tsap-banner-hover-text");
  if (!banner || !textEl) return;

  /* preload Kannada */
  textEl.textContent = firstGreeting;

  let interval;
  let mobileTimer;

  /* Fisher–Yates shuffle */
  function shuffle(array) {
    let a = array.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  /* Randomised safe placement */
  function randomisePosition() {
    const rect = banner.getBoundingClientRect();

    const textW = textEl.offsetWidth;
    const textH = textEl.offsetHeight;

    const margin = 4;
    const maxX = Math.max(0, rect.width  - textW - margin);
    const maxY = Math.max(0, rect.height - textH - margin);

    const x = Math.random() * maxX + margin / 2;
    const y = Math.random() * maxY + margin / 2;

    textEl.style.left = `${x}px`;
    textEl.style.top  = `${y}px`;
  }

  function startRotation() {

    textEl.style.opacity = "1";
    randomisePosition();

    /* Create new random order each time */
    const sequence = [firstGreeting, ...shuffle(otherGreetings)];

    let i = 0;

    interval = setInterval(() => {
      i = (i + 1) % sequence.length;
      textEl.textContent = sequence[i];
      randomisePosition();
    }, 1400);
  }

  function stopRotation() {
    clearInterval(interval);
    textEl.textContent = firstGreeting;  // reset to Kannada
    textEl.style.opacity = "0";
  }

  /* Desktop hover */
  banner.addEventListener("mouseenter", startRotation);
  banner.addEventListener("mouseleave", stopRotation);

  /* Mobile tap */
  banner.addEventListener("click", () => {
    stopRotation();
    startRotation();

    clearTimeout(mobileTimer);
    mobileTimer = setTimeout(stopRotation, 14000); // 14s
  });

});
</script>
