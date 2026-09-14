---
layout: default
title: "No Shouting"
description: "No Shouting as a behavioural guideline of The Sunil Abraham Project (TSAP)."
categories: [TSAP Documentation]
permalink: /tsap/noshout/
created: 2026-09-14
---

<div class="noshout-box" aria-label="TSAP is a No Shouting Zone">
  <div class="noshout-pretitle">TSAP is a</div>
  <div class="noshout-title">
    <span class="noshout-icon" aria-hidden="true">🔇</span>
    No Shouting Zone
    <span class="noshout-icon" aria-hidden="true">🤫</span>
  </div>
  <div class="noshout-subtitle">Talk softly, please.</div>
</div>

## No Shouting Zone

The Sunil Abraham Project (TSAP) is a "No Shouting Zone". All contributors, including the Founder, as well as participants, are expected not to raise their voice or shout for any reason while participating in or contributing to TSAP.

We understand that there are situations where you may feel forced to shout because, if you speak "normally", people will not listen. In such situations, we should attempt to improve the environment rather than making your blood pressure rise. 

If you find it difficult to avoid shouting, it may be worth considering whether you need some support for your mental wellbeing.

In brief, TSAP is a no shouting zone. Do not shout, please.

<style>
.noshout-box {
  position: relative;
  overflow: hidden;
  margin: 1.5em 0 2em;
  padding: 2em 1.4em;
  border: 3px solid #7c3aed;
  border-radius: 18px;
  text-align: center;
  background:
    radial-gradient(circle at 15% 20%, rgba(59, 130, 246, 0.18), transparent 30%),
    radial-gradient(circle at 85% 80%, rgba(236, 72, 153, 0.18), transparent 30%),
    linear-gradient(135deg, #eff6ff, #faf5ff 50%, #fdf2f8);
  color: #172033;
  box-shadow:
    0 8px 25px rgba(79, 70, 229, 0.16),
    inset 0 0 30px rgba(255, 255, 255, 0.6);
  animation: noshout-float 4s ease-in-out infinite;
}

.noshout-box::before,
.noshout-box::after {
  content: "";
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0.45;
}

.noshout-box::before {
  width: 110px;
  height: 110px;
  top: -55px;
  left: -35px;
  background: #60a5fa;
  animation: noshout-orbit 7s ease-in-out infinite;
}

.noshout-box::after {
  width: 90px;
  height: 90px;
  right: -30px;
  bottom: -45px;
  background: #f472b6;
  animation: noshout-orbit 6s ease-in-out infinite reverse;
}

.noshout-pretitle {
  position: relative;
  z-index: 1;
  font-size: 1.15em;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: #4338ca;
}

.noshout-title {
  position: relative;
  z-index: 1;
  margin-top: 0.2em;
  font-size: clamp(1.8em, 5vw, 2.8em);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.02em;
  background: linear-gradient(90deg, #2563eb, #7c3aed, #db2777);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: noshout-glow 3s ease-in-out infinite;
}

.noshout-icon {
  display: inline-block;
  font-size: 0.75em;
  vertical-align: middle;
  animation: noshout-bounce 2.5s ease-in-out infinite;
}

.noshout-icon:last-child {
  animation-delay: 0.3s;
}

.noshout-subtitle {
  position: relative;
  z-index: 1;
  margin-top: 0.7em;
  font-size: 1.05em;
  font-weight: 600;
  color: #be185d;
}

@keyframes noshout-float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-4px);
  }
}

@keyframes noshout-orbit {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  50% {
    transform: translate(15px, 10px) scale(1.12);
  }
}

@keyframes noshout-glow {
  0%, 100% {
    filter: drop-shadow(0 0 0 rgba(124, 58, 237, 0));
  }
  50% {
    filter: drop-shadow(0 3px 10px rgba(124, 58, 237, 0.25));
  }
}

@keyframes noshout-bounce {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-5px) rotate(-5deg);
  }
}

/* =========================================================
   Active Class Architecture Dark Mode Overrides
   ========================================================= */

body.tsap-dark-mode .noshout-box {
  border-color: #38bdf8 !important;
  background:
    radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.15), transparent 35%),
    radial-gradient(circle at 85% 80%, rgba(30, 95, 191, 0.20), transparent 35%),
    linear-gradient(135deg, #0f172a, #1e293b 50%, #172334) !important;
  color: #f8fafc !important;
  box-shadow:
    0 8px 28px rgba(0, 0, 0, 0.45),
    inset 0 0 30px rgba(56, 189, 248, 0.05) !important;
}

body.tsap-dark-mode .noshout-box::before {
  background: #1e5fbf !important;
  opacity: 0.35;
}

body.tsap-dark-mode .noshout-box::after {
  background: #38bdf8 !important;
  opacity: 0.25;
}

body.tsap-dark-mode .noshout-pretitle {
  color: #94a3b8 !important;
}

body.tsap-dark-mode .noshout-title {
  background: linear-gradient(90deg, #38bdf8, #60a5fa, #93c5fd) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  color: transparent !important;
}

body.tsap-dark-mode .noshout-subtitle {
  color: #38bdf8 !important;
}

@media (max-width: 480px) {
  .noshout-box {
    padding: 1.6em 0.9em;
    border-radius: 14px;
  }

  .noshout-title {
    font-size: clamp(1.65em, 8vw, 2.2em);
    letter-spacing: -0.01em;
  }

  .noshout-icon {
    font-size: 0.65em;
  }

  .noshout-pretitle {
    font-size: 1.05em;
  }

  .noshout-subtitle {
    font-size: 1em;
  }
}

/* Accessibility: respect users who prefer reduced motion */
@media (prefers-reduced-motion: reduce) {
  .noshout-box,
  .noshout-box::before,
  .noshout-box::after,
  .noshout-title,
  .noshout-icon {
    animation: none !important;
  }
}
</style>
