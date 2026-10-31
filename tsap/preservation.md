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

TSAP maintains ongoing public web archival workflows across three external services: the [Internet Archive Wayback Machine](https://web.archive.org/web/*/https://sunilabraham.in/), [Archive.today](https://archive.ph/https://sunilabraham.in/), and [Ghost Archive](https://ghostarchive.org/search?term=https://sunilabraham.in/). The Wayback Machine is the primary service and receives the most archival activity. Archive.today and Ghost Archive provide additional, independent copies, although their coverage is lower because submissions are currently made manually and both services can present operational obstacles.

### Internet Archive Wayback Machine

Wayback preservation combines manual submissions with several established workflows:

- **Browser-based submissions:** Pages can be submitted through the Wayback Machine website and its browser extension. The extension also allows a page to be archived from a link using the browser's context menu.
- **Google Apps Script:** An automated script submits pages selected from TSAP's published `pages.json` index on an hourly schedule. Some scheduled runs make multiple submission runs. The workflow has been used for several months, although some recent submissions have failed with a Wayback-side message such as "Wayback address not found". The cause of these intermittent failures has not been established.
- **Python random archiver:** The repository includes `scripts/wayback_random_archiver.py`, which selects eligible TSAP URLs, submits them to Wayback, and records successful captures, failures, and session reports. Its dedicated [documentation](/tsap/wayback-machine-random-archiver-documentation/) describes its operation and logs. The maintainer runs it manually, sometimes during other maintenance work.
- **Official Telegram bot:** The official Wayback Machine Telegram bot is another currently working route for submitting pages for archiving.

The published `pages.json` index supports these workflows by providing a structured list of TSAP pages. See the [Pages Index documentation](/tsap/pages-json-documentation/) for details.

The maintainer also checks the resulting capture history rather than treating submission attempts as successful archives. Based on these checks, the homepage has more than 400 successful Wayback captures. Important pages often have around 25-30 captures, and across the collection of more than 1,300 pages, existing pages generally have at least 15 captures and often 20 or more. Pages published very recently naturally have had less time to accumulate captures. These are observed capture-history figures, not counts of submission attempts.

### Archive.today

Archive.today submissions are currently performed manually. The maintainer commonly starts from TSAP's newest-pages listing, right-clicks a page link and uses the Archive Page browser extension or the service's submission interface. Pages that have not yet been captured are prioritised; when Archive.today reports an existing capture, the maintainer decides whether to request another snapshot, generally favouring a recapture when the previous one is at least a week or two old.

Archive.today sometimes becomes unavailable or fails to complete captures. The maintainer has observed such interruptions across different IP addresses and has received third-party reports of availability problems. When the service is unavailable, submissions are deferred until it works again.

The service sometimes presents a CAPTCHA for the first submission in a session. After it is solved, further submissions may be possible for a short period without another challenge, allowing several pages to be submitted in one session. The length of this period is variable and has not been measured consistently. The workflow remains manual: the maintainer completes the challenges and decides whether to recapture pages. No CAPTCHA-solving script or bot is used.

### Ghost Archive

Ghost Archive provides another independent preservation layer. Submissions are currently made manually by copying a page URL from TSAP's newest-pages listing and pasting it into the Ghost Archive website. The maintainer prioritises newer pages that do not yet have a Ghost Archive capture.

Ghost Archive can sometimes be unavailable or fail to complete a submission. It also frequently presents hCaptcha challenges, sometimes involving multiple steps that require careful human interpretation. When the challenge is too difficult to interpret, the maintainer may skip that submission and return to it later. At other times, Ghost Archive accepts a submission without presenting a CAPTCHA, allowing more pages to be submitted during that session. CAPTCHA frequency and service-side causes have not been independently established.

The maintainer handles these challenges manually and does not use scripts or bots to solve or bypass CAPTCHAs. No automated submission method is currently in use for Archive.today or Ghost Archive.

### Incremental Coverage and Reader Access

These workflows combine automated and manual preservation rather than relying on a single bulk export. Wayback receives the most sustained activity through the browser interface, Google Apps Script, the Python utility and the official Telegram bot. Archive.today and Ghost Archive are maintained through manual submissions, with the number of pages captured depending on service availability and CAPTCHA requirements.

TSAP also includes direct archival links in the footer of every page, allowing readers to look for preserved versions of the current page through the Internet Archive Wayback Machine, Archive.today and Ghost Archive. These links are generated dynamically using the page URL and form part of the project's broader commitment to transparency, public preservation, and long-term accessibility.

## Zenodo Preservation
<span class="preservation-status status-experimental">Experimental</span>

TSAP has begun publishing selected curated materials and archival collections through the [Zenodo Archives](/zenodo/) portal. Zenodo provides DOI-backed scholarly preservation infrastructure, helping ensure long-term citability, archival stability, and independent preservation outside the primary website infrastructure.

Zenodo deposits may include curated datasets, archival compilations, preserved research publications, structured metadata collections, and static exports of historically significant materials. The use of DOI-backed archival infrastructure complements the project's broader preservation strategy based on redundancy, distributed storage, and open formats.

## Repository Preservation
<span class="preservation-status status-active">Active</span>

TSAP incorporates repository-level preservation workflows based on Git, distributed version control, public source code hosting, and independent archival infrastructure. These workflows support long-term preservation, historical version tracking, disaster recovery, repository redundancy, and independent verification of the project's development history.

Because the project is built primarily using static files and open formats, repository-level preservation forms an important part of the long-term archival strategy of TSAP. Git enables detailed version tracking, historical recovery, distributed cloning, and preservation of the project's evolution over time.

### Software Heritage

The TSAP GitHub repository is preserved through Software Heritage, an independent long-term archival service for software source code and development history. The first TSAP repository snapshot was archived on 31 May 2026 at 17:16:46 UTC. Following the completion of TSAP Version 2.0, an additional archival snapshot was requested in June 2026 to preserve the repository at the conclusion of that development cycle.

Software Heritage preservation is ongoing. Multiple archival snapshots of the TSAP repository have now been recorded, providing independently preserved copies of the repository and its Git history at different points in the project's development. Rather than listing individual snapshots here, the complete history of preserved visits can be viewed through Software Heritage:

- [All preserved snapshots of the main TSAP repository](https://archive.softwareheritage.org/browse/origin/visits/?origin_url=https://github.com/sunilabrahamindia/sunilabraham&visit_type=git)
- [All preserved snapshots of the TSAP media repository](https://archive.softwareheritage.org/browse/origin/visits/?origin_url=https://github.com/sunilabrahamindia/sunilabrahammedia&visit_type=git)

Software Heritage adds an independent preservation layer beyond GitHub, web archiving services, local backups, and other preservation mechanisms, helping preserve not only the current source files but also the project's development history over time.

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

## Preservation-Oriented Architecture
<span class="preservation-status status-active">Active</span>

TSAP follows a preservation-oriented architecture that prioritises long-term accessibility, portability, and survivability over feature complexity. Whenever practical, the project prefers static technologies, open standards, and build-time processing in order to minimise long-term operational dependencies and reduce the risk of service disruption.

Rather than relying on continuously running backend infrastructure, TSAP is intentionally designed so that the complete website can be reconstructed from its Git repository using widely available open-source tools. The project therefore favours static site generation, plain text source files, distributed version control, and open file formats over database-driven or server-dependent solutions.

This philosophy also influences decisions about new features. Functionality that can be implemented during the static build process is generally preferred over features requiring permanent server-side services. While dynamic services may be introduced where they provide significant value, they are evaluated carefully against their long-term maintenance requirements and potential impact on preservation.

### Design Principles

- Static-first architecture
- Open and well-documented file formats
- Distributed version control using Git
- Minimal operational dependencies
- Build-time rather than run-time processing wherever practical
- Multiple independent preservation layers
- Reproducible website builds
- Preference for technologies that remain understandable and maintainable over long periods

### Canonical Site and Mirror

TSAP is automatically deployed to multiple independent hosting platforms from the same Git repository.

The primary public website is hosted at <https://sunilabraham.in/> using GitHub Pages. A secondary deployment on Cloudflare Pages functions as a preservation mirror, redundancy layer, and disaster recovery platform. The mirror is intentionally excluded from search engine indexing using the `X-Robots-Tag` HTTP response header to prevent duplicate indexing while preserving an independently hosted copy of the website.

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


{% include navbox-tsap.html %}

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
