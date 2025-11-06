---
layout: default
title: "Fixing Aadhaar: Security developers' task is to trim chances of data breach"
description: "An opinion column by Sunil Abraham on Aadhaar security design, highlighting the need for tokenisation and multiple identity systems to prevent nationwide data breaches."
categories: [Publications, Media]
date: 2018-01-10
authors: ["Sunil Abraham"]
source: "Business Standard"
permalink: /publications/fixing-aadhaar-security-developers-task-is-to-trim-chances-of-data-breach/
---

**Fixing Aadhaar: Security developers' task is to trim chances of data breach** is an opinion piece by Sunil Abraham, originally published in *Business Standard* on 10 January 2018.  
The column analyses the fragility of centralised identity systems like Aadhaar and argues for systemic design changes such as tokenisation and multi-identifier frameworks to eliminate the possibility of large-scale breaches.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)  
4. [Key Points](#key-points)  
5. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Business Standard</em></dd>

  <dt>📅 Date:</dt>
  <dd>10 January 2018</dd>

  <dt>👤 Author:</dt>
  <dd>Sunil Abraham</dd>

  <dt>📄 Type:</dt>
  <dd>Opinion Column</dd>
</dl>

<figure class="media-image">
  <img src="https://raw.githubusercontent.com/sunilabrahamindia/sunilabraham/main/publications/images/Aadhaar%20verification%20queue.jpg"
       alt="People queueing for Aadhaar registration, illustrating digital identity enrolment in India.">
  <figcaption>File photo of Aadhaar registration being done.</figcaption>
</figure>

## Full Text

<div class="highlighted-text" id="fulltext">
I feel no joy when my prophecies about digital identity systems come true. This is because from a Popperian perspective these are low-risk prophecies. I had said that all centralised identity databases will be breached in the future. That may or may not happen within my lifetime, so I can go to my grave without worries about being proven wrong. Therefore, the task before a security developer is not only to reduce the probability but, more importantly, to eliminate the possibility of certain occurrences.

The blame for fragility in digital identity systems today can be partially laid on a World Bank document titled *Ten Principles on Identification for Sustainable Development*, which has contributed to the harmonisation of approaches across jurisdictions. Principle three says, “Establishing a robust — unique, secure, and accurate — identity.” The keyword here is “a”. Like *The Lord of the Rings*, the World Bank wants “one digital ID to rule them all”. For Indians, this approach must be epistemologically repugnant as ours is a land which has recognised the multiplicity of truth since ancient times.

In *Identities Research Project: Final Report* funded by the Omidyar Network and published by Caribou Digital, the number one finding is “people have always had, and managed, multiple personal identities”. And the fourth finding is “people select and combine identity elements for transactions during the course of everyday life”. As researchers they have employed indirect language; for laypersons, the key takeaway is that a single national ID for all persons and all purposes is an ahistorical and unworkable solution.

There are many ways in which such an identity monoculture can be prevented. The traditional approach is followed in the United States — you could have multiple documents that are accepted as valid ID. Or you could have multiple identity providers issuing ID artefacts using an interoperable framework as they do in the United Kingdom. Another approach is tokenisation.

The first time tokenisation was suggested in the Aadhaar context was in an academic paper published in August 2016 by Shweta Agrawal, Subhashis Banerjee and Subodh Sharma from IIT Delhi titled *Privacy and Security of Aadhaar: A Computer Science Perspective*. The paper, in its fourth key recommendation, says “cryptographically embed Aadhaar ID into Authentication User Agency (AUAs) and KYC User Agency (KUAs)–specific IDs making correlation impossible”. The paper considers several designs for such local identifiers.

*Revoke all Aadhaar numbers that have been compromised, breached, leaked, illegally published or inadvertently disclosed, and regenerate new global identifiers.*

There are many ways to prevent an identity monoculture. Tokenisation and multiple identity providers offer systemic resilience — they trim, if not eliminate, the chances of identity data breach. The challenge before security developers is not just to make Aadhaar harder to hack, but to re-architect it so that no single breach can ever compromise an entire nation’s data.
</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This article was written in the aftermath of early Aadhaar-related data breach reports and public debates on privacy and surveillance in India. At that time, civil society experts and technologists were raising concerns about the structural design of the Aadhaar ecosystem — particularly the risks of using a single, centralised identifier for billions of citizens.  

Sunil Abraham's argument anticipates many of the recommendations later echoed in privacy and digital identity policy circles, emphasising the need for tokenisation, revocation of compromised IDs, and plural identity frameworks.

## Key Points

- **Centralised identity systems are inherently fragile.**  
  Security developers must design to *eliminate* breaches, not merely reduce their probability.  

- **Global development frameworks often promote monocultures.**  
  The World Bank’s “one ID to rule them all” approach ignores cultural and epistemological diversity.  

- **India’s identity system should recognise multiplicity.**  
  People manage multiple identities in practice; digital policy should reflect this lived reality.  

- **Tokenisation offers a viable technical fix.**  
  Embedding cryptographic IDs for each AUA or KUA can prevent correlation and systemic data leaks.  

- **Compromised Aadhaar numbers should be revoked and reissued.**  
  This measure would rebuild trust and ensure long-term data integrity.

{% include back-to-top.html %}

## External Link

- [Read on Business Standard](https://www.business-standard.com/article/opinion/fixing-aadhaar-security-developers-task-is-to-trim-chances-of-data-breach-118010901281_1.html)

{% include back-to-top.html %}

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
.media-image {
  text-align: center;
  margin: 1.5rem auto;
  max-width: 720px;
}
.media-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.media-image figcaption {
  font-size: 0.9rem;
  color: #555;
  margin-top: 0.5rem;
}
</style>

<script>
document.querySelectorAll('.copy-btn-full').forEach(button => {
  button.addEventListener('click', async () => {
    const targetSelector = button.getAttribute('data-copytarget');
    const targetElement = document.querySelector(targetSelector);
    if (targetElement) {
      const text = targetElement.innerText.trim();
      await navigator.clipboard.writeText(text);
      button.textContent = 'Copied!';
      setTimeout(() => (button.textContent = 'Copy Full Text'), 1500);
    }
  });
});
</script>
