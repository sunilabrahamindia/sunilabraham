---
layout: default
title: Versions
categories: [Project pages, Versions]
description: "Version history of the Sunil Abraham Project website, documenting updates, milestones, and design improvements."
permalink: /versions/
page_id: TSAP-0009
created: 2025-10-21
---

The **Versions** page documents the release history of the Sunil Abraham Project website. Each entry records structural updates, content milestones, and technical improvements across successive releases, providing a chronological record of the project's evolution.

📚 Older versions are available in the [**Versions Archive 1**](/versions/1/) and [**Versions Archive 2**](/versions/2/).

## Contents
1. [Version 2.1](#version-21)
2. [Version 2.1.1](#version-211)
3. [Version 2.1.2](#version-212)

<div align="center" style="width:75%; margin:auto;">
  <img    src="https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/Every%20Sun%20New%20Version%20banner.png?raw=true" 
    alt="Psychedelic poster for The Sunil Abraham Project with large text: 'Every Sun, New Version'" 
    style="width:100%; height:auto; max-width:480px;">
</div>

## Version 2.1

Because Version 2.0 was completed mid-week on 17 June 2026, the weekly report for Sunday, 21 June 2026, was omitted. A new reporting cycle has now begun.

Between 17 June and 27 June 2026, 29 new pages were published.

**GitHub Release**
- Extended the formal release history of The Sunil Abraham Project (TSAP) by creating and publishing the GitHub release for Version 2.0.
- The release is anchored to the historical repository snapshot of 17 June 2026 through the Git tag `v2.0`, providing a stable and verifiable reference point marking the completion of the Version 2.0 development cycle.

**Page ID System**
- Completed the assignment of permanent Page IDs to all eligible production pages.
- Updated the `add_page_ids.py` utility to continue numbering from the highest existing Page ID rather than restarting from the beginning, ensuring that Page IDs remain permanent, are never renumbered, and are never reused.

**Digital Preservation**
- Created a new preservation snapshot of the GitHub repository in [Software Heritage](https://www.softwareheritage.org/) following completion of Version 2.0.
- Updated the [Preservation](/tsap/preservation/) page to document the latest archival snapshot.

**Offline Preservation**
- Initiated the Offline TSAP preservation workflow by creating the first offline backup of the project's Git repository following completion of Version 2.0.
- The repository, including its complete Git history, has been preserved on local storage and uploaded to the public [Google Drive preservation archive](https://drive.google.com/drive/folders/1HM0vSnyA5uZWuHZFYt3zudDawZczGat3).
- Updated the [Preservation](/tsap/preservation/) page to document the new offline preservation workflow.

**Status** ✅ Done  
Completion date: 27 June 2026

## Version 2.1.1

Between 28 June and 4 July 2026, 14 new pages were published.

**Dark Mode**
- Continued the systematic rollout of the TSAP dark mode architecture, making substantial progress across the site.
- Following the transition to a centralised CSS custom properties framework, major layout improvements were completed for the Artificial Intelligence index, the A. M. A. Ayrookuzhiel portal, the Timeline biography, and the Query lookup tool.
- Experimental dark mode has now been enabled site-wide. It follows the user's device preference and may also be toggled manually using the Alt + Shift + D keyboard shortcut.
- Development and ongoing refinements are tracked in [Issue #8](https://github.com/sunilabrahamindia/sunilabraham/issues/8).

**TSAP Incidents**
- Published [Git Repository Storage Inflation Incident (1 July 2026)](/tsap/git-repository-storage-inflation/).
- Published [Git Repository Corruption Recovery (1 July 2026)](/tsap/git-repository-corruption-recovery/).

**Centre for Internet and Society**
- On 4 July 2026, marking the 18th anniversary of the Centre for Internet and Society, published [Centre for Internet and Society: 18th Anniversary](/cis/18/).

**Status** ✅ Done  
Completion date: 4 July 2026

## Version 2.1.2

Between 5 July and 11 July 2026, 12 new pages were published.

**TSAP Status**
- Developed and deployed the first public TSAP Status page. A lightweight monitoring system was built using Google Apps Script to perform hourly checks of selected website resources and record the results in a private Google Sheets spreadsheet. The monitoring data is exposed through a JSON API, while a Cloudflare Worker renders a public, mobile-friendly status page under a custom domain. This provides TSAP with an independent, serverless monitoring system built using free services and establishes a foundation for future additions such as expanded service checks, incident history, and uptime reporting. Please see it [here](https://status.sunilabraham.in/).

**Biographical and Book Articles**
- Started an article on [Rev. Dr. Y. T. Vinayaraj](/vinayaraj/).
- Started work on [*Sacrafanations: Dalit Religion(s): Epistemology, Theology, and Politics*](/amaa/sacrafanations/), edited by Y. T. Vinayaraj.

**A. M. A. Ayrookuzhiel**
- Started [Unfinished Manuscript of A. M. A. Ayrookuzhiel (Working Document)](/amaa/unfinished-manuscript/), a preparatory project to document and explore the possible reconstruction of an unfinished manuscript by Rev. Dr. A. M. A. Ayrookuzhiel, tentatively titled *Dalit and Hindu Religious Identity*. The manuscript remained incomplete at the time of his death in 1996 and was intended to explore questions surrounding caste identity and religious identity in India.
- Started work on [*The Dalit Deśiyata: The Kerala Experience in Development and Class Struggle*](/amaa/the-dalit-desiyata/), a 1990 volume edited by Rev. Dr. A. M. A. Ayrookuzhiel that brings together perspectives on the experiences of Dalit communities in Kerala in relation to development, class struggle, and wider social, economic, and political conditions.

**Status** ✅ Done  
Completion date: 11 July 2026

{% include versions.html %}
