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
4. [Version 2.1.3](#version-213)
5. [Version 2.2](#version-22)
6. [Version 2.2.1](#version-221)
7. [Version 2.2.2](#version-222)

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

## Version 2.1.3

Between 12 and 18 July 2026, 16 new pages were published.

**Pages Index Automation**
- The generation and publication of TSAP's `pages.json` index were successfully automated using GitHub Actions. The workflow now regenerates the index automatically when relevant Markdown content changes, commits updates only when necessary, ignores its own commits to prevent recursive runs, and correctly skips commits when no changes are detected.
- The automation was fully verified when the newly created *Template:Versions* page was automatically added to `pages.json` without manual intervention. The Pages Index documentation was updated accordingly. Further details are available in [GitHub Issue #23](https://github.com/sunilabrahamindia/sunilabraham/issues/23).

**TSAP Monitoring Systems**
- Documented the development and implementation of the [TSAP Status Monitor](/tsap/status-monitoring-system/).
- Started work on the [TSAP Domain Expiry Monitor](/tsap/domain-expiry-monitor/), an automated system that monitors the registration expiry date of TSAP's primary domain. The system periodically retrieves authoritative registration data from the official NIXI RDAP service, detects domain renewals, and sends email reminders as the expiry date approaches.

**A. M. A. Ayrookuzhiel**
- Started the [A. M. A. Ayrookuzhiel Storytelling Project](/amaa/storytelling/), which documents the planning, development, and implementation of accessible storytelling resources based on the writings and ideas of Rev. Dr. A. M. A. Ayrookuzhiel.

**TSAP Documentation**
- Created [Linux and Git Commands for TSAP Repository Maintenance](/tsap/linux-git-commands/), documenting commands frequently used in the maintenance and management of the TSAP repository.

**Centre for Internet and Society**
- Following the 18th anniversary of the Centre for Internet and Society (CIS) in July 2026, continued work on documenting the organisation's history between 2008–2019.
- Articles created during this period include [Centre for Internet and Society Section 12A Registration](/cis/12a-registration-2010/) (2010), [Centre for Internet and Society FCRA Registration](/cis/fcra-registration-2012/) (2012), [Centre for Internet and Society FCRA Registration Renewal](/cis/fcra-renewal-2016/) (2016), and [Organisational Policies of the Centre for Internet and Society](/cis/organisational-policies-2019/) (2019).

**Status** ✅ Done  
Completion date: 18 July 2026

## Version 2.2

Between 19 and 25 July 2026, 17 new pages were published.

**Honesty**
- Started documenting [Honesty](/tsap/honesty/) as a core value of The Sunil Abraham Project. The page proposes that honesty is essential to the project and that everyone involved should make every sincere effort to be honest in their work, conduct, and interactions. The page remains under construction.

**Repository Maintenance**
- Added a repository-level `.gitignore` file covering common Python cache files, local virtual environments, environment variable and secret files, Jekyll build output, local Git backups, operating system artefacts, and editor-specific files.
- The `.git-backup/` directory is now explicitly ignored, helping prevent local Git backup data from being accidentally committed to the repository.

**Category System**
- Added optional support for “main article” links on TSAP category pages. Categories can now identify a principal overview page or work through their front matter, displaying a short “The main article for this category is...” notice below the category description and above the alphabetical page listing. The feature was initially implemented for the Swami Anand Thirth category.
- Improved the category system to support custom category permalinks while maintaining compatibility with existing category links. This allows category pages to use shorter, more meaningful URLs without disrupting existing categories or internal navigation.

**Automatic Last Updated Dates**
- Enhanced TSAP's [Automatic Last Updated Dates](/tsap/automatic-last-updated-dates-documentation/) system to prevent non-substantive maintenance changes from appearing as meaningful page updates.
- The system now ignores the repository-wide Page ID migration commit and commits explicitly marked with `[Minor]`, `[Minor edit]`, `[Metadata]`, `[Batch edit]`, or `[Maintenance]`, continuing backwards through Git history to identify the latest substantive edit.
- The updated system was tested across 1,169 Markdown files, verified to produce deterministic output, and manually checked against page history.

**ICANN Documentary Information Disclosure Policy**
- Started documenting the [ICANN Documentary Information Disclosure Policy (DIDP)](/didp/), covering the policy and process, selected requests and responses, and related transparency and accountability resources. The page will serve as the central hub for DIDP-related documentation, research, and archival work on TSAP.

**Status** ✅ Done  
Completion date: 25 July 2026

## Version 2.2.1

Between 26 July and 1 August 2026, 16 new pages were published.

**Category System**
- Fixed a category display issue where unwanted spaces appeared before commas separating category names. The problem was caused by whitespace within inline `<li>` elements and was resolved by placing each `<li><a>...</a></li>` element on a single line without requiring CSS changes.
- Added support for hidden maintenance categories. Pages can now use a `hidden_categories` front matter field so maintenance categories remain part of the site's category system while being omitted from the category list displayed at the bottom of individual pages.
- Introduced automatic population of technical maintenance categories, with the first implementation identifying pages containing embedded YouTube videos.

**Elonnai Hickok**
- Started a biographical article on [Elonnai Hickok](/elonnai/) together with several related articles, primarily documenting blog posts written by Elonnai in 2010.
- The pages are grouped under [Template:Elonnai Hickok](/elonnai/template).

**Centre for Internet and Society**
- Started [Category:CIS-A2K](/categories/cis-a2k/) under the Centre for Internet and Society category. This category will document selected articles relating to the history of CIS-A2K during the period when Sunil Abraham served as Executive Director of the organisation.

**Status** ✅ Done  
Completion date: 1 August 2026

## Version 2.2.2

Between 2 August and 8 August 2026, 20 new pages were published on The Sunil Abraham Project.

**Elonnai Hickok**
- Expanded [Template:Elonnai Hickok](/elonnai/template/) and continued documenting her CIS Blog posts. 12 new pages were published as part of this work during the week.

**Maintenance Categories**
- Started [Maintenance Categories](/category/maintenance-categories/) as a dedicated space for technical tracking, editorial workflows, and other site maintenance tasks.
- The section currently contains 8 maintenance categories.

**Dark Mode**
- Continued the site-wide dark mode audit and implemented a range of page-specific fixes and refinements.
- Further details are documented in [GitHub Issue #8](https://github.com/sunilabrahamindia/sunilabraham/issues/8).

**Status** ✅ Done  
Completion date: 8 August 2026

{% include versions.html %}
