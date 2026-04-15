---
layout: default
title: "What's Up with WhatsApp?"
description: "An Asia Times analysis by Aayush Rathi and Sunil Abraham questioning WhatsApp's end-to-end encryption claims, data storage practices, and privacy policy inconsistencies."
categories: [Media articles, Publications]
date: 2018-04-20
authors: ["Aayush Rathi", "Sunil Abraham"]
source: "Asia Times"
permalink: /publications/whats-up-with-whatsapp-asia-times/
created: 2026-04-15
---

**What's Up with WhatsApp?** is an *Asia Times* article published on 20 April 2018, co-authored by Aayush Rathi and [Sunil Abraham](/sunil/). The piece scrutinises WhatsApp's end-to-end encryption implementation, examines discrepancies between the platform's stated data deletion policy and observable behaviour, and raises questions about the company's broader privacy commitments following its acquisition by Facebook.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Asia Times</em></dd>

  <dt>📅 Date:</dt>
  <dd>20 April 2018</dd>

  <dt>👤 Authors:</dt>
  <dd>Aayush Rathi and Sunil Abraham</dd>

  <dt>📄 Type:</dt>
  <dd>Analysis / Opinion</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>
    <a class="btn" href="https://asiatimes.com/2018/04/whats-up-with-whatsapp/">
      Read Online
    </a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>Back in April 2016, when WhatsApp Inc announced it was rolling out end-to-end encryption (E2EE) for its billion-plus strong user base as a default setting, the messaging behemoth signaled to its users it was at the forefront of providing technological solutions to protect privacy.</p>

<p>Emphasized in the security white paper explaining the implementation of the technology is the encryption of both forms of communication – one-to-one and group and also of all types of messages shared within such communications – text as well as media.</p>

<p>Simply put, all communication taking place over WhatsApp would be decipherable only to the sender and recipient – it would be virtual gibberish even to WhatsApp.</p>

<p>This announcement came in the backdrop of Apple locking horns with the FBI after being asked to provide a backdoor to unlock the San Bernardino mass shooter's iPhone. This further reinforced WhatsApp Inc's stand on the ensuing debate between the interplay of privacy and security in the digital age.</p>

<p>Kudos to WhatsApp, for there is growing discussion around how encryption and anonymity is central to enabling secure online communication which in turn is integral to essential human rights such as those of freedom of opinion and expression.</p>

<p>WhatsApp may have taken encryption to the masses, but here we outline why WhatsApp's provisioning of privacy and security measures needs a more granular analysis – is the company doing what it claims to be doing? Security issues with WhatsApp's messaging protocol certainly are not new.</p>

<p><strong>Man-in-the-middle attacks</strong></p>

<p>A study published by a group of German researchers from Ruhr University highlighted issues with WhatsApp's implementation of its E2EE protocol to group communications. Another paper points out how WhatsApp's session establishment strategy itself could be problematic and potentially be targeted for what are called man-in-the-middle (MITM) attacks.</p>

<p>An MITM attack takes the form of a malicious actor, as the term suggests, placing itself between the communicating parties to eavesdrop or impersonate. The Electronic Frontier Foundation also highlighted other security vulnerabilities, or trade-offs, depending upon ideological inclinations, with respect to WhatsApp allowing for storage of unencrypted backups, issues with WhatsApp's web client and also with its approach to cryptographic key change notifications.</p>

<p>Much has been written questioning WhatsApp's shifting approach to ensuring privacy too. Quoting straight from WhatsApp's Privacy Policy: "We joined the Facebook family of companies in 2014. As part of the Facebook family of companies, WhatsApp receives information from, and shares information with, this family of companies." Speaking of Facebook …</p>

<p>Culling out larger issues with WhatsApp's privacy policies is not the intention here. What we specifically seek to explore is right at the nexus of WhatsApp's security and privacy provisioning clashing with its marketing strategy: the storage of data on WhatsApp's servers, or 'blobs,' as they are referred to in the technical paper. Facebook's rather. In WhatsApp's words: "Once your messages (including your chats, photos, videos, voice messages, files and share location information) are delivered, they are deleted from our servers. Your messages are stored on your own device."</p>

<p>In fact, this non-storage of data on their 'blobs' is emphasized at several other points on the official website. Let us call this the deletion-upon-delivery model.</p>

<p><strong>A simple experiment</strong></p>

<p>While drawing up a rigorous proof of concept, made near-impossible thanks to WhatsApp being a closed source messaging protocol, a simple experiment is enough to raise some very pertinent questions about WhatsApp's outlined deletion-upon-delivery model. It should, however, be mentioned that the Signal Protocol developed by Open Whisper Systems and pivotal in WhatsApp's rolling out of E2EE is open source. Here is how the experiment proceeds:</p>

<p>Rick sends Morty an attachment.<br>
Morty then switches off the data on her mobile device.<br>
Rick downloads the attachment, an image.<br>
Subsequently, Rick deletes the image from his mobile device's internal storage.<br>
Rick then logs into a WhatsApp's web client on his browser. (Prior to this experiment, both Rick and Morty had logged out from all instances of the web client)<br>
Upon a fresh log-in to the web client and opening the chat with Morty, the option to download the image is available to Rick.</p>

<p>The experiment concludes with bewilderment at WhatsApp's claim of deletion-upon-delivery as outlined earlier. The only place from which Morty could have downloaded the image would be from Facebook's 'blobs.' The attachment could not have been retrieved from Morty's mobile device as it had no way of sending data and neither from Rick's mobile device as it no longer existed in the device's storage.</p>

<p>As per the Privacy Policy, the data is stored on the 'blobs' for a period of 30 days after transmission of a message only when it can't be delivered to the recipient. Upon delivery, the deletion-upon-delivery model is supposed to kick in.</p>

<p>Another straightforward experiment that leads to a similar conclusion is seeing the difference in time taken for a large attachment to be forwarded as opposed to when the same large attachment is uploaded. Forwarding is palpably quicker than uploading afresh: non-storage of attachments on the 'blob' would entail that the same amount should be taken for both.</p>

<p>The plot thickens. WhatsApp's Privacy Policy goes on to state: "To improve performance and deliver media messages more efficiently, such as when many people are sharing a popular photo or video, we may retain that content on our servers for a longer period of time." The technical paper offers no help in understanding how WhatsApp systems assess frequently shared encrypted media messages without decrypting it at its end.</p>

<p>A possible explanation could be the usage of metadata by WhatsApp, which it discloses in its Privacy Policy while simultaneously being sufficiently vague about the specifics of it. That WhatsApp may be capable of reading encrypted communication through the inclusion of a backdoor bodes well for law enforcement, but not so much for unsuspecting users.</p>

<p><strong>The weakest link in the chain</strong></p>

<p>Concerns about backdoors in WhatsApp's product have led the French government to start developing their own encrypted messaging service. This will be built using Matrix – an open protocol designed for real-time communication. Indeed, the Privacy Policy lays out that the company "may collect, use, preserve, and share your information if we have a good-faith belief that it is reasonably necessary to respond pursuant to applicable law or regulations, to legal process, or to government requests."</p>

<p>The Signal Protocol is the undisputed gold standard of E2EE implementations. It is the integration with the surrounding functionality that WhatsApp offers which leads to vulnerabilities. After all, a chain is only as strong as its weakest link. Assuming that the attachments stored on the 'blobs' are in encrypted form, indecipherable to all but the intended recipients, this does not pose a privacy risk for the users from a technological point of view.</p>

<p>However, it is easy lose sight of the fact that the Privacy Policy is a legally binding document and it specifically states that messages are not stored on the 'blobs' as a matter of routine. As a side note, WhatsApp's Privacy Policy and Terms of Service are refreshing in their readability and lack of legalese.</p>

<p>As we were putting the final touches to this piece, news from WABetaInfo, a well-reputed source of information on WhatsApp features, has broken that newer updates of WhatsApp for Android are permitting users to re-download media deleted up to three months back. WhatsApp cannot possibly achieve this without storing the media in the 'blobs,' or in other words, in violation of its Privacy Policy.</p>

<p>As the aphorism goes: "When the service is free, you are the product."</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This article appeared at a time when WhatsApp's privacy credentials were coming under renewed pressure. The platform had rolled out end-to-end encryption in April 2016, positioning itself as a privacy-first service, yet its 2014 acquisition by Facebook had already raised concerns about data sharing between the two companies.

The piece draws on a gap between WhatsApp's stated deletion-upon-delivery policy and what two simple reproducible experiments appeared to show. This kind of technical scrutiny from civil society researchers was part of a broader pattern in the late 2010s, as encryption debates, sharpened by the Apple vs FBI case over the San Bernardino shooter's device, pushed platform accountability into public discourse.


## External Link

- [Read on Asia Times](https://asiatimes.com/2018/04/whats-up-with-whatsapp/)

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
