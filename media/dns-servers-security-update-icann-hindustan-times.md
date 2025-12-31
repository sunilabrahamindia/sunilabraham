---
layout: default
title: "Internet Services Not to Be Affected as DNS Servers Undergo Update"
description: "A Hindustan Times report on ICANN's cryptographic key rollover for DNS security, with Indian ISPs confirming preparedness to avoid service disruptions, though experts expressed uncertainty about compliance rates."
categories: [Media mentions]
date: 2018-10-12
source: "Hindustan Times"
permalink: /media/dns-servers-security-update-icann-hindustan-times/
created: 2025-12-31
---

**Internet Services Not to Be Affected as DNS Servers Undergo Update** is a *Hindustan Times* report published on 12 October 2018. The article examines ICANN's coordination of a DNS Root Key Signing Key rollover—the first such change since DNSSEC implementation—with National Cyber Security Coordinator Gulshan Rai confirming Indian ISPs had updated systems, whilst Centre for Internet and Society's Sunil Abraham questioned whether compliance rates would prove adequate.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)  
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Hindustan Times</em></dd>

  <dt>📅 Date:</dt>
  <dd>12 October 2018</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>
    <a class="btn" href="https://www.hindustantimes.com/india-news/internet-services-not-to-be-affected-as-dns-servers-undergo-update/story-uLxsOyPoQoUtrPiJMHfVXN.html">
      Read Online
    </a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>Internet services across the country are unlikely to be impacted over the next 48 hours even as the Domain Name System (DNS) servers undergo a security update coordinated by global regulator, Internet Corporation of Assigned Names and Numbers (ICANN).</p>

<p>"ICANN, the global certifying authority for DNS security, had taken a decision a year back to change the Trust Key. All ISPs were notified to update their configuration to the new key. Accordingly, the Internet Service Providers (ISP) have confirmed that they have already updated their DNS servers with the new key and the country does not carry any risk of impact on Internet services," said National Cyber Security Coordinator Gulshan Rai in a statement on Friday. DNS servers are like the phone book for the Internet which translates human-friendly computer labels into their respective IP addresses. If the DNS servers become inactive, it will be impossible for users to access different websites in the absence of this translation.</p>

<p>The ICANN's ongoing maintenance work over the next two days is to change the cryptographic key that helps protect DNS. This has been necessitated to counter the rising incidents of cyber attacks, ICANN said.</p>

<p>Rai had held a meeting with all ISPs in this regard on September 5. During which ISPs said that they had taken all necessary steps to update their systems in order to avoid any inconvenience to their users. Rai reviewed the situation again on Friday.</p>

<p>Sunil Abraham, founder, Centre for Internet and Society, said, "This security update is the responsibility of the management and network administrators at ISPs and telcos. Only time will tell what percentage of people have done their job. It's very likely that this number is very small, in case of people who haven't updated their servers," he explained.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This report appeared on the eve of ICANN's first Root Zone Key Signing Key (KSK) rollover since DNS Security Extensions (DNSSEC) were deployed globally. The KSK functions as the cryptographic foundation for DNS security, authenticating the chain of trust that prevents cache poisoning and other attacks. ICANN had announced the rollover a year earlier, giving network operators time to update resolver software to recognize the new key when it became active on 11 October 2018.

The stakes were significant: ISPs whose DNS resolvers failed to update would be unable to validate DNSSEC-signed domains, potentially breaking internet access for millions of users. National Cyber Security Coordinator Gulshan Rai's assurance that Indian ISPs had confirmed readiness followed a 5 September meeting where providers reported completing updates. However, Sunil Abraham's sceptical assessment—suggesting compliance rates might be "very small"—highlighted the gap between official assurances and operational reality.

The tension between Rai's confidence and Abraham's caution reflected a recurring pattern in internet infrastructure updates: whilst major ISPs typically maintain professional operations teams capable of implementing technical changes, smaller providers often lack resources or expertise. Abraham's observation that "only time will tell" acknowledged that the true test would come when the new key activated, potentially revealing which operators had failed to prepare despite a year's notice.

The article thus documented a moment of managed uncertainty, where government coordination and industry self-reporting suggested preparedness, but expert commentary indicated that actual implementation quality remained unknown until the rollover occurred.

## External Link

- <a href="https://www.hindustantimes.com/india-news/internet-services-not-to-be-affected-as-dns-servers-undergo-update/story-uLxsOyPoQoUtrPiJMHfVXN.html">Read on Hindustan Times</a>

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
