---
layout: default
title: "Aadhaar: 'Safety Is Regularly Evolving'"
description: "A Kaplan Herald report by Alnoor Peermohamed on Aadhaar's new security features, quoting Sunil Abraham and others on biometric reliability and identity safety."
categories: [Media mentions]
date: 2018-02-05
authors: ["Alnoor Peermohamed"]
source: "Kaplan Herald"
permalink: /media/aadhaar-safety-is-regularly-evolving-kaplan-herald/
created: 2026-06-23
---

**"Aadhaar: 'Safety Is Regularly Evolving'"** is a *Kaplan Herald* report by Alnoor Peermohamed published on 5 February 2018. The article examines UIDAI's introduction of face authentication, virtual ID, and limited KYC as new security measures, with [Sunil Abraham](/sunil/) questioning whether face authentication would resolve the fundamental problems already associated with biometric systems.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Kaplan Herald</em></dd>

  <dt>📅 Date:</dt>
  <dd>5 February 2018</dd>

  <dt>👤 Author:</dt>
  <dd>Alnoor Peermohamed</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>Not available online</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>While the introduction of new features such as face authentication, virtual ID, and limited know-your-customer (KYC) by the Unique Identification Authority of India are being seen as reactions to mounting public pressure over the security of Aadhaar, experts, who have helped build the citizen identity system, say these have been in the pipeline for a long time.</p>

<p>Pegged to be fully functional by July 1, the new features will make Aadhaar more secure, but that hasn't stopped the UIDAI from drawing flak over the recent issue of rogue agents selling demographic data of individuals.</p>

<p>Moreover, the agency's handling of the issue has not inspired confidence among the public and security researchers.</p>

<p>Experts say for a system of Aadhaar's size, security is continually evolving.</p>

<p>Lalitesh Katragadda, former head of Google's product centre in India and who also helped build Aadhaar, says as a country we need to understand there's 'no such thing as a 100 per cent secure system'.</p>

<p>While security gaps will always exist, he says it's the UIDAI's duty to ensure there's no 'large-scale theft of people's identity'.</p>

<p>According to him, the new security features will help significantly in this regard.</p>

<p>Face authentication will be another biometric Aadhaar will begin offering to combat the reportedly high failure rates of fingerprint authentication.</p>

<p>The system will use common Webcams to capture photos of individuals and match them with the existing photo on the UIDAI's database.</p>

<p>The system will not use any high-end hardware backed facial recognition like the recently launched iPhone X, which the company claims is more accurate than its previous fingerprint authentication technology.</p>

<p>The UIDAI will work around this issue by clubbing face authentication with other forms of authentication — fingerprint, iris scan or a one-time password sent to a user's mobile phone.</p>

<p>While it isn't known how exactly the feature will be built into apps relying on Aadhaar authentication, Srikanth Nadhamuni, the former chief technology officer of Aadhaar, envisions a scenario where a photo of an individual could be captured and matched when fingerprint authentication fails, in order to improve the probability of a match.</p>

<p>But even this isn't a foolproof plan, some believe.</p>

<p>"Your face is again a biometric, and that comes with the same host of issues that is plaguing the other biometrics that have so far been used," says Sunil Abraham, executive director at the Bengaluru-based think-tank, Centre for Internet and Society.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

The article appeared in early 2018, when UIDAI was under sustained pressure following reports of security vulnerabilities in the Aadhaar ecosystem, including incidents involving rogue operators accessing or selling personal data. The three features announced — face authentication, virtual ID, and limited KYC — were presented as a response, though critics noted they were reactive rather than structural fixes.

The broader debate at the time centred on whether iterative security upgrades could adequately address concerns about a centralised biometric database. Sunil Abraham's point in the article reflects a recurring argument in that discussion: adding a new biometric layer does not eliminate the underlying risks common to all biometric systems, including degradation over time, false rejection rates, and the irreversibility of compromise.

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
