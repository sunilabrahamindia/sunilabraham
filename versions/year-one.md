---
layout: default
title: Year One Lookback
description: "A look back at the first year of The Sunil Abraham Project, from 2 October 2025 to 2 October 2026."
categories: [Project pages, Versions]
permalink: /versions/year-one/
created: 2026-10-02
---

<style>
.year-one {
  --yo-navy: #0a2e57;
  --yo-blue: #005cc5;
  --yo-teal: #087f8c;
  --yo-maroon: #8f173d;
  --yo-amber: #a35a00;
  --yo-surface: var(--bg-surface, #fff);
  --yo-text: var(--text-main, #1a1a1a);
  --yo-muted: var(--text-muted, #555);
  --yo-border: var(--border-main, #eaecef);
  color: var(--yo-text);
}

.year-one * {
  box-sizing: border-box;
}

.year-one a {
  text-underline-offset: 0.16em;
}

.year-one-hero {
  position: relative;
  overflow: hidden;
  margin: -0.5rem -0.5rem 2rem;
  padding: clamp(1.5rem, 5vw, 3.5rem);
  border-radius: 16px;
  background:
    radial-gradient(circle at 88% 18%, rgba(255, 196, 61, 0.9) 0 7%, transparent 7.5%),
    linear-gradient(135deg, #0a2e57 0%, #123f68 62%, #087f8c 100%);
  color: #fff;
}

.year-one-hero::after {
  content: "";
  position: absolute;
  right: -8%;
  bottom: -35%;
  width: 55%;
  height: 75%;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  pointer-events: none;
}

.year-one-kicker {
  margin: 0 0 0.5rem;
  color: #ffd166;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.year-one-hero h1 {
  position: relative;
  z-index: 1;
  margin: 0;
  max-width: 12ch;
  color: #fff;
  font-size: clamp(2.2rem, 7vw, 4.5rem);
  line-height: 0.98;
  letter-spacing: -0.035em;
}

.year-one-deck {
  position: relative;
  z-index: 1;
  max-width: 58rem;
  margin: 1.25rem 0 0;
  color: #f7fbff;
  font-size: clamp(1.05rem, 2.2vw, 1.3rem);
  line-height: 1.65;
}

.year-one-date {
  position: relative;
  z-index: 1;
  margin: 1.25rem 0 0;
  color: #e6f2ff;
  font-weight: 700;
}

.year-one-intro {
  max-width: 70rem;
  margin: 0 auto 2.5rem;
  font-size: 1.08rem;
}

.year-one-section {
  margin: 3rem 0;
  scroll-margin-top: 2rem;
}

.year-one-section h2 {
  margin-bottom: 1rem;
}

.year-one-section h3 {
  margin-top: 1.6rem;
  color: var(--text-heading, #0a2e57);
}

.year-one-lead {
  font-size: 1.12rem;
}

.year-one-stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.85rem;
  margin: 1.5rem 0 2.25rem;
}

.year-one-stat {
  min-width: 0;
  padding: 1.15rem;
  border: 1px solid var(--yo-border);
  border-top: 5px solid var(--yo-blue);
  border-radius: 10px;
  background: var(--yo-surface);
}

.year-one-stat:nth-child(2) { border-top-color: var(--yo-maroon); }
.year-one-stat:nth-child(3) { border-top-color: var(--yo-teal); }
.year-one-stat:nth-child(4) { border-top-color: var(--yo-amber); }

.year-one-stat strong {
  display: block;
  color: var(--text-heading, #0a2e57);
  font-size: clamp(1.65rem, 4vw, 2.25rem);
  line-height: 1;
}

.year-one-stat span {
  display: block;
  margin-top: 0.5rem;
  color: var(--yo-muted);
  font-size: 0.9rem;
  line-height: 1.45;
}

.year-one-note,
.year-one-callout {
  margin: 1.5rem 0;
  padding: 1.1rem 1.25rem;
  border-left: 5px solid var(--yo-teal);
  border-radius: 0 9px 9px 0;
  background: color-mix(in srgb, var(--yo-teal) 8%, var(--yo-surface));
}

.year-one-callout strong {
  color: var(--text-heading, #0a2e57);
}

.year-one-timeline {
  position: relative;
  margin: 1.75rem 0;
  padding-left: 1.35rem;
  border-left: 3px solid var(--yo-border);
}

.year-one-event {
  position: relative;
  margin: 0 0 1.65rem;
  padding-left: 1rem;
}

.year-one-event::before {
  content: "";
  position: absolute;
  left: -1.58rem;
  top: 0.35rem;
  width: 0.75rem;
  height: 0.75rem;
  border: 3px solid var(--yo-surface);
  border-radius: 50%;
  background: var(--yo-blue);
  box-shadow: 0 0 0 2px var(--yo-blue);
}

.year-one-event:nth-child(3n)::before { background: var(--yo-maroon); box-shadow: 0 0 0 2px var(--yo-maroon); }
.year-one-event:nth-child(3n+1)::before { background: var(--yo-teal); box-shadow: 0 0 0 2px var(--yo-teal); }

.year-one-event time {
  display: block;
  margin-bottom: 0.25rem;
  color: var(--yo-muted);
  font-size: 0.88rem;
  font-weight: 800;
}

.year-one-event h3 {
  margin: 0 0 0.35rem;
}

.year-one-event p {
  margin-bottom: 0;
}

.year-one-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.year-one-card {
  padding: 1.25rem;
  border: 1px solid var(--yo-border);
  border-radius: 12px;
  background: var(--yo-surface);
}

.year-one-card h3 {
  margin-top: 0;
}

.year-one-card ul {
  margin-bottom: 0;
}

.year-one-quote {
  margin: 2rem 0;
  padding: 1.4rem 1.5rem;
  border: 1px solid var(--yo-border);
  border-left: 6px solid var(--yo-maroon);
  border-radius: 10px;
  background: color-mix(in srgb, var(--yo-maroon) 7%, var(--yo-surface));
  font-size: clamp(1.12rem, 2.4vw, 1.35rem);
  font-weight: 700;
  line-height: 1.5;
}

.year-one-table-wrap {
  margin: 1.5rem 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border: 1px solid var(--yo-border);
  border-radius: 10px;
}

.year-one-table {
  width: 100%;
  min-width: 620px;
  margin: 0;
}

.year-one-table th {
  background: var(--yo-navy);
  color: #fff;
}

.year-one-table th,
.year-one-table td {
  vertical-align: top;
}

.year-one-links {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.65rem;
  margin-top: 1rem;
}

.year-one-links a {
  display: block;
  padding: 0.75rem 0.9rem;
  border: 1px solid var(--yo-border);
  border-radius: 8px;
  background: var(--yo-surface);
  font-weight: 700;
}

.year-one-end {
  margin-top: 3rem;
  padding: 1.5rem;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--yo-navy), #123f68);
  color: #fff;
}

.year-one-end h2 {
  color: #fff;
  border-bottom-color: rgba(255, 255, 255, 0.35);
}

.year-one-end p:last-child {
  margin-bottom: 0;
}

.year-one-small {
  color: var(--yo-muted);
  font-size: 0.9rem;
}

@media (max-width: 800px) {
  .year-one-hero {
    margin: -0.25rem -0.25rem 1.5rem;
    border-radius: 12px;
  }

  .year-one-stats,
  .year-one-grid,
  .year-one-links {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 560px) {
  .year-one-hero {
    padding: 1.35rem;
  }

  .year-one-stats,
  .year-one-grid,
  .year-one-links {
    grid-template-columns: 1fr;
  }

  .year-one-section {
    margin: 2.25rem 0;
  }

  .year-one-timeline {
    padding-left: 0.9rem;
  }

  .year-one-event {
    padding-left: 0.8rem;
  }

  .year-one-event::before {
    left: -1.15rem;
  }

  .year-one-callout,
  .year-one-note,
  .year-one-quote {
    padding: 1rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .year-one * {
    scroll-behaviour: auto;
  }
}

body.tsap-dark-mode .year-one {
  --yo-navy: #93c5fd;
  --yo-blue: #60a5fa;
  --yo-teal: #2dd4bf;
  --yo-maroon: #f472b6;
  --yo-amber: #fbbf24;
}

body.tsap-dark-mode .year-one-hero {
  background: linear-gradient(135deg, #172554 0%, #164e63 100%);
}

body.tsap-dark-mode .year-one-hero h1,
body.tsap-dark-mode .year-one-end h2 {
  color: #f8fafc;
}

body.tsap-dark-mode .year-one-table th {
  background: #172554;
  color: #f8fafc;
}

body.tsap-dark-mode .year-one-end {
  background: linear-gradient(135deg, #172554, #164e63);
}

@media (max-width: 768px) {
  .year-one-hero {
    line-height: 1.4;
  }
}
</style>

<div class="year-one">

<div class="year-one-hero">
<p class="year-one-kicker">The Sunil Abraham Project</p>
<h1>Year One Lookback</h1>
<p class="year-one-deck">A year of building an archive into an open research infrastructure.</p>
<p class="year-one-date">2 October 2025 – 2 October 2026</p>
</div>

<div class="year-one-intro">
<p class="year-one-lead">The Sunil Abraham Project completed its first year on 2 October 2026. What began as an effort to bring together dispersed writings, media coverage, research material and family archives became, within twelve months, a substantial public digital archive with more than 1,300 published pages, a formal version history, structured collections, research portals, preservation layers, custom tools and original creative work.</p>

<p>The important story is therefore not simply how much was published. It is how a growing collection was gradually turned into an infrastructure in which material can be found, related, contextualised, preserved and revisited.</p>
</div>

<div class="year-one-stats" aria-label="Selected first-year figures">
<div class="year-one-stat"><strong>1,300+</strong><span>published pages by 29 September 2026</span></div>
<div class="year-one-stat"><strong>365</strong><span>articles by 31 December 2025</span></div>
<div class="year-one-stat"><strong>48</strong><span>new media clusters in Version 2.0</span></div>
<div class="year-one-stat"><strong>228</strong><span>pages in the Chaitali content cycle</span></div>
</div>

<section class="year-one-section" id="beginning">
<h2>From four pages to a public archive</h2>

<p>TSAP was founded on 2 October 2025. The first four pages were deployed on 19 October: Home, Publications, Projects and Contact. The project then entered a period of rapid acquisition and organisation.</p>

<p>The archive reached 100 articles on 23 November 2025, 200 on 11 December, 300 on 22 December and 365 by the end of the year. The 500-article milestone followed on 23 January 2026. By 21 May, the archive had reached 1,000 articles. During the second half of the year, the measurement itself broadened from article counts to total published pages: 1,100 on 28 June, 1,200 on 9 August, 1,250 on 3 September and 1,300 on 29 September.</p>

<div class="year-one-callout">
<strong>The change in scale changed the problem.</strong>
<p>Once the archive became large, simply adding more pages was no longer enough. Navigation, metadata, identifiers, clustering, documentation, preservation and accessibility became part of the publishing work itself.</p>
</div>
</section>

<section class="year-one-section" id="timeline">
<h2>The first year, month by month</h2>

<div class="year-one-timeline">
<div class="year-one-event">
<time datetime="2025-10-02">2 October 2025</time>
<h3>Project founded</h3>
<p>The Sunil Abraham Project begins as a digital publishing, documentation and archiving initiative.</p>
</div>

<div class="year-one-event">
<time datetime="2025-10-19">19 October 2025</time>
<h3>First four pages deployed</h3>
<p>Home, Publications, Projects and Contact establish the first public site structure.</p>
</div>

<div class="year-one-event">
<time datetime="2025-11-29">29 November 2025</time>
<h3>A. M. A. Ayrookuzhiel Portal launched</h3>
<p>The portal becomes an important early research strand, launched alongside the 29th death anniversary observance.</p>
</div>

<div class="year-one-event">
<time datetime="2025-12-31">31 December 2025</time>
<h3>365 articles</h3>
<p>Version 1.0 records the rapid build phase and the first major consolidation of the archive.</p>
</div>

<div class="year-one-event">
<time datetime="2026-01-01">1 January 2026</time>
<h3>Version 1.0</h3>
<p>The project moves from its initial build into a more deliberate cycle of clusters, portals, tools and documentation.</p>
</div>

<div class="year-one-event">
<time datetime="2026-03-18">18 March 2026</time>
<h3>TSAP Documentation launched</h3>
<p>The project begins documenting not only the material it preserves, but also how the archive itself works.</p>
</div>

<div class="year-one-event">
<time datetime="2026-06-17">17 June 2026</time>
<h3>Version 2.0 completed</h3>
<p>The major cycle closes with 695 new pages, 48 new media clusters, 228 pages in the Chaitali cycle and 29 documentation pages.</p>
</div>

<div class="year-one-event">
<time datetime="2026-06-27">27 June 2026</time>
<h3>Preservation strengthened</h3>
<p>Permanent Page IDs, a Software Heritage snapshot and the first offline preservation workflow strengthen the project's long-term continuity.</p>
</div>

<div class="year-one-event">
<time datetime="2026-07-04">4 July 2026</time>
<h3>CIS anniversary and institutional history</h3>
<p>The Centre for Internet and Society archive expands into organisational history, registration, policy and related institutional material.</p>
</div>

<div class="year-one-event">
<time datetime="2026-08-26">26 August 2026</time>
<h3>A. M. A. Ayrookuzhiel Knowledge Engine</h3>
<p>The preparatory Knowledge Engine marks a shift from publishing archival pages towards organising material for exploration and search.</p>
</div>

<div class="year-one-event">
<time datetime="2026-09-29">29 September 2026</time>
<h3>1,300-page milestone</h3>
<p>The archive passes 1,300 published pages as the first year approaches its formal boundary.</p>
</div>

<div class="year-one-event">
<time datetime="2026-10-02">2 October 2026</time>
<h3>Year One completed</h3>
<p>The first twelve-month period closes. The project enters its second year with a mature publishing and preservation foundation.</p>
</div>
</div>
</section>

<section class="year-one-section" id="versions">
<h2>Versions became institutional memory</h2>

<p>The version system became one of the project's most useful records. It began as a weekly change log and developed into a structured historical archive documenting editorial priorities, technical changes, content initiatives, preservation decisions, incidents and lessons.</p>

<div class="year-one-table-wrap">
<table class="year-one-table">
<thead>
<tr><th>Release</th><th>Period</th><th>What it established</th></tr>
</thead>
<tbody>
<tr><td>Version 1.0</td><td>1 January 2026</td><td>Consolidation after the rapid build phase; 365 articles, clusters and major portals.</td></tr>
<tr><td>Version 2.0</td><td>17 June 2026</td><td>695 new pages from 1 January–16 June; 48 media clusters; 228 Chaitali pages; 29 documentation pages.</td></tr>
<tr><td>Version 2.1</td><td>17–27 June</td><td>Permanent Page IDs, Software Heritage preservation and offline preservation strengthened.</td></tr>
<tr><td>Version 2.1.1–2.1.3</td><td>28 June–18 July</td><td>Dark mode architecture, incident documentation, TSAP Status, pages.json automation and domain monitoring.</td></tr>
<tr><td>Version 2.2–2.2.3</td><td>19 July–15 August</td><td>Honesty principle, repository safeguards, category improvements, maintenance systems and archive expansion.</td></tr>
<tr><td>Version 2.3–2.3.2</td><td>16 August–5 September</td><td>CIS and Elonnai Hickok archival expansion, Time &amp; Date Converter, authority control and documentation.</td></tr>
<tr><td>Version 2.4–2.4.2</td><td>6–26 September</td><td>TSPA comics, Simulation #1, essays, tools, accessibility and institutional history.</td></tr>
<tr><td>Version 2.5</td><td>27 September–3 October</td><td>Year One release work, the 1,300-page milestone, new TSPA material and related research.</td></tr>
</tbody>
</table>
</div>

<p>See the <a href="/versions/">Versions archive</a>, including the detailed <a href="/versions/1.0/">Version 1.0 lookback</a> and <a href="/versions/2.0/">Version 2.0 lookback</a>.</p>
</section>

<section class="year-one-section" id="collections">
<h2>A collection of collections</h2>

<p>The first year established TSAP as more than one undifferentiated archive. The project developed thematic and source-based structures so that readers can approach material through people, organisations, publications, subjects and historical contexts.</p>

<div class="year-one-grid">
<div class="year-one-card">
<h3>Media clusters</h3>
<p>By Version 2.0, 48 new media clusters had been developed. These act as curated archival entry points, connecting related documents without erasing the identity of individual pages.</p>
</div>

<div class="year-one-card">
<h3>Research portals</h3>
<p>The A. M. A. Ayrookuzhiel Portal, Artificial Intelligence Portal and Centre for Internet and Society section developed into substantial research spaces rather than simple landing pages.</p>
</div>

<div class="year-one-card">
<h3>Chaitali cycle</h3>
<p>The content-development cycle from 1 March to 14 April 2026 produced 228 pages, demonstrating that intensive research could be organised as a defined editorial programme.</p>
</div>

<div class="year-one-card">
<h3>Machine-readable structure</h3>
<p>Permanent Page IDs and the generated <code>pages.json</code> index turned a growing collection into a more manageable and machine-readable corpus.</p>
</div>
</div>
</section>

<section class="year-one-section" id="amaa">
<h2>A. M. A. Ayrookuzhiel: from archive to research environment</h2>

<p>A. M. A. Ayrookuzhiel's work became one of the most substantial archival strands of the first year. The work developed from biographical and bibliographical documentation into a research portal, full-text work, authority-control resources, storytelling experiments and a major commemorative programme.</p>

<p>The 30th Death Anniversary Commemoration became a major programme during the second half of the year. Monthly bulletins began in April 2026, documenting archival work, planning, full-text publication, authority control, storytelling and related preparation. By September, six bulletins had been published alongside a dedicated invitation page.</p>

<p>The <a href="/amaa/">A. M. A. Ayrookuzhiel Portal</a> and the preparatory <a href="/amaa/knowledge-engine/">Knowledge Engine</a> show the project's broader movement from collecting pages towards building research infrastructure around them.</p>
</section>

<section class="year-one-section" id="cis">
<h2>Preserving the institutional world around the archive</h2>

<p>The Centre for Internet and Society became another major archival strand, particularly during and after Version 2.0. The work expanded into institutional history, registration records, policies, publications, anniversaries and the work of people associated with CIS.</p>

<p>The Elonnai Hickok collection grew rapidly from late July onwards, preserving CIS-era writing and related material on privacy, surveillance, data protection and technology policy. The September work also began documenting the wider intellectual and publishing environment around A. M. A. Ayrookuzhiel and CISRS, including Religion and Society, Asian Trading Corporation and the Indian Society for Promoting Christian Knowledge.</p>

<div class="year-one-quote">The archive widened from one person's work to the institutions, publications and networks that shaped that work, giving future researchers a richer historical context while preserving the identity of individual sources.</div>

<p>Explore the <a href="/cis/">Centre for Internet and Society collection</a>.</p>
</section>

<section class="year-one-section" id="technology">
<h2>Small systems for a growing archive</h2>

<p>Technology was not merely an implementation detail. As the archive grew, TSAP repeatedly built small systems to solve practical editorial, maintenance, retrieval and preservation problems.</p>

<div class="year-one-grid">
<div class="year-one-card">
<h3>Publishing</h3>
<p>Jekyll, Markdown, YAML and GitHub Pages provide a low-dependency, reproducible publication system in which source, content, metadata and history remain together.</p>
</div>

<div class="year-one-card">
<h3>Identifiers and indexing</h3>
<p>Permanent Page IDs and <code>pages.json</code> provide stable identifiers and a machine-readable index for retrieval and maintenance workflows.</p>
</div>

<div class="year-one-card">
<h3>Monitoring</h3>
<p>TSAP Status, the Domain Expiry Monitor and related lightweight services provide independent monitoring using serverless and free-service components.</p>
</div>

<div class="year-one-card">
<h3>Tools</h3>
<p>The Versions Helper and Time &amp; Date Converter address recurring project tasks without requiring a conventional database-backed application.</p>
</div>

<div class="year-one-card">
<h3>Dark mode</h3>
<p>A centralised CSS custom-property architecture allowed dark mode to become a site-wide system rather than a collection of unrelated page fixes.</p>
</div>

<div class="year-one-card">
<h3>Documented incidents</h3>
<p>The July 2026 repository storage incident and recovery were documented as project knowledge, preserving both the failure and the restoration process.</p>
</div>
</div>

<div class="year-one-callout">
<strong>The engineering lesson:</strong>
<p>A static site can support sophisticated systems when structured metadata, version control and small focused tools are used deliberately.</p>
</div>
</section>

<section class="year-one-section" id="preservation">
<h2>Preservation as a design objective</h2>

<p>Preservation became one of the strongest distinguishing features of the project. The approach treats continuity, accessibility, survivability and verifiability as design objectives rather than afterthoughts.</p>

<div class="year-one-grid">
<div class="year-one-card">
<h3>Primary layer</h3>
<ul>
<li>GitHub repository and complete Git history</li>
<li>Public static website</li>
<li>Open Markdown and YAML source</li>
</ul>
</div>

<div class="year-one-card">
<h3>Independent layers</h3>
<ul>
<li>Software Heritage snapshot</li>
<li>Internet Archive and other web archive captures</li>
<li>Offline repository copies</li>
<li>Secondary hosting and preservation storage</li>
</ul>
</div>
</div>

<p>Following Version 2.0, the project created its first offline repository backup and retained copies on local storage and in a public Google Drive preservation archive. A Cloudflare Pages mirror was also explored as a preservation and disaster-recovery layer rather than simply as another search-engine destination.</p>

<p>The July repository storage incident reinforced the principle. Instead of treating an operational failure as something to hide, the project documented what happened and how the repository was restored. See the <a href="/tsap/preservation/">preservation documentation</a>.</p>
</section>

<section class="year-one-section" id="accessibility">
<h2>Accessibility and public usability</h2>

<p>Accessibility was treated as an architectural concern. The project's Version 1.0 approach already emphasised mobile-first presentation, readability, clear navigation and inclusive access across devices and abilities. During the year, that approach expanded into centralised CSS variables, dark-mode support and page-specific refinements.</p>

<div class="year-one-stats" aria-label="Accessibility principles">
<div class="year-one-stat"><strong>Mobile</strong><span>Responsive presentation and readable layouts</span></div>
<div class="year-one-stat"><strong>Dark</strong><span>Site-wide dark-mode architecture</span></div>
<div class="year-one-stat"><strong>Clear</strong><span>Multiple routes through the archive</span></div>
<div class="year-one-stat"><strong>Open</strong><span>Inspectable source and structured data</span></div>
</div>

<p>Clusters, categories, templates, portals, permanent identifiers, the Newest Pages index, the Versions archive and machine-readable page indexes provide different routes into the same body of material. The continuing design principle is straightforward: new tools and components should retain keyboard access, readable contrast, clear labels and sensible mobile behaviour.</p>
</section>

<section class="year-one-section" id="creative">
<h2>When the archive began to create</h2>

<p>The first year was dominated by archival work, but its final months marked a notable expansion into original creative and conceptual work.</p>

<div class="year-one-grid">
<div class="year-one-card">
<h3>TSPA comics</h3>
<p>The TSPA comic project introduced recurring characters and a visual language that combines commentary, technology and everyday observation.</p>
</div>

<div class="year-one-card">
<h3>Simulation #1</h3>
<p>An experimental project opened a different mode of expression within a site that had previously been dominated by documentation and archival acquisition.</p>
</div>

<div class="year-one-card">
<h3>Essays and concepts</h3>
<p>Original essays and conceptual pieces began to create space for interpretation rather than preservation alone.</p>
</div>

<div class="year-one-card">
<h3>A new direction</h3>
<p>The Internet and Free Knowledge in India initiative began immediately after the formal Year One boundary. It is not counted as a Year One output, but it points towards the direction created by the first year's foundation.</p>
</div>
</div>

<p>Explore the <a href="/tspa/">TSPA creative work</a>.</p>
</section>

<section class="year-one-section" id="governance">
<h2>A public record of change</h2>

<p>The project developed a lightweight form of governance embedded in documented principles, version history, repository history, metadata standards and public project records.</p>

<p>The Versions archive is effectively a public change-management record. It records what was done, why it was done, the number of pages created during reporting cycles, issues, technical incidents and areas for improvement. This makes the evolution of the project legible to future maintainers and readers.</p>

<p>The project also increasingly separated routine maintenance from substantive editorial work. Automatic last-updated logic, hidden maintenance categories, documentation pages and structured templates help distinguish infrastructure changes from public content.</p>

<div class="year-one-note">
<strong>Transparency also means acknowledging limitations.</strong>
<p>Version 2.0 explicitly noted the relative underdevelopment of original writing, the absence of a mature social-media strategy and the need for stronger institutional, financial and organisational foundations. Page count alone should not be mistaken for institutional maturity.</p>
</div>
</section>

<section class="year-one-section" id="lessons">
<h2>What the first year taught us</h2>

<div class="year-one-table-wrap">
<table class="year-one-table">
<thead>
<tr><th>Lesson</th><th>Implication</th></tr>
</thead>
<tbody>
<tr><td>Scale is useful, but structure makes scale sustainable.</td><td>At more than 1,300 pages, categories, clusters, portals, templates and permanent identifiers are essential to navigation.</td></tr>
<tr><td>Archiving creates its own knowledge.</td><td>Documentation about workflows, incidents, preservation and metadata becomes part of the historical record.</td></tr>
<tr><td>Static technology can support sophisticated systems.</td><td>Jekyll, Markdown, YAML, Git and focused serverless tools can provide substantial publishing, search and monitoring capabilities.</td></tr>
<tr><td>Preservation must be redundant.</td><td>GitHub alone is not enough; independent archival services, offline copies and mirrors improve resilience.</td></tr>
<tr><td>Accessibility must be architectural.</td><td>Contrast, dark mode, mobile presentation, keyboard interaction and predictable navigation should be built into systems.</td></tr>
<tr><td>Creative work needs deliberate space.</td><td>Rapid archival acquisition can crowd out original thinking; the next cycle needs protected space for essays, analysis and experiments.</td></tr>
<tr><td>Public visibility is a separate function.</td><td>Publishing material does not automatically create an audience. Public engagement needs its own strategy.</td></tr>
<tr><td>Institutional resilience matters.</td><td>As the archive becomes more valuable, sustainability, succession, funding and documented responsibilities become increasingly important.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="year-one-section" id="year-two">
<h2>The question for Year Two</h2>

<p>The first year created a strong platform. The second year should therefore be more selective and intentional. The project does not need to prove its existence through ever-increasing page counts; it needs to deepen the value of what has already been built.</p>

<div class="year-one-grid">
<div class="year-one-card">
<h3>Original research and writing</h3>
<p>Increase the proportion of essays, analysis, reflections and original research alongside archival acquisition.</p>
</div>

<div class="year-one-card">
<h3>A. M. A. Ayrookuzhiel programme</h3>
<p>Complete the 30th death anniversary commemoration while ensuring that the resulting archive remains useful as a permanent research collection.</p>
</div>

<div class="year-one-card">
<h3>Internet and Free Knowledge in India</h3>
<p>Develop IFKI as a clearly scoped research project with literature, people and institutions, publications and historical chronology.</p>
</div>

<div class="year-one-card">
<h3>Quality and metadata review</h3>
<p>Introduce periodic systematic review of titles, descriptions, categories, identifiers, links and accessibility.</p>
</div>

<div class="year-one-card">
<h3>Preservation maturity</h3>
<p>Move from experimental redundancy towards a documented schedule for snapshots, offline exports and independent archival copies.</p>
</div>

<div class="year-one-card">
<h3>Public engagement and resilience</h3>
<p>Develop a realistic communication strategy and document roles, decision-making, succession, funding possibilities and maintenance responsibilities.</p>
</div>
</div>

<div class="year-one-quote">The archive is now large enough that the central question is no longer simply "What can we add?" but "What is most valuable to preserve, explain, connect and create next?"</div>
</section>

<section class="year-one-section" id="sources">
<h2>Sources and further reading</h2>

<p>This lookback is assembled from the project's own published records. The formal period is 2 October 2025 to 2 October 2026. Developments immediately after that boundary are kept separate from the first-year account.</p>

<div class="year-one-links">
<a href="/versions/">Versions archive</a>
<a href="/versions/1.0/">Version 1.0 lookback</a>
<a href="/versions/2.0/">Version 2.0 lookback</a>
<a href="/articles/sunil-abraham-project/">The Sunil Abraham Project</a>
<a href="/newest/">Newest Pages</a>
<a href="/tsap/project-updates/">Project Updates</a>
<a href="/tsap/preservation/">Preservation</a>
<a href="/amaa/">A. M. A. Ayrookuzhiel Portal</a>
<a href="/cis/">Centre for Internet and Society</a>
<a href="/tspa/">TSPA</a>
</div>

<p class="year-one-small">The figures on this page retain the precision used by the project's records. In particular, the first-year milestone is stated as more than 1,300 published pages by 29 September 2026 rather than as an invented exact total.</p>
</section>

<div class="year-one-end">
<h2>Year One, completed</h2>
<p>From four deployed pages to a public archive, from rapid acquisition to structured research infrastructure, the first year established the systems on which the next phase can build.</p>
<p>The work now is not simply to make the archive larger. It is to make it more useful, more explainable, more resilient and more capable of supporting new research and creative work.</p>
</div>

</div>
