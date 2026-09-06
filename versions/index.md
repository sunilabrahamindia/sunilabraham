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
8. [Version 2.2.3](#version-223)
9. [Version 2.3](#version-23)
10. [Version 2.3.1](#version-231)
11. [Version 2.3.2](#version-232)

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

## Version 2.2.3

Between 9 August and 15 August 2026

- 25 new pages have been published on The Sunil Abraham Project.

**Elonnai Hickok**
- Continued documenting and archiving the works of [Elonnai Hickok](/elonnai/), including [*An Interview with Dr. Ann Cavoukian, Information and Privacy Commissioner, Ontario, Canada*](/elonnai/interview-with-anne-cavoukian/), [*Privacy Perspectives on the 2012–2013 Goa Beach Shack Policy*](/elonnai/privacy-perspectives-on-the-2012-2013-goa-beach-shack-policy/), and [*SCOSTA and UID Comparison Not Valid, Says Finance Committee*](/elonnai/scosta-uid-comparison-invalid/).

**General Maintenance**
- Carried out general fixes and maintenance, including removing the Utilities option from the Top Bar and restoring the first version of the Top Bar.
- The Utility Toolbox has not yet been restored. Progress is being tracked in [GitHub Issue #16](https://github.com/sunilabrahamindia/sunilabraham/issues/16).

**Status** ✅ Done  
Completion date: 15 August 2026

## Version 2.3

From Sunday 16 August 2026 to Saturday 22 August 2026, 11 pages were created. Some of those are—

* **[Draft International Principles on Communications Surveillance and Human Rights](/elonnai/draft-intl-principles-on-communications-surveillance-and-human-rights/)**, created on 17 August 2026 – A 2013 CIS post by Elonnai Hickok outlining the Draft International Principles on Communications Surveillance and Human Rights developed by Privacy International and the Electronic Frontier Foundation, with feedback from CIS and other international participants under the SAFEGUARDS project.
* **[Data Retention in India](/elonnai/data-retention-in-india/)**, created on 17 August 2026 – A 2013 CIS post by Elonnai Hickok examining data retention mandates and practices in India, comparing them with European and US approaches, and presenting findings from RTI requests filed with BSNL and MTNL under the SAFEGUARDS project.
* **[A Comparison of Indian Legislation to Draft International Principles on Surveillance of Communications](/elonnai/comparison-of-indian-legislation-and-draft-principles-on-surveillance-of-communications/)**, created on 18 August 2026 – A 31 January 2013 CIS post by Elonnai Hickok comparing Indian surveillance legislation, including the Indian Telegraph Act and Information Technology Act rules, against the Draft International Principles on Surveillance of Communications developed under the SAFEGUARDS project.
* **[2012: Privacy Highlights in India](/elonnai/2012-privacy-highlights-in-india/)**, created on 19 August 2026 – A February 2013 CIS post by Elonnai Hickok summarising the major privacy developments of 2012 in India, including the Report of Group of Experts on Privacy, the RIM standoff, the Nira Radia controversy, the Centralised Monitoring System, and the UID project.
* **[Surveillance Camp IV: Disproportionate State Surveillance — A Violation of Privacy](/elonnai/disproportionate-state-surveillance-a-violation-of-privacy/)**, created on 20 August 2026 – A February 2013 EFF Deeplinks post co-written by Katitza Rodriguez and Elonnai Hickok, the fourth in a series mapping global surveillance challenges discussed at EFF's State Surveillance and Human Rights Camp in Rio de Janeiro, examining state-mandated identity verification, encryption restrictions, and blanket interception mandates.
* **[Unique Identification Scheme (UID) & National Population Register (NPR), and Governance](/elonnai/uid-and-npr-a-background-note/)**, created on 22 August 2026 – A March 2013 CIS background note by Elonnai Hickok examining the UID and NPR schemes in India, their legal grounding, enrolment processes, adoption by different states, and the differences and controversies between the two projects, prepared under the SAFEGUARDS project.
* **[Draft Human DNA Profiling Bill (April 2012): High Level Concerns](/elonnai/draft-human-dna-profiling-bill-april-2012/)**, created on 22 August 2026 – A March 2013 CIS post by Elonnai Hickok outlining high-level concerns with the April 2012 working draft of the Human DNA Profiling Bill, examining overreaching offence categories, weak access controls, inadequate consent provisions, and missing privacy safeguards, prepared under the SAFEGUARDS project.

* **Time and Date Converter** We created a [Time & Date Converter tool](/tools/timeanddate). We needed such a tool for our meetings and events a few times, so we built an in-house, customised tool. One can also generate a shareable link that carries the date, time, timezone and an optional event name/location, so anyone who opens it immediately sees the time converted into their own timezone. 

**Git activity:** 58 commits.

**GitHub issues created:** 1.
* #28 [Standardise category permalinks to /categories/](https://github.com/sunilabrahamindia/sunilabraham/issues/28), created on 20 August 2026

## Version 2.3.1
From Sunday 23 August 2026 to Saturday 29 August 2026, 18 pages were created.

* **[Open Letter to "Not" Recognize India as Data Secure Nation till Enactment of Privacy Legislation](/elonnai/open-letter-to-not-recognize-india-as-data-secure-nation/)**, created on 23 August 2026 – A June 2013 CIS open letter by Elonnai Hickok urging European Data Protection Commissioners not to recognise India as a data secure nation until it enacts comprehensive privacy legislation, prepared under the SAFEGUARDS project.
* **[More than a Hundred Global Groups Make a Principled Stand against Surveillance](/elonnai/more-than-hundred-global-groups-make-principled-stand-against-surveillance/)**, created on 23 August 2026 – A July 2013 CIS post by Elonnai Hickok announcing the formal launch of the International Principles on the Application of Human Rights to Communications Surveillance, co-signed by over a hundred global organisations and led by Privacy International, Access, and the Electronic Frontier Foundation.
* **[Versions Helper Tool](/versions/helper/)**, created on 24 August 2026 – A helper tool for generating version reports for The Sunil Abraham Project from any selected date range.
* **[Does TSAP Use a Wiki Engine?](/tsap/wiki-engine/)**, created on 24 August 2026 – An explanation of how TSAP is built without a conventional wiki engine, and how Jekyll, Markdown, YAML, Git, GitHub, and custom TSAP scripts provide many wiki-like capabilities.
* **[An Interview with Suresh Ramasubramanian](/elonnai/interview-with-suresh-ramasubramanian/)**, created on 24 August 2026 – A September 2013 CIS interview conducted by Elonnai Hickok with Suresh Ramasubramanian, ICS Quality Representative for IBM SmartCloud, covering cybersecurity, cloud data jurisdiction, encryption, spam regulation, and state-sponsored surveillance malware, prepared under the SAFEGUARDS project.
* **[22 August 2026 Meeting: Methodology and Vision for the Unfinished Manuscript](/amaa/unfinished-manuscript-meeting-2026-08-22/)**, created on 24 August 2026 – Documentation of the 22 August 2026 meeting in which Sunil Abraham discussed the methodology, reconstruction process and broader vision for the unfinished manuscript of A. M. A. Ayrookuzhiel.
* **[A Privacy Meeting with the Federal Trade Commission in New Delhi](/elonnai/privacy-meeting-with-ftc-new-delhi/)**, created on 25 August 2026 – A September 2013 CIS post by Elonnai Hickok recounting a roundtable meeting between the Centre for Internet and Society and Federal Trade Commission officials Betsy Broder and Sarah Schroeder in New Delhi, comparing the US sectoral approach to privacy regulation with emerging frameworks and challenges in India.
* **[Open Letter to Members of the European Parliament of the Civil Liberties, Justice and Home Affairs Committee](/elonnai/open-letter-members-european-parliament-civil-liberties-justice-home-affairs-committee/)**, created on 25 August 2026 – An October 2013 CIS open letter by Elonnai Hickok expressing support for the EU's proposed General Data Protection Regulation, while raising four concerns around purpose limitation, interpretation of broad terms, jurisdictional scope, and foreign intelligence access, sent as part of a joint initiative with Privacy International and other NGOs.
* **[CIS and International Coalition Calls upon Governments to Protect Privacy](/elonnai/cis-and-international-coalition-calls-upon-governments-to-protect-privacy/)**, created on 25 August 2026 – A September 2013 CIS post by Elonnai Hickok reporting on the Centre for Internet and Society's participation in an international coalition presenting the 13 International Principles on the Application of Human Rights to Communications Surveillance at the UN Human Rights Council in Geneva.
* **[An Interview with Jacob Kohnstamm, Dutch Data Protection Authority and Chairman of the Article 29 Working Party](/elonnai/interview-with-jacob-kohnstamm/)**, created on 26 August 2026 – An October 2013 CIS interview with Jacob Kohnstamm, then head of the Dutch Data Protection Authority and Chairman of the Article 29 Working Party, covering the DPA's supervisory powers, funding, organisational structure, and his views on possible privacy legislation and regulatory structures for India.
* **[A. M. A. Ayrookuzhiel — Knowledge Engine](/amaa/search/)**, created on 26 August 2026 – Explore and interact with the writings, research, and archival material of A. M. A. Ayrookuzhiel.
* **[What India Can Learn from the Snowden Revelations](/elonnai/yahoo-october-23-2013-what-india-can-learn-from-snowden-revelations/)**, created on 27 August 2026 – An October 2013 Yahoo op-ed by Elonnai Hickok examining India's legal gaps in surveillance oversight, its response to the Snowden and PRISM revelations, and the case for domestic servers and stronger privacy safeguards.
* **[Seventh Privacy Round-table](/elonnai/report-of-seventh-privacy-round-table/)**, created on 28 August 2026 – A November 2013 CIS report by Elonnai Hickok on the seventh and final Privacy Round-table held in New Delhi, featuring presentations by Jacob Kohnstamm, Chantal Bernier, and Christopher Graham on privacy frameworks in the EU, Canada, and the UK, and discussions on India's Privacy Protection Bill, 2013.
* **[Internet Privacy in India](/elonnai/internet-privacy-in-india/)**, created on 28 August 2026 – A January 2013 CIS knowledge repository article by Elonnai Hickok examining internet privacy in India, covering the changing nature of online personal data, jurisdictional complications, current legal provisions under the IT Act, cyber café surveillance rules, the Report of the Group of Experts on Privacy's nine national privacy principles, and the state of privacy legislation in Indiao.
* **[CIS Supports the UN Resolution on "The Right to Privacy in the Digital Age"](/elonnai/cis-supports-the-un-resolution-on-the-right-to-privacy-in-the-digital-age/)**, created on 28 August 2026 – A November 2013 CIS post by Elonnai Hickok welcoming the UN General Assembly's non-binding resolution on the Right to Privacy in the Digital Age, drafted by Brazil and Germany, and situating it alongside the Necessary and Proportionate principles as a framework for evaluating India's surveillance regime.
* **[UIDAI Practices and the Information Technology Act, Section 43A and Subsequent Rules](/elonnai/uidai-practices-and-the-information-technology-act-section-43a-and-subsequent-rules/)**, created on 29 August 2026 – A February 2014 CIS post by Elonnai Hickok examining UIDAI practices against Section 43A of the Information Technology Act and the Information Technology Reasonable Security Practices and Procedures and Sensitive Personal Data or Information Rules, 2011, using publicly available UIDAI documents and the Aadhaar enrolment form.
* **[GNI Assessment Finds ICT Companies Protect User Privacy and Freedom of Expression](/elonnai/gni-assessment-finds-ict-companies-protect-user-privacy-and-freedom-of-expression/)**, created on 29 August 2026 – A January 2014 CIS post by Elonnai Hickok analysing the Global Network Initiative's Public Report on the Independent Assessment Process for Google, Microsoft, and Yahoo, which found the three companies in compliance with GNI principles on privacy and freedom of expression.
* **[Comparison of Section 35(1) of the Draft Human DNA Profiling Bill and Section 4 of the Identification Act Revised Statute of Canada](/elonnai/comparison-of-section-35-1-of-draft-human-dna-profiling-bill-and-section-4-of-identification-act-revised-statute-of-canada/)**, created on 29 August 2026 – A March 2014 CIS post by Elonnai Hickok comparing section 35(1) of India's Draft Human DNA Profiling Bill with section 4 of Canada's Identification Act, Revised Statute of Canada, and examining best practices for communicating DNA profile information to law enforcement, DNA laboratories, courts, and tribunals.

**Git activity:** 87 commits.

**GitHub issues created:** 6.
* #29 [Status Monitoring System v2](https://github.com/sunilabrahamindia/sunilabraham/issues/29), created on 26 August 2026
* #30 [Implement "main article" links across applicable category pages](https://github.com/sunilabrahamindia/sunilabraham/issues/30), created on 26 August 2026
* #31 [Broken links cleanup — August 2026](https://github.com/sunilabrahamindia/sunilabraham/issues/31), created on 26 August 2026
* #32 [Automate regular Software Heritage archival](https://github.com/sunilabrahamindia/sunilabraham/issues/32), created on 29 August 2026
* #33 [Create short URLs for important content](https://github.com/sunilabrahamindia/sunilabraham/issues/33), created on 29 August 2026
* #34 [Add Alt + Shift + H keyboard shortcut for Home](https://github.com/sunilabrahamindia/sunilabraham/issues/34), created on 29 August 2026

## Version 2.3.2
From Sunday 30 August 2026 to Saturday 5 September 2026, 11 pages were created.

* **[Leaked Privacy Bill: 2014 vs. 2011](/elonnai/leaked-privacy-bill-2014-vs-2011/)**, created on 30 August 2026 – A March 2014 CIS post by Elonnai Hickok comparing the leaked draft Privacy Bill 2014, prepared by the Department of Personnel and Training, against the previously leaked September 2011 Privacy Bill, covering changes to scope, definitions, exceptions, privacy principles, and enforcement mechanisms.
* **[Intermediary Liability Resources](/elonnai/intermediary-liability-resources-2014/)**, created on 30 August 2026 – A CIS resource roundup by Elonnai Hickok collecting reports, papers, and interviews on internet intermediary liability from organisations including CDT, Article 19, WIPO, EFF, the European Commission, GNI, and the Association for Progressive Communications.
* **[Report of the Group of Experts on Privacy vs. The Leaked 2014 Privacy Bill](/elonnai/report-of-group-of-experts-on-privacy-vs-leaked-2014-privacy-bill/)**, created on 31 August 2026 – An April 2014 CIS post by Elonnai Hickok comparing the recommendations of the Justice AP Shah Committee's Report of the Group of Experts on Privacy against the text of the leaked 2014 Privacy Bill, identifying where the Bill incorporates the Report's recommendations and where it departs from them.
* **[Security, Governments, and Data: Technology and Policy](/elonnai/security-governments-and-data-technology-and-policy/)**, created on 1 September 2026 – A January 2015 CIS and Observer Research Foundation conference in New Delhi, with the event post written by Elonnai Hickok, examining the technologies, policies, and practices around cyber security and surveillance in India.
* **[Dalit Kavithakal: Oru Padanam](/amaa/dalit-kavithakal/)**, created on 2 September 2026 – A Malayalam-language book by Paul Chirakkarodu, M. Sathyaprakasham and Athanasius Mathen Abraham Ayrookuzhiel, published by Christian Literature Society in Tiruvalla in 1992.
* **[Authority Control: Elonnai Hickok](/elonnai/authority-control/)**, created on 3 September 2026 – Authority control identifiers, bibliographic records, scholarly profiles, archival references, and related metadata associated with Elonnai Hickok.
* **[Dalit Sahityam](/amaa/dalit-sahityam/)**, created on 3 September 2026 – A Malayalam-language book by Paul Chirakkarod and Athanasius Mathen Abraham Ayrookuzhiel, published in Tiruvalla in 1995.
* **[Religion, Culture and Power (Editorial)](/amaa/religion-culture-and-power-editorial-1985-03/)**, created on 4 September 2026 – An editorial by A. M. Abraham Ayrookuzhiel on religion, culture and power, published in Religion and Society, Vol. 32, No. 1, March 1985.
* **[The Witness](/tito/witness/)**, created on 5 September 2026 – A visual meditation on the Witness — awareness that remains still while the cosmos moves.
* **[Category:TSAP Exhibition](/categories/tsap-exhibition/)**, created on 5 September 2026 – Visual, artistic, and contemplative works presented as part of The Sunil Abraham Project's exhibition space.
* **[Category:Tito Dutta](/categories/tito-dutta/)**, created on 5 September 2026 – Content related to Tito Dutta (Zone) on The Sunil Abraham Project, including ideas, plans, analysis, commentaries, and other related work.

**Git activity:** 81 commits.

**GitHub issues created:** 5.
* #35 [Bulletin 5.1 — Preparatory Bulletin](https://github.com/sunilabrahamindia/sunilabraham/issues/35), created on 2 September 2026
* #36 [Create Dalit Kavithakal: Oru Padanam (Dalit Poems: A Study) article](https://github.com/sunilabrahamindia/sunilabraham/issues/36), created on 2 September 2026
* #37 [Create Dalit Sahityam (Dalit Literature) book article](https://github.com/sunilabrahamindia/sunilabraham/issues/37), created on 3 September 2026
* #38 [Mapping and Documentation of Recently Scanned Essays of A. M. A. Ayrookuzhiel](https://github.com/sunilabrahamindia/sunilabraham/issues/38), created on 4 September 2026
* #39 [Create Google Apps Script to monitor repository size](https://github.com/sunilabrahamindia/sunilabraham/issues/39), created on 4 September 2026


{% include versions.html %}
