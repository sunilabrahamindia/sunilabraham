---
layout: default
title: "The Human Brain"
categories: [TSAP Exhibition, Tito Dutta]
hidden_categories:
  - Pages needing regular archiving
authors: [Tito Dutta]
description: "Explore an anatomically detailed interactive 3D brain atlas, with selectable structures, rotation, search and layered views."
permalink: /tito/brain/
created: 2026-10-22
---

{% include author-date.html %}

Explore the human brain through an interactive anatomical atlas. Rotate the model, search for named structures, select individual parts, and examine how the brain is organised from the cerebral cortex to deeper structures and connecting pathways. This is a reference-based anatomical visualisation, not a simplified collection of coloured shapes.

<div id="tito-brain-atlas">
  <div class="brain-atlas-intro">
    <p class="brain-atlas-kicker">INTERACTIVE ANATOMICAL ATLAS</p>
    <p class="brain-atlas-instructions">Drag to rotate. Scroll or pinch to zoom. Select a structure to inspect it, or use the atlas search and layer controls to explore the anatomy.</p>
  </div>

  <div class="brain-atlas-frame">
    <iframe
      src="https://itayinbarr.github.io/brainproject/"
      title="Interactive 3D human brain atlas with individually selectable anatomical structures"
      loading="lazy"
      allow="fullscreen"
      referrerpolicy="strict-origin-when-cross-origin"
    ></iframe>
  </div>

  <p class="brain-atlas-fallback">If the interactive atlas does not appear in this browser, <a href="https://itayinbarr.github.io/brainproject/">open the 3D brain atlas directly</a>.</p>

  <details class="brain-atlas-about">
    <summary>About this model, its sources and licence</summary>
    <p>The interactive viewer and its anatomical assets are provided by the open-source Brain Project. Its model contains individually named structures derived from anatomical and imaging data, including cortical gyri and sulci, deep grey matter, white-matter tracts, ventricles, the brainstem, cerebellum, blood vessels and cranial nerves. The atlas is intended for education, not clinical diagnosis.</p>
    <p>Viewer code: Apache License 2.0. Anatomical assets and related metadata: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0). The original project credits Z-Anatomy contributors and BodyParts3D / DBCLS, along with additional imaging-atlas sources.</p>
    <p>Sources: <a href="https://github.com/itayinbarr/brainproject">Brain Project source code and documentation</a>; <a href="https://github.com/itayinbarr/brainproject/blob/main/LICENSE">licence and attribution details</a>.</p>
  </details>
</div>

## A guide to major brain regions

The atlas provides detailed anatomical structures. The short guide below introduces some broad regions; their functions depend on networks that work together rather than on isolated parts.

<div class="brain-guide-grid">
  <section>
    <h3>Frontal lobe</h3>
    <p>Contributes to planning, decision-making, voluntary movement, working memory and aspects of social behaviour.</p>
  </section>
  <section>
    <h3>Parietal lobe</h3>
    <p>Integrates sensory information and contributes to body awareness, spatial processing and directing attention.</p>
  </section>
  <section>
    <h3>Temporal lobe</h3>
    <p>Contains areas involved in hearing, aspects of language comprehension, object recognition and memory-related processing.</p>
  </section>
  <section>
    <h3>Occipital lobe</h3>
    <p>Contains visual-processing areas that analyse features such as orientation, colour and motion as part of a wider visual system.</p>
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
    <h3>Hippocampal formation</h3>
    <p>Deep in the temporal lobe, this system is important for forming many kinds of new memories and for aspects of spatial navigation.</p>
  </section>
  <section>
    <h3>Thalamus</h3>
    <p>A major hub for routing and processing much sensory information, and for communication across brain networks.</p>
  </section>
</div>

{% include navbox-tito.html %}

<style>
#tito-brain-atlas {
  --brain-atlas-ink: #172033;
  --brain-atlas-muted: #46536a;
  --brain-atlas-border: #b8c4d4;
  margin: 1.5rem 0 2rem;
  color: var(--brain-atlas-ink);
}
#tito-brain-atlas * { box-sizing: border-box; }
#tito-brain-atlas .brain-atlas-intro {
  border-left: 4px solid #245ca6;
  padding: .2rem 0 .2rem 1rem;
  margin: 1.25rem 0 1rem;
}
#tito-brain-atlas .brain-atlas-kicker {
  margin: 0 0 .5rem;
  color: #245ca6;
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .09em;
}
#tito-brain-atlas .brain-atlas-instructions {
  margin: 0;
  max-width: 70ch;
  line-height: 1.65;
}
#tito-brain-atlas .brain-atlas-frame {
  width: 100%;
  height: min(82vh, 900px);
  min-height: 620px;
  overflow: hidden;
  border: 1px solid var(--brain-atlas-border);
  border-radius: 4px;
  background: #101722;
}
#tito-brain-atlas .brain-atlas-frame iframe {
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
  background: #101722;
}
#tito-brain-atlas .brain-atlas-fallback {
  margin: .75rem 0 1.25rem;
  font-size: .92rem;
  line-height: 1.6;
}
#tito-brain-atlas .brain-atlas-about {
  border-top: 1px solid var(--brain-atlas-border);
  border-bottom: 1px solid var(--brain-atlas-border);
  padding: .9rem 0;
  margin: 1.25rem 0 2rem;
}
#tito-brain-atlas .brain-atlas-about summary {
  cursor: pointer;
  font-weight: 650;
  padding: .25rem 0;
}
#tito-brain-atlas .brain-atlas-about p {
  line-height: 1.65;
  max-width: 85ch;
}
#tito-brain-atlas a { color: #174f9b; text-decoration: underline; text-underline-offset: .15em; }
#tito-brain-atlas a:focus-visible,
#tito-brain-atlas summary:focus-visible {
  outline: 3px solid #a45b00;
  outline-offset: 3px;
}
.brain-guide-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin: 1rem 0 2rem;
}
.brain-guide-grid section {
  border-top: 2px solid #71839c;
  padding: .8rem 0 .2rem;
}
.brain-guide-grid h3 { margin: 0 0 .45rem; font-size: 1.12rem; }
.brain-guide-grid p { margin: 0; line-height: 1.65; }
body.tsap-dark-mode #tito-brain-atlas { --brain-atlas-ink: #e5eaf2; --brain-atlas-muted: #bdc7d6; --brain-atlas-border: #536176; }
body.tsap-dark-mode #tito-brain-atlas .brain-atlas-kicker,
body.tsap-dark-mode #tito-brain-atlas a { color: #9fc5ff; }
body.tsap-dark-mode .brain-guide-grid section { border-top-color: #71839c; }
@media (max-width: 700px) {
  #tito-brain-atlas .brain-atlas-frame { height: 78vh; min-height: 560px; }
  .brain-guide-grid { grid-template-columns: 1fr; gap: .8rem; }
}
@media (prefers-reduced-motion: reduce) {
  #tito-brain-atlas * { scroll-behavior: auto !important; }
}
</style>
