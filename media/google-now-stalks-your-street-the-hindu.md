---
layout: default
title: "Google Now Stalks Your Street"
description: "A Hindu report on Google Street View's launch in Bangalore in 2011, examining the privacy concerns it raises in the absence of Indian privacy legislation, with commentary from Sunil Abraham of CIS."
categories: [Media mentions]
date: 2011-05-27
source: "The Hindu"
permalink: /media/google-now-stalks-your-street-the-hindu/
created: 2026-04-20
---

**Google Now Stalks Your Street** is a *The Hindu* report published on 27 May 2011, covering Google's announcement that it would begin collecting Street View imagery in Bangalore, the first Indian city to be mapped for the service. The article examines the privacy concerns the initiative raises in the absence of Indian privacy legislation, drawing on comment from [Sunil Abraham](/sunil/) of the [Centre for Internet and Society](/cis/).

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>The Hindu</em></dd>

  <dt>📅 Date:</dt>
  <dd>27 May 2011</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Publication Link:</dt>
  <dd>Not available online</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>Not too long from now, Google Map will allow you a sneak peek into the smallest cul-de-sac in the city, zoom into the most popular restaurant on the block, or even check out a home you want to rent.</p>

<p>Google on Thursday announced it will begin collecting images in Bangalore for its controversial Street View service, which will be offered on Google Maps. The service will allow you to explore places through its 360-degree, street-level imagery.</p>

<p>This, it intends to do by using cars and "trikes" (three-wheel pedicab) fitted with a camera system on top. The vehicles "will start gathering images from select locations in and around Bangalore, such as the Nrityagram Dance Village over the next few weeks," Google said in a communiqué.</p>

<p>"We decided to start driving in Bangalore because it is the IT capital of India and feel that the IT-savvy users will be able to leverage the benefits of the product to the fullest," said Vinay Goel, Product Head, Google India. Street View, introduced in May 2007 in the U.S., has since expanded to 27 countries. "It is useful for urban development planners, law enforcement agencies, house-hunters, and travellers," Mr. Goel said.</p>

<h3>Privacy issues</h3>

<p>But is Google venturing too close for comfort? The service has begun to draw criticism over a host of privacy issues here, just as it has done in several countries where it is in use. This despite Google assurance that it will blur people's faces and licence plates so they are not identified.</p>

<p>However, in the absence of a broad privacy law, there is no mechanism by which the Indian Government can hold Google and its service accountable, explains Sunil Abraham, Director of the Centre for Internet and Society.</p>

<p>"For example, the Japanese Government found that Google's footage was recording the insides of people's homes," he pointed out. Subsequently, the Japanese Government decided to reduce the height of the camera by 16 inches.</p>

<p>"Every country has a different concept of privacy and any project by Google has to adhere to the local sensibility. But India lacks the mechanism to do so." Further, Mr. Abraham said, given the fact that 90 per cent of the population is offline, and a third illiterate, a Google logo on the van may not serve as implicit consent (unlike in the U.S. where it is a widely recognised brand).</p>

<h3>Not real time</h3>

<p>According to Google, it protects privacy because Street View images are not real time, but are between a few months to a few years old. There are "easily accessible tools that [allow] users to request further blurring of any image that features the user, their family, their car or their home," says the Google Maps website. "Users can also request the removal of images that feature inappropriate content (for example, nudity or violence)."</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

Google Street View had been expanding internationally since its 2007 US launch, and by 2011 it was operating in 27 countries. Its arrival in India prompted immediate questions about consent and accountability, given that India had no dedicated privacy legislation at the time. The absence of a legal framework meant that even where Google's own practices were found to be inadequate, as had happened in Japan and several European countries, Indian authorities had no clear statutory basis on which to intervene.

Sunil Abraham's point about implicit consent is grounded in a practical reality of the Indian context: the Google brand, widely recognised among urban and online populations in the US and Europe as a signal of data collection activity, carried no such meaning for the majority of Indian citizens who were offline. The argument raises a broader question about whether consent frameworks designed for high-connectivity societies translate to contexts with very different levels of digital literacy and internet access.

The issues raised in the article illustrate early concerns about how global digital services would operate within India's regulatory environment, particularly in the absence of clearly defined privacy safeguards at the time.

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
.highlighted-text h3 {
  font-size: 1rem;
  font-weight: 600;
  margin: 1.2rem 0 0.6rem;
  color: #1b2a49;
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
