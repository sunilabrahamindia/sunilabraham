---
layout: default
title: "An Open Letter to the Finance Committee: SCOSTA Standards"
description: "A CIS blog post presenting an open letter to the Parliamentary Standing Committee on Finance, comparing the SCOSTA smart card standard with the Aadhaar biometric standard for identity authentication."
authors: ["Elonnai Hickok"]
categories: [Elonnai Hickok]
date: 2011-01-06
source: "Centre for Internet and Society"
permalink: /elonnai/an-open-letter-to-the-finance-committee-scosta-standards/
created: 2026-08-05
---

**"An Open Letter to the Finance Committee: SCOSTA Standards"** is a blog post by [Elonnai Hickok](/elonnai/) published by the [Centre for Internet and Society](/cis/) on 6 January 2011. It details a civil society submission to the Parliamentary Standing Committee on Finance evaluating identity authentication mechanisms within the Unique Identification (UID) scheme. The piece presents a comparative technical analysis between the Smart Card Operating System for Transport Applications (SCOSTA) standard and the Aadhaar biometric standard, advocating for the adoption of decentralized smart card authentication to enhance security, protect domestic industry, and reduce single points of failure.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published by:</dt>
  <dd><em>Centre for Internet and Society</em></dd>

  <dt>📅 Date:</dt>
  <dd>6 January 2011</dd>

  <dt>✍️ Author:</dt>
  <dd>Elonnai Hickok</dd>

  <dt>📄 Type:</dt>
  <dd>Blog post</dd>

  <dt>🔗 Original Link:</dt>
  <dd>
    <a href="https://cis-india.org/internet-governance/blog/privacy/letter-to-finance-committee">Read the original post</a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>The UID Bill has been placed to the Finance Committee for review and approval. Through a series of open letters to the Finance Committee, civil society is asking the committee to take into consideration and change certain aspects of the Bill and the project. The below note compares the SCOSTA standard with the Aadhaar biometric standard, and explains why we believe the SCOSTA standard should replace the Aadhaar biometric standard for the authentication process in the UID scheme.</p>

<hr class="article-separator">

<h3>Introduction</h3>

<p>This note is intended to demonstrate how the Aadhaar biometric standard is weaker than the SCOSTA standard. Through a comparison of the SCOSTA standard-based smart card and the Aadhaar biometric-based identification number, it will show how the SCOSTA standard is a more secure, structurally sound, and cost-effective approach to authentication of identity for India. Though we recognize that Aadhaar biometrics are useful for the de-duplication and identification of individuals, we believe that the SCOSTA standard is more appropriate for the authentication of individuals. Thus, we ask that the Aadhaar biometric-based authentication process be replaced with a SCOSTA standard-based authentication process.</p>

<h3>A background of the two standards</h3>

<p>The SCOSTA standard is used in smart cards and was developed by the National Informatics Centre in India. It is:</p>

<ol>
<li>Compliant with the international standard ISO-7816 for smart cards.</li>
<li>Based on a public/private key and pin authentication factor</li>
<li>Authentication factor refers to an individual's keys, pass-phrases, and pin.</li>
</ol>

<p>The biometric standard authenticates the identity of an individual based on his or her physical fingerprints and iris scans (in the case of the UID). The standard:</p>

<ol>
<li>Verifies if the individual exists within a known population by comparing the biometric data to those of other individuals stored in a secured centralized database.</li>
<li>Based on a symmetric authentication factor</li>
</ol>

<h3>A comparison of the two standards</h3>

<div class="table-container">
<table>
  <thead>
    <tr>
      <th>Standard</th>
      <th>SCOSTA MNIC smart card</th>
      <th>Aadhaar Biometric - UID number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Architecture</strong></td>
      <td><strong>Decentralized</strong><br>SCOSTA standards require a pair and key combination with a pin, and thus can be structured in a decentralized manner</td>
      <td><strong>Centralized</strong><br>Aadhaar biometric standards require symmetric authentication factors, and thus must be structured in a centralized manner</td>
    </tr>
    <tr>
      <td><strong>Standards for Technology</strong></td>
      <td><strong>Open standard</strong><br>Creates security through transparency</td>
      <td><strong>Closed standard</strong><br>Creates security through obscurity</td>
    </tr>
    <tr>
      <td><strong>Points of failure</strong></td>
      <td><strong>Multiple points of failure</strong><br>The SCOSTA standard has multiple points of failure, because of decentralized structure, thus if one database is compromised all data is not lost.</td>
      <td><strong>Single point of failure</strong><br>The Aadhaar Biometric standard has one single point of failure, because of centralized structure, thus if the database is compromised all data is lost</td>
    </tr>
    <tr>
      <td><strong>Impact on local industry</strong></td>
      <td><strong>Encourages</strong><br>Open standards allow local industry to compete in manufacturing technology</td>
      <td><strong>Discourages</strong><br>Closed standards allow foreign players to monopolize the manufacturing of technology</td>
    </tr>
    <tr>
      <td><strong>Cost analysis</strong></td>
      <td><strong>Cost-effective</strong><br>Increased competition keeps prices low</td>
      <td><strong>Cost-ineffective</strong><br>Decreased competition keeps prices high</td>
    </tr>
    <tr>
      <td><strong>Revocation</strong></td>
      <td><strong>Revocable</strong><br>If the key pair and pin are stolen, a new set of passwords can be issued</td>
      <td><strong>Permanent</strong><br>If the biometrics of an individual are stolen, they cannot be re-issued</td>
    </tr>
    <tr>
      <td><strong>Possibility of fraudulent authentication</strong></td>
      <td><strong>Lower</strong><br>A thief must steal your smart card and your secret pin to commit fraud</td>
      <td><strong>Higher</strong><br>A thief only needs to collect your fingerprints using a glass tumbler to commit fraud</td>
    </tr>
    <tr>
      <td><strong>Viability of Technology</strong></td>
      <td>Proven effective for large populations</td>
      <td>Not proven effective for large populations</td>
    </tr>
  </tbody>
</table>
</div>

</div>

{% include back-to-top.html %}

## Context and Background

In early 2011, parliamentary scrutiny of the National Identification Authority of India Bill, 2010 provided a formal mechanism for technical and policy interventions by civil society groups. As the Parliamentary Standing Committee on Finance evaluated the proposed legislation, open letters were submitted to highlight architectural vulnerabilities in the Unique Identification Authority of India (UIDAI) design. A key aspect of this advocacy was differentiating between de-duplication—where biometrics ensure an individual is registered only once in a database—and routine authentication, which verifies an individual's identity during day-to-day transactions.

The technical comparison centered on the Smart Card Operating System for Transport Applications (SCOSTA), an open standard developed domestically by the National Informatics Centre (NIC). SCOSTA utilizes public-key cryptography and personal identification numbers (PINs) embedded within microchip smart cards, allowing verification to occur offline or via decentralized networks. In contrast, the Aadhaar model relies on real-time, symmetric biometric matching against a central repository. Civil society experts argued that centralizing authentication requests creates systemic risks, including single points of failure, network dependency, and potential exposure of sensitive personal data during transmission.

Security, economic, and operational considerations further supported the case for smart-card-based authentication. From a security standpoint, compromised cryptographic keys or PINs can be revoked and reissued, whereas compromised biometrics—such as latent fingerprints—are permanent physical traits that cannot be altered once replicated. Economically, open technical standards like SCOSTA foster competitive local manufacturing and vendor neutrality, avoiding dependence on proprietary foreign biometric technologies and specialized hardware.

Ultimately, the open letter advocated for a hybrid identity architecture that limits biometric processing strictly to initial database de-duplication. By substituting centralized biometric queries with decentralized, user-controlled smart card authentication for routine transactions, the proposal aimed to strengthen systemic security, protect individual privacy, and establish a resilient framework for public service delivery across India.

## External Link

- [An Open Letter to the Finance Committee: SCOSTA Standards](https://cis-india.org/internet-governance/blog/privacy/letter-to-finance-committee)

{% include navbox-elonnai.html %}

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
.highlighted-text ul,
.highlighted-text ol {
  margin: 0 0 1rem 1.5rem;
}
.article-separator {
  border: none;
  border-top: 1px solid rgba(0,0,0,0.08);
  margin: 0.75rem 0 1rem 0;
}

.table-container {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0;
}

.highlighted-text table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
  background-color: #fff;
  font-size: 0.92rem;
}

.highlighted-text th,
.highlighted-text td {
  border: 1px solid #d8e2f0;
  padding: 0.6rem 0.8rem;
  text-align: left;
  vertical-align: top;
}

.highlighted-text th {
  background-color: #f0f4f8;
  color: #1b2a49;
  font-weight: 600;
}
  
body.tsap-dark-mode .highlighted-text th {
  background: #1b2636;
  color: #f3f4f6;
}

body.tsap-dark-mode .highlighted-text td,
body.tsap-dark-mode .highlighted-text th {
  border-color: #374151;
  color: #e5e7eb;
}
  body.tsap-dark-mode .highlighted-text table {
  background: #243244;
  border-color: #374151;
}
</style>
