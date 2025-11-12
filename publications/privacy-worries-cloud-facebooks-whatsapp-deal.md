---
layout: default
title: "Privacy Worries Cloud Facebook's WhatsApp Deal"
description: "An article by Sunil Abraham in The Economic Times analysing the privacy and competition concerns arising from Facebook’s acquisition of WhatsApp, and the need for data protection regulation in India."
categories: [Media articles, Publications]
date: 2014-03-14
authors: ["Sunil Abraham"]
source: "The Economic Times"
permalink: /publications/privacy-worries-cloud-facebooks-whatsapp-deal/
---

**Privacy Worries Cloud Facebook's WhatsApp Deal** is an article by Sunil Abraham, published in *The Economic Times* on 14 March 2014.  
The piece examines global and Indian responses to Facebook’s acquisition of WhatsApp, highlighting the absence of comprehensive data protection in India and warning that users’ privacy will remain vulnerable until national regulation and enforcement mechanisms are in place.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)  

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>The Economic Times</em></dd>

  <dt>📅 Date:</dt>
  <dd>14 March 2014</dd>

  <dt>👤 Author:</dt>
  <dd>Sunil Abraham</dd>

  <dt>📄 Type:</dt>
  <dd>Opinion Article</dd>

  <dt>📰 Publication Link:</dt>
  <dd>
    Link unavailable (archived source referenced)
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">
  <p>Privacy activists in the United States have asked the competition regulator, the Federal Trade Commission, to put on hold Facebook's acquisition of WhatsApp. Why have they done this when Facebook has promised to leave WhatsApp untouched as a standalone app?</p>

  <p>Activists have five main concerns.</p>

  <ol>
    <li>Facebook has a track record of not keeping its promises to users.</li>
    <li>The ethos of both companies when it comes to privacy is diametrically opposite.</li>
    <li>The probability that WhatsApp messages and content will be intercepted because of Facebook’s participation in the NSA’s PRISM spying programme.</li>
    <li>Facebook slurping WhatsApp’s large repository of phone numbers.</li>
    <li>Two hundred trackers already monitor your internet use when you are not using Facebook, and now they are tracking mobile use much more granularly.</li>
  </ol>

  <p>This week the Indian competition regulator (CCI) also told the media that the acquisition would be subject to scrutiny. However, unlike the US regulator, the Indian regulator does not have the mandate to examine the acquisition from a privacy perspective.</p>

  <p>LIRNEasia research in Indonesia paints a very similar picture to what we have in India. When Indonesian mobile phone users were asked if they used Facebook they answered in the affirmative. Then the very same users were asked if they used the internet and they replied in the negative. A large number of Facebook users in these other similar economies are trapped within what are called “walled gardens”.</p>

  <p>Walled gardens allow mobile phone subscribers without data connections to get access to a single over-the-top service provider like Facebook because their telecom provider has an arrangement. Software such as Facebook on every phone makes it possible for feature-phone users to also enter the walled garden.</p>

  <p>According to Facebook it "is a fast and easy-to-use native app that works on more than 3,000 different types of feature phones from almost every handset manufacturer that exists today".</p>

  <p>Unlike North American and European users of Facebook, who freely roam the “world wide web” and then choose to visit Facebook when they want to, many Indian users will first experience data services in a domesticated fashion within a walled garden.</p>

  <p>Whether or not they will wander in the wild when they have full access to the internet remains to be seen. But given our poor rates of penetration, dogmatic insistence on network neutrality at this early stage of internet adoption may not be the right way to maximise welfare and consumer interest.</p>

  <p>Fortunately for Facebook and unfortunately for us, India still does not have a comprehensive data protection or horizontal privacy law. The Justice A. P. Shah Committee that was constituted by the Planning Commission in October 2012 recommended that the Privacy Act articulate national privacy principles and establish the office of the Privacy Commissioner. It further recommended that data protection and surveillance be regulated for both the private sector and the state.</p>

  <p>Since then the Department of Personnel and Training has updated the draft bill to implement these recommendations and has been working towards consensus within government.</p>

  <p>Since we still do not have our own privacy regulator we will have to depend on foreign data protection authorities and privacy commissioners to protect us from the voracious appetite for personal data of over-the-top service providers like Facebook. This is woefully insufficient because they will not act on harm caused to Indian consumers or be aware of how Facebook acts differently in the Indian market.</p>

  <p>As we approach the first general election in India when social media will play a small but influential role, it would have been excellent if we had someone to look out for our right to privacy.</p>
</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This article was written shortly after Facebook announced its acquisition of WhatsApp in early 2014. Sunil Abraham situates the debate within a global context of rising concern over digital surveillance and platform monopolies. He warns that India’s absence of a dedicated privacy regulator leaves citizens and businesses unprotected, and that network neutrality debates must consider stages of market development alongside user welfare.

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
.media-details dt { font-weight: 600; color: #1b2a49; margin-top: 0.7rem; }
.media-details dd { margin: 0 0 0.3rem 0.3rem; color: #555; }

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
