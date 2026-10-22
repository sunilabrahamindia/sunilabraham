---
layout: default
title: "The Human Brain"
categories: [TSAP Exhibition, Tito Dutta]
hidden_categories:
  - Pages needing regular archiving
authors: [Tito Dutta]
description: "An interactive exploration of the human brain, its major regions, and the networks that support perception, movement, memory and thought."
permalink: /tito/brain/
created: 2026-10-22
---

{% include author-date.html %}


Explore the brain as a living system of connected structures. Rotate the model, select a region, and discover some of the functions it contributes to - from interpreting sensory information to coordinating movement, memory and language. These functions are distributed across connected areas; the descriptions here are an introduction, not a map of isolated mental abilities.

The interactive model below is designed for exploration on desktop and mobile. Drag to rotate, use the controls to zoom, and select a labelled region to read about it. If the 3D scene does not load, the region guide remains available below.

<div id="tito-brain-explorer" aria-label="Interactive 3D human brain explorer">
  <div class="brain-toolbar">
    <div>
      <p class="brain-eyebrow">INTERACTIVE ANATOMY</p>
      <h2 id="brain-current-title">Explore the brain</h2>
      <p id="brain-current-summary" aria-live="polite">Select a region in the model or use the region list.</p>
    </div>
    <div class="brain-view-controls" aria-label="Model controls">
      <button type="button" id="brain-reset">Reset view</button>
      <button type="button" id="brain-auto" aria-pressed="false">Auto-rotate: off</button>
    </div>
  </div>

  <div class="brain-stage">
    <div id="brain-canvas-wrap">
      <canvas id="brain-canvas" aria-label="Rotatable 3D brain model. Select a region using the region buttons below."></canvas>
      <div id="brain-loading" role="status">Preparing the 3D model...</div>
      <div class="brain-stage-hint">Drag to rotate · Scroll or pinch to zoom</div>
    </div>
    <aside class="brain-info" aria-labelledby="brain-info-title">
      <p class="brain-eyebrow">REGION GUIDE</p>
      <h3 id="brain-info-title">A connected system</h3>
      <p id="brain-info-copy">Choose a region to explore its location and some of its better-established functions.</p>
      <h4>Functions and roles</h4>
      <ul id="brain-function-list">
        <li>Perception and interpretation</li>
        <li>Movement and coordination</li>
        <li>Learning, memory and attention</li>
      </ul>
      <p class="brain-note">The colours are a navigation aid, not a clinical or diagnostic classification.</p>
    </aside>
  </div>

  <div class="brain-region-list" aria-label="Choose a brain region">
    <button type="button" data-region="frontal" aria-pressed="false">Frontal lobe</button>
    <button type="button" data-region="parietal" aria-pressed="false">Parietal lobe</button>
    <button type="button" data-region="temporal" aria-pressed="false">Temporal lobe</button>
    <button type="button" data-region="occipital" aria-pressed="false">Occipital lobe</button>
    <button type="button" data-region="cerebellum" aria-pressed="false">Cerebellum</button>
    <button type="button" data-region="brainstem" aria-pressed="false">Brainstem</button>
    <button type="button" data-region="hippocampus" aria-pressed="false">Hippocampus</button>
    <button type="button" data-region="thalamus" aria-pressed="false">Thalamus</button>
  </div>
  <p class="brain-disclaimer">This is an educational visualisation. The external surface is a simplified model, and deeper structures are represented schematically rather than exposed as a precise medical reconstruction.</p>
</div>

## A guide to the regions

<div class="brain-guide-grid">
  <section>
    <h3>Frontal lobe</h3>
    <p>Contributes to planning, decision-making, voluntary movement, working memory and aspects of social behaviour. These functions depend on wider networks, not on the frontal lobe alone.</p>
  </section>
  <section>
    <h3>Parietal lobe</h3>
    <p>Integrates information from the senses and contributes to body awareness, spatial processing and directing attention.</p>
  </section>
  <section>
    <h3>Temporal lobe</h3>
    <p>Contains areas involved in hearing, aspects of language comprehension, object recognition and memory-related processing.</p>
  </section>
  <section>
    <h3>Occipital lobe</h3>
    <p>Contains visual-processing areas that analyse features such as edges, orientation, colour and motion as part of a wider visual system.</p>
  </section>
  <section>
    <h3>Cerebellum</h3>
    <p>Helps coordinate movement, timing and balance, and contributes to motor learning and some cognitive processes.</p>
  </section>
  <section>
    <h3>Brainstem</h3>
    <p>Connects the brain with the spinal cord and supports essential functions including breathing, alertness and cardiovascular regulation.</p>
  </section>
  <section>
    <h3>Hippocampus</h3>
    <p>A structure deep in the temporal lobe that is important for forming many kinds of new memories and for aspects of spatial navigation.</p>
  </section>
  <section>
    <h3>Thalamus</h3>
    <p>Acts as a major relay and processing hub for much sensory information and participates in attention, arousal and communication across brain networks.</p>
  </section>
</div>

{% include navbox-tito.html %}

<style>
#tito-brain-explorer {
  --brain-bg: #f4f7fb;
  --brain-panel: #ffffff;
  --brain-text: #172b4d;
  --brain-muted: #425466;
  --brain-border: #cbd5e1;
  --brain-accent: #155eef;
  --brain-accent-dark: #1047b8;
  color: var(--brain-text);
  margin: 1.5rem 0 2rem;
}
#tito-brain-explorer * { box-sizing: border-box; }
#tito-brain-explorer .brain-toolbar {
  display: flex; align-items: flex-start; justify-content: space-between;
  gap: 1rem; padding: 1.1rem 1.2rem; border: 1px solid var(--brain-border);
  border-bottom: 0; border-radius: 12px 12px 0 0; background: var(--brain-panel);
}
#tito-brain-explorer .brain-eyebrow {
  margin: 0 0 .35rem; color: var(--brain-accent); font-size: .75rem;
  font-weight: 750; letter-spacing: .09em;
}
#tito-brain-explorer h2 { margin: 0 0 .35rem; font-size: clamp(1.3rem, 3vw, 1.8rem); }
#tito-brain-explorer #brain-current-summary { margin: 0; color: var(--brain-muted); max-width: 42rem; }
#tito-brain-explorer .brain-view-controls { display: flex; flex-wrap: wrap; gap: .5rem; }
#tito-brain-explorer button {
  font: inherit; font-size: .9rem; line-height: 1.35; cursor: pointer;
  color: var(--brain-accent-dark); background: #fff; border: 1px solid #8da9dc;
  border-radius: 7px; padding: .6rem .8rem; min-height: 42px;
}
#tito-brain-explorer button:hover { background: #eaf1ff; border-color: var(--brain-accent); }
#tito-brain-explorer button:focus-visible { outline: 3px solid #f0a202; outline-offset: 3px; }
#tito-brain-explorer .brain-stage {
  display: grid; grid-template-columns: minmax(0, 1.65fr) minmax(260px, .85fr);
  min-height: 440px; border: 1px solid var(--brain-border); background: var(--brain-bg);
}
#tito-brain-explorer #brain-canvas-wrap { min-height: 440px; position: relative; overflow: hidden; }
#tito-brain-explorer #brain-canvas { display: block; width: 100%; height: 100%; min-height: 440px; touch-action: pan-y; outline: none; }
#tito-brain-explorer #brain-loading {
  position: absolute; inset: 0; display: grid; place-items: center;
  padding: 2rem; text-align: center; color: var(--brain-muted); pointer-events: none;
}
#tito-brain-explorer .brain-stage-hint {
  position: absolute; bottom: .8rem; left: .8rem; padding: .4rem .6rem;
  border-radius: 5px; background: rgba(255,255,255,.92); color: #334155; font-size: .78rem;
}
#tito-brain-explorer .brain-info { padding: 1.2rem; background: var(--brain-panel); border-left: 1px solid var(--brain-border); }
#tito-brain-explorer .brain-info h3 { margin: 0 0 .7rem; font-size: 1.4rem; }
#tito-brain-explorer .brain-info h4 { margin: 1.2rem 0 .4rem; }
#tito-brain-explorer .brain-info p { line-height: 1.6; }
#tito-brain-explorer #brain-function-list { padding-left: 1.2rem; line-height: 1.65; }
#tito-brain-explorer .brain-note, #tito-brain-explorer .brain-disclaimer { color: var(--brain-muted); font-size: .88rem; line-height: 1.55; }
#tito-brain-explorer .brain-region-list {
  display: flex; flex-wrap: wrap; gap: .55rem; padding: 1rem;
  border: 1px solid var(--brain-border); border-top: 0; background: var(--brain-panel);
}
#tito-brain-explorer .brain-region-list button[aria-pressed="true"] {
  color: #fff; background: var(--brain-accent-dark); border-color: var(--brain-accent-dark);
}
#tito-brain-explorer .brain-disclaimer { margin: .75rem 0 0; }
.brain-guide-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; margin: 1rem 0 2rem; }
.brain-guide-grid section { border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; }
.brain-guide-grid h3 { margin-top: 0; }
.brain-guide-grid p { margin-bottom: 0; line-height: 1.65; }
body.tsap-dark-mode #tito-brain-explorer {
  --brain-bg: #111827; --brain-panel: #172033; --brain-text: #f1f5f9;
  --brain-muted: #c0ccdc; --brain-border: #475569; --brain-accent: #93c5fd;
  --brain-accent-dark: #1d4ed8;
}
body.tsap-dark-mode #tito-brain-explorer button { color: #dbeafe; background: #1e293b; border-color: #64748b; }
body.tsap-dark-mode #tito-brain-explorer button:hover { background: #334155; }
body.tsap-dark-mode #tito-brain-explorer .brain-region-list button[aria-pressed="true"] { background: #1d4ed8; color: #fff; }
body.tsap-dark-mode #tito-brain-explorer .brain-stage-hint { background: rgba(15,23,42,.94); color: #f1f5f9; }
body.tsap-dark-mode .brain-guide-grid section { border-color: #475569; }
@media (max-width: 760px) {
  #tito-brain-explorer .brain-toolbar { flex-direction: column; }
  #tito-brain-explorer .brain-stage { grid-template-columns: 1fr; }
  #tito-brain-explorer #brain-canvas-wrap, #tito-brain-explorer #brain-canvas { min-height: 340px; height: 340px; }
  #tito-brain-explorer .brain-info { border-left: 0; border-top: 1px solid var(--brain-border); }
  .brain-guide-grid { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  #tito-brain-explorer *, .brain-guide-grid * { scroll-behavior: auto !important; transition: none !important; animation: none !important; }
}
</style>

<script type="module">
(() => {
  const root = document.getElementById('tito-brain-explorer');
  if (!root) return;

  const regions = {
    frontal: { name: 'Frontal lobe', colour: 0x3288d8, summary: 'The front portion of the cerebral cortex contributes to planning, voluntary movement and flexible behaviour.', functions: ['Planning and decision-making', 'Voluntary movement', 'Working memory and attention', 'Aspects of social behaviour'] },
    parietal: { name: 'Parietal lobe', colour: 0x54a879, summary: 'The parietal lobe integrates sensory information and helps represent the body and surrounding space.', functions: ['Touch and body sensation', 'Spatial awareness', 'Sensory integration', 'Attention to locations and objects'] },
    temporal: { name: 'Temporal lobe', colour: 0xe6a23c, summary: 'The temporal lobe is involved in hearing, aspects of language, recognition and memory-related processing.', functions: ['Auditory processing', 'Aspects of language comprehension', 'Object and face recognition', 'Memory-related processing'] },
    occipital: { name: 'Occipital lobe', colour: 0xd76572, summary: 'The occipital lobe contains cortical areas central to processing visual information.', functions: ['Visual features and patterns', 'Colour and orientation processing', 'Motion-sensitive processing', 'Communication with other visual areas'] },
    cerebellum: { name: 'Cerebellum', colour: 0x9271c8, summary: 'The cerebellum helps coordinate timing and accuracy of movement and also contributes to learning and cognition.', functions: ['Movement coordination', 'Balance and posture', 'Motor learning', 'Timing and prediction'] },
    brainstem: { name: 'Brainstem', colour: 0x9a8170, summary: 'The brainstem connects the brain and spinal cord and contains circuits essential for life-sustaining functions.', functions: ['Breathing regulation', 'Cardiovascular regulation', 'Sleep and alertness', 'Pathways between brain and body'] },
    hippocampus: { name: 'Hippocampus', colour: 0x35a6a0, summary: 'The hippocampus is a deep structure important for forming many new memories and for spatial navigation.', functions: ['Formation of new memories', 'Memory organisation', 'Spatial navigation', 'Contextual learning'] },
    thalamus: { name: 'Thalamus', colour: 0x8a93a5, summary: 'The thalamus is a major hub for routing and processing information across the brain.', functions: ['Relay of much sensory information', 'Attention and arousal', 'Communication between cortical areas', 'Coordination of information flow'] }
  };

  const title = root.querySelector('#brain-info-title');
  const copy = root.querySelector('#brain-info-copy');
  const list = root.querySelector('#brain-function-list');
  const headline = root.querySelector('#brain-current-title');
  const summary = root.querySelector('#brain-current-summary');
  const loading = root.querySelector('#brain-loading');
  const regionButtons = [...root.querySelectorAll('[data-region]')];
  const canvas = root.querySelector('#brain-canvas');
  let renderer, scene, camera, controls, raycaster, pointer, brainParts = [], activeRegion = null, autoRotate = false;

  function chooseRegion(key) {
    const data = regions[key];
    if (!data) return;
    activeRegion = key;
    title.textContent = data.name;
    copy.textContent = data.summary;
    headline.textContent = data.name;
    summary.textContent = data.summary;
    list.replaceChildren(...data.functions.map(text => {
      const li = document.createElement('li'); li.textContent = text; return li;
    }));
    regionButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.region === key)));
    brainParts.forEach(part => {
      const selected = part.userData.region === key;
      part.material.emissive.setHex(selected ? 0x26384d : 0x000000);
      part.material.emissiveIntensity = selected ? 0.42 : 0.04;
    });
  }
  regionButtons.forEach(button => button.addEventListener('click', () => chooseRegion(button.dataset.region)));

  async function start() {
    try {
      const THREE = await import('https://cdn.jsdelivr.net/npm/three@0.164.1/build/three.module.js');
      const { OrbitControls } = await import('https://cdn.jsdelivr.net/npm/three@0.164.1/examples/jsm/controls/OrbitControls.js');
      scene = new THREE.Scene();
      scene.background = new THREE.Color(0xf4f7fb);
      camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
      camera.position.set(0, 1.5, 8.8);
      renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.8));
      renderer.outputColorSpace = THREE.SRGBColorSpace;
      renderer.setClearColor(0xf4f7fb, 1);
      controls = new OrbitControls(camera, canvas);
      controls.enableDamping = true;
      controls.dampingFactor = 0.06;
      controls.minDistance = 5;
      controls.maxDistance = 13;
      controls.target.set(0, 0.1, 0);
      raycaster = new THREE.Raycaster();
      pointer = new THREE.Vector2();

      scene.add(new THREE.HemisphereLight(0xffffff, 0x9aa9bf, 2.1));
      const keyLight = new THREE.DirectionalLight(0xffffff, 2.2);
      keyLight.position.set(4, 6, 7); scene.add(keyLight);
      const fillLight = new THREE.DirectionalLight(0xb7d9ff, 1.1);
      fillLight.position.set(-5, 2, -4); scene.add(fillLight);

      const brain = new THREE.Group();
      scene.add(brain);
      const materials = {};
      Object.entries(regions).forEach(([key, data]) => {
        materials[key] = new THREE.MeshStandardMaterial({ color: data.colour, roughness: 0.72, metalness: 0.02, emissive: 0x000000 });
      });
      function addPart(key, geometry, position, scale, rotation = [0,0,0]) {
        const mesh = new THREE.Mesh(geometry, materials[key]);
        mesh.position.set(...position); mesh.scale.set(...scale); mesh.rotation.set(...rotation);
        mesh.userData.region = key; brain.add(mesh); brainParts.push(mesh); return mesh;
      }
      // Segmented educational model. Separate coloured meshes make the regions selectable;
      // this is a simplified anatomical illustration, not a clinical reconstruction.
      const lobeGeo = new THREE.SphereGeometry(1, 40, 32);
      addPart('frontal', lobeGeo, [-1.02, 0.35, 0.02], [1.18, 1.02, 0.92], [0,0,-0.12]);
      addPart('parietal', lobeGeo, [0.03, 0.83, 0.0], [1.02, 0.93, 0.89], [0,0,0.08]);
      addPart('occipital', lobeGeo, [1.0, 0.18, -0.01], [0.66, 0.79, 0.84], [0,0,0.12]);
      addPart('temporal', lobeGeo, [0.0, -0.45, 0.23], [1.28, 0.58, 0.77], [0,0,-0.06]);
      addPart('cerebellum', new THREE.SphereGeometry(0.72, 32, 24), [1.0, -1.0, -0.22], [1.0, 0.65, 0.78], [0,0,-0.2]);
      addPart('brainstem', new THREE.CylinderGeometry(0.22, 0.32, 1.35, 24), [0.48, -1.28, -0.05], [0.9,1,0.9], [0,0,-0.12]);

      // Two small internal structures are shown schematically and can be selected.
      addPart('hippocampus', new THREE.TorusGeometry(0.42, 0.14, 12, 36, Math.PI * 1.35), [-0.15, -0.12, 0.72], [0.85,0.8,0.8], [0.15,0.1,0.35]);
      addPart('thalamus', new THREE.SphereGeometry(0.3, 24, 20), [0.02, 0.05, 0.72], [1.0,0.9,0.8]);

      // Surface folds: fine curved lines suggest gyri without implying anatomical precision.
      const foldMaterial = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.9, transparent: true, opacity: 0.22 });
      for (let i = 0; i < 19; i++) {
        const points = [];
        const x = -1.8 + i * 0.19;
        for (let j = 0; j <= 24; j++) {
          const t = -1.15 + j * (2.3 / 24);
          const y = 0.25 + 0.74 * Math.sin(t) + 0.045 * Math.sin(j * 1.7 + i);
          const z = 0.72 * Math.cos(t) + 0.05;
          points.push(new THREE.Vector3(x + 0.06 * Math.sin(t * 2 + i), y, z));
        }
        const curve = new THREE.CatmullRomCurve3(points);
        const line = new THREE.Mesh(new THREE.TubeGeometry(curve, 32, 0.012, 4, false), foldMaterial);
        brain.add(line);
      }
      // A discreet floor grid provides spatial context.
      const grid = new THREE.GridHelper(12, 24, 0xc4d0df, 0xdbe3ed);
      grid.position.y = -2.05; scene.add(grid);

      function resize() {
        const rect = canvas.parentElement.getBoundingClientRect();
        const width = Math.max(1, rect.width);
        const height = Math.max(300, rect.height);
        renderer.setSize(width, height, false);
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
      }
      const observer = new ResizeObserver(resize);
      observer.observe(canvas.parentElement); resize();

      function onPointerMove(event) {
        const rect = canvas.getBoundingClientRect();
        pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
        raycaster.setFromCamera(pointer, camera);
        const hit = raycaster.intersectObjects(brainParts, false)[0];
        canvas.style.cursor = hit ? 'pointer' : 'grab';
      }
      function onPick(event) {
        const rect = canvas.getBoundingClientRect();
        pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
        raycaster.setFromCamera(pointer, camera);
        const hit = raycaster.intersectObjects(brainParts, false)[0];
        if (hit) chooseRegion(hit.object.userData.region);
      }
      canvas.addEventListener('pointermove', onPointerMove);
      canvas.addEventListener('click', onPick);
      root.querySelector('#brain-reset').addEventListener('click', () => {
        camera.position.set(0, 1.5, 8.8); controls.target.set(0, 0.1, 0); controls.update();
      });
      root.querySelector('#brain-auto').addEventListener('click', event => {
        autoRotate = !autoRotate;
        controls.autoRotate = autoRotate;
        event.currentTarget.setAttribute('aria-pressed', String(autoRotate));
        event.currentTarget.textContent = 'Auto-rotate: ' + (autoRotate ? 'on' : 'off');
      });
      loading.hidden = true;
      chooseRegion('frontal');
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        controls.autoRotate = false;
      }
      function animate() {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
      }
      animate();
    } catch (error) {
      loading.textContent = 'The 3D scene could not be loaded in this browser. Use the region buttons and guide below; check whether the network blocks the 3D library.';
      console.error('Brain explorer initialisation failed:', error);
    }
  }
  start();
})();
</script>
