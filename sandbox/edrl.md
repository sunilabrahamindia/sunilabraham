---
layout: default
title: "EDRL: An Interactive Book Space"
description: "A sandbox experiment exploring Essays on Dalits, Religion and Liberation as an interactive 3D space."
permalink: /sandbox/edrl/
sitemap: false
robots: noindex
---

<section class="edrl-lab" aria-labelledby="edrl-title">
  <header class="edrl-lab__header">
    <p class="edrl-lab__eyebrow">Sandbox experiment · Web 3D / XR</p>
    <h1 id="edrl-title">Essays on Dalits, Religion and Liberation</h1>
    <p class="edrl-lab__lede">Explore the book as a small, navigable space. On a computer, drag to look around and use the theme controls below. If your browser and headset support WebXR, you can also enter immersive VR. A headset is not required to try this prototype.</p>
  </header>

  <div class="edrl-stage-wrap">
    <div id="edrl-stage" class="edrl-stage" role="img" aria-label="Interactive three-dimensional book space. It contains the book cover and three thematic panels: Religious Colonisation and Deconstruction, Reconstruction of Authentic Dalit Culture, and Subversive Language of Theology.">
      <p class="edrl-stage__fallback">Loading the 3D book space…</p>
    </div>
    <div class="edrl-stage__toolbar" aria-label="3D view controls">
      <button type="button" class="edrl-button edrl-button--primary" id="edrl-reset">Reset view</button>
      <button type="button" class="edrl-button" id="edrl-xr" hidden>Enter VR</button>
    </div>
    <p class="edrl-stage__hint" id="edrl-stage-status" aria-live="polite">Drag to rotate · Scroll or pinch to zoom · Select a theme below to read its summary.</p>
  </div>

  <section class="edrl-themes" aria-labelledby="edrl-themes-title">
    <div class="edrl-section-heading">
      <p class="edrl-lab__eyebrow">Three themes from the book</p>
      <h2 id="edrl-themes-title">Explore the ideas</h2>
      <p>These summaries follow the existing TSAP article about the collection. Select a theme to highlight its panel in the 3D space.</p>
    </div>

    <div class="edrl-theme-grid">
      <article class="edrl-theme" data-theme="0">
        <p class="edrl-theme__number">01</p>
        <h3>Religious Colonisation and Deconstruction</h3>
        <p>Examines how Dalit gods, myths and rituals were appropriated into a Brahmanical order, and calls for inherited religious identities to be critically deconstructed.</p>
        <button type="button" class="edrl-button edrl-theme__select" data-select-theme="0">Explore this theme</button>
      </article>
      <article class="edrl-theme" data-theme="1">
        <p class="edrl-theme__number">02</p>
        <h3>Reconstruction of Authentic Dalit Culture</h3>
        <p>Draws on fieldwork, oral traditions and performance to recover Dalit histories, cultural agency and the continuing search for dignity and belonging.</p>
        <button type="button" class="edrl-button edrl-theme__select" data-select-theme="1">Explore this theme</button>
      </article>
      <article class="edrl-theme" data-theme="2">
        <p class="edrl-theme__number">03</p>
        <h3>Subversive Language of Theology</h3>
        <p>Explores how faith can be expressed through story, song, humour and satire, including the folk ritual of Pottan Theyyam as a challenge to caste hierarchy.</p>
        <button type="button" class="edrl-button edrl-theme__select" data-select-theme="2">Explore this theme</button>
      </article>
    </div>
  </section>

  <aside class="edrl-context">
    <h2>About this experiment</h2>
    <p><em>Essays on Dalits, Religion and Liberation</em> is a posthumous collection of essays by A. M. A. Ayrookuzhiel (1933–1996), published in 2006 by the Asian Trading Corporation for the Christian Institute for the Study of Religion and Society (CISRS). The original article remains the authoritative reading page; this sandbox is only an experimental way to explore its themes.</p>
    <p><a href="/amaa/edrl/">Read the full EDRL article</a> · <a href="/amaa/edrl-introduction/">Read K. C. Abraham's introduction</a></p>
  </aside>

  <noscript><p>This interactive experiment requires JavaScript. The three theme summaries and links above remain available without it.</p></noscript>
</section>

<style>
  .edrl-lab {
    --edrl-paper: #f5f2eb;
    --edrl-surface: #fffefa;
    --edrl-ink: #202a35;
    --edrl-muted: #4b5563;
    --edrl-line: #cbd0d2;
    --edrl-blue: #174a70;
    --edrl-blue-hover: #103650;
    --edrl-rust: #87412f;
    --edrl-ochre: #76551d;
    --edrl-green: #315d4a;
    color: var(--edrl-ink);
    max-width: 76rem;
    margin: 0 auto;
  }

  .edrl-lab__header { max-width: 54rem; margin: 0 auto 1.5rem; }
  .edrl-lab__eyebrow { margin: 0 0 .45rem; color: var(--edrl-muted); font-size: .82rem; letter-spacing: .07em; text-transform: uppercase; }
  .edrl-lab__header h1 { margin-top: 0; }
  .edrl-lab__lede { max-width: 52rem; font-size: 1.05rem; line-height: 1.7; }
  .edrl-stage-wrap { margin: 1.5rem 0 2.5rem; }
  .edrl-stage {
    position: relative;
    min-height: 28rem;
    height: min(65vh, 42rem);
    overflow: hidden;
    border: 1px solid var(--edrl-line);
    background: var(--edrl-paper);
    color: var(--edrl-ink);
  }
  .edrl-stage canvas { display: block; width: 100%; height: 100%; touch-action: pan-y; }
  .edrl-stage__fallback { padding: 2rem; }
  .edrl-stage__toolbar { display: flex; flex-wrap: wrap; gap: .65rem; margin-top: .8rem; }
  .edrl-stage__hint { margin: .55rem 0 0; color: var(--edrl-muted); font-size: .92rem; }
  .edrl-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 2.75rem;
    padding: .6rem .9rem;
    border: 1px solid #718096;
    border-radius: 3px;
    background: var(--edrl-surface);
    color: var(--edrl-ink);
    font: inherit;
    font-weight: 600;
    line-height: 1.3;
    cursor: pointer;
  }
  .edrl-button:hover { border-color: var(--edrl-blue); }
  .edrl-button:focus-visible { outline: 3px solid #0b6fc2; outline-offset: 3px; }
  .edrl-button--primary { background: var(--edrl-blue); color: #fff; border-color: var(--edrl-blue); }
  .edrl-button--primary:hover { background: var(--edrl-blue-hover); color: #fff; }
  .edrl-themes { margin: 2.5rem 0; }
  .edrl-section-heading { max-width: 52rem; margin-bottom: 1.25rem; }
  .edrl-section-heading h2 { margin-top: 0; }
  .edrl-theme-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }
  .edrl-theme {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 1.25rem;
    border: 1px solid var(--edrl-line);
    border-top: 4px solid var(--edrl-blue);
    background: var(--edrl-surface);
    min-width: 0;
  }
  .edrl-theme:nth-child(2) { border-top-color: var(--edrl-green); }
  .edrl-theme:nth-child(3) { border-top-color: var(--edrl-rust); }
  .edrl-theme__number { margin: 0 0 .4rem; color: var(--edrl-muted); font-size: .82rem; letter-spacing: .08em; }
  .edrl-theme h3 { margin: 0 0 .65rem; font-size: 1.15rem; }
  .edrl-theme p:not(.edrl-theme__number) { flex: 1; line-height: 1.65; }
  .edrl-theme.is-selected { outline: 3px solid var(--edrl-blue); outline-offset: 2px; }
  .edrl-theme__select { margin-top: .5rem; }
  .edrl-context { margin: 2.5rem 0 1rem; padding: 1.25rem 1.5rem; border-left: 4px solid var(--edrl-blue); background: var(--edrl-paper); }
  .edrl-context h2 { margin-top: 0; font-size: 1.35rem; }
  .edrl-context p:last-child { margin-bottom: 0; }

  body.tsap-dark-mode .edrl-lab {
    --edrl-paper: #182230;
    --edrl-surface: #1f2937;
    --edrl-ink: #e5e7eb;
    --edrl-muted: #cbd5e1;
    --edrl-line: #4b5563;
    --edrl-blue: #275d85;
    --edrl-blue-hover: #1d496a;
    --edrl-rust: #c08068;
    --edrl-ochre: #d2b16d;
    --edrl-green: #7eb49a;
  }
  body.tsap-dark-mode .edrl-stage { background: #182230; }
  body.tsap-dark-mode .edrl-button:not(.edrl-button--primary) { background: #1f2937; color: #f3f4f6; border-color: #64748b; }
  body.tsap-dark-mode .edrl-context { background: #182230; }
  body.tsap-dark-mode .edrl-button:focus-visible { outline-color: #93c5fd; }

  @media (max-width: 800px) {
    .edrl-stage { min-height: 24rem; height: 52vh; }
    .edrl-theme-grid { grid-template-columns: 1fr; }
    .edrl-theme { padding: 1rem; }
  }
  @media (max-width: 480px) {
    .edrl-stage { min-height: 21rem; height: 48vh; }
    .edrl-lab__lede { font-size: 1rem; }
  }
  @media (prefers-reduced-motion: reduce) {
    .edrl-lab *, .edrl-lab *::before, .edrl-lab *::after { scroll-behavior: auto !important; animation: none !important; transition: none !important; }
  }
</style>

<script type="module">
  const stage = document.getElementById('edrl-stage');
  const status = document.getElementById('edrl-stage-status');
  const resetButton = document.getElementById('edrl-reset');
  const xrButton = document.getElementById('edrl-xr');
  const themeButtons = [...document.querySelectorAll('[data-select-theme]')];
  const themeCards = [...document.querySelectorAll('.edrl-theme')];

  const coverURL = 'https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/EDRL%20front%20cover.png?raw=true';
  const themeData = [
    { title: '01  RELIGIOUS COLONISATION', subtitle: 'Deconstruction', body: 'Question inherited religious identities and recover suppressed narratives.', colour: '#174a70' },
    { title: '02  DALIT CULTURE', subtitle: 'Reconstruction', body: 'Recover history, oral traditions, performance and cultural agency.', colour: '#315d4a' },
    { title: '03  THEOLOGY', subtitle: 'Subversive language', body: 'Story, song, humour and ritual can challenge caste hierarchy.', colour: '#87412f' }
  ];

  let THREE;
  let renderer;
  let scene;
  let camera;
  let world;
  let bookGroup;
  let themeMeshes = [];
  let animationFrame;
  let selectedTheme = -1;
  let dragging = false;
  let lastX = 0;
  let lastY = 0;
  let startRotationY = 0;
  let startRotationX = 0;
  let previousPointer = null;
  let xrSession = null;

  function makeLabelTexture(THREE, item) {
    const canvas = document.createElement('canvas');
    canvas.width = 768;
    canvas.height = 640;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#fffdf7';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = item.colour;
    ctx.fillRect(0, 0, 16, canvas.height);
    ctx.fillStyle = '#29323b';
    ctx.font = '600 28px Arial, sans-serif';
    ctx.fillText(item.title, 48, 82, 670);
    ctx.fillStyle = item.colour;
    ctx.fillRect(48, 112, 110, 5);
    ctx.fillStyle = '#202a35';
    ctx.font = 'bold 43px Georgia, serif';
    ctx.fillText(item.subtitle, 48, 190, 660);
    ctx.fillStyle = '#4b5563';
    ctx.font = '28px Arial, sans-serif';
    const words = item.body.split(' ');
    let line = '';
    let y = 258;
    for (const word of words) {
      const test = line ? line + ' ' + word : word;
      if (ctx.measureText(test).width > 660 && line) {
        ctx.fillText(line, 48, y);
        line = word;
        y += 42;
      } else line = test;
    }
    if (line) ctx.fillText(line, 48, y);
    ctx.fillStyle = '#6b7280';
    ctx.font = '20px Arial, sans-serif';
    ctx.fillText('ESSAYS ON DALITS, RELIGION AND LIBERATION', 48, 594, 670);
    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    return texture;
  }

  function setSelected(index) {
    selectedTheme = index;
    themeCards.forEach((card, i) => {
      card.classList.toggle('is-selected', i === index);
      const button = card.querySelector('button');
      if (button) button.setAttribute('aria-pressed', String(i === index));
    });
    themeMeshes.forEach((mesh, i) => {
      const active = i === index;
      mesh.scale.set(active ? 1.06 : 1, active ? 1.06 : 1, 1);
      mesh.material.opacity = index < 0 || active ? 1 : 0.82;
    });
    status.textContent = index < 0
      ? 'Drag to rotate · Scroll or pinch to zoom · Select a theme below to read its summary.'
      : 'Selected: ' + themeData[index].subtitle + '. Use Reset view to return to the full book space.';
  }

  function resize() {
    if (!renderer || !camera) return;
    const width = Math.max(1, stage.clientWidth);
    const height = Math.max(1, stage.clientHeight);
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
  }

  function addTexturedPanel(THREE, item, index) {
    const geometry = new THREE.PlaneGeometry(1.65, 1.38);
    const material = new THREE.MeshBasicMaterial({
      map: makeLabelTexture(THREE, item),
      transparent: true,
      opacity: 1,
      side: THREE.DoubleSide
    });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(0.45 + index * 1.88, 0.15 + (index === 1 ? 0.1 : 0), 0.1);
    mesh.userData.themeIndex = index;
    world.add(mesh);
    themeMeshes.push(mesh);

    const backing = new THREE.Mesh(
      new THREE.BoxGeometry(1.72, 1.45, 0.055),
      new THREE.MeshStandardMaterial({ color: item.colour, roughness: 0.82, metalness: 0.02 })
    );
    backing.position.set(mesh.position.x, mesh.position.y, -0.045);
    world.add(backing);
  }

  async function init() {
    try {
      THREE = await import('https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js');
      scene = new THREE.Scene();
      scene.background = new THREE.Color(0xf5f2eb);
      scene.fog = new THREE.Fog(0xf5f2eb, 15, 30);
      camera = new THREE.PerspectiveCamera(42, stage.clientWidth / stage.clientHeight, 0.1, 100);
      camera.position.set(0, 0, 5.5);

      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      renderer.setSize(stage.clientWidth, stage.clientHeight, false);
      renderer.outputColorSpace = THREE.SRGBColorSpace;
      renderer.xr.enabled = true;
      renderer.domElement.setAttribute('aria-hidden', 'true');
      stage.replaceChildren(renderer.domElement);

      scene.add(new THREE.HemisphereLight(0xffffff, 0x77716a, 2.2));
      const keyLight = new THREE.DirectionalLight(0xffffff, 2.3);
      keyLight.position.set(-3, 6, 8);
      scene.add(keyLight);

      world = new THREE.Group();
      // Keep the exhibit in front of the viewer in both normal and immersive views.
      // WebXR places the viewer at the origin, unlike the desktop camera.
      world.scale.setScalar(0.65);
      world.position.set(0, 0, -4);
      scene.add(world);
      bookGroup = new THREE.Group();
      bookGroup.position.set(-2.6, 0.05, 0);
      bookGroup.rotation.y = -0.12;
      world.add(bookGroup);

      const bookMaterial = new THREE.MeshBasicMaterial({ color: 0xe5dfd2 });
      const book = new THREE.Mesh(new THREE.BoxGeometry(2.15, 3.15, 0.22), bookMaterial);
      bookGroup.add(book);

      const loader = new THREE.TextureLoader();
      loader.load(coverURL, texture => {
        texture.colorSpace = THREE.SRGBColorSpace;
        const cover = new THREE.Mesh(
          new THREE.PlaneGeometry(2.08, 3.08),
          new THREE.MeshBasicMaterial({ map: texture, side: THREE.DoubleSide })
        );
        cover.position.z = 0.116;
        bookGroup.add(cover);
      }, undefined, () => {
        status.textContent = 'The 3D scene loaded, but the cover image could not be fetched. The book object and theme panels are still available.';
      });

      const spine = new THREE.Mesh(
        new THREE.BoxGeometry(0.13, 3.15, 0.24),
        new THREE.MeshStandardMaterial({ color: 0x3c3027, roughness: 0.9 })
      );
      spine.position.x = -1.08;
      bookGroup.add(spine);

      themeData.forEach((item, index) => addTexturedPanel(THREE, item, index));

      const floor = new THREE.Mesh(
        new THREE.PlaneGeometry(18, 9),
        new THREE.MeshStandardMaterial({ color: 0xe5dfd2, roughness: 1, metalness: 0 })
      );
      floor.rotation.x = -Math.PI / 2;
      floor.position.set(0.2, -2.15, -1);
      world.add(floor);

      const raycaster = new THREE.Raycaster();
      const pointer = new THREE.Vector2();
      renderer.domElement.addEventListener('pointerdown', event => {
        dragging = true;
        previousPointer = { x: event.clientX, y: event.clientY };
        lastX = event.clientX;
        lastY = event.clientY;
        startRotationY = world.rotation.y;
        startRotationX = world.rotation.x;
        renderer.domElement.setPointerCapture?.(event.pointerId);
      });
      renderer.domElement.addEventListener('pointermove', event => {
        if (!dragging || !previousPointer) return;
        world.rotation.y = startRotationY + (event.clientX - lastX) * 0.006;
        world.rotation.x = Math.max(-0.25, Math.min(0.25, startRotationX + (event.clientY - lastY) * 0.003));
      });
      renderer.domElement.addEventListener('pointerup', event => {
        if (dragging && previousPointer && Math.abs(event.clientX - previousPointer.x) + Math.abs(event.clientY - previousPointer.y) < 8) {
          const rect = renderer.domElement.getBoundingClientRect();
          pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
          pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
          raycaster.setFromCamera(pointer, camera);
          const hits = raycaster.intersectObjects(themeMeshes, false);
          if (hits.length) setSelected(hits[0].object.userData.themeIndex);
        }
        dragging = false;
        previousPointer = null;
      });
      renderer.domElement.addEventListener('pointercancel', () => { dragging = false; previousPointer = null; });
      renderer.domElement.addEventListener('wheel', event => {
        if (renderer.xr.isPresenting) return;
        event.preventDefault();
        camera.position.z = Math.max(6.2, Math.min(13, camera.position.z + event.deltaY * 0.008));
      }, { passive: false });

      window.addEventListener('resize', resize);
      if (navigator.xr && await navigator.xr.isSessionSupported('immersive-vr').catch(() => false)) {
        xrButton.hidden = false;
      }
      renderer.setAnimationLoop(() => renderer.render(scene, camera));
    } catch (error) {
      stage.innerHTML = '<p class="edrl-stage__fallback">The 3D view could not start in this browser. Try a current browser with WebGL enabled. The theme summaries below still work without the 3D view.</p>';
      status.textContent = '3D is unavailable here; use the accessible theme summaries below.';
      console.error('EDRL 3D sandbox:', error);
    }
  }

  resetButton.addEventListener('click', () => {
    if (world) {
      world.rotation.set(0, 0, 0);
      camera.position.set(0, 0, 5.5);
      camera.lookAt(0, 0, -4);
      bookGroup.rotation.set(0, -0.12, 0);
    }
    setSelected(-1);
  });

  themeButtons.forEach(button => button.addEventListener('click', () => {
    const index = Number(button.dataset.selectTheme);
    setSelected(index);
    if (world) {
      world.rotation.set(0, 0, 0);
      camera.position.set(index === 0 ? -0.25 : index === 1 ? 0.25 : 0.65, 0, 4.3);
      const targetX = (themeMeshes[index]?.position.x ?? 0) * 0.65;
      camera.lookAt(targetX, 0, -4);
    }
  }));

  xrButton.addEventListener('click', async () => {
    if (!renderer || !navigator.xr) return;
    try {
      if (xrSession) {
        await xrSession.end();
        return;
      }
      xrSession = await navigator.xr.requestSession('immersive-vr', { optionalFeatures: ['local-floor', 'bounded-floor'] });
      xrSession.addEventListener('end', () => {
        xrSession = null;
        xrButton.textContent = 'Enter VR';
      });
      await renderer.xr.setSession(xrSession);
      xrButton.textContent = 'Exit VR';
    } catch (error) {
      status.textContent = 'Could not start VR. Check that the headset browser supports WebXR and that the page is served over HTTPS.';
      console.error('EDRL WebXR:', error);
    }
  });

  setSelected(-1);
  init();
</script>
