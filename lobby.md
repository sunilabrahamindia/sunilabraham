---
layout: default
title: Lobby
description: "A fully illustrated Indian–Modern drawing room lobby with sofa, rug, coffee table, bookshelf and wooden newspaper stand. Responsive and accessible."
permalink: /lobby/
categories: [Project pages]
---
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Drawing Room Lobby</title>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: system-ui, -apple-system, Roboto, 'Segoe UI', sans-serif;
  background: linear-gradient(180deg, #f5e6d3 0%, #e8d5c4 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  overflow-x: hidden;
}

.room-container {
  width: 100%;
  max-width: 1200px;
  aspect-ratio: 16/10;
  position: relative;
}

svg {
  width: 100%;
  height: 100%;
  display: block;
}

.interactive {
  cursor: pointer;
  transition: all 0.3s ease;
}

.cushion:hover {
  transform: translateY(-5px);
}

.book:hover {
  opacity: 0.8;
}

.plant-leaf {
  animation: wiggle 3s ease-in-out infinite;
  transform-origin: bottom center;
}

.plant-leaf:nth-child(2) {
  animation-delay: 0.5s;
}

.plant-leaf:nth-child(3) {
  animation-delay: 1s;
}

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(2deg); }
  75% { transform: rotate(-2deg); }
}

.frame:hover {
  transform: rotate(-2deg);
}

.window-glow {
  transition: opacity 0.4s ease;
}

.window:hover .window-glow {
  opacity: 0.9;
}

.coffee-table:hover {
  filter: brightness(1.1);
}

.newspaper:hover {
  transform: translateX(3px);
}

.modal {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 30px 40px;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
  z-index: 1000;
  text-align: center;
  max-width: 90%;
}

.modal.active {
  display: block;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translate(-50%, -60%); }
  to { opacity: 1; transform: translate(-50%, -50%); }
}

.modal h2 {
  color: #8b4513;
  margin-bottom: 15px;
  font-size: 24px;
}

.modal p {
  color: #555;
  margin-bottom: 20px;
  line-height: 1.6;
}

.modal button {
  background: #d2691e;
  color: white;
  border: none;
  padding: 10px 25px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-family: inherit;
}

.modal button:hover {
  background: #a0522d;
}

.overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  z-index: 999;
}

.overlay.active {
  display: block;
}

@media (max-width: 768px) {
  .room-container {
    aspect-ratio: 4/5;
  }
  
  .modal {
    padding: 20px;
  }
  
  .modal h2 {
    font-size: 20px;
  }
}
</style>
</head>
<body>

<div class="room-container">
  <svg viewBox="0 0 1200 750" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="wallGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#f4e4d7;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#e6d5c3;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="floorGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#8b6f47;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#6b5436;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="sofaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#b8956f;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#9a7a5a;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="windowGlow" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#fffacd;stop-opacity:0.6" />
        <stop offset="100%" style="stop-color:#ffd700;stop-opacity:0.3" />
      </linearGradient>
    </defs>
    
    <!-- Wall -->
    <rect width="1200" height="500" fill="url(#wallGrad)"/>
    
    <!-- Floor -->
    <rect y="500" width="1200" height="250" fill="url(#floorGrad)"/>
    
    <!-- Window -->
    <g class="window interactive">
      <rect x="850" y="80" width="280" height="320" fill="#87ceeb" rx="8"/>
      <rect class="window-glow" x="850" y="80" width="280" height="320" fill="url(#windowGlow)" rx="8" opacity="0.5"/>
      <line x1="990" y1="80" x2="990" y2="400" stroke="#8b7355" stroke-width="6"/>
      <line x1="850" y1="240" x2="1130" y2="240" stroke="#8b7355" stroke-width="6"/>
      <rect x="845" y="75" width="290" height="330" fill="none" stroke="#6b5436" stroke-width="12" rx="8"/>
    </g>
    
    <!-- Picture Frame -->
    <g class="frame interactive">
      <rect x="100" y="120" width="200" height="160" fill="#8b4513" rx="4"/>
      <rect x="115" y="135" width="170" height="130" fill="#d2691e"/>
      <circle cx="200" cy="200" r="40" fill="#cd853f"/>
      <path d="M 160 220 Q 200 180 240 220" stroke="#8b4513" stroke-width="3" fill="none"/>
    </g>
    
    <!-- Bookshelf -->
    <rect x="50" y="320" width="180" height="280" fill="#8b4513"/>
    <rect x="60" y="330" width="160" height="260" fill="#a0522d"/>
    
    <!-- Books -->
    <a href="#" class="book interactive">
      <rect x="70" y="340" width="25" height="80" fill="#8b0000"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="100" y="340" width="25" height="80" fill="#006400"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="130" y="340" width="25" height="80" fill="#00008b"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="160" y="340" width="25" height="80" fill="#8b4513"/>
    </a>
    
    <a href="#" class="book interactive">
      <rect x="70" y="430" width="30" height="70" fill="#2f4f4f"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="105" y="430" width="25" height="70" fill="#dc143c"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="135" y="430" width="28" height="70" fill="#ff8c00"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="168" y="430" width="22" height="70" fill="#4682b4"/>
    </a>
    
    <a href="#" class="book interactive">
      <rect x="70" y="510" width="35" height="75" fill="#556b2f"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="110" y="510" width="28" height="75" fill="#800080"/>
    </a>
    <a href="#" class="book interactive">
      <rect x="143" y="510" width="32" height="75" fill="#d2691e"/>
    </a>
    
    <!-- Rug -->
    <ellipse cx="600" cy="630" rx="300" ry="100" fill="#d2691e" opacity="0.7"/>
    <ellipse cx="600" cy="630" rx="250" ry="80" fill="#cd853f" opacity="0.8"/>
    <ellipse cx="600" cy="630" rx="200" ry="60" fill="#daa520" opacity="0.6"/>
    
    <!-- Sofa -->
    <g class="sofa interactive" id="sofa">
      <!-- Left arm -->
      <path d="M 300 480 Q 280 450 290 420 L 310 420 L 320 480 Z" fill="url(#sofaGrad)"/>
      <!-- Right arm -->
      <path d="M 900 480 Q 920 450 910 420 L 890 420 L 880 480 Z" fill="url(#sofaGrad)"/>
      <!-- Main body -->
      <rect x="320" y="420" width="560" height="100" fill="url(#sofaGrad)" rx="10"/>
      <rect x="320" y="500" width="560" height="80" fill="#8b6f47" rx="5"/>
      <!-- Backrest -->
      <rect x="330" y="380" width="540" height="50" fill="#9a7a5a" rx="8"/>
    </g>
    
    <!-- Cushions -->
    <g class="cushion interactive">
      <rect x="380" y="430" width="80" height="60" fill="#20b2aa" rx="8"/>
      <ellipse cx="420" cy="460" rx="30" ry="20" fill="#1a9e96" opacity="0.5"/>
    </g>
    
    <g class="cushion interactive">
      <rect x="560" y="430" width="80" height="60" fill="#ff6347" rx="8"/>
      <ellipse cx="600" cy="460" rx="30" ry="20" fill="#e5533d" opacity="0.5"/>
    </g>
    
    <g class="cushion interactive">
      <rect x="740" y="430" width="80" height="60" fill="#daa520" rx="8"/>
      <ellipse cx="780" cy="460" rx="30" ry="20" fill="#c08e1c" opacity="0.5"/>
    </g>
    
    <!-- Coffee Table -->
    <g class="coffee-table interactive">
      <ellipse cx="600" cy="600" rx="150" ry="40" fill="#8b4513"/>
      <ellipse cx="600" cy="595" rx="150" ry="38" fill="#a0522d"/>
      <!-- Legs -->
      <rect x="480" y="600" width="12" height="40" fill="#6b4423"/>
      <rect x="708" y="600" width="12" height="40" fill="#6b4423"/>
      <rect x="530" y="600" width="12" height="40" fill="#6b4423"/>
      <rect x="658" y="600" width="12" height="40" fill="#6b4423"/>
    </g>
    
    <!-- Newspaper Stand -->
    <g>
      <rect x="950" y="500" width="80" height="120" fill="#8b4513" rx="4"/>
      <rect x="960" y="510" width="60" height="100" fill="#a0522d"/>
      
      <a href="#" class="newspaper interactive">
        <rect x="965" y="515" width="50" height="25" fill="#f5f5dc"/>
        <line x1="970" y1="520" x2="1005" y2="520" stroke="#333" stroke-width="1"/>
        <line x1="970" y1="525" x2="1005" y2="525" stroke="#333" stroke-width="1"/>
        <line x1="970" y1="530" x2="1000" y2="530" stroke="#333" stroke-width="1"/>
      </a>
      
      <a href="#" class="newspaper interactive">
        <rect x="965" y="545" width="50" height="25" fill="#fff8dc"/>
        <line x1="970" y1="550" x2="1005" y2="550" stroke="#333" stroke-width="1"/>
        <line x1="970" y1="555" x2="1005" y2="555" stroke="#333" stroke-width="1"/>
        <line x1="970" y1="560" x2="1000" y2="560" stroke="#333" stroke-width="1"/>
      </a>
      
      <a href="#" class="newspaper interactive">
        <rect x="965" y="575" width="50" height="25" fill="#faebd7"/>
        <line x1="970" y1="580" x2="1005" y2="580" stroke="#333" stroke-width="1"/>
        <line x1="970" y1="585" x2="1005" y2="585" stroke="#333" stroke-width="1"/>
        <line x1="970" y1="590" x2="1000" y2="590" stroke="#333" stroke-width="1"/>
      </a>
    </g>
    
    <!-- Plant -->
    <g>
      <!-- Pot -->
      <path d="M 1050 580 L 1070 640 L 1130 640 L 1150 580 Z" fill="#cd853f"/>
      <ellipse cx="1100" cy="580" rx="50" ry="15" fill="#a0522d"/>
      
      <!-- Leaves -->
      <ellipse class="plant-leaf" cx="1080" cy="540" rx="25" ry="45" fill="#228b22" transform="rotate(-20 1080 540)"/>
      <ellipse class="plant-leaf" cx="1100" cy="520" rx="28" ry="50" fill="#2e8b57" transform="rotate(0 1100 520)"/>
      <ellipse class="plant-leaf" cx="1120" cy="540" rx="25" ry="45" fill="#228b22" transform="rotate(20 1120 540)"/>
      <ellipse class="plant-leaf" cx="1090" cy="560" rx="22" ry="40" fill="#32cd32" transform="rotate(-10 1090 560)"/>
      <ellipse class="plant-leaf" cx="1110" cy="560" rx="22" ry="40" fill="#32cd32" transform="rotate(10 1110 560)"/>
    </g>
  </svg>
</div>

<div class="overlay" id="overlay"></div>
<div class="modal" id="modal">
  <h2 id="modalTitle">Welcome</h2>
  <p id="modalText">Have a seat and make yourself comfortable.</p>
  <button onclick="closeModal()">Close</button>
</div>

<script>
const modal = document.getElementById('modal');
const overlay = document.getElementById('overlay');
const modalTitle = document.getElementById('modalTitle');
const modalText = document.getElementById('modalText');

function showModal(title, text) {
  modalTitle.textContent = title;
  modalText.textContent = text;
  modal.classList.add('active');
  overlay.classList.add('active');
}

function closeModal() {
  modal.classList.remove('active');
  overlay.classList.remove('active');
}

overlay.addEventListener('click', closeModal);

document.getElementById('sofa').addEventListener('click', (e) => {
  e.preventDefault();
  showModal('The Sofa', 'Have a seat and make yourself comfortable. This is where ideas come to life.');
});

document.querySelector('.coffee-table').addEventListener('click', (e) => {
  e.preventDefault();
  showModal('Coffee Table', 'A perfect spot for your morning chai and evening conversations.');
});

document.querySelector('.window').addEventListener('click', (e) => {
  e.preventDefault();
  showModal('Window View', 'Look outside and let your mind wander. Fresh perspectives await.');
});

document.querySelector('.frame').addEventListener('click', (e) => {
  e.preventDefault();
  showModal('Wall Art', 'Every picture tells a story. This one speaks of warmth and heritage.');
});

document.querySelectorAll('.cushion').forEach((cushion, index) => {
  cushion.addEventListener('click', (e) => {
    e.preventDefault();
    const colors = ['Teal', 'Coral', 'Gold'];
    showModal(`${colors[index]} Cushion`, 'Comfort is in the details. Sink in and relax.');
  });
});
</script>

</body>
</html>
