---
layout: default
title: "Hits And Misses With The Draft Encryption Policy"
description: "An article by Sunil Abraham in The Wire analysing India's draft encryption policy, its technical flaws, and the tension between surveillance objectives and information security principles."
categories: [Media articles, Publications]
date: 2015-09-26
authors: ["Sunil Abraham"]
source: "The Wire"
permalink: /publications/hits-and-misses-with-the-draft-encryption-policy/
---

**Hits And Misses With The Draft Encryption Policy** is an article by Sunil Abraham, published in *The Wire* on 26 September 2015. The article examines India's draft encryption policy, highlighting its contradictory mandates, impractical compliance requirements, and failure to protect user privacy or promote open standards.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>The Wire</em></dd>

  <dt>📅 Date:</dt>
  <dd>26 September 2015</dd>

  <dt>👤 Author:</dt>
  <dd>Sunil Abraham</dd>

  <dt>📄 Type:</dt>
  <dd>Opinion Article</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">
  <p>Most encryption standards are open standards. They are developed by open participation in a publicly scrutable process by industry, academia and governments in standard setting organisations (SSOs) using the principles of “rough consensus” – sometimes established by the number of participants humming in unison – and "running code" — a working implementation of the standard. The open model of standards development is based on the Free and Open Source Software (FOSS) philosophy that "many eyes make all bugs shallow".</p>
  
  <p>This model has largely been a success but as Edward Snowden in his revelations has told us, the US with its large army of mathematicians has managed to compromise some of the standards that have been developed under public and peer scrutiny. Once a standard is developed, its success or failure depends on voluntary adoption by various sections of the market – the private sector, government (since in most markets the scale of public procurement can shape the market) and end-users. This process of voluntary adoption usually results in the best standards rising to the top. Mandates on high quality encryption standards and minimum key-sizes are an excellent idea within the government context to ensure that state, military, intelligence and law enforcement agencies are protected from foreign surveillance and traitors from within. In other words, these mandates are based on a national security imperative.</p>

  <p>However, similar mandates for corporations and ordinary citizens are based on a diametrically opposite imperative – surveillance. Therefore these mandates usually require the use of standards that governments can compromise usually via a brute force method (wherein supercomputers generate and attempt every possible key) and smaller key-lengths for it is generally the case that the smaller the key-length the quicker it is for the supercomputers to break in. These mandates, unlike the ones for state, military, intelligence and law enforcement agencies, interfere with the market-based voluntary adoption of standards and therefore are examples of inappropriate regulation that will undermine the security and stability of information societies.</p>

  <p><strong>Plain-text storage requirement</strong><br>
  First, the draft policy mandates that Business to Business (B2B) users and Consumer to Consumer (C2C) users store equivalent plain text (decrypted versions) of their encrypted communications and storage data for 90 days from the date of transaction. This requirement is impossible to comply with for three reasons. Foremost, encryption for web sessions are based on dynamically generated keys and users are not even aware that their interaction with web servers (including webmail such as Gmail and Yahoo Mail) are encrypted. Next, from a usability perspective, this would require additional manual steps which no one has the time for as part of their daily usage of technologies. Finally, the plain text storage will become a honey pot for attackers. In effect this requirement is as good as saying "don't use encryption".</p>

  <p>Second, the policy mandates that B2C and "service providers located within and outside India, using encryption" shall provide readable plain-text along with the corresponding encrypted information using the same software/hardware used to produce the encrypted information when demanded in line with the provisions of the laws of the country. From the perspective of lawful interception and targeted surveillance, it is indeed important that corporations cooperate with Indian intelligence and law enforcement agencies in a manner that is compliant with international and domestic human rights law. However, there are three circumstances where this is unworkable: 1) when the service providers are FOSS communities like the TOR project which don’t retain any user data and as far as we know don’t cooperate with any government; 2) when the service provider provides consumers with solutions based on end-to-end encryption and therefore do not hold the private keys that are required for decryption; and 3) when the Indian market is too small for a foreign provider to take requests from the Indian government seriously.</p>

  <p>Where it is technically possible for the service provider to cooperate with Indian law enforcement and intelligence, greater compliance can be ensured by Indian participation in multilateral and multi-stakeholder internet governance policy development to ensure greater harmonisation of substantive and procedural law across jurisdictions. Options here for India include reform of the Mutual Legal Assistance Treaty (MLAT) process and standardisation of user data request formats via the Internet Jurisdiction Project.</p>

  <p><strong>Regulatory design</strong><br>
  Governments don’t have unlimited regulatory capability or capacity. They have to be conservative when designing regulation so that a high degree of compliance can be ensured. The draft policy mandates that citizens only use “encryption algorithms and key sizes will be prescribed by the government through notification from time to time.” This would be near impossible to enforce given the burgeoning multiplicity of encryption technologies available and the number of citizens that will get online in the coming years. Similarly the mandate that “service providers located within and outside India…must enter into an agreement with the government”, “vendors of encryption products shall register their products with the designated agency of the government” and “vendors shall submit working copies of the encryption software / hardware to the government along with professional quality documentation, test suites and execution platform environments” would be impossible for two reasons: that cloud based providers will not submit their software since they would want to protect their intellectual property from competitors, and that smaller and non-profit service providers may not comply since they can’t be threatened with bans or block orders.</p>

  <p>This approach to regulation is inspired by license raj thinking where enforcement requires enforcement capability and capacity that we don’t have. It would be more appropriate to have a “harms”-based approach wherein the government targets only those corporations that don’t comply with legitimate law enforcement and intelligence requests for user data and interception of communication.</p>

  <p>Also, while the “Technical Advisory Committee” is the appropriate mechanism to ensure that policies remain technologically neutral, it does not appear that the annexure of the draft policy, i.e. “Draft Notification on modes and methods of Encryption prescribed under Section 84A of Information Technology Act 2000”, has been properly debated by technical experts. According to my colleague Pranesh Prakash, “of the three symmetric cryptographic primitives that are listed – AES, 3DES, and RC4 – one, RC4, has been shown to be a broken cipher.”</p>

  <p>The draft policy also doesn’t take into account the security requirements of the IT, ITES, BPO and KPO industries that handle foreign intellectual property and personal information that is protected under European or American data protection law. If clients of these Indian companies feel that the Indian government would be able to access their confidential information, they will take their business to competing countries such as the Philippines.</p>

  <p><strong>And the good news is…</strong><br>
  On the other hand, the second objective of the policy, which encourages “wider usage of digital Signature by all entities including Government for trusted communication, transactions and authentication” is laudable but should have ideally been a mandate for all government officials as this will ensure non-repudiation. Government officials would not be able to deny authorship for their communications or approvals that they grant for various applications and files that they process.</p>

  <p>Second, the setting up of “testing and evaluation infrastructure for encryption products” is also long overdue. The initiation of “research and development programs … for the development of indigenous algorithms and manufacture of indigenous products” is slightly utopian because it will be a long time before indigenous standards are as good as the global state of the art but also notable as an important start.</p>

  <p>The more important step for the government is to ensure high quality Indian participation in global SSOs and contributions to global standards. This has to be done through competition and market-based mechanisms wherein at least a billion dollars from the last spectrum auction should be immediately spent on funding existing government organisations, research organisations, independent research scholars and private sector organisations. These decisions should be made by peer-based committees and based on publicly verifiable measures of scientific rigour such as number of publications in peer-reviewed academic journals and acceptance of “running code” by SSOs.</p>

  <p>Additionally the government needs to start making mathematics a viable career in India by either employing mathematicians directly or funding academic and independent research organisations who employ mathematicians. The basis of all encryption standards is mathematics and we urgently need the tribe of Indian mathematicians to increase dramatically in this country.</p>
</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This article was written after the publication of India's Draft National Encryption Policy (2015), which was later withdrawn following public criticism.

Sunil Abraham argues that while government encryption mandates may protect state security, applying them to citizens and corporations would undermine digital privacy, innovation, and information security. He calls for open standards, a harm-based regulatory model, and stronger Indian participation in global standard-setting bodies.

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
});
</script>
