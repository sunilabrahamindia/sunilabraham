---
layout: default
title: "And Now, Aadhaar-Enabled Smartphones for Easy Verification and Money Transfer"
description: "A Business Insider report on the government's plan for Aadhaar-enabled smartphones, quoting Sunil Abraham on the biometric data interception risk in the proposed hardware architecture."
categories: [Media mentions]
date: 2016-08-10
source: "Business Insider"
permalink: /media/and-now-aadhaar-enabled-smartphones-for-easy-verification-and-money-transfer-business-insider/
created: 2026-06-13
---

**"And Now, Aadhaar-Enabled Smartphones for Easy Verification and Money Transfer"** is a *Business Insider* report published on 10 August 2016. The article examines the Indian government's plan to build Aadhaar authentication directly into smartphones, with [Sunil Abraham](/sunil/) of the [Centre for Internet and Society](/cis/) pointing out a specific interception vulnerability in the proposed hardware security architecture.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Business Insider</em></dd>

  <dt>📅 Date:</dt>
  <dd>10 August 2016</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>Not available online</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>As reported earlier, the Indian government has planned to make Aadhaar-enabled smartphones, with which users would be able to self-authenticate and let businesses and banks verify the identity of their clients. This would also help in the government's aim of a cashless society.</p>

<p>While applauding this plan Nandan Nikelani, former chairman of UIDAI told ET that, "Iris and fingerprint sensors are now becoming a standard feature in smartphones anyway, and this requirement will only take a minor tweak to the operating system. Once enabled, people will be able to use phones to do self-authentication and KYC (know your customer)."</p>

<p>In July, senior executives of UIDAI and smartphone companies met to discuss ways to allow smartphones let citizens authenticate their fingerprints and iris on the phone, so that they could avail government services from the comfort of their homes.</p>

<p>The most immediate use for these smartphones would be the Unified Payment Interface (UPI), a new payment system which would allow money transfer between any two parties by simply using their mobile phones and a virtual payment address.</p>

<p>"The two-factor authentication in UPI is now being done with mobile phone as one factor, and MPIN as the second factor. But once you have Aadhaar authentication on the phone, then the second factor can be biometric authentication through Aadhaar," said Nilekani.</p>

<p>With time, Aadhaar authentication will also be made open to third party apps, said another person familiar with the ongoing discussions on the condition of anonymity.</p>

<p>This would let users allow apps to access their biometric and iris scans, just like they grant access to other features like camera, contacts, SMS etc. However, from their end, handset makers have raised security concerns about using iris scan for Aadhar authentication.</p>

<p>"The primary challenge lies in safe storing of the iris scan between the time it is captured by the camera and then sent to UIDAI server seeking authentication," said an industry insider.</p>

<p>For this, the proposal includes a "hardware secure zone" which would encrypt biometric data before sending it out. However, even this isn't a foolproof idea.</p>

<p>"Unfortunately, from the biometric sensor the data goes to the hardware secure zone via the operating system. Therefore, the biometric data can be intercepted by the operating system before it is sent to the hardware secure zone," said Sunil Abraham, executive director at Bengaluru-based research organisation, the Centre for Internet and Society.</p>

<p>To this, Nilekani said, "the reluctance to make changes at the vendor level is mainly coming from a desire for control of biometric data for strategic and commercial purposes. Privacy and security are bogus reasons." He added that both ends, the handset and the Aadhaar database, will be using the highest level of encryption.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

By mid-2016 the Indian government was pushing to extend Aadhaar from a welfare delivery tool into the payments and commerce infrastructure through the Unified Payment Interface. Embedding Aadhaar biometric authentication directly into smartphone hardware was part of that expansion, framed as enabling citizens to self-authenticate from home and reducing reliance on intermediaries.

The article sits at the intersection of two debates that were running in parallel at the time: the security of centralised biometric data storage, and the technical safeguards available at the device level. The proposal for a hardware secure zone was a response to concerns from handset makers, but the architecture still routed biometric data through the operating system before encryption, which introduced an interception window.

Sunil Abraham's comment identifies that specific technical gap precisely. His point is not a general objection to biometric authentication but a narrow and concrete observation about a flaw in the proposed data pathway between sensor and secure zone, which Nilekani's response does not directly address.

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
