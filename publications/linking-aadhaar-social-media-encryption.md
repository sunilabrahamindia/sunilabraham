---
layout: default
title: "Linking Aadhaar with social media or ending encryption is counterproductive"
description: "An opinion article by Sunil Abraham in Prime Time examining the debate on linking Aadhaar with social media accounts and the implications of weakening encryption for national security and privacy."
categories: [Media articles, Publications]
date: 2019-08-26
authors: ["Sunil Abraham"]
source: "Prime Time"
permalink: /publications/linking-aadhaar-social-media-encryption/
---

**Linking Aadhaar with social media or ending encryption is counterproductive** is an opinion column by Sunil Abraham, published in *Prime Time* on 26 August 2019. The article analyses the policy debate surrounding the linking of Aadhaar numbers with social media accounts and the potential consequences of curbing encryption. Abraham argues that such moves would undermine privacy, national security, and technological sovereignty.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)  

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Prime Time</em></dd>

  <dt>📅 Date:</dt>
  <dd>26 August 2019</dd>

  <dt>👤 Author:</dt>
  <dd>Sunil Abraham</dd>

  <dt>📄 Type:</dt>
  <dd>Opinion Article</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>
    Not available
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">
  <p>Should Aadhaar be used as KYC for social media accounts? We have recently seen a debate on this question with even the courts hearing arguments in favour and against such a move.</p>

  <p>The case began in the Madras High Court and later Facebook moved the Supreme Court seeking transfer of the petition to the apex court. The original petition was filed in July 2018 and sought linking of Aadhaar numbers with user accounts to further traceability of messages.</p>

  <p>Before we try and answer this question, we need to first understand the differences between the different types of data on social media and messaging platforms. If a crime happens on an end-to-end cryptographically secure channel like WhatsApp, the police may request the following from the provider to help solve the case:</p>

  <ol>
    <li>Identity data: Phone numbers of the accused, names and addresses of the accused.</li>
    <li>Metadata: Sender, receiver(s), time, size of message, flag identifying a forwarded message, delivery status, read status, etc.</li>
    <li>Payload data: Actual content of the text and multimedia messages.</li>
  </ol>

  <p>Different countries have taken different approaches to solving different layers of the surveillance problem. Let us start with identity data. Some, like India, require KYC for sale of SIM cards while others, like the UK, allow anonymous purchases. Corporations also have policies when it comes to anonymous speech on their platforms — Facebook, for instance, enforces a soft real-ID policy while Twitter does not crack down on anonymous speech. The trouble with KYC the old-fashioned way is that it exposes citizens to further risk. Every possessor of your identity documents is a potential attack surface. Indian regulation should not result in Indian identity documents being available in the millions to foreign corporations.</p>

  <p>Technical innovations are possible, like tokenisation, Aadhaar paperless local e-KYC or Aadhaar offline QR code along with one-time passwords. These privacy-protective alternatives must be mandatory for all, and the Aadhaar numbers must be deleted from previously seeded databases.</p>

  <p>Countries that do not require KYC have an alternative approach to security and law enforcement. They know that if someone like me commits a crime, it would be easy to catch me because I have been using the same telecom provider for the last fifteen years. This is true of long-term customers regardless of whether they are pre-paid or post-paid. The security risk lies in the new numbers without this history that confirms identity. These countries use targeted big-data analytics to determine risk and direct surveillance operations to target new SIM cards. My current understanding is that when it comes to basic user data, all the internet giants in India comply with what they consider legitimate law enforcement requests. Some proprietary and free and open source (FOSS) alternatives to services offered by the giants do not provide such direct cooperation in India.</p>

  <p>When it comes to payload data, it is almost impossible (meaning you will need supercomputers) to access the data unless the service or software provider breaks end-to-end cryptography. It is unwise, like some policy-makers are proposing, to prohibit end-to-end cryptography or mandate back doors because our national sovereignty and our capacity for technological self-determination depend on strong cryptography. A targeted ban or prohibition against proprietary providers might have a counterproductive consequence with users migrating to FOSS alternatives like Signal, which will not even give the police identity data. As a supporter of the free software movement, I would see this as a positive development, but as a citizen I am aware that the fight against crime and terror will become harder. So the government must pursue other strategies for getting payload data, such as a comprehensive government hacking programme.</p>

  <p>Meta-data is critical when it comes to separating the guilty from the innocent and apportioning blame during an investigation. For example, who was the originator of a message? Who got it and read it last? WhatsApp claims that it has implemented the Signal protocol faithfully, meaning that they hold no meta-data when it comes to the messages and calls. Currently there is no regulation which mandates data retention for over-the-top providers, but such requirements do exist for telecom providers. Just like access to meta-data provides some visibility into illegal activities, it also provides visibility into legal activities. Therefore, those using end-to-end cryptography on platforms with comprehensive meta-data retention policies will have their privacy compromised even though the payload data remains secure.</p>

  <p>Here is a parallel example to understand why this is important. Early last year, the Internet Engineering Task Force chose a version of TLS 1.3 that revealed less meta-data over one that provided greater visibility into the communications. This hardening of global open standards, through the elimination of availability of meta-data for middle-boxes, makes it harder for foreign governments to intercept Indian military and diplomatic communications via imported telecom infrastructure.</p>

  <p>Courts and policy makers across the world have to grapple with the following question: Are meta-data retention mandates for the entire population of users a "necessary and proportionate" legal measure to combat crime and terror? For me, it should not be illegal for a provider who voluntarily wishes to retain data, provided it is within legally sanctioned limits, but it should not be a requirement under law.</p>

  <p>There are technical solutions that are yet to be properly discussed and developed as an alternative to blanket meta-data retention measures. For example, Dr V Kamakoti has made a traceability proposal at the Madras High Court. This proposal has been critiqued by Anand Venkatanarayanan as being violative in spirit of the principles of end-to-end cryptography. Other technical solutions are required for those seeking justice and for those who wish to serve as informers for terror plots. I have proposed client-side metadata retention. If a person who has been subjected to financial fraud wishes to provide all the evidence from their client, it should be possible for them to create a digitally signed archive of messages for the police. This could be signed by the sender, the provider and also the receiver so that technical non-repudiation raises the evidentiary quality of the digital evidence. However, there may be other legal requirements such as the provision of notice to the sender so that they know that client-side data retention has been turned on.</p>

  <p>The need of the hour is sustained research and development of privacy-protecting surveillance mechanisms. These solutions need to be debated thoroughly amongst mathematicians, cryptographers, scientists, technologists, lawyers, social scientists and designers so that solutions with the least negative impact can be rolled out either voluntarily by providers or as a result of regulation.</p>
</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This article was published at a time when the Indian government and courts were debating whether to link Aadhaar to social media accounts and whether to allow law enforcement access to encrypted messages.  
Sunil Abraham argues that weakening encryption or linking Aadhaar would erode privacy and national sovereignty, and that instead, India should invest in privacy-preserving surveillance mechanisms and open, participatory policy design.

{% include back-to-top.html %}

<style>
/* Accessibility-focused article styling */
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
