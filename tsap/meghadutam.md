---
layout: default
title: "Meghadutam"
description: "Meghadutam is a monsoon content enrichment event on The Sunil Abraham Project. Inspired by Kalidasa's Meghadutam, it emphasises content excellence rather than article count."
permalink: /meghadutam/
categories: [Project pages, TSAP Events and Rituals]
created: 2026-06-20
---

<style>
  /* ============================================================
     MEGHADUTAM 2026 — TSAP Hero Banner
     Monsoon atmosphere, Rajput/Pahari miniature inspiration
     Self-contained: HTML + CSS + inline SVG only
     ============================================================ */

  :root {
    /* Monsoon palette */
    --mg-sky-deep:      #0b1220;
    --mg-sky-mid:       #1a2540;
    --mg-cloud-dark:    #1e2d4a;
    --mg-cloud-mid:     #2e3f5e;
    --mg-cloud-light:   #3d5275;
    --mg-cloud-wisp:    #4a6080;
    --mg-horizon:       #0f3020;
    --mg-green-deep:    #0d2b18;
    --mg-green-mid:     #1a4226;
    --mg-green-bright:  #2a6338;
    --mg-rain:          rgba(180, 210, 230, 0.18);
    --mg-lightning:     #c8dff5;
    --mg-gold:          #c8a84b;
    --mg-gold-muted:    #9e7e36;
    --mg-text-bright:   #e8e0d0;
    --mg-text-muted:    #a09880;
    --mg-border-gold:   rgba(200, 168, 75, 0.35);
    --mg-border-subtle: rgba(180, 200, 220, 0.12);

    /* Type */
    --font-display: 'Georgia', 'Palatino Linotype', 'Book Antiqua', serif;
    --font-body:    'Georgia', serif;

    /* Fluid type */
    --text-xs:   clamp(0.75rem,  0.7rem  + 0.25vw, 0.875rem);
    --text-sm:   clamp(0.875rem, 0.8rem  + 0.35vw, 1rem);
    --text-base: clamp(1rem,     0.95rem + 0.25vw, 1.125rem);
    --text-lg:   clamp(1.125rem, 1rem    + 0.75vw, 1.5rem);
    --text-xl:   clamp(1.5rem,   1.2rem  + 1.25vw, 2.25rem);
    --text-2xl:  clamp(2rem,     1.2rem  + 2.5vw,  3.5rem);
    --text-3xl:  clamp(2.5rem,   1rem    + 4vw,    5rem);
  }

  /* Reset for banner context */
  .mg-banner *, .mg-banner *::before, .mg-banner *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  /* ── Outer wrapper ─────────────────────────────────────────── */
  .mg-banner {
    position: relative;
    width: 100%;
    min-height: clamp(280px, 35vw, 420px);
    overflow: hidden;
    background-color: var(--mg-sky-deep);
    font-family: var(--font-body);
    -webkit-font-smoothing: antialiased;
    isolation: isolate;
  }

  /* ── Sky gradient ──────────────────────────────────────────── */
  .mg-sky {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to bottom,
      #060c17 0%,
      #0b1528 18%,
      #111e3a 38%,
      #192945 58%,
      #1e3245 75%,
      #1a3838 88%,
      #0f2b22 100%
    );
    z-index: 0;
  }

  /* ── Star layer (very subtle) ──────────────────────────────── */
  .mg-stars {
    position: absolute;
    inset: 0;
    z-index: 1;
    opacity: 0.5;
  }

  /* ── SVG cloud scene ───────────────────────────────────────── */
  .mg-cloudscape {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
  }

  /* ── Rain overlay ──────────────────────────────────────────── */
  .mg-rain-layer {
    position: absolute;
    inset: 0;
    z-index: 6;
    pointer-events: none;
    overflow: hidden;
  }

  .mg-rain-layer svg {
    width: 100%;
    height: 100%;
  }

  /* ── Ground / landscape ────────────────────────────────────── */
  .mg-ground {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 5;
  }

  /* ── Decorative border frame ───────────────────────────────── */
  .mg-frame {
    position: absolute;
    inset: clamp(12px, 2vw, 22px);
    border: 1px solid var(--mg-border-gold);
    z-index: 8;
    pointer-events: none;
  }

  .mg-frame::before {
    content: '';
    position: absolute;
    inset: 4px;
    border: 1px solid var(--mg-border-subtle);
  }

  /* Corner ornaments */
  .mg-frame-corner {
    position: absolute;
    width: 18px;
    height: 18px;
  }
  .mg-frame-corner--tl { top: -1px; left: -1px; }
  .mg-frame-corner--tr { top: -1px; right: -1px; transform: scaleX(-1); }
  .mg-frame-corner--bl { bottom: -1px; left: -1px; transform: scaleY(-1); }
  .mg-frame-corner--br { bottom: -1px; right: -1px; transform: scale(-1); }

  /* ── Typography container ──────────────────────────────────── */
  .mg-text-block {
    position: relative;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
     min-height: clamp(280px, 35vw, 420px);
    padding: clamp(2.5rem, 6vw, 5rem) clamp(1.5rem, 6vw, 4rem);
    text-align: center;
  }

  /* Eyebrow */
  .mg-eyebrow {
    font-family: var(--font-body);
    font-size: var(--text-xs);
    font-weight: 400;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--mg-gold);
    opacity: 0.85;
    margin-bottom: clamp(0.75rem, 2vw, 1.25rem);
  }

  /* Title */
  .mg-title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 3.5vw, 3.5rem);
    font-weight: 400;
    letter-spacing: 0.04em;
    line-height: 1.05;
    color: var(--mg-text-bright);
    text-shadow:
      0 0 60px rgba(12, 20, 40, 0.9),
      0 2px 24px rgba(8, 14, 28, 0.8),
      0 0 120px rgba(0, 0, 0, 0.6);
    margin-bottom: clamp(0.75rem, 2vw, 1.25rem);
  }

  /* Thin divider rule */
  .mg-rule {
    width: clamp(48px, 8vw, 80px);
    height: 1px;
    background: linear-gradient(
      to right,
      transparent,
      var(--mg-gold-muted),
      var(--mg-gold),
      var(--mg-gold-muted),
      transparent
    );
    margin: 0 auto clamp(0.75rem, 2vw, 1.25rem);
    opacity: 0.7;
  }

  /* Subtitle */
  .mg-subtitle {
    font-family: var(--font-display);
    font-size: var(--text-lg);
    font-weight: 400;
    font-style: italic;
    letter-spacing: 0.025em;
    line-height: 1.4;
    color: var(--mg-text-bright);
    opacity: 0.82;
    text-shadow: 0 1px 12px rgba(8, 14, 28, 0.9);
    margin-bottom: clamp(0.5rem, 1.5vw, 0.875rem);
    max-width: 38ch;
  }

  /* Fine print */
  .mg-caption {
    font-family: var(--font-body);
    font-size: var(--text-xs);
    font-weight: 400;
    letter-spacing: 0.12em;
    color: var(--mg-text-muted);
    opacity: 0.7;
    margin-top: clamp(0.25rem, 1vw, 0.5rem);
  }

  /* ── Animations ────────────────────────────────────────────── */

  @keyframes mg-rain-fall {
    from { transform: translateY(-120px); }
    to   { transform: translateY(0px); }
  }

  @keyframes mg-cloud-drift-slow {
    0%   { transform: translateX(0); }
    50%  { transform: translateX(-12px); }
    100% { transform: translateX(0); }
  }

  @keyframes mg-cloud-drift-med {
    0%   { transform: translateX(0); }
    50%  { transform: translateX(10px); }
    100% { transform: translateX(0); }
  }

  @keyframes mg-lightning-flash {
    0%, 92%, 96%, 100% { opacity: 0; }
    93%                { opacity: 0.6; }
    94%                { opacity: 0.1; }
    95%                { opacity: 0.5; }
  }

  @keyframes mg-text-rise {
    from {
      opacity: 0;
      transform: translateY(18px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes mg-shimmer {
    0%, 100% { opacity: 0.75; }
    50%       { opacity: 1; }
  }

  /* Apply drift to cloud groups */
  .mg-cloud-back  { animation: mg-cloud-drift-slow 22s ease-in-out infinite; }
  .mg-cloud-mid-g { animation: mg-cloud-drift-med  16s ease-in-out infinite 2s; }
  .mg-cloud-fore  { animation: mg-cloud-drift-slow 19s ease-in-out infinite 5s; }

  /* Lightning group */
  .mg-lightning-group {
    animation: mg-lightning-flash 9s ease-in-out infinite 4s;
  }
  .mg-lightning-group-2 {
    animation: mg-lightning-flash 13s ease-in-out infinite 1s;
  }

  /* Rain SVG lines animate */
  .mg-rain-anim {
    animation: mg-rain-fall 0.7s linear infinite;
  }

  /* Text entrance */
  .mg-eyebrow   { animation: mg-text-rise 1.2s cubic-bezier(0.16,1,0.3,1) both 0.3s; }
  .mg-title     { animation: mg-text-rise 1.2s cubic-bezier(0.16,1,0.3,1) both 0.55s; }
  .mg-rule      { animation: mg-text-rise 1.2s cubic-bezier(0.16,1,0.3,1) both 0.75s; }
  .mg-subtitle  { animation: mg-text-rise 1.2s cubic-bezier(0.16,1,0.3,1) both 0.9s; }
  .mg-caption   { animation: mg-text-rise 1.2s cubic-bezier(0.16,1,0.3,1) both 1.1s; }

  /* Gold eyebrow shimmer */
  .mg-eyebrow { animation:
    mg-text-rise 1.2s cubic-bezier(0.16,1,0.3,1) both 0.3s,
    mg-shimmer 4s ease-in-out infinite 2s;
  }

  /* Reduced motion: disable all animations */
  @media (prefers-reduced-motion: reduce) {
    .mg-cloud-back,
    .mg-cloud-mid-g,
    .mg-cloud-fore,
    .mg-lightning-group,
    .mg-lightning-group-2,
    .mg-rain-anim,
    .mg-eyebrow,
    .mg-title,
    .mg-rule,
    .mg-subtitle,
    .mg-caption {
      animation: none !important;
      opacity: 1 !important;
      transform: none !important;
    }
  }

  /* Responsive adjustments */
  @media (max-width: 480px) {
    .mg-frame { inset: 8px; }
    .mg-frame-corner { width: 13px; height: 13px; }
  }
</style>

<!-- ═══════════════════════════════════════════════
     MEGHADUTAM 2026 BANNER
     The Sunil Abraham Project
     ═══════════════════════════════════════════════ -->
<section
  class="mg-banner"
  aria-label="Meghadutam 2026 — A Monsoon in Search of Excellence at TSAP"
  role="banner"
>

  <!-- Sky gradient base -->
  <div class="mg-sky" aria-hidden="true"></div>

  <!-- Stars: very sparse, mostly hidden by clouds -->
  <svg class="mg-stars" aria-hidden="true" viewBox="0 0 1200 680" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
    <circle cx="92"  cy="38"  r="0.7" fill="#c8d8e8" opacity="0.6"/>
    <circle cx="240" cy="22"  r="0.5" fill="#c8d8e8" opacity="0.5"/>
    <circle cx="380" cy="45"  r="0.8" fill="#d8e4ee" opacity="0.55"/>
    <circle cx="510" cy="18"  r="0.6" fill="#c8d8e8" opacity="0.4"/>
    <circle cx="680" cy="32"  r="0.7" fill="#d0dce8" opacity="0.5"/>
    <circle cx="820" cy="12"  r="0.5" fill="#c8d8e8" opacity="0.45"/>
    <circle cx="940" cy="48"  r="0.9" fill="#d4e0ec" opacity="0.5"/>
    <circle cx="1060" cy="28" r="0.6" fill="#c8d8e8" opacity="0.4"/>
    <circle cx="1150" cy="55" r="0.7" fill="#d0dce8" opacity="0.5"/>
    <circle cx="150" cy="62"  r="0.5" fill="#c0d0e0" opacity="0.35"/>
    <circle cx="470" cy="70"  r="0.6" fill="#c8d8e8" opacity="0.3"/>
    <circle cx="760" cy="58"  r="0.5" fill="#c0d0e0" opacity="0.35"/>
    <circle cx="1000" cy="68" r="0.7" fill="#c8d8e8" opacity="0.3"/>
  </svg>

  <!-- Main cloudscape + landscape SVG -->
  <svg
    class="mg-cloudscape"
    aria-hidden="true"
    viewBox="0 0 1200 680"
    preserveAspectRatio="xMidYMid slice"
    xmlns="http://www.w3.org/2000/svg"
  >
    <defs>
      <!-- Deep cloud gradient -->
      <radialGradient id="mg-cg-deep" cx="50%" cy="40%" r="55%">
        <stop offset="0%"   stop-color="#2a3d5c"/>
        <stop offset="100%" stop-color="#0d1828"/>
      </radialGradient>

      <!-- Mid cloud gradient -->
      <radialGradient id="mg-cg-mid" cx="50%" cy="35%" r="58%">
        <stop offset="0%"   stop-color="#384f70"/>
        <stop offset="100%" stop-color="#18263d"/>
      </radialGradient>

      <!-- Lighter cloud edge -->
      <radialGradient id="mg-cg-light" cx="50%" cy="30%" r="55%">
        <stop offset="0%"   stop-color="#445e80" stop-opacity="0.7"/>
        <stop offset="100%" stop-color="#1e3050" stop-opacity="0.2"/>
      </radialGradient>

      <!-- Green ground gradient -->
      <linearGradient id="mg-ground-g" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%"   stop-color="#2a6338"/>
        <stop offset="40%"  stop-color="#1a4226"/>
        <stop offset="100%" stop-color="#0b2014"/>
      </linearGradient>

      <!-- Horizon glow -->
      <radialGradient id="mg-horizon-g" cx="50%" cy="100%" r="60%">
        <stop offset="0%"   stop-color="#1e5038" stop-opacity="0.7"/>
        <stop offset="100%" stop-color="#0b1a28" stop-opacity="0"/>
      </radialGradient>

      <!-- Lightning glow -->
      <filter id="mg-lightning-glow" x="-30%" y="-30%" width="160%" height="160%">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>

      <!-- Cloud soft blur -->
      <filter id="mg-cloud-blur" x="-5%" y="-5%" width="110%" height="110%">
        <feGaussianBlur stdDeviation="4"/>
      </filter>

      <!-- Cloud medium blur -->
      <filter id="mg-cloud-blur-md" x="-5%" y="-5%" width="110%" height="110%">
        <feGaussianBlur stdDeviation="7"/>
      </filter>

      <!-- Soft glow on title -->
      <filter id="mg-title-glow">
        <feGaussianBlur stdDeviation="12" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>

      <!-- Rain line blur -->
      <filter id="mg-rain-blur">
        <feGaussianBlur stdDeviation="0.4"/>
      </filter>
    </defs>

    <!-- ── Horizon glow ── -->
    <ellipse cx="600" cy="680" rx="700" ry="260"
      fill="url(#mg-horizon-g)" opacity="0.6"/>

    <!-- ══════════════════════════════════════
         CLOUD LAYERS — back to front
    ══════════════════════════════════════ -->

    <!-- Layer 1: Deepest background clouds (very dark, large masses) -->
    <g class="mg-cloud-back">
      <!-- Far left mass -->
      <ellipse cx="-30" cy="130" rx="280" ry="130" fill="#0e1a2e" opacity="0.95"/>
      <ellipse cx="80"  cy="80"  rx="200" ry="90"  fill="#111e32" opacity="0.9"/>
      <ellipse cx="40"  cy="160" rx="220" ry="100" fill="#0d1828" opacity="0.85"/>

      <!-- Centre-left billowing mass -->
      <ellipse cx="350" cy="100" rx="310" ry="140" fill="#141e30" opacity="0.9"/>
      <ellipse cx="280" cy="60"  rx="200" ry="80"  fill="#111828" opacity="0.85"/>
      <ellipse cx="420" cy="140" rx="240" ry="110" fill="#0f1a2c" opacity="0.8"/>

      <!-- Right mass -->
      <ellipse cx="950" cy="90"  rx="320" ry="130" fill="#121c2e" opacity="0.92"/>
      <ellipse cx="1080" cy="50" rx="210" ry="90"  fill="#0f1826" opacity="0.88"/>
      <ellipse cx="1200" cy="140" rx="250" ry="110" fill="#0d1624" opacity="0.85"/>

      <!-- Top wispy fringe -->
      <ellipse cx="600" cy="20"  rx="500" ry="55"  fill="#0a1220" opacity="0.7"/>
      <ellipse cx="600" cy="0"   rx="650" ry="35"  fill="#070e1a" opacity="0.8"/>
    </g>

    <!-- Layer 2: Mid clouds — slightly lighter, Rajput-esque rounded billows -->
    <g class="mg-cloud-mid-g">
      <!-- Left billow cluster -->
      <ellipse cx="120" cy="200" rx="230" ry="100" fill="url(#mg-cg-deep)" opacity="0.88"/>
      <ellipse cx="60"  cy="240" rx="180" ry="80"  fill="#1a2b42" opacity="0.7"/>
      <ellipse cx="190" cy="170" rx="160" ry="70"  fill="#22334e" opacity="0.65"/>
      <!-- top lobes -->
      <ellipse cx="80"  cy="170" rx="90"  ry="55"  fill="#253445" opacity="0.6"/>
      <ellipse cx="160" cy="145" rx="75"  ry="48"  fill="#2a3a50" opacity="0.55"/>

      <!-- Central tower — tall cumulonimbus suggestion -->
      <ellipse cx="580" cy="260" rx="280" ry="120" fill="#1c2d46" opacity="0.82"/>
      <ellipse cx="600" cy="200" rx="230" ry="100" fill="#1f3148" opacity="0.75"/>
      <ellipse cx="560" cy="155" rx="175" ry="82"  fill="#243650" opacity="0.7"/>
      <ellipse cx="610" cy="110" rx="130" ry="65"  fill="#283a55" opacity="0.65"/>
      <ellipse cx="590" cy="72"  rx="90"  ry="52"  fill="#2d3f5a" opacity="0.6"/>
      <!-- anvil top -->
      <ellipse cx="600" cy="45"  rx="170" ry="38"  fill="#1e2e48" opacity="0.5"/>

      <!-- Right billow cluster -->
      <ellipse cx="1060" cy="195" rx="210" ry="95"  fill="url(#mg-cg-deep)" opacity="0.85"/>
      <ellipse cx="1140" cy="160" rx="170" ry="75"  fill="#1f2f46" opacity="0.7"/>
      <ellipse cx="1000" cy="220" rx="180" ry="80"  fill="#1a2840" opacity="0.65"/>
      <ellipse cx="1100" cy="130" rx="110" ry="58"  fill="#253545" opacity="0.6"/>
    </g>

    <!-- Layer 3: Foreground clouds — most detail, mini-painting rounded lobes -->
    <g class="mg-cloud-fore">
      <!-- Lower left cloud bank -->
      <ellipse cx="0"   cy="340" rx="220" ry="90"  fill="#1e2f48" opacity="0.75"/>
      <ellipse cx="80"  cy="310" rx="180" ry="75"  fill="#233448" opacity="0.7"/>
      <ellipse cx="160" cy="285" rx="140" ry="65"  fill="#283a50" opacity="0.65"/>
      <!-- rounded lobes at top -->
      <circle  cx="60"  cy="290" r="55"  fill="#243040" opacity="0.6"/>
      <circle  cx="130" cy="265" r="48"  fill="#283550" opacity="0.55"/>
      <circle  cx="200" cy="252" r="42"  fill="#2d3a52" opacity="0.5"/>

      <!-- Lower right cloud bank -->
      <ellipse cx="1200" cy="330" rx="230" ry="95"  fill="#1d2e48" opacity="0.75"/>
      <ellipse cx="1100" cy="300" rx="195" ry="82"  fill="#223348" opacity="0.7"/>
      <ellipse cx="1020" cy="278" rx="150" ry="68"  fill="#273845" opacity="0.65"/>
      <circle  cx="1130" cy="282" r="52"  fill="#243040" opacity="0.58"/>
      <circle  cx="1060" cy="260" r="46"  fill="#283550" opacity="0.52"/>
      <circle  cx="990"  cy="248" r="40"  fill="#2c3850" opacity="0.48"/>

      <!-- Wispy lower fringe across the mid-band -->
      <ellipse cx="480" cy="385" rx="260" ry="55"  fill="#182840" opacity="0.45" filter="url(#mg-cloud-blur)"/>
      <ellipse cx="720" cy="370" rx="240" ry="50"  fill="#182840" opacity="0.4"  filter="url(#mg-cloud-blur)"/>
    </g>

    <!-- ══════════════════════════════════════
         LIGHTNING (subtle, CSS-animated)
    ══════════════════════════════════════ -->
    <g class="mg-lightning-group" filter="url(#mg-lightning-glow)">
      <!-- Branching bolt left-centre -->
      <polyline
        points="420,70 412,130 424,140 410,210 420,215 400,300"
        fill="none" stroke="#c8dff5" stroke-width="1.2" opacity="0.9"/>
      <polyline
        points="424,140 440,175 448,172"
        fill="none" stroke="#c8dff5" stroke-width="0.7" opacity="0.7"/>
      <!-- Glow ellipse behind bolt -->
      <ellipse cx="415" cy="185" rx="60" ry="120"
        fill="#4060a0" opacity="0.12" filter="url(#mg-cloud-blur-md)"/>
    </g>

    <g class="mg-lightning-group-2" filter="url(#mg-lightning-glow)">
      <!-- Right bolt -->
      <polyline
        points="820,55 815,120 828,130 812,205 822,210 808,280"
        fill="none" stroke="#d0e8f8" stroke-width="1.1" opacity="0.85"/>
      <polyline
        points="828,130 845,162 852,159"
        fill="none" stroke="#d0e8f8" stroke-width="0.65" opacity="0.65"/>
      <ellipse cx="820" cy="170" rx="55" ry="110"
        fill="#3858a0" opacity="0.1" filter="url(#mg-cloud-blur-md)"/>
    </g>

    <!-- ══════════════════════════════════════
         RAIN — diagonal strokes
    ══════════════════════════════════════ -->
    <g class="mg-rain-anim" filter="url(#mg-rain-blur)" opacity="0.55">
      <!-- Dense rain lines — short, angled 10° from vertical -->
      <line x1="50"   y1="300" x2="44"   y2="340" stroke="#b0cce0" stroke-width="0.5"/>
      <line x1="85"   y1="320" x2="79"   y2="362" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="120"  y1="290" x2="114"  y2="336" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="160"  y1="310" x2="154"  y2="355" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="200"  y1="280" x2="194"  y2="325" stroke="#b4d0e2" stroke-width="0.4"/>
      <line x1="240"  y1="300" x2="234"  y2="346" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="285"  y1="290" x2="279"  y2="336" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="330"  y1="310" x2="324"  y2="356" stroke="#a8c8de" stroke-width="0.45"/>
      <line x1="370"  y1="285" x2="364"  y2="332" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="415"  y1="305" x2="409"  y2="352" stroke="#aacce0" stroke-width="0.5"/>
      <line x1="460"  y1="295" x2="454"  y2="342" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="500"  y1="315" x2="494"  y2="362" stroke="#a8c8de" stroke-width="0.45"/>
      <line x1="545"  y1="290" x2="539"  y2="338" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="590"  y1="310" x2="584"  y2="358" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="635"  y1="285" x2="629"  y2="334" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="678"  y1="305" x2="672"  y2="354" stroke="#a8c8de" stroke-width="0.45"/>
      <line x1="722"  y1="292" x2="716"  y2="340" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="766"  y1="312" x2="760"  y2="360" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="810"  y1="288" x2="804"  y2="336" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="855"  y1="308" x2="849"  y2="356" stroke="#a8c8de" stroke-width="0.45"/>
      <line x1="900"  y1="295" x2="894"  y2="344" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="945"  y1="315" x2="939"  y2="364" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="990"  y1="290" x2="984"  y2="340" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="1035" y1="310" x2="1029" y2="360" stroke="#a8c8de" stroke-width="0.45"/>
      <line x1="1080" y1="285" x2="1074" y2="336" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="1125" y1="305" x2="1119" y2="356" stroke="#a8c8de" stroke-width="0.5"/>
      <line x1="1168" y1="292" x2="1162" y2="342" stroke="#b0cce0" stroke-width="0.4"/>
      <!-- second staggered pass -->
      <line x1="70"   y1="350" x2="64"   y2="400" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="145"  y1="365" x2="139"  y2="415" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="220"  y1="345" x2="214"  y2="396" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="310"  y1="360" x2="304"  y2="410" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="400"  y1="348" x2="394"  y2="400" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="485"  y1="365" x2="479"  y2="415" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="565"  y1="345" x2="559"  y2="396" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="655"  y1="362" x2="649"  y2="412" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="745"  y1="350" x2="739"  y2="400" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="835"  y1="366" x2="829"  y2="416" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="920"  y1="348" x2="914"  y2="400" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="1010" y1="364" x2="1004" y2="414" stroke="#b0cce0" stroke-width="0.4"/>
      <line x1="1100" y1="350" x2="1094" y2="400" stroke="#a8c8de" stroke-width="0.4"/>
      <line x1="1185" y1="366" x2="1179" y2="416" stroke="#b0cce0" stroke-width="0.4"/>
    </g>

    <!-- ══════════════════════════════════════
         LANDSCAPE — lush green ground
    ══════════════════════════════════════ -->
    <!-- Ground fill -->
    <path d="M0,680 L0,530
      C60,510 100,500 140,505
      C180,510 200,500 240,495
      C280,490 310,498 350,492
      C390,486 420,490 460,488
      C500,486 530,492 570,488
      C610,484 640,490 680,488
      C720,486 750,490 790,488
      C830,486 860,492 900,488
      C940,484 970,490 1010,488
      C1060,484 1100,492 1150,500
      C1180,505 1200,510 1200,515
      L1200,680 Z"
      fill="url(#mg-ground-g)"
    />

    <!-- Ground highlight band (where land meets rain-soaked sky) -->
    <path d="M0,540
      C60,520 100,512 140,517
      C180,522 200,512 240,507
      C280,502 310,510 350,504
      C390,498 420,502 460,500
      C500,498 530,504 570,500
      C610,496 640,502 680,500
      C720,498 750,502 790,500
      C830,498 860,504 900,500
      C940,496 970,502 1010,500
      C1060,496 1100,504 1150,512
      C1180,517 1200,522 1200,527
      L1200,540
      C1150,533 1100,526 1060,522
      C1010,516 970,510 940,514
      C900,518 860,512 820,514
      C780,516 750,510 700,512
      C660,514 630,508 590,510
      C550,512 520,506 480,508
      C440,510 420,504 380,506
      C340,508 310,502 270,505
      C230,508 200,502 160,506
      C120,510 80,516 40,522 Z"
      fill="#2a6338" opacity="0.6"
    />

    <!-- Vegetation texture — Pahari hills distant -->
    <path d="M0,558 C40,540 70,535 95,545 C110,550 115,548 130,538
      C155,525 175,530 200,535 C220,540 230,535 255,528
      C280,521 300,530 325,528 C350,526 365,518 385,522
      C408,527 420,520 440,516 C455,513 468,520 485,518
      C510,515 525,508 545,512 C565,516 580,510 600,508
      C618,506 632,512 648,510 C670,507 682,500 700,504
      C720,508 735,502 755,500 C775,498 790,504 810,502
      C830,500 845,494 865,498 C885,502 900,496 920,500
      C940,504 955,498 975,502 C995,506 1010,500 1030,498
      C1052,495 1068,502 1090,506 C1110,510 1130,504 1155,510
      C1175,515 1190,520 1200,525
      L1200,560
      C1175,548 1140,542 1100,542
      C1060,542 1030,548 1000,546
      C970,544 950,550 920,548
      C890,546 870,552 840,550
      C810,548 790,554 760,552
      C730,550 710,556 680,554
      C650,552 630,558 600,556
      C570,554 550,560 520,558
      C490,556 470,562 440,560
      C410,558 390,564 360,562
      C330,560 310,566 280,564
      C250,562 230,568 200,566
      C170,564 150,570 120,568
      C90,566 60,572 30,570
      C15,568 0,565 0,565 Z"
      fill="#1d4a28" opacity="0.75"
    />

    <!-- ── Trees — two stylised trees, Pahari silhouette ── -->
    <!-- Tree 1 — left, tall slender type -->
    <g>
      <!-- Trunk -->
      <rect x="168" y="510" width="6" height="52"
        fill="#0d2015" rx="2"/>
      <!-- Foliage — layered rounded masses -->
      <ellipse cx="171" cy="492" rx="32" ry="42"
        fill="#1a3e20" opacity="0.92"/>
      <ellipse cx="171" cy="478" rx="26" ry="34"
        fill="#215228" opacity="0.85"/>
      <ellipse cx="171" cy="466" rx="20" ry="26"
        fill="#2a6034" opacity="0.8"/>
      <ellipse cx="171" cy="456" rx="14" ry="18"
        fill="#328040" opacity="0.75"/>
      <ellipse cx="171" cy="450" rx="9"  ry="12"
        fill="#3a9048" opacity="0.7"/>
      <!-- highlight dot -->
      <ellipse cx="167" cy="458" rx="5" ry="7"
        fill="#3eaa52" opacity="0.3"/>
    </g>

    <!-- Tree 2 — right, slightly different silhouette (broader) -->
    <g>
      <!-- Trunk -->
      <rect x="1018" y="508" width="7" height="54"
        fill="#0c1e14" rx="2"/>
      <!-- Foliage -->
      <ellipse cx="1021" cy="494" rx="36" ry="38"
        fill="#193b1e" opacity="0.9"/>
      <ellipse cx="1021" cy="478" rx="30" ry="32"
        fill="#1e4c24" opacity="0.85"/>
      <ellipse cx="1021" cy="464" rx="24" ry="27"
        fill="#275e2e" opacity="0.8"/>
      <ellipse cx="1021" cy="453" rx="18" ry="20"
        fill="#307236" opacity="0.75"/>
      <ellipse cx="1021" cy="447" rx="12" ry="14"
        fill="#388440" opacity="0.7"/>
      <!-- left sub-branch mass -->
      <ellipse cx="1006" cy="468" rx="16" ry="18"
        fill="#225228" opacity="0.65"/>
      <!-- highlight -->
      <ellipse cx="1017" cy="457" rx="5" ry="7"
        fill="#409850" opacity="0.28"/>
    </g>

    <!-- Wet ground puddle glints — tiny horizontal ellipses -->
    <ellipse cx="300" cy="565" rx="18" ry="3"
      fill="#4080a0" opacity="0.15"/>
    <ellipse cx="700" cy="570" rx="24" ry="3.5"
      fill="#3878a0" opacity="0.14"/>
    <ellipse cx="900" cy="560" rx="16" ry="2.5"
      fill="#4080a0" opacity="0.13"/>

    <!-- ── Low horizon mist ── -->
    <rect x="0" y="500" width="1200" height="50"
      fill="#0e2a20"
      opacity="0.25"
      filter="url(#mg-cloud-blur-md)"
    />

    <!-- ── Pahari border motif: subtle repeating diamond band ── -->
    <!-- Top decorative band -->
    <rect x="0" y="0" width="1200" height="6"
      fill="none"
      stroke="#c8a84b"
      stroke-width="0.5"
      stroke-dasharray="3,8"
      opacity="0.35"
    />
    <!-- Bottom decorative band -->
    <rect x="0" y="674" width="1200" height="6"
      fill="none"
      stroke="#c8a84b"
      stroke-width="0.5"
      stroke-dasharray="3,8"
      opacity="0.35"
    />

  </svg><!-- end .mg-cloudscape -->

  <!-- Decorative Pahari-style frame -->
  <div class="mg-frame" aria-hidden="true">
    <!-- Corner ornaments (inline SVG) -->
    <svg class="mg-frame-corner mg-frame-corner--tl" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M1 17 L1 1 L17 1" stroke="#c8a84b" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="1" cy="1" r="2" fill="#c8a84b" fill-opacity="0.5"/>
    </svg>
    <svg class="mg-frame-corner mg-frame-corner--tr" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M1 17 L1 1 L17 1" stroke="#c8a84b" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="1" cy="1" r="2" fill="#c8a84b" fill-opacity="0.5"/>
    </svg>
    <svg class="mg-frame-corner mg-frame-corner--bl" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M1 17 L1 1 L17 1" stroke="#c8a84b" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="1" cy="1" r="2" fill="#c8a84b" fill-opacity="0.5"/>
    </svg>
    <svg class="mg-frame-corner mg-frame-corner--br" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M1 17 L1 1 L17 1" stroke="#c8a84b" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="1" cy="1" r="2" fill="#c8a84b" fill-opacity="0.5"/>
    </svg>
  </div>

  <!-- Typography -->
  <div class="mg-text-block">
    <p class="mg-eyebrow">The Sunil Abraham Project</p>
    <h1 class="mg-title">Meghadutam 2026</h1>
    <div class="mg-rule" aria-hidden="true"></div>
    <p class="mg-subtitle">A Monsoon in Search of Excellence at TSAP</p>
  </div>

</section>
<!-- end .mg-banner -->
