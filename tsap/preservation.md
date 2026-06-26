---
layout: default
title: "Preservation"
description: "An overview of the archival, preservation, redundancy, and backup strategies used across The Sunil Abraham Project (TSAP)."
categories: [TSAP Documentation]
permalink: /tsap/preservation/
page_id: TSAP-1014
created: 2026-05-25
homepage_featured: true
---

{% include documentation-notice.html %}

**Preservation** on **The Sunil Abraham Project** (TSAP) refers to the long-term protection, continuity, accessibility, and survivability of the project's content, metadata, and research materials. As a static, Git-based digital archive, TSAP follows a preservation-oriented architecture built around open formats, distributed storage, version control, redundancy, and public accessibility. The project incorporates principles from digital archiving, scholarly preservation, and library science, including concepts such as the 3-2-1 backup rule, LOCKSS ("Lots Of Copies Keep Stuff Safe"), versioned preservation through Git, and the use of external archival services such as GitHub, Zenodo, the Internet Archive, and Archive.today. The goal is not only to prevent data loss, but also to ensure that the material remains readable, portable, verifiable, and accessible over long periods of time across changing technologies and platforms.

<div class="preservation-meta" role="note" aria-label="Preservation review information">
  <strong>Last reviewed:</strong> June 2026
</div>

<div class="preservation-legend" role="note" aria-label="Preservation status guide">
  <strong>Status guide:</strong>

  <span class="preservation-status status-active">
    Active
  </span>
  Implemented and regularly used

  <span class="preservation-status status-experimental">
    Experimental
  </span>
  Implemented but still evolving

  <span class="preservation-status status-planned">
    Planned
  </span>
  Proposed or under consideration

  <span class="preservation-status status-not-started">
    Not Started
  </span>
  Identified but not yet implemented
</div>

## Web Archiving
<span class="preservation-status status-active">Active</span>

TSAP maintains ongoing public web archival workflows using external archival services including the [Internet Archive Wayback Machine](https://web.archive.org/web/*/https://sunilabraham.in/) and [Archive.today](https://archive.ph/https://sunilabraham.in/). Archival snapshots are created both manually and through browser-based tools. Rather than relying solely on infrequent bulk exports, TSAP follows a continuous preservation approach in which pages are archived incrementally over time. A small number of pages may be archived daily, while larger archival sessions are periodically conducted to preserve batches of pages together.

Current tools and services used include the Wayback Machine browser extension ([Chrome](https://chromewebstore.google.com/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/)) and the Archive Page browser extension ([Chrome](https://chromewebstore.google.com/detail/archive-page/gcaimhkfmliahedmeklebabdgagipbia), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/archive-page/)). Similar archival and preservation-oriented browser extensions and tools are also available for other browsers and platforms.

In June 2026, TSAP began creating manual preservation snapshots using Ghost Archive. Ghost Archive provides an additional independent web archiving service that complements existing preservation workflows based on the Internet Archive Wayback Machine and Archive.today. TSAP uses two primary methods for creating Ghost Archive snapshots: Using the [Web Archives browser extension](https://chromewebstore.google.com/detail/web-archives/hkligngkgcpcolhcnkgccglchdafcnao) and manual submission and archiving through the Ghost Archive website.

These workflows help reduce link rot risk, preserve historical page states, improve public survivability, maintain independent external copies, and provide resilience against accidental deletion or hosting failure. Because TSAP is a continuously evolving project, archival snapshots taken at different points in time also function as historical records documenting the evolution of the archive itself.

TSAP also includes direct archival links in the footer of every page, allowing readers to immediately access preserved versions of the current page through both the Internet Archive Wayback Machine and Archive.today. These links are generated dynamically using the page URL and form part of the project's broader commitment to transparency, public preservation, and long-term accessibility.

## Zenodo Preservation
<span class="preservation-status status-experimental">Experimental</span>

TSAP has begun publishing selected curated materials and archival collections through the [Zenodo Archives](/zenodo/) portal. Zenodo provides DOI-backed scholarly preservation infrastructure, helping ensure long-term citability, archival stability, and independent preservation outside the primary website infrastructure.

Zenodo deposits may include curated datasets, archival compilations, preserved research publications, structured metadata collections, and static exports of historically significant materials. The use of DOI-backed archival infrastructure complements the project's broader preservation strategy based on redundancy, distributed storage, and open formats.

## Repository Preservation
<span class="preservation-status status-active">Active</span>

TSAP incorporates repository-level preservation workflows based on Git, distributed version control, public source code hosting, and independent archival infrastructure. These workflows support long-term preservation, historical version tracking, disaster recovery, repository redundancy, and independent verification of the project's development history.

Because the project is built primarily using static files and open formats, repository-level preservation forms an important part of the long-term archival strategy of TSAP. Git enables detailed version tracking, historical recovery, distributed cloning, and preservation of the project's evolution over time.

### Software Heritage

On 31 May 2026 at 17:16:46 UTC, the GitHub repository of The Sunil Abraham Project (TSAP) was archived on Software Heritage.

Following the completion of TSAP Version 2.0, an additional Software Heritage archival snapshot was requested to preserve the repository at the conclusion of the Version 2.0 development cycle. This provides an updated independently archived copy of the repository and its Git history, complementing the earlier preservation snapshot and documenting the project's continued development.

Software Heritage is an international initiative dedicated to collecting, preserving, and providing long-term access to software source code and development history. Its inclusion in TSAP's preservation workflow adds an additional layer of archival resilience beyond GitHub, web archiving services, local backups, and other preservation mechanisms.

## Offline TSAP
<span class="preservation-status status-experimental">Experimental</span>

As part of its broader preservation and accessibility strategy, TSAP has begun implementing an offline preservation workflow based on repository snapshots. Following the completion of TSAP Version 2.0, the first offline preservation copy of the project's Git repository was created and retained as an independent backup.

At present, one offline repository backup is stored on the project maintainer's local hard disk. As this is an active personal laptop rather than dedicated archival storage, this copy should be regarded as a working preservation backup rather than a permanent archival copy.

To provide an additional independent preservation copy, the same repository snapshot has also been uploaded to Google Drive. It may be downloaded by anyone wishing to maintain an offline copy of TSAP on external storage such as a USB flash drive, external hard disk, or other archival media.

Google Drive archive: [26 June 2026](https://drive.google.com/drive/folders/1HM0vSnyA5uZWuHZFYt3zudDawZczGat3)

Future work may include periodic repository snapshots taken at major project milestones, offline website exports, portable archival packages, and copies stored on dedicated external storage media and institutional repositories.

## Redundancy and Mirror Infrastructure
<span class="preservation-status status-experimental">Experimental</span>

As part of its broader preservation strategy, TSAP also experiments with redundant deployment and mirror infrastructure across multiple hosting environments. This includes parallel static deployments intended to improve resilience, continuity, survivability, and disaster recovery capability in the event of hosting failures or service disruption.

Some secondary deployments are intentionally treated as infrastructure-level preservation mirrors rather than primary public access points. These mirrors primarily exist to support redundancy, preservation testing, continuity planning, and long-term archival resilience.

## Future Plans
<span class="preservation-status status-planned">Planned</span>

As TSAP continues to expand, additional preservation-oriented workflows, standards, and documentation systems may gradually be introduced over time. These future directions are intended to strengthen long-term accessibility, archival durability, metadata quality, portability, and historical continuity across the project.

### Accessibility as Preservation

TSAP treats accessibility as an important part of long-term preservation. Future work may include broader accessibility audits, improved semantic structure, enhanced screen reader support, reduced-motion compatibility, improved colour contrast, and other measures intended to ensure that archived knowledge remains usable and accessible across different devices, abilities, and technological environments.

### Open Formats

TSAP strongly prefers open and preservation-friendly formats such as HTML, Markdown, YAML, TXT, CSV, JPEG, and PDF wherever practical. Future preservation planning may further strengthen format standardisation, portability, export workflows, and compatibility with long-term archival systems and offline distribution methods.

### Metadata Preservation

Future preservation work may place additional emphasis on the long-term preservation of metadata including publication dates, authorship information, categories, citations, structured data, archival references, and URL stability. Metadata preservation is considered important because contextual and descriptive information often becomes historically valuable over time.

### Long-Term Link Stability

TSAP aims to minimise link rot and maintain stable long-term URLs wherever possible. Future work may include improved redirect systems, permalink audits, archival link expansion, canonical URL maintenance, and additional preservation-oriented approaches intended to support durable citation and long-term discoverability.

<style>
.preservation-meta {
  margin: 1rem 0 1.2rem;
  padding: 10px 14px;
  background: #f5f7f9;
  border: 1px solid #d8dee4;
  border-radius: 10px;
  font-size: 0.95em;
  color: #2b2b2b;
}

.preservation-legend {
  margin: 1rem 0 1.8rem;
  padding: 14px 16px;
  background: #fafafa;
  border: 1px solid #d8dee4;
  border-radius: 12px;
  font-size: 0.92em;
  line-height: 2;
  color: #222;
}

.preservation-status {
  display: inline-block;
  padding: 4px 10px;
  margin-left: 8px;
  margin-right: 6px;
  margin-top: 4px;
  margin-bottom: 4px;
  border-radius: 999px;
  font-size: 0.82em;
  font-weight: 600;
  vertical-align: middle;
  white-space: nowrap;
}

.status-active {
  background: #dff5e3;
  color: #166534;
  border: 1px solid #9ed8aa;
}

.status-experimental {
  background: #fff4d6;
  color: #8a5a00;
  border: 1px solid #e7c46a;
}

.status-planned {
  background: #e8f0ff;
  color: #1e4fa1;
  border: 1px solid #b8cdf5;
}

.status-not-started {
  background: #ffe3e3;
  color: #9b1c1c;
  border: 1px solid #e7a5a5;
}

@media (max-width: 640px) {
  .preservation-legend {
    line-height: 2.2;
    padding: 12px 14px;
  }

  .preservation-status {
    margin-left: 0;
  }
}
</style>
