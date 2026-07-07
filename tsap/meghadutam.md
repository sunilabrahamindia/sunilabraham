---
layout: default
title: "Meghadutam"
description: "Meghadutam is a monsoon content enrichment event on The Sunil Abraham Project. Inspired by Kalidasa's Meghadutam, it emphasises content excellence rather than article count."
permalink: /meghadutam/
categories: [Project pages, TSAP Events and Rituals]
page_id: TSAP-1078
created: 2026-06-20
---

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
         RAIN — varied, clustered, monsoon-like
    ══════════════════════════════════════ -->

    <!-- Light, diffuse rain veil -->
    <g class="mg-rain-anim-slow" filter="url(#mg-rain-blur)" opacity="0.34">
      <line x1="38"   y1="286" x2="31"   y2="334" stroke="#a9c9dd" stroke-width="0.34"/>
      <line x1="104"  y1="304" x2="96"   y2="351" stroke="#a7c6da" stroke-width="0.32"/>
      <line x1="187"  y1="278" x2="180"  y2="322" stroke="#afcee1" stroke-width="0.28"/>
      <line x1="266"  y1="296" x2="260"  y2="340" stroke="#a9c9dd" stroke-width="0.3"/>
      <line x1="352"  y1="287" x2="345"  y2="333" stroke="#a7c6da" stroke-width="0.29"/>
      <line x1="438"  y1="300" x2="432"  y2="347" stroke="#b2d0e2" stroke-width="0.33"/>
      <line x1="516"  y1="282" x2="510"  y2="327" stroke="#a9c9dd" stroke-width="0.3"/>
      <line x1="603"  y1="296" x2="596"  y2="343" stroke="#a7c6da" stroke-width="0.32"/>
      <line x1="676"  y1="285" x2="669"  y2="332" stroke="#afcee1" stroke-width="0.28"/>
      <line x1="762"  y1="302" x2="754"  y2="350" stroke="#a9c9dd" stroke-width="0.31"/>
      <line x1="846"  y1="281" x2="840"  y2="327" stroke="#a7c6da" stroke-width="0.29"/>
      <line x1="924"  y1="297" x2="917"  y2="344" stroke="#b2d0e2" stroke-width="0.33"/>
      <line x1="1011" y1="284" x2="1004" y2="332" stroke="#a9c9dd" stroke-width="0.31"/>
      <line x1="1098" y1="300" x2="1091" y2="346" stroke="#a7c6da" stroke-width="0.3"/>
      <line x1="1172" y1="289" x2="1165" y2="336" stroke="#afcee1" stroke-width="0.28"/>

      <line x1="82"   y1="344" x2="75"   y2="394" stroke="#a7c6da" stroke-width="0.29"/>
      <line x1="228"  y1="338" x2="221"  y2="387" stroke="#a9c9dd" stroke-width="0.31"/>
      <line x1="386"  y1="352" x2="379"  y2="401" stroke="#b2d0e2" stroke-width="0.33"/>
      <line x1="548"  y1="340" x2="541"  y2="389" stroke="#a7c6da" stroke-width="0.29"/>
      <line x1="708"  y1="348" x2="701"  y2="398" stroke="#afcee1" stroke-width="0.3"/>
      <line x1="882"  y1="342" x2="875"  y2="391" stroke="#a9c9dd" stroke-width="0.31"/>
      <line x1="1044" y1="350" x2="1036" y2="401" stroke="#b2d0e2" stroke-width="0.32"/>
      <line x1="1150" y1="346" x2="1143" y2="395" stroke="#a7c6da" stroke-width="0.29"/>
    </g>

    <!-- Main rain field with clusters and gaps -->
    <g class="mg-rain-anim" filter="url(#mg-rain-blur)" opacity="0.52">
      <!-- Left cluster -->
      <line x1="56"  y1="296" x2="49"  y2="338" stroke="#b0cce0" stroke-width="0.52"/>
      <line x1="71"  y1="309" x2="63"  y2="358" stroke="#b7d4e5" stroke-width="0.56"/>
      <line x1="94"  y1="286" x2="88"  y2="330" stroke="#a8c8de" stroke-width="0.41"/>
      <line x1="118" y1="321" x2="111" y2="370" stroke="#b4d0e2" stroke-width="0.47"/>
      <line x1="146" y1="298" x2="138" y2="351" stroke="#aacce0" stroke-width="0.5"/>
      <line x1="173" y1="281" x2="166" y2="326" stroke="#b0cce0" stroke-width="0.4"/>

      <!-- Gap -->

      <!-- Left-centre moderate field -->
      <line x1="254" y1="302" x2="247" y2="348" stroke="#a8c8de" stroke-width="0.42"/>
      <line x1="286" y1="287" x2="279" y2="333" stroke="#b0cce0" stroke-width="0.39"/>
      <line x1="319" y1="312" x2="312" y2="361" stroke="#aacce0" stroke-width="0.48"/>
      <line x1="347" y1="292" x2="341" y2="338" stroke="#a8c8de" stroke-width="0.43"/>

      <!-- Slightly heavier central curtain -->
      <line x1="404" y1="278" x2="397" y2="328" stroke="#bdd8e8" stroke-width="0.58"/>
      <line x1="419" y1="296" x2="411" y2="350" stroke="#b9d5e6" stroke-width="0.6"/>
      <line x1="437" y1="286" x2="429" y2="339" stroke="#aacce0" stroke-width="0.44"/>
      <line x1="452" y1="309" x2="444" y2="365" stroke="#c0dbea" stroke-width="0.62"/>
      <line x1="468" y1="291" x2="461" y2="340" stroke="#b0cce0" stroke-width="0.46"/>
      <line x1="487" y1="318" x2="479" y2="374" stroke="#c4ddeb" stroke-width="0.64"/>
      <line x1="506" y1="300" x2="499" y2="349" stroke="#aacce0" stroke-width="0.44"/>

      <!-- Gap before centre-right -->

      <line x1="592" y1="286" x2="585" y2="334" stroke="#b0cce0" stroke-width="0.42"/>
      <line x1="617" y1="305" x2="609" y2="357" stroke="#a8c8de" stroke-width="0.46"/>
      <line x1="648" y1="291" x2="641" y2="340" stroke="#b4d0e2" stroke-width="0.43"/>

      <!-- Heavy patch under right storm cell -->
      <line x1="730" y1="280" x2="722" y2="334" stroke="#c1dbea" stroke-width="0.58"/>
      <line x1="744" y1="295" x2="735" y2="352" stroke="#c8e0ed" stroke-width="0.67"/>
      <line x1="760" y1="287" x2="752" y2="340" stroke="#b6d3e4" stroke-width="0.5"/>
      <line x1="776" y1="304" x2="767" y2="362" stroke="#c4ddeb" stroke-width="0.63"/>
      <line x1="794" y1="289" x2="786" y2="343" stroke="#b2d0e2" stroke-width="0.47"/>
      <line x1="812" y1="311" x2="803" y2="370" stroke="#c8e0ed" stroke-width="0.66"/>
      <line x1="833" y1="293" x2="825" y2="347" stroke="#b4d0e2" stroke-width="0.48"/>

      <!-- Broken field -->
      <line x1="902" y1="301" x2="895" y2="350" stroke="#aacce0" stroke-width="0.43"/>
      <line x1="938" y1="286" x2="930" y2="338" stroke="#b0cce0" stroke-width="0.45"/>

      <!-- Far-right cluster -->
      <line x1="1018" y1="283" x2="1010" y2="335" stroke="#bdd8e8" stroke-width="0.55"/>
      <line x1="1035" y1="299" x2="1027" y2="353" stroke="#b6d3e4" stroke-width="0.5"/>
      <line x1="1053" y1="287" x2="1045" y2="340" stroke="#aacce0" stroke-width="0.43"/>
      <line x1="1075" y1="310" x2="1067" y2="365" stroke="#c1dbea" stroke-width="0.58"/>
      <line x1="1096" y1="292" x2="1088" y2="344" stroke="#b0cce0" stroke-width="0.46"/>
      <line x1="1122" y1="304" x2="1114" y2="359" stroke="#bdd8e8" stroke-width="0.55"/>
      <line x1="1156" y1="289" x2="1148" y2="342" stroke="#a8c8de" stroke-width="0.41"/>

      <!-- Lower broken pass -->
      <line x1="128" y1="347" x2="120" y2="398" stroke="#a8c8de" stroke-width="0.39"/>
      <line x1="182" y1="362" x2="175" y2="414" stroke="#b0cce0" stroke-width="0.41"/>
      <line x1="298" y1="351" x2="290" y2="404" stroke="#aacce0" stroke-width="0.4"/>
      <line x1="431" y1="357" x2="423" y2="412" stroke="#b9d5e6" stroke-width="0.48"/>
      <line x1="471" y1="349" x2="463" y2="403" stroke="#c1dbea" stroke-width="0.52"/>
      <line x1="621" y1="356" x2="613" y2="411" stroke="#aacce0" stroke-width="0.41"/>
      <line x1="772" y1="349" x2="763" y2="407" stroke="#c1dbea" stroke-width="0.54"/>
      <line x1="814" y1="363" x2="805" y2="421" stroke="#c8e0ed" stroke-width="0.58"/>
      <line x1="952" y1="351" x2="944" y2="404" stroke="#aacce0" stroke-width="0.4"/>
      <line x1="1078" y1="360" x2="1070" y2="415" stroke="#b9d5e6" stroke-width="0.47"/>
      <line x1="1138" y1="346" x2="1130" y2="399" stroke="#aacce0" stroke-width="0.4"/>
    </g>

    <!-- Fine, fast streaks for occasional monsoon intensity -->
    <g class="mg-rain-anim-fast" filter="url(#mg-rain-blur)" opacity="0.22">
      <line x1="82"   y1="272" x2="74"   y2="332" stroke="#d1e6f1" stroke-width="0.34"/>
      <line x1="162"  y1="286" x2="153"  y2="350" stroke="#d1e6f1" stroke-width="0.36"/>
      <line x1="447"  y1="268" x2="438"  y2="334" stroke="#d7e9f3" stroke-width="0.38"/>
      <line x1="489"  y1="280" x2="479"  y2="352" stroke="#d7e9f3" stroke-width="0.4"/>
      <line x1="748"  y1="270" x2="738"  y2="338" stroke="#d7e9f3" stroke-width="0.39"/>
      <line x1="808"  y1="282" x2="798"  y2="353" stroke="#dbeaf4" stroke-width="0.42"/>
      <line x1="1048" y1="274" x2="1039" y2="341" stroke="#d1e6f1" stroke-width="0.36"/>
      <line x1="1118" y1="286" x2="1108" y2="354" stroke="#d7e9f3" stroke-width="0.38"/>

      <line x1="214"  y1="334" x2="205"  y2="397" stroke="#d1e6f1" stroke-width="0.35"/>
      <line x1="456"  y1="342" x2="446"  y2="410" stroke="#d7e9f3" stroke-width="0.38"/>
      <line x1="789"  y1="336" x2="779"  y2="405" stroke="#dbeaf4" stroke-width="0.4"/>
      <line x1="1088" y1="340" x2="1079" y2="405" stroke="#d1e6f1" stroke-width="0.36"/>
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

    <!-- ── Trees — revised to be clearly distinct and fully visible ── -->

    <!-- Tree 1 — left, tall and slender, cypress-like miniature form -->
    <g>
      <!-- Trunk -->
      <rect x="166" y="500" width="5" height="42"
        fill="#0d2015" rx="2"/>

      <!-- Narrow vertical canopy -->
      <ellipse cx="168.5" cy="484" rx="22" ry="44"
        fill="#16361d" opacity="0.93"/>
      <ellipse cx="168.5" cy="469" rx="18" ry="35"
        fill="#1d4824" opacity="0.88"/>
      <ellipse cx="168.5" cy="454" rx="14" ry="28"
        fill="#25592d" opacity="0.82"/>
      <ellipse cx="168.5" cy="441" rx="10" ry="20"
        fill="#2d6e36" opacity="0.77"/>
      <ellipse cx="168.5" cy="432" rx="7" ry="13"
        fill="#378742" opacity="0.72"/>

      <!-- Subtle asymmetry, miniature style -->
      <ellipse cx="162" cy="468" rx="7" ry="16"
        fill="#1b4322" opacity="0.5"/>
      <ellipse cx="174" cy="456" rx="6" ry="13"
        fill="#2a6034" opacity="0.42"/>

      <!-- Highlight -->
      <ellipse cx="165.5" cy="446" rx="4" ry="8"
        fill="#44a958" opacity="0.22"/>
    </g>

    <!-- Tree 2 — right, broader and rounded, banyan/mango-like miniature form -->
    <g>
      <!-- Trunk and branching base -->
      <rect x="1015" y="506" width="8" height="36"
        fill="#0c1e14" rx="2"/>
      <path d="M1019,505 C1018,494 1014,487 1008,482
               C1013,488 1014,495 1014,505 Z"
        fill="#0c1e14" opacity="0.8"/>
      <path d="M1019,503 C1021,492 1026,486 1032,482
               C1027,488 1025,495 1024,504 Z"
        fill="#0c1e14" opacity="0.78"/>

      <!-- Broad canopy -->
      <ellipse cx="1019" cy="488" rx="47" ry="31"
        fill="#17381d" opacity="0.92"/>
      <ellipse cx="991"  cy="481" rx="22" ry="18"
        fill="#1c4723" opacity="0.82"/>
      <ellipse cx="1045" cy="480" rx="24" ry="19"
        fill="#1c4723" opacity="0.82"/>
      <ellipse cx="1019" cy="470" rx="38" ry="24"
        fill="#215228" opacity="0.86"/>
      <ellipse cx="996"  cy="466" rx="16" ry="14"
        fill="#275e2e" opacity="0.76"/>
      <ellipse cx="1041" cy="466" rx="17" ry="14"
        fill="#275e2e" opacity="0.76"/>
      <ellipse cx="1019" cy="454" rx="26" ry="18"
        fill="#2f7338" opacity="0.74"/>
      <ellipse cx="1019" cy="444" rx="16" ry="11"
        fill="#388440" opacity="0.68"/>

      <!-- Lower skirt to make it feel older and wider -->
      <ellipse cx="1001" cy="498" rx="18" ry="10"
        fill="#163a1d" opacity="0.5"/>
      <ellipse cx="1036" cy="497" rx="19" ry="10"
        fill="#163a1d" opacity="0.5"/>

      <!-- Highlight -->
      <ellipse cx="1013" cy="456" rx="6" ry="7"
        fill="#4aa85a" opacity="0.24"/>
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

**Meghadutam** is a content enrichment event on The Sunil Abraham Project. The main difference is that Meghadutam does not count the number of articles created during the event period, unlike our other reports. Instead, it seeks to showcase the most excellent content created and enriched during the event. The name is inspired by *Meghadutam* by Kalidasa.

The event will continue throughout the monsoon season of 2026.

<div class="mg-epigraph">
  <p>
    कश्चित्कान्ताविरहगुरुणा स्वाधिकारात्प्रमत्तः<br>
    शापेनास्तंगमितमहिमा वर्षभोग्येण भर्तुः ।<br>
    यक्षश्चक्रे जनकतनयास्नानपुण्योदकेषु<br>
    स्निग्धच्छायातरुषु वसतिं रामगिर्याश्रमेषु ॥
  </p>
</div>

## Featured works
<div class="mg-featured-item">
  <div class="mg-featured-date">Sunday, 21 June 2026</div>

  <p>
    <a href="/media/aadhaar-biometrique-liberation/">
      «En Inde, le biométrique version très grand public» (Biometrics in India Goes Mainstream)
    </a> — A bilingual edition of a 2017 Libération article in French and English. The article examines the expansion of Aadhaar in India and includes comments from Sunil Abraham on biometric security, privacy, and surveillance.
  </p>
</div>

<div class="mg-featured-item">
  <div class="mg-featured-date">Sunday, 21 June 2026</div>

  <p>
    <a href="/media/privacy-ruling-puts-tech-industry-on-notice-cnnmoney/">
      Privacy Ruling Puts Tech Industry on Notice
    </a> — Selected for Meghadutam because it documents contemporary reactions to the Supreme Court's landmark privacy judgment and captures an important moment in the development of India's digital rights and data protection debates.
  </p>
</div>

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
    font-size: clamp(2rem, 4vw, 4rem);
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

  @keyframes mg-rain-fall-slow {
    from { transform: translateY(-105px); }
    to   { transform: translateY(0px); }
  }

  @keyframes mg-rain-fall-fast {
    from { transform: translateY(-138px); }
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
    animation: mg-lightning-flash 6s ease-in-out infinite 4s;
  }
  .mg-lightning-group-2 {
    animation: mg-lightning-flash 10s ease-in-out infinite 1s;
  }

  /* Rain SVG groups animate at slightly different rates */
  .mg-rain-anim {
    animation: mg-rain-fall 0.7s linear infinite;
  }

  .mg-rain-anim-slow {
    animation: mg-rain-fall-slow 0.92s linear infinite;
  }

  .mg-rain-anim-fast {
    animation: mg-rain-fall-fast 0.56s linear infinite;
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
    .mg-rain-anim-slow,
    .mg-rain-anim-fast,
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
  
  .mg-epigraph {
    text-align: center;
    margin: 2.5rem auto 3rem auto;
    max-width: 42rem;
  }

  .mg-epigraph p {
    margin: 0;
    font-size: clamp(1rem, 2.5vw, 1.2rem);
    color: #444;
    font-weight: 400;
  }

  /* ============================================================
     MEGHADUTAM 2026 — Featured Works: Monsoon Chronicle Entries
     Redesigned: stronger visual identity per variant,
     monsoon-led palette, gold as secondary accent only
     ============================================================ */

  /* ── Shared keyframes ──────────────────────────────────────── */

  /* Slow cloud-like lateral sway */
  @keyframes mg-fe-cloud-sway {
    0%, 100% { transform: translateX(0); }
    40%       { transform: translateX(3px); }
    70%       { transform: translateX(-2px); }
  }

  /* Rain curtain scrolling diagonally downward */
  @keyframes mg-fe-rain-scroll {
    from { background-position: 0 0; }
    to   { background-position: -30px 120px; }
  }

  /* Mist pulse — opacity swell, slow */
  @keyframes mg-fe-mist-pulse {
    0%, 100% { opacity: 0.55; }
    50%       { opacity: 1; }
  }

  /* Horizon line breathe — border darkens and returns */
  @keyframes mg-fe-horizon-breathe {
    0%, 100% { border-bottom-color: rgba(42, 99, 56, 0.35); }
    50%       { border-bottom-color: rgba(42, 99, 56, 0.72); }
  }

  /* Left rule wash — left border swells in brightness */
  @keyframes mg-fe-rule-wash {
    0%, 100% { border-left-color: rgba(74, 112, 148, 0.4); }
    50%       { border-left-color: rgba(74, 112, 148, 0.8); }
  }

  /* Slow inward fade for mist entries */
  @keyframes mg-fe-veil-drift {
    0%, 100% { opacity: 0.5; transform: scaleX(1); }
    50%       { opacity: 1;   transform: scaleX(1.015); }
  }

  @media (prefers-reduced-motion: reduce) {
    .mg-featured-item,
    .mg-featured-item::before,
    .mg-featured-item::after {
      animation: none !important;
      transition: none !important;
    }
  }

  /* ── Base shared styles ────────────────────────────────────── */

  .mg-featured-item {
    position: relative;
    padding: 1.1rem 1.1rem 1.1rem 1.5rem;
    margin-block: 0;
    overflow: hidden;
    box-sizing: border-box;
    max-width: 100%;
    line-height: 1.7;
    /* Reset border — each variant defines its own */
    border: none;
  }

  /* Dividing line between entries: a fine rain-grey rule */
  .mg-featured-item + .mg-featured-item {
    border-top: 1px solid rgba(160, 195, 220, 0.14);
  }

  /* Date line — slate-rain tone as base, variants may shift hue */
  .mg-featured-date {
    display: block;
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    font-style: normal;
    margin-bottom: 0.4rem;
    color: #7a9eb8;
  }

  /* Paragraph text — readable against the page's light background */
  .mg-featured-item p {
    margin: 0;
    color: inherit;
  }

  /* Links */
  .mg-featured-item a {
    color: #3a7ca8;
    text-decoration: none;
    border-bottom: 1px solid rgba(58, 124, 168, 0.35);
    transition: color 180ms ease, border-bottom-color 180ms ease;
  }

  .mg-featured-item a:hover,
  .mg-featured-item a:focus-visible {
    color: #1e5f8a;
    border-bottom-color: rgba(30, 95, 138, 0.65);
  }

  /* Accessible focus ring — rain-blue */
  .mg-featured-item a:focus-visible {
    outline: 2px solid rgba(58, 124, 168, 0.8);
    outline-offset: 2px;
    border-radius: 1px;
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 1 — Heavy rain curtain
     A dense diagonal rain-line texture fills the left third.
     Left rule: strong slate-blue. Date: rain grey.
     ============================================================== */
  .mg-featured-item:nth-child(8n+1) {
    border-left: 3px solid rgba(74, 112, 148, 0.7);
    padding-left: 1.6rem;
    animation: mg-fe-rule-wash 8s ease-in-out infinite;
  }

  .mg-featured-item:nth-child(8n+1)::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 56px;
    height: 100%;
    background-image: repeating-linear-gradient(
      168deg,
      transparent 0px,
      transparent 7px,
      rgba(160, 200, 228, 0.11) 7px,
      rgba(160, 200, 228, 0.11) 8px
    );
    animation: mg-fe-rain-scroll 2s linear infinite;
    pointer-events: none;
  }

  .mg-featured-item:nth-child(8n+1) .mg-featured-date {
    color: #6a9ab8;
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 2 — Deep cloud layer
     Dark indigo-grey wash, left rule in deep cloud colour.
     Evokes the banner's heaviest cloud masses.
     ============================================================== */
  .mg-featured-item:nth-child(8n+2) {
    border-left: 4px solid rgba(35, 52, 78, 0.7);
    padding-left: 1.6rem;
    background: linear-gradient(
      to right,
      rgba(26, 37, 58, 0.09) 0%,
      rgba(26, 37, 58, 0.04) 30%,
      transparent 60%
    );
    animation: mg-fe-cloud-sway 18s ease-in-out infinite;
  }

  .mg-featured-item:nth-child(8n+2)::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(
      ellipse 70% 80% at 0% 50%,
      rgba(30, 45, 74, 0.1) 0%,
      transparent 100%
    );
    pointer-events: none;
  }

  .mg-featured-item:nth-child(8n+2) .mg-featured-date {
    color: #8da8c4;
    letter-spacing: 0.2em;
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 3 — Mountain horizon
     Bold bottom-line in deep monsoon green.
     No left border. Spacious, ground-level feeling.
     ============================================================== */
  .mg-featured-item:nth-child(8n+3) {
    border-left: none;
    border-bottom: 2px solid rgba(42, 99, 56, 0.55);
    padding-left: 0.9rem;
    padding-bottom: 1.3rem;
    animation: mg-fe-horizon-breathe 12s ease-in-out infinite;
  }

  .mg-featured-item:nth-child(8n+3) + .mg-featured-item {
    border-top: none;
  }

  /* A faint green horizon wash at the foot */
  .mg-featured-item:nth-child(8n+3)::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 28px;
    background: linear-gradient(
      to top,
      rgba(26, 66, 38, 0.09),
      transparent
    );
    pointer-events: none;
  }

  .mg-featured-item:nth-child(8n+3) .mg-featured-date {
    color: #6fa880;
  }

  .mg-featured-item:nth-child(8n+3) a {
    color: #3a8c58;
    border-bottom-color: rgba(58, 140, 88, 0.35);
  }

  .mg-featured-item:nth-child(8n+3) a:hover,
  .mg-featured-item:nth-child(8n+3) a:focus-visible {
    color: #266840;
    border-bottom-color: rgba(38, 104, 64, 0.65);
  }

  .mg-featured-item:nth-child(8n+3) a:focus-visible {
    outline-color: rgba(58, 140, 88, 0.8);
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 4 — Low mist / horizon veil
     Full-width mist strip rising from the bottom.
     Soft blue-grey tonal wash with animated pulse.
     ============================================================== */
  .mg-featured-item:nth-child(8n+4) {
    border-left: 2px solid rgba(120, 155, 185, 0.45);
    padding-left: 1.5rem;
  }

  .mg-featured-item:nth-child(8n+4)::before {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 55%;
    background: linear-gradient(
      to top,
      rgba(26, 48, 72, 0.1) 0%,
      rgba(30, 50, 78, 0.05) 50%,
      transparent 100%
    );
    animation: mg-fe-veil-drift 11s ease-in-out infinite 1s;
    pointer-events: none;
    transform-origin: bottom center;
  }

  .mg-featured-item:nth-child(8n+4) .mg-featured-date {
    color: #7fa8c4;
    letter-spacing: 0.15em;
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 5 — Wide-margin rain scatter
     Full-width rain lines across the entry, low opacity,
     resembling rain through a window on wet paper.
     ============================================================== */
  .mg-featured-item:nth-child(8n+5) {
    border-left: 1px solid rgba(140, 180, 210, 0.4);
    padding-left: 1.5rem;
    background-image: repeating-linear-gradient(
      170deg,
      transparent 0px,
      transparent 22px,
      rgba(155, 196, 224, 0.07) 22px,
      rgba(155, 196, 224, 0.07) 23px
    );
    animation: mg-fe-rain-scroll 3.5s linear infinite;
  }

  .mg-featured-item:nth-child(8n+5) .mg-featured-date {
    color: #6898b8;
    letter-spacing: 0.13em;
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 6 — Gold Pahari accent (secondary; used sparingly)
     Echoes the banner's frame. Top rule only — miniature
     border-band convention. Gold date. No left border.
     ============================================================== */
  .mg-featured-item:nth-child(8n+6) {
    border-left: none;
    border-top: 1px solid rgba(200, 168, 75, 0.42);
    padding-left: 0.9rem;
    padding-top: 1.2rem;
  }

  .mg-featured-item:nth-child(8n+6) + .mg-featured-item {
    border-top: none;
  }

  /* Gold gradient bloom on the top rule */
  .mg-featured-item:nth-child(8n+6)::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(
      to right,
      transparent 0%,
      rgba(158, 126, 54, 0.4) 10%,
      rgba(200, 168, 75, 0.75) 35%,
      rgba(210, 178, 90, 0.85) 50%,
      rgba(200, 168, 75, 0.75) 65%,
      rgba(158, 126, 54, 0.4) 90%,
      transparent 100%
    );
    pointer-events: none;
  }

  .mg-featured-item:nth-child(8n+6) .mg-featured-date {
    color: #c8a84b;
    letter-spacing: 0.22em;
  }

  .mg-featured-item:nth-child(8n+6) a {
    color: #9e7e36;
    border-bottom-color: rgba(158, 126, 54, 0.38);
  }

  .mg-featured-item:nth-child(8n+6) a:hover,
  .mg-featured-item:nth-child(8n+6) a:focus-visible {
    color: #7a5e28;
    border-bottom-color: rgba(122, 94, 40, 0.65);
  }

  .mg-featured-item:nth-child(8n+6) a:focus-visible {
    outline-color: rgba(200, 168, 75, 0.8);
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 7 — Storm-anvil top mass
     Thick top border in deep cloud-blue, with a radial glow
     descending from it — the underside of a cumulonimbus.
     ============================================================== */
  .mg-featured-item:nth-child(8n+7) {
    border-left: none;
    border-top: 3px solid rgba(28, 45, 70, 0.75);
    padding-left: 0.9rem;
    padding-top: 1.2rem;
  }

  .mg-featured-item:nth-child(8n+7) + .mg-featured-item {
    border-top: none;
  }

  .mg-featured-item:nth-child(8n+7)::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 40px;
    background: linear-gradient(
      to bottom,
      rgba(22, 36, 58, 0.14) 0%,
      transparent 100%
    );
    pointer-events: none;
    animation: mg-fe-mist-pulse 10s ease-in-out infinite 2s;
  }

  .mg-featured-item:nth-child(8n+7) .mg-featured-date {
    color: #8aaac8;
    letter-spacing: 0.17em;
  }

  /* ══════════════════════════════════════════════════════════════
     VARIANT 8 — Wet earth / monsoon-drenched ground
     Left border in deep wet-soil green. Bottom receives a damp
     earth wash. Earthy, grounded in the landscape band.
     ============================================================== */
  .mg-featured-item:nth-child(8n+0) {
    border-left: 3px solid rgba(15, 48, 30, 0.65);
    padding-left: 1.6rem;
    background: linear-gradient(
      to right,
      rgba(13, 43, 24, 0.08) 0%,
      transparent 25%
    );
  }

  .mg-featured-item:nth-child(8n+0)::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(
      to right,
      rgba(26, 66, 38, 0.45),
      rgba(42, 99, 56, 0.28) 50%,
      rgba(26, 66, 38, 0.45)
    );
    pointer-events: none;
  }

  .mg-featured-item:nth-child(8n+0) .mg-featured-date {
    color: #5a9870;
    letter-spacing: 0.16em;
  }

  .mg-featured-item:nth-child(8n+0) a {
    color: #2e7a4a;
    border-bottom-color: rgba(46, 122, 74, 0.35);
  }

  .mg-featured-item:nth-child(8n+0) a:hover,
  .mg-featured-item:nth-child(8n+0) a:focus-visible {
    color: #1a5a34;
    border-bottom-color: rgba(26, 90, 52, 0.65);
  }

  .mg-featured-item:nth-child(8n+0) a:focus-visible {
    outline-color: rgba(46, 122, 74, 0.8);
  }

  /* ── Mobile ────────────────────────────────────────────────── */
  @media (max-width: 640px) {
    .mg-featured-item {
      padding-left: 1rem;
      padding-right: 0.5rem;
    }

    .mg-featured-item:nth-child(8n+1),
    .mg-featured-item:nth-child(8n+2),
    .mg-featured-item:nth-child(8n+0) {
      padding-left: 1.1rem;
    }

    .mg-featured-item:nth-child(8n+3),
    .mg-featured-item:nth-child(8n+6),
    .mg-featured-item:nth-child(8n+7) {
      padding-left: 0.75rem;
    }

    .mg-featured-date {
      letter-spacing: 0.1em;
    }
  }

  /* =========================================================
     Active Class Architecture Dark Mode Overrides
     ========================================================= */

  body.tsap-dark-mode .mg-epigraph p {
    color: var(--text-muted) !important;
  }

  body.tsap-dark-mode .mg-featured-item {
    color: var(--text-main) !important;
    border-top-color: rgba(255, 255, 255, 0.08) !important;
  }

  body.tsap-dark-mode .mg-featured-item a {
    color: #38bdf8 !important;
    border-bottom-color: rgba(56, 189, 248, 0.35) !important;
  }

  body.tsap-dark-mode .mg-featured-item a:hover {
    color: #7dd3fc !important;
    border-bottom-color: rgba(125, 211, 252, 0.65) !important;
    text-decoration: none !important;
  }

  body.tsap-dark-mode .mg-featured-item:nth-child(8n+2) {
    background: linear-gradient(
      to right,
      rgba(56, 189, 248, 0.05) 0%,
      transparent 60%
    ) !important;
  }

  body.tsap-dark-mode .mg-featured-item:nth-child(8n+4)::before {
    background: linear-gradient(
      to top,
      rgba(30, 41, 59, 0.6) 0%,
      transparent 100%
    ) !important;
  }

  body.tsap-dark-mode .mg-featured-item:nth-child(8n+8) {
    background: linear-gradient(
      to right,
      rgba(42, 99, 56, 0.1) 0%,
      transparent 25%
    ) !important;
  }
</style>
