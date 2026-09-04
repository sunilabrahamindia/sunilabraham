---
layout: default
title: The Witness
categories: [Project pages, Tito Dutta, TSAP Exhibition]
description: A visual meditation on the Witness — awareness that remains still while the cosmos moves.
permalink: /tito/witness/
created: 2026-09-05
---

<div class="witness-universe-container" role="region" aria-label="The Witness - An interactive contemplative visual experience">
  <style>
    .witness-universe-container {
      position: relative;
      width: 100%;
      height: 100vh;
      height: 100dvh;
      min-height: 540px;
      background-color: #030308;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #e2e8f0;
      box-sizing: border-box;
      user-select: none;
      -webkit-user-select: none;
    }

    .witness-universe-container *,
    .witness-universe-container *::before,
    .witness-universe-container *::after {
      box-sizing: inherit;
    }

    .witness-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      display: block;
      pointer-events: none;
    }

    .witness-nebula-layer {
      position: absolute;
      inset: -20%;
      width: 140%;
      height: 140%;
      background: 
        radial-gradient(ellipse at 48% 52%, rgba(26, 16, 61, 0.45) 0%, transparent 60%),
        radial-gradient(ellipse at 55% 45%, rgba(12, 43, 77, 0.35) 0%, transparent 65%),
        radial-gradient(circle at 50% 50%, rgba(4, 7, 24, 0.8) 0%, #030308 90%);
      z-index: 0;
      pointer-events: none;
      filter: blur(40px);
      will-change: transform;
      transform: translate3d(0, 0, 0);
    }

    /* Strict isolation against theme card/main styles */
    .witness-universe-container .witness-core {
      position: relative;
      z-index: 2;
      width: 88vw;
      max-width: 580px;
      min-width: 260px;
      aspect-ratio: 16 / 10;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
      background: transparent !important;
      background-color: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      box-shadow: none !important;
      outline: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }

    @media (min-width: 768px) {
      .witness-universe-container .witness-core {
        width: 48vw;
        max-width: 620px;
      }
    }

    @media (min-width: 1440px) {
      .witness-universe-container .witness-core {
        width: 38vw;
        max-width: 680px;
      }
    }

    .witness-svg {
      width: 100%;
      height: 100%;
      overflow: visible;
      filter: drop-shadow(0 0 45px rgba(37, 25, 94, 0.55));
    }

    .witness-aura-pulse {
      transform-origin: 250px 150px;
      animation: witnessAuraGlow 11s ease-in-out infinite alternate;
    }

    .witness-iris-spin {
      transform-origin: 250px 150px;
      animation: witnessIrisDrift 95s linear infinite;
    }

    .witness-gaze-group {
      will-change: transform;
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .witness-lid {
      transform-origin: 250px 150px;
      transition: transform 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .witness-scripture {
      position: absolute;
      bottom: 8%;
      left: 0;
      width: 100%;
      text-align: center;
      z-index: 3;
      pointer-events: none;
      padding: 0 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
    }

    .witness-title {
      margin: 0;
      font-size: 0.82rem;
      letter-spacing: 0.42em;
      text-transform: uppercase;
      font-weight: 300;
      color: rgba(215, 226, 255, 0.72);
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 2.8s ease, transform 2.8s ease;
    }

    .witness-subtext {
      margin: 0;
      font-size: 0.7rem;
      letter-spacing: 0.15em;
      line-height: 1.6;
      font-weight: 200;
      color: rgba(147, 163, 204, 0.55);
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 3.2s ease 1.6s, transform 3.2s ease 1.6s;
    }

    .witness-scripture.revealed .witness-title,
    .witness-scripture.revealed .witness-subtext {
      opacity: 1;
      transform: translateY(0);
    }

    @keyframes witnessAuraGlow {
      0% {
        opacity: 0.55;
        transform: scale(0.97);
      }
      50% {
        opacity: 0.85;
        transform: scale(1.025);
      }
      100% {
        opacity: 0.6;
        transform: scale(0.98);
      }
    }

    @keyframes witnessIrisDrift {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    @media (prefers-reduced-motion: reduce) {
      .witness-aura-pulse,
      .witness-iris-spin {
        animation: none !important;
      }
      .witness-gaze-group,
      .witness-lid {
        transition: none !important;
      }
    }
  </style>

  <div class="witness-nebula-layer" id="witnessNebula" aria-hidden="true"></div>
  <canvas class="witness-canvas" id="witnessCanvas" aria-hidden="true"></canvas>

  <div class="witness-core">
    <svg class="witness-svg" viewBox="0 0 500 300" role="img" aria-labelledby="witnessTitleId witnessDescId">
      <title id="witnessTitleId">The Witness - The Third Eye</title>
      <desc id="witnessDescId">An open spiritual third eye floating motionless amid an ancient moving cosmos of stars and nebulas.</desc>
      <defs>
        <radialGradient id="gradAura" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#4c2889" stop-opacity="0.32" />
          <stop offset="45%" stop-color="#162354" stop-opacity="0.2" />
          <stop offset="75%" stop-color="#091129" stop-opacity="0.08" />
          <stop offset="100%" stop-color="#030308" stop-opacity="0" />
        </radialGradient>

        <radialGradient id="gradVessel" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#090d1f" />
          <stop offset="70%" stop-color="#04060d" />
          <stop offset="100%" stop-color="#020306" />
        </radialGradient>

        <radialGradient id="gradIrisBase" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#010206" />
          <stop offset="28%" stop-color="#0b173b" />
          <stop offset="58%" stop-color="#2a1b63" />
          <stop offset="78%" stop-color="#16517e" />
          <stop offset="91%" stop-color="#2dd4bf" stop-opacity="0.9" />
          <stop offset="97%" stop-color="#d4af37" stop-opacity="0.5" />
          <stop offset="100%" stop-color="#070a14" stop-opacity="0.95" />
        </radialGradient>

        <linearGradient id="gradGoldRim" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#795548" stop-opacity="0.1" />
          <stop offset="25%" stop-color="#bfa15f" stop-opacity="0.45" />
          <stop offset="50%" stop-color="#fdf4d7" stop-opacity="0.8" />
          <stop offset="75%" stop-color="#bfa15f" stop-opacity="0.45" />
          <stop offset="100%" stop-color="#795548" stop-opacity="0.1" />
        </linearGradient>

        <clipPath id="witnessEyeClip">
          <path d="M 50 150 C 130 65, 370 65, 450 150 C 370 235, 130 235, 50 150 Z" />
        </clipPath>
      </defs>

      <ellipse class="witness-aura-pulse" cx="250" cy="150" rx="220" ry="120" fill="url(#gradAura)" />

      <path d="M 50 150 C 130 65, 370 65, 450 150 C 370 235, 130 235, 50 150 Z" 
            fill="url(#gradVessel)" stroke="#1a2238" stroke-width="1.2" />

      <g clip-path="url(#witnessEyeClip)">
        <rect x="0" y="0" width="500" height="300" fill="#04060f" opacity="0.6" />
        
        <g id="witnessGazeGroup" class="witness-gaze-group">
          <circle cx="250" cy="150" r="76" fill="none" stroke="rgba(45, 212, 191, 0.18)" stroke-width="1.5" />
          <circle cx="250" cy="150" r="74" fill="url(#gradIrisBase)" />

          <g class="witness-iris-spin" opacity="0.65">
            <line x1="250" y1="78" x2="250" y2="222" stroke="#5eead4" stroke-width="0.35" stroke-opacity="0.4" />
            <line x1="178" y1="150" x2="322" y2="150" stroke="#5eead4" stroke-width="0.35" stroke-opacity="0.4" />
            <line x1="199" y1="99" x2="301" y2="201" stroke="#93c5fd" stroke-width="0.35" stroke-opacity="0.4" />
            <line x1="199" y1="201" x2="301" y2="99" stroke="#93c5fd" stroke-width="0.35" stroke-opacity="0.4" />
            <line x1="222" y1="81" x2="278" y2="219" stroke="#c084fc" stroke-width="0.35" stroke-opacity="0.3" />
            <line x1="278" y1="81" x2="222" y2="219" stroke="#c084fc" stroke-width="0.35" stroke-opacity="0.3" />
            
            <circle cx="232" cy="120" r="0.75" fill="#ffffff" opacity="0.8" />
            <circle cx="268" cy="132" r="0.85" fill="#fef08a" opacity="0.75" />
            <circle cx="274" cy="172" r="0.6" fill="#67e8f9" opacity="0.85" />
            <circle cx="225" cy="168" r="0.75" fill="#ffffff" opacity="0.7" />
            <circle cx="242" cy="186" r="0.65" fill="#e9d5ff" opacity="0.7" />
            <circle cx="258" cy="112" r="0.65" fill="#ffffff" opacity="0.9" />
          </g>

          <circle cx="250" cy="150" r="32" fill="#010204" />
          <circle cx="250" cy="150" r="32.5" fill="none" stroke="rgba(12, 18, 38, 0.9)" stroke-width="0.8" />

          <circle cx="239" cy="141" r="3.2" fill="#ffffff" opacity="0.88" />
          <circle cx="243" cy="138" r="1.4" fill="#a5f3fc" opacity="0.7" />
          <circle cx="261" cy="159" r="1.2" fill="#ffffff" opacity="0.35" />
        </g>
      </g>

      <path d="M 50 150 C 130 65, 370 65, 450 150" 
            fill="none" stroke="url(#gradGoldRim)" stroke-width="1.6" stroke-linecap="round" />
      <path d="M 50 150 C 130 235, 370 235, 450 150" 
            fill="none" stroke="rgba(180, 160, 115, 0.25)" stroke-width="1.2" stroke-linecap="round" />

      <path id="witnessUpperLid" class="witness-lid" 
            d="M 46 150 C 130 40, 370 40, 454 150 C 370 55, 130 55, 46 150 Z" 
            fill="#030308" opacity="0" />
      <path id="witnessLowerLid" class="witness-lid" 
            d="M 46 150 C 130 260, 370 260, 454 150 C 370 245, 130 245, 46 150 Z" 
            fill="#030308" opacity="0" />
    </svg>
  </div>

  <div class="witness-scripture" id="witnessScripture" aria-live="polite">
    <h1 class="witness-title">The Witness</h1>
    <p class="witness-subtext">The First Consecrated Deity<br>The Sunil Abraham Project</p>
  </div>

  <script>
    (function () {
      'use strict';

      const container = document.querySelector('.witness-universe-container');
      const canvas = document.getElementById('witnessCanvas');
      const ctx = canvas.getContext('2d');
      const nebula = document.getElementById('witnessNebula');
      const gazeGroup = document.getElementById('witnessGazeGroup');
      const upperLid = document.getElementById('witnessUpperLid');
      const lowerLid = document.getElementById('witnessLowerLid');
      const scripture = document.getElementById('witnessScripture');

      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      setTimeout(() => {
        if (scripture) scripture.classList.add('revealed');
      }, 1400);

      let width = 0;
      let height = 0;
      let dpr = 1;
      let stars = [];
      let animId = null;
      let isVisible = true;

      let mouseX = 0;
      let mouseY = 0;
      let currentX = 0;
      let currentY = 0;

      function initDimensions() {
        if (!container || !canvas) return;
        width = container.clientWidth;
        height = container.clientHeight;
        dpr = Math.min(window.devicePixelRatio || 1, 2);

        canvas.width = Math.floor(width * dpr);
        canvas.height = Math.floor(height * dpr);
        ctx.scale(dpr, dpr);

        buildStars();
      }

      function buildStars() {
        stars = [];
        const baseArea = 1920 * 1080;
        const currentArea = width * height;
        const count = Math.floor(Math.min(650, Math.max(160, (currentArea / baseArea) * 550)));

        for (let i = 0; i < count; i++) {
          stars.push({
            x: Math.random() * width,
            y: Math.random() * height,
            size: Math.random() * 1.35 + 0.35,
            depth: Math.random() * 0.85 + 0.15,
            alpha: Math.random() * 0.7 + 0.2,
            baseAlpha: Math.random() * 0.6 + 0.25,
            twinkleSpeed: Math.random() * 0.015 + 0.004,
            hue: Math.random() > 0.82 ? (Math.random() > 0.5 ? 210 : 265) : 0
          });
        }
      }

      let time = 0;
      function renderCanvas() {
        if (!isVisible) return;

        ctx.clearRect(0, 0, width, height);

        currentX += (mouseX - currentX) * 0.035;
        currentY += (mouseY - currentY) * 0.035;

        time += 0.008;

        for (let i = 0; i < stars.length; i++) {
          const s = stars[i];

          if (!prefersReducedMotion) {
            s.y -= s.depth * 0.18;
            if (s.y < -4) s.y = height + 4;
            s.alpha = s.baseAlpha + Math.sin(time * 8 * s.twinkleSpeed + i) * 0.22;
          }

          const px = s.x + currentX * s.depth * 18;
          const py = s.y + currentY * s.depth * 18;

          ctx.beginPath();
          ctx.arc(px, py, s.size * (s.depth * 0.6 + 0.6), 0, Math.PI * 2);

          if (s.hue > 0) {
            ctx.fillStyle = `hsla(${s.hue}, 80%, 75%, ${Math.max(0.05, Math.min(1, s.alpha))})`;
          } else {
            ctx.fillStyle = `rgba(255, 255, 255, ${Math.max(0.05, Math.min(1, s.alpha))})`;
          }
          ctx.fill();
        }

        if (!prefersReducedMotion) {
          nebula.style.transform = `translate3d(${currentX * -15}px, ${currentY * -15}px, 0)`;
          
          const eyeShiftX = currentX * 4.2;
          const eyeShiftY = currentY * 3.8;
          gazeGroup.style.transform = `translate3d(${eyeShiftX}px, ${eyeShiftY}px, 0)`;
        }

        animId = requestAnimationFrame(renderCanvas);
      }

      function handlePointerMove(e) {
        if (prefersReducedMotion) return;
        const rect = container.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
        const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;

        const normX = ((clientX - rect.left) / rect.width) * 2 - 1;
        const normY = ((clientY - rect.top) / rect.height) * 2 - 1;

        mouseX = Math.max(-1, Math.min(1, normX));
        mouseY = Math.max(-1, Math.min(1, normY));
      }

      function handlePointerLeave() {
        mouseX = 0;
        mouseY = 0;
      }

      function triggerBlink() {
        if (prefersReducedMotion || !isVisible) {
          scheduleNextBlink();
          return;
        }

        upperLid.style.opacity = '1';
        lowerLid.style.opacity = '1';
        upperLid.style.transform = 'translateY(48px) scaleY(1.4)';
        lowerLid.style.transform = 'translateY(-48px) scaleY(1.4)';

        setTimeout(() => {
          upperLid.style.transform = 'translateY(0) scaleY(1)';
          lowerLid.style.transform = 'translateY(0) scaleY(1)';
          setTimeout(() => {
            upperLid.style.opacity = '0';
            lowerLid.style.opacity = '0';
            scheduleNextBlink();
          }, 240);
        }, 160);
      }

      function scheduleNextBlink() {
        const nextInterval = Math.random() * 11000 + 8000;
        setTimeout(triggerBlink, nextInterval);
      }

      let autoAngle = 0;
      function updateAutonomousDrift() {
        if (!prefersReducedMotion && mouseX === 0 && mouseY === 0) {
          autoAngle += 0.009;
          currentX = Math.cos(autoAngle) * 0.28;
          currentY = Math.sin(autoAngle * 0.8) * 0.22;
        }
      }
      setInterval(updateAutonomousDrift, 32);

      function onVisibilityChange() {
        isVisible = !document.hidden;
        if (isVisible && !animId) {
          animId = requestAnimationFrame(renderCanvas);
        } else if (!isVisible && animId) {
          cancelAnimationFrame(animId);
          animId = null;
        }
      }

      let resizeTimeout;
      function onResize() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(initDimensions, 100);
      }

      window.addEventListener('resize', onResize, { passive: true });
      document.addEventListener('visibilitychange', onVisibilityChange);
      container.addEventListener('mousemove', handlePointerMove, { passive: true });
      container.addEventListener('mouseleave', handlePointerLeave, { passive: true });

      initDimensions();
      animId = requestAnimationFrame(renderCanvas);
      scheduleNextBlink();
    })();
  </script>
</div>
