---
layout: default
title: "How Does the Government Track All Its Legal Cases?"
description: "A Mint news report by Shreeja Sen on the Legal Information Management and Briefing System (LIMBS), its scope, structure, and the data security concerns it raises."
categories: [Media mentions]
date: 2016-09-13
authors: ["Shreeja Sen"]
source: "Mint"
permalink: /media/how-does-the-government-track-all-its-legal-cases-mint/
created: 2026-02-21
---

**How Does the Government Track All Its Legal Cases?** is a *Mint* news report by Shreeja Sen published on 13 September 2016. The article examines the Legal Information Management and Briefing System (LIMBS), a law ministry platform designed to centralise records of all government litigation under Digital India, and notes the data security concerns raised by [Sunil Abraham](/sunil).

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Mint</em></dd>

  <dt>📅 Date:</dt>
  <dd>13 September 2016</dd>

  <dt>👤 Author:</dt>
  <dd>Shreeja Sen</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>
    <a class="btn" href="https://www.livemint.com/Politics/e8NH6lBlIFbBss0cP54hrJ/How-does-the-government-track-all-its-legal-cases.html">
      Read Online
    </a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>New Delhi: More than one lakh cases currently exist on a law ministry platform curated in the last 13 months. The Legal Information Management and Briefing System (LIMBS), aimed to be a database of all the ongoing cases with the government as a party, is part of the government's push towards digital India.</p>

<p>Law secretary Suresh Chandra said this is a big step under the Digital India project, intended to monitor and ultimately reduce spending on government litigation.</p>

<p>"The aim is to conduct cases properly. If our system works, along with the national litigation policy, we will be able to prevent 50% cases before they are even filed," Chandra said.</p>

<p>According to the government, the project will help reduce delays in filing responses in cases, contempt notices because of such delays and consequent monetary penalties.</p>

<p>The website has also undergone the required security audit under the NIC (national informatics centre), to ensure the data is safe and protected.</p>

<p>However, a database like this on the internet comes with its challenges.</p>

<p>"To ensure client confidentiality, communication should be bilateral between lawyer and client and should be encrypted and even watermarked. If this project allows access to documents by multiple stakeholders without encrypting it for the recipient, then if there is any leak, the documents cannot be traced back to the person who was responsible," said Sunil Abraham, executive director at Centre for Internet and Society, a non-profit research organisation.</p>

<p>The LIMBS project began internally at the ministry of railway sometime in 2013, but was soon expanded as a single platform across ministries. In July 2015, it was hosted on the NIC server. The law ministry, by a gazette notification on 8 February, formally launched LIMBS to monitor cases filed against the Union government.</p>

<p>As of now, there is no special budget allocated for this project, which is being handled in house with a team of eight people – four developers on the technology side and four implementers for the case details. The development of the website is being handled by Ajay Gupta, deputy chief vigilance officer, northern railway. From the law ministry, Spriha Johari is the project director responsible for the website.</p>

<p>As of 12 September, the five ministries with the most uploads on the website were railways (69,469 cases), communications and information technology (7,830), finance (4452), environment (3,189) and defence (2,565).</p>

<p>Every day, nearly 400-500 cases are added to the portal. In all 58 ministries and their 202 departments have been brought under the LIMBS project.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

LIMBS was part of a broader push under the Digital India programme to digitise government processes and improve administrative efficiency. The platform was formally notified by the law ministry in February 2016, several months before this article was published, though the project had been in development since at least 2013 within the Railways ministry.

The article was published during a period of active debate around the government's handling of digital infrastructure, data protection, and centralised platforms — themes that ran in parallel with the Aadhaar litigation then before the Supreme Court. Abraham's concerns about encryption and document traceability echoed wider civil society arguments about the risks of aggregating sensitive state data on insufficiently secured platforms.

LIMBS remains in operation and has since been expanded, though questions around secure access and lawyer-client confidentiality for documents uploaded to government-managed portals have continued to feature in discussions about legal technology in India.

## External Link

- [Read on Mint](https://www.livemint.com/Politics/e8NH6lBlIFbBss0cP54hrJ/How-does-the-government-track-all-its-legal-cases.html)

<style>
.media-details {
  background: #f9fbfe;
  border: 1px solid #d8e2f0;
  border-radius: 10px;
  padding: 1.2rem 1.4rem;
  max-width: 700px;
  margin: 1.2rem auto;
  font-size: 0.96rem;
  line-height: 1.5;
  color: #333;
  box-shadow: 0 2px 4px rgba(0,0,0,0.04);
}
.media-details dt {
  font-weight: 600;
  color: #1b2a49;
  margin-top: 0.7rem;
}
.media-details dd {
  margin: 0 0 0.3rem 0.3rem;
  color: #555;
}
.highlighted-text {
  background-color: #fffbea;
  border-left: 4px solid #f2ce61;
  padding: 1rem 1.2rem;
  border-radius: 8px;
  line-height: 1.65;
  color: #333;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  margin-bottom: 0.8rem;
}
.highlighted-text p {
  margin-bottom: 1rem;
}
.copy-btn-full {
  display: inline-block;
  background: #f1f1f1;
  border: 1px solid #ccc;
  font-size: 0.85rem;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.2s ease;
  margin-bottom: 1.5rem;
}
.copy-btn-full:hover {
  background: #e5e5e5;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.copy-btn-full').forEach(btn => {
    btn.addEventListener('click', async () => {
      const target = document.querySelector(btn.getAttribute('data-copytarget'));
      if (!target) return;
      try {
        await navigator.clipboard.writeText(target.innerText.trim());
        const original = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => (btn.textContent = original), 1500);
      } catch (e) {
        btn.textContent = 'Copy failed';
        setTimeout(() => (btn.textContent = 'Copy Full Text'), 1500);
      }
    });
  });
});
</script>
