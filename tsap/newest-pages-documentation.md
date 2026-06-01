---
layout: default
title: "Newest Pages (Documentation)"
description: "A permanent record of articles featured in the 'From the Newest Pages' section on the TSAP home page, with the dates they were displayed."
categories: [TSAP Documentation]
permalink: /tsap/newest-pages-documentation/
created: 2026-04-25
---

The **From the Newest Pages** section on the [home page](/) features a rotating selection of recently added pages. This archive records which articles were shown and when, as a permanent editorial log.

Each entry below reflects one edition of the section — the five articles displayed on that date, in the order they appeared (newest created, first).

## 24 April 2026

On Friday, 24 April 2026, the following five articles were featured in the Newest Pages section on the home page.

<ol class="newest-archive-list">

  <li class="newest-archive-item">
    <a href="/amaa/role-of-religion-dalit-liberation/" class="newest-archive-title">The Role of Religion in Dalit Liberation: Some Reflections</a>
    <span class="newest-archive-date">Created: 24 April 2026</span>
    <p class="newest-archive-desc">A. M. A. Ayrookuzhiel's essay examining the role of religion, caste, and political structures in Dalit liberation through a series of ten theses.</p>
  </li>

  <li class="newest-archive-item">
    <a href="/cis/moa/" class="newest-archive-title">Memorandum of Association (MoA) of the Centre for Internet and Society</a>
    <span class="newest-archive-date">Created: 22 April 2026</span>
    <p class="newest-archive-desc">The Memorandum of Association and Rules and Regulations of the Centre for Internet and Society (CIS), registered on 4 July 2008 under the Karnataka Societies Registration Act, 1960.</p>
  </li>

  <li class="newest-archive-item">
    <a href="/media/worldwide-webmaster-bangalore-mirror/" class="newest-archive-title">Worldwide Webmaster</a>
    <span class="newest-archive-date">Created: 21 April 2026</span>
    <p class="newest-archive-desc">A <em>Bangalore Mirror</em> profile of Sunil Abraham, former Executive Director of the Centre for Internet and Society, published in the Work section on 16 March 2014.</p>
  </li>

  <li class="newest-archive-item">
    <a href="/media/indias-struggle-for-online-freedom-smh/" class="newest-archive-title">India's Struggle for Online Freedom</a>
    <span class="newest-archive-date">Created: 18 April 2026</span>
    <p class="newest-archive-desc">A <em>Sydney Morning Herald</em> opinion piece by Rebecca MacKinnon on India's growing internet freedom movement, the 2008 IT Act, the 2011 intermediary rules, and the risk of self-censorship.</p>
  </li>

  <li class="newest-archive-item">
    <a href="/media/on-the-internet-how-much-is-too-much-the-hindu/" class="newest-archive-title">On the Internet, How Much Is Too Much?</a>
    <span class="newest-archive-date">Created: 14 April 2026</span>
    <p class="newest-archive-desc">A <em>The Hindu</em> report by Deepa Kurup examining free speech and defamation online in India, with quotes from Sunil Abraham on the chilling effect of the IT Act.</p>
  </li>

</ol>

## 1 June 2026

On 1 June 2026, the "From the Newest Pages" section on the home page was redesigned and converted from a manually maintained feature into an automated system. Prior to this change, the section was updated by directly editing the `_includes/newest.html` file whenever a new article was selected for display. Titles, URLs, descriptions, and creation dates had to be copied manually into the homepage code, creating a separate layer of maintenance and duplicating information that already existed within the articles themselves.

The redesigned system uses page metadata to generate the section automatically. Pages intended to be eligible for inclusion are marked with `homepage_featured: true` in their front matter. The homepage then identifies all pages carrying this parameter, sorts them by their `created:` date, and displays the five most recently created featured pages. The title, description, URL, and creation date are retrieved directly from page metadata, ensuring that the information displayed on the homepage remains consistent with the underlying pages.

The change was made primarily to reduce routine maintenance and eliminate unnecessary duplication. Adding a page to the section no longer requires editing the homepage; instead, editors simply add `homepage_featured: true` to the page's front matter. As new featured pages are created, older entries automatically fall out of the displayed list without manual intervention. The entries above are preserved as a historical record of the manually maintained era of the feature and document the final configuration of the section before automation was introduced.

<style>
.newest-archive-list {
  list-style: none;
  padding: 0;
  margin: 1.5rem 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.newest-archive-item {
  padding: 1rem 1.25rem;
  border-left: 3px solid #005cc5;
  background: #f7f9ff;
  border-radius: 6px;
}

.newest-archive-title {
  display: block;
  font-weight: 700;
  font-size: 0.97rem;
  color: #003f8a;
  text-decoration: none;
  margin-bottom: 0.2rem;
}

.newest-archive-title:hover {
  text-decoration: underline;
}

.newest-archive-date {
  display: block;
  font-size: 0.75rem;
  color: #777;
  margin-bottom: 0.4rem;
}

.newest-archive-desc {
  font-size: 0.88rem;
  color: #444;
  line-height: 1.6;
  margin: 0;
}
</style>
