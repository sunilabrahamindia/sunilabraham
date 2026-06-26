---
layout: default
title: "Hammered Government Offers Virtual ID Firewall to Protect Your Aadhaar"
description: "A The New Indian Express report on UIDAI's Virtual ID protocol, covering its scope and limitations, with Sunil Abraham calling for a full redo of Aadhaar-KYC."
categories: [Media mentions]
date: 2018-01-11
source: "The New Indian Express"
permalink: /media/hammered-government-offers-virtual-id-firewall-aadhaar-the-new-indian-express/
page_id: TSAP-1084
created: 2026-06-22
---

**"Hammered Government Offers Virtual ID Firewall to Protect Your Aadhaar"** is a *The New Indian Express* report published on 11 January 2018. The article covers UIDAI's announcement of a Virtual ID system as a response to reported security breaches in the Aadhaar programme, with [Sunil Abraham](/sunil/) arguing that the measure would only be effective if the Aadhaar-KYC process were redone entirely from scratch.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>The New Indian Express</em></dd>

  <dt>📅 Date:</dt>
  <dd>11 January 2018</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>Not available online</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>NEW DELHI: Days after reports surfaced claiming security breaches, the Unique Identification Authority of India (UIDAI) on Wednesday announced the implementation of a new security protocol that would remove the need to divulge Aadhaar numbers during authentication processes and limit third-party access to KYC details.</p>

<p>Admitting that the "collection and storage of Aadhaar numbers by various entities has heightened privacy concerns", the UIDAI circular said Authentication User Agencies (AUAs) providing Aadhaar services have to be ready to implement the protocol from March 1, 2018. From June 1 use of Virtual ID for authentication would be mandatory.</p>

<p>The linchpin of the new protocol will be the virtual ID (VID) — a "temporary, revocable 16-digit random number" that can be used instead of Aadhaar to verify or link services. VIDs will have a limited validity and can be generated only by the Aadhaar holder. "UIDAI will provide various options to generate, retrieve and replace VIDs… these will be made available via UIDAI's resident portal, Aadhaar Enrolment Centre, mAadhaar mobile application, etc.," it said. While only one VID per Aadhaar number will be valid at a time, users can revoke and generate new VIDs as many times as desired.</p>

<p>UIDAI will also limit KYC details accessible by AUAs by classifying them as Global AUAs, which are required to use Aadhaar e-KYC by law, and Local AUAs. Only the former will have full access to e-KYC details and can store Aadhaar numbers. Local AUAs will only have access to limited KYC details and be prohibited from storing Aadhaar numbers. UIDAI will also generate UID tokens which will be used to identify customers within agencies' systems, but these will not be usable by other AUAs.</p>

<p>However, cybersecurity experts say that even if the new "patch" is effective, verification processes will have to be redone to prevent misuse of already-leaked Aadhaar numbers. "The concept is attractive, but the devil is in the details," observed Pavan Duggal, cyberlaw expert, adding that the new system does not address those who have already gained unauthorised access to Aadhaar numbers. Sunil Abraham, executive director, Centre for Internet and Society, was more categorical. "If it has to be effective, they will have to redo (Aadhaar-KYC) from scratch."</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

By January 2018, Aadhaar had become the subject of sustained public controversy. Reports of data breaches, including a Tribune investigation that claimed access to the database could be purchased for a nominal sum, placed the UIDAI under acute pressure to respond. The Virtual ID announcement was the authority's attempt to address the most visible concern, which was the wide-scale storage and circulation of actual Aadhaar numbers across agencies and service providers.

The Virtual ID system introduced a layer of indirection, replacing the permanent 12-digit number with a temporary token for authentication. Critics, however, pointed out that this did not resolve the problem of Aadhaar data that had already been compromised or stored without authorisation. That gap between the proposed fix and the pre-existing exposure was the crux of the scepticism expressed in the article.

The Supreme Court's landmark privacy judgment from August 2017 had, in the preceding months, sharpened public and legal scrutiny of Aadhaar's data handling practices. The UIDAI's January 2018 circular can be read partly as an administrative response to that wider pressure.

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
