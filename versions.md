---
layout: default
title: Versions
categories: [Project pages]
description: "Version history of the Sunil Abraham Project website, documenting updates, milestones, and design improvements."
created: 2025-10-21
---

This page serves as a version log for the **Sunil Abraham Project** website. Each entry documents updates, milestones, and improvements across different releases — helping track design, structure, and content evolution over time.

## Contents
1. [Version 0.1](#version-01)
2. [Version 0.2](#version-02)
3. [Version 0.3](#version-03)
4. [Version 0.3.1](#version-031)
5. [Version 0.3.2](#version-032)


<div align="center" style="width:75%; margin:auto;">
  <img    src="https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/Every%20Sun%20New%20Version%20banner.png?raw=true" 
    alt="Psychedelic poster for The Sunil Abraham Project with large text: 'Every Sun, New Version'" 
    style="width:100%; height:auto; max-width:480px;">
</div>

## Version 0.1

Version 0.1 of the **Sunil Abraham Project** website is now live at [sunilabraham.in](https://www.sunilabraham.in/).  
The website has been built using **GitHub Pages** with a fully custom design and professional open documentation theme.  
It currently includes the following sections:

- **Home** – Overview of the project and its purpose.  
- **Projects** – Current work, including documentation on *A. M. Abraham Aryookuzhiel* and *Artificial Intelligence*.  
- **Publications** – Listing selected writings and research interests.  
- **Videos** – Embedded playlist of talks, lectures, and interviews.  
- **Contact** – Direct email link and collaboration note.

✅ **Status:** Completed — Version 0.1 is live.  
📅 **Completion Date:** 19 October 2025  
🗃️ **Internet Archive:** [Archived Snapshot (21 Oct 2025)](https://web.archive.org/web/20251021024650/https://www.sunilabraham.in/) 

## Version 0.2

Version 0.2 of the **Sunil Abraham Project** website continues to refine structure, navigation, and usability.  
This update focuses on strengthening the site’s foundational layout, consistency across pages, and transparency documentation.  
Key additions and improvements include:

- **General Design Improvement** — General design improvement, top share bar etc.
- **Footer Template** – A default footer has been created under `_includes`, allowing uniform use across all pages.  
- **Disclaimer Page** – Introduced to clarify authorship, delegation, and the possibility of occasional errors.  
- **Layout (default)** – Basic layout implemented and synchronised across pages for visual consistency.  
- **Privacy Policy Page** – Added with essential information and confirmation that no trackers are currently active.
- **Videos Page Expand** — Added more videos. The videos page have 30 videos now.
- **Sitemap Page** – A first version of the sitemap created to support navigation and automatic indexing.

✅ **Status:** Completed — Version 0.2 deployed.  
📅 **Completion Date:** 25 October 2025  
🗃️ **Internet Archive:** [Archived Snapshot (25 Oct 2025)](https://web.archive.org/web/20251025131339/https://sunilabraham.in/)

## Version 0.3

Version 0.3 of the **Sunil Abraham Project** website focuses on visual refinement, structural balance, and accessibility improvements.  
This release improves readability, layout consistency, and ease of navigation while keeping the design simple and functional.

**Sandbox Creation** – A new `/sandbox` subdirectory created for experimentation and safe testing of new features or layouts.  
  Note: included page; any error might disrupt default layout and other structure.  
- **robots.txt Setup** – Implemented to manage search engine visibility.  
  The `/sandbox` directory is excluded from indexing.  
- **Sitemap (XML) Creation** – Automatic sitemap generated at [https://sunilabraham.in/sitemap.xml](https://sunilabraham.in/sitemap.xml).  
  The `Sitemap.md` page improved with description and alphabetical sorting.  
- **Documentation Directory** – Work started on a dedicated `/doc` (or `/docs`) section for structured documentation and internal reference materials.  
- **A. M. Abraham Aryookuzhiel Biography Article** – First draft completed, one book article added.
- **Sunil Bio Compilation (First Draft)** – Compilation of Sunil Abraham’s biography begun, collecting key references, timelines, and curated notes.  
- **Categorisation** – Initiated categorisation of pages and articles for easier navigation.  
- **Template Development** –  
  - Back to Top button.  
  - Under Construction label.  
  - Under Construction percentage indicator (in progress).  
- **Videos Page Restructure** – Videos split into multiple yearly pages such as `/videos/2009`, `/videos/2010`, etc.  
- **Image Expansion Feature** – Planned feature to allow image enlargement when clicked (lightbox-style view).  

✅ **Status:** Completed — Version 0.3 completed.  
📅 **Completion Date:** 2 November 2025  
🗃️ **Internet Archive:** [Archived Snapshot (2 Nov 2025)](https://web.archive.org/web/20251102024245/https://sunilabraham.in/)


## Version 0.3.1

Version 0.3.1 of the **Sunil Abraham Project** marks a major expansion in the **Publications** section and continued refinement of the website’s structural and accessibility frameworks.  

This version emphasises content development, modular template creation, and user accessibility through shortcuts and keyboard navigation.

**🧾 Publications Section Expansion**
- **Major Update of the Week:** The Publications section underwent a comprehensive expansion, adding 20 new first-version articles across various themes such as open knowledge, digital culture, governance, and rights.  
- Each publication now follows a standardised seven-part structure — including *Lead section*, *Publication details*, *Abstract/Summary*, *Context and Background*, *Key Themes or Findings*, *Collaborators and Acknowledgements*, and *Related Publications*.  
- **Improved linking system:** Articles now include embedded links to related pages, PDFs, and cross-references within the site.  
- **File management:** New PDFs were uploaded to `/files/` and linked properly to their respective pages, ensuring consistent naming and SEO-friendly URLs (e.g., `/publications/digital-natives-with-a-cause/`).  
- **Accessibility and readability:** Enhanced layout consistency, alt-text coverage, and improved paragraph flow for better screen reader interpretation.

**🧩 Template Creation and Refinement**
- **Stub Template:** Introduced a new `stub.html` template for in-progress or partially completed pages, visually indicating a page under development.  
- **Notice Template:** Implemented the following include for dynamic notices that can display contextual information across multiple pages:

**Accesskey and Shortcuts**
- Introduced keyboard shortcuts (accesskeys) for major navigation areas to enhance accessibility for users with mobility or visual impairments.  
- Ensured compatibility across major browsers and assistive technologies.

**🧱 Structural and Ongoing Improvements**
- Internal consistency check for article front matter (`layout`, `title`, `description`, `categories`, and `date` fields).  
- Preparations started for integrating accessibility guidelines into future style.scss modularisation (refer to Version 0.3 roadmap).  
- Minor style adjustments for better mobile responsiveness in new article templates.  
- Archive verification for `/publications/` directory and newly added article pages.

✅ **Status:** Completed — Version 0.3.1 completed.  
📅 **Completion Date:** 9 November 2025  
🗃️ **Internet Archive:** [Archived Snapshot (9 Nov 2025)](https://web.archive.org/web/20251109062755/https://sunilabraham.in/)

## Version 0.3.2

Version 0.3.2 continues the major content-building phase of the **Sunil Abraham Project**, with a strong focus on expanding the Publications section, improving navigation, and strengthening the website’s organisational structure.

**📚 Publications Expansion (Major Focus)**  
- The Publications section remained the top priority this week.  
- **At least 10 new articles were added**, bringing the total to 82 articles, of which 57 fall under the Publications category.  
- Versions 0.3.1 and 0.3.2 together represent a significant leap in content development, especially in standardising templates, improving metadata, and ensuring internal consistency.

**👥 Collaboration & Author Pages**  
- **Author (Collaboration) page created** to help readers discover authors connected to the project or those who may collaborate in the future.  
- A dedicated Authors Directory page added to support collaboration visibility and cross-site navigation.

**📰 Media Directory**  
- A comprehensive Media Directory has been created to classify and list media articles, improving browsing for visitors and organising long-term archives.

**🔍 Google Search Console Integration**  
- Google Search Console account created.  
- XML sitemap successfully submitted for indexing.  
- This ensures improved SEO visibility, indexing accuracy, and long-term search performance.

**🧪 Sandbox Restructure**  
- The `/sandbox/` page was restructured to allow safe experiments to go live without being indexed.  
- Sandbox is now publicly accessible but excluded from sitemap and disallowed in robots.txt, ensuring experiments do not appear in search results.

**🌍 Content Enhancements**  
- Major expansion of the Students for Peace article with improved structure and detail.  
- Added a Did You Know (DYK) section on the Home page to increase engagement and highlight interesting facts.

**🧱 Additional Improvements**  
- Internal consistency updates across new pages.  
- Confirmed placement of collaboration and directory sections for long-term site organisation.

✅ **Status:** Completed — Version 0.3.2 done.  
📅 **Completion Date:** 16 November 2025  
🗃️ **Internet Archive:** [Archived Snapshot (16 Nov 2025)](https://web.archive.org/web/20251115231351/https://sunilabraham.in/)


