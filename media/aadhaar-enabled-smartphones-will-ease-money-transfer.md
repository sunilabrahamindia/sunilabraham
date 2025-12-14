---
layout: default
title: "Aadhaar-Enabled Smartphones Will Ease Money Transfer"
description: "An Economic Times report on government plans to integrate Aadhaar biometric authentication into smartphone operating systems for payment verification, featuring technical security concerns raised by Sunil Abraham regarding operating system interception vulnerabilities in the proposed data flow architecture."
categories: [Media mentions]
date: 2016-08-10
source: "The Economic Times"
authors: ["Neha Alawadhi", "Gulveen Aulakh"]
permalink: /media/aadhaar-enabled-smartphones-will-ease-money-transfer/
created: 2025-12-14
---

**Aadhaar-Enabled Smartphones Will Ease Money Transfer** is a report published in *The Economic Times* on 10 August 2016, written by Neha Alawadhi and Gulveen Aulakh. The article examines UIDAI's initiative to enable biometric authentication directly through smartphone hardware, primarily targeting integration with the newly launched Unified Payment Interface for secure money transfers. It features critical technical analysis from Sunil Abraham identifying a fundamental architectural vulnerability where biometric data must transit through the device operating system before reaching secure enclaves, creating interception opportunities.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)  
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>The Economic Times</em></dd>

  <dt>✍️ Authors:</dt>
  <dd>Neha Alawadhi, Gulveen Aulakh</dd>

  <dt>📅 Date:</dt>
  <dd>10 August 2016</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>
    <a class="btn" href="https://economictimes.indiatimes.com/industry/banking/finance/banking/aadhaar-enabled-smartphones-will-ease-money-transfer/articleshow/53625690.cms">Read Online</a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p><strong>Synopsis</strong><br>
"The two-factor authentication in UPI is now being done with mobile phone as one factor, and MPIN as the second factor," said Nandan Nilekani.</p>

<p>NEW DELHI: With its plans to make smartphones Aadhaar-enabled, the government hopes to provide users a means to do self-authentication and let businesses and banks verify the identity of their clients through their smartphones, a move that could potentially lead the way to a cashless society.</p>

<p>"Iris and fingerprint sensors are now becoming a standard feature in smartphones anyway, and this requirement will only take a minor tweak to the operating system. Once enabled, people will be able to use phones to do self-authentication and KYC (know your customer)," Nandan Nilekani, former chairman of the Unique Identification Authority of India, told ET, welcoming the government's plan to make smartphones Aadhaar-enabled.</p>

<p>ET was the first to report that on July 27 a meeting between UIDAI, which administers Aadhaar, and senior executives of smartphone-makers discussed ways to allow smartphone handsets let citizens authenticate their fingerprints and iris on the phone to get services. The most immediate use for the Aadhaar-enabled smartphones is the Unified Payment Interface (UPI), the new payment system that allows money transfer between any two parties using mobile phones and a virtual payment address.</p>

<p>"The two-factor authentication in UPI is now being done with mobile phone as one factor, and MPIN as the second factor. But once you have Aadhaar authentication on the phone, then the second factor can be biometric authentication through Aadhaar," said Nilekani. Over time, the idea is to open Aadhaar authentication to third party apps, said another person familiar with the ongoing discussions, who did not wish to be named.</p>

<p>In effect, biometric and iris scan authentication could become one of the permissions a user grants to different third party apps, such as access to camera, contacts, phone book and so on. Handset makers have raised concerns about some security issues on using iris scan for Aadhaar authentication. Also, companies such as Apple that have very closed ecosystems, would not be easy to get on board, several people told ET.</p>

<p>"The primary challenge lies in safe storing of the iris scan between the time it is captured by the camera and then sent to UIDAI server seeking authentication," said an industry insider, who is aware of the discussions, requesting anonymity. The proposal for smartphone makers includes a "hardware secure zone" where biometric data will be encrypted and sent out. It will not leave the electronic secure zone without encryption, and every phone doing Aadhaar authentication will be registered in the UID system.</p>

<p>"Unfortunately, from the biometric sensor the data goes to the hardware secure zone via the operating system. Therefore, the biometric data can be intercepted by the operating system before it is sent to the hardware secure zone," said Sunil Abraham, executive director at Bengaluru-based research organisation, the Centre for Internet and Society.</p>

<p>"The reluctance to make changes at the vendor level are mainly coming from a desire for control of biometric data for strategic and commercial purposes. Privacy and security are bogus reasons," Nilekani said, adding that both ends - the handset and the Aadhaar database — will use the highest level of encryption.</p>

<p>Samsung India, which in May launched the Galaxy Tab Iris, a device that uses Aadhaar authentication, said it has taken care that its user's biometric data does not fall into the wrong hands. "We ensure that biometric data is encrypted as per UIDAI specifications in device itself for Galaxy Tab Iris," Sukesh Jain, vice president, Samsung India Electronics, told ET in an email response.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This August 2016 report documented UIDAI's push to integrate Aadhaar authentication into consumer smartphones, coinciding with the government's April 2016 launch of the Unified Payment Interface. The timing followed demonetisation preparations and reflected broader efforts to expand digital payment infrastructure beyond dedicated point-of-sale terminals and business correspondent micro-ATMs.

Sunil Abraham identified a critical architectural flaw in the proposed implementation: biometric data captured by fingerprint or iris sensors must traverse the device operating system before reaching hardware secure enclaves for encryption. This created an unavoidable interception point where compromised or malicious operating system components could capture biometric credentials in plaintext. Unlike external network attacks that encryption could prevent, this vulnerability existed within the device's trusted computing base itself.

The proposal to treat biometric authentication as an app permission—comparable to camera or contact access—raised additional concerns about third-party application access to authentication capabilities. Whilst existing permissions governed access to device features, biometric authentication involved transmitting sensitive personal identifiers to external verification systems, representing a qualitatively different security requirement than local device functions.

Handset manufacturers' resistance stemmed partly from legitimate engineering challenges regarding secure data pathways, but also from commercial and strategic interests in controlling biometric data flows. Apple's closed ecosystem presented particular obstacles, as iOS architecture prioritised manufacturer control over hardware-software integration, making government-mandated authentication protocols difficult to implement without compromising Apple's security model.

The initiative ultimately faced limited adoption. Technical complexities in securing biometric data flows, manufacturer reluctance to modify operating system architectures, and competitive dynamics between device makers prevented the standardised Aadhaar-enabled smartphone ecosystem UIDAI envisioned. UPI instead achieved mass adoption through simpler PIN-based authentication, demonstrating that usability and ecosystem simplicity often mattered more than biometric sophistication for payment system success.

## External Link

- <a href="https://economictimes.indiatimes.com/industry/banking/finance/banking/aadhaar-enabled-smartphones-will-ease-money-transfer/articleshow/53625690.cms">Read on The Economic Times</a>

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
.media-details dt { font-weight: 600; color: #1b2a49; margin-top: 0.7rem; }
.media-details dd { margin: 0 0 0.3rem 0.3rem; color: #555; }
.highlighted-text {
  background-color: #fffbea;
  border-left: 4px solid #f2ce61;
  padding: 1rem 1.2rem;
  border-radius: 8px;
  line-height: 1.65;
  color: #333;
  margin-bottom: 0.8rem;
}
.highlighted-text p { margin-bottom: 1rem; }
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
.copy-btn-full:hover { background: #e5e5e5; }
.copy-btn-full:focus { outline: 3px solid #ffbf47; outline-offset: 2px; }
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
    btn.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter' || ev.key === ' ') {
        ev.preventDefault();
        btn.click();
      }
    });
  });
});
</script>
