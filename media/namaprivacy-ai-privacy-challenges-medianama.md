---
layout: default
title: "#NAMAprivacy: Challenges in Understanding and Regulating AI and Privacy"
description: "A MediaNama report by Aroon Deep documenting discussions on algorithmic complexity, recommendation systems, unintended consequences, and proxy data from MediaNama's privacy conference in Bangalore, featuring experts from CIS, Takshashila, iSPIRT, and industry practitioners."
categories: [Media mentions]
date: 2017-10-18
authors: ["Aroon Deep"]
source: "MediaNama"
permalink: /media/namaprivacy-ai-privacy-challenges-medianama/
created: 2026-01-07
---

**#NAMAprivacy: Challenges in Understanding and Regulating AI and Privacy** is a *MediaNama* article published on 18 October 2017 by Aroon Deep. The report documents the third part of discussions from MediaNama's privacy conference held in Bangalore on 5 October, examining the inherent complexity of algorithmic systems and regulatory challenges they pose. The article features contributions from Sunil Abraham of the Centre for Internet & Society, alongside researchers, engineers, and policy experts debating recommendation systems, data collection intent, sectoral regulatory conflicts, unintended consequences, and proxy data issues.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
<dt>📰 Published in:</dt>
<dd><em>MediaNama</em></dd>

<dt>📅 Date:</dt>
<dd>18 October 2017</dd>

<dt>👤 Authors:</dt>
<dd>Aroon Deep</dd>

<dt>📄 Type:</dt>
<dd>Conference Report</dd>

<dt>📰 Article Link:</dt>
<dd>
<a class="btn" href="https://www.medianama.com/2017/10/223-ai-privacy-challenges-understanding-regulating/">
Read Online
</a>
</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p><em>On 5th October, MediaNama held a #NAMAprivacy conference in Bangalore focused on Privacy in the context of Artificial Intelligence, Internet of Things and the issue of consent, supported by Google, Amazon, Mozilla, ISOC, E2E Networks and Info Edge, with community partners HasGeek and Takshashila Institution. Part 1 of the notes from the discussion on AI and Privacy are <a href="https://www.medianama.com/2017/10/223-namaprivacy-artificial-intelligence-privacy/" rel="nofollow noopener noreferrer">here</a> Part 2 is here. Part 3:</em></p>

<p>Algorithms are incredibly complex, and it is sometimes impossible to fully understand them, even for creators.</p>

<h2>Recommendations</h2>

<p>One of the most common implementations of algorithms come in recommendations, like those on search results or streaming services like Netflix.</p>

<p><strong>Anupam Manur from the Takshashila Foundation</strong> pointed out: "Recommendations like Netflix movie recommendations may not be harmful, but concentrated recommendations in Twitter will lead to echo chambers, and that can be harmful in an aggregated way." Indeed, filter bubbles are a known phenomenon.</p>

<p><strong>Sanjay Jain from iSPIRT</strong> argued that tangible harms should be targeted: "The whole question of personalization, recommendations, etc, is going to be a theoretical discussion. We should start from the harm. If a recommendation system causes me harm, and says that because of who I am, I have to pay a higher taxi rate, and the reason why I pay it is because of a certain protected category. Let's say you're a female and end up with a higher rate on the taxi company then that becomes unfair. Per se, recommendation systems cannot be argued to be fair or unfair, it comes back again to outcomes, harms, and that's where you start from."</p>

<h2>Intent of data collection</h2>

<p><strong>Anand Venkatanarayanan, a senior engineer at NetApp</strong>, said: "Recently companies have been having interesting experiments on data collection for threat detection. So they have started collecting everything a user does on their company laptop. Everything, <em>n = all</em>. Because they figured out that this is the only way in which they can do large-scale threat detection with thirty-minute responses. People had been very unhappy about it, because in the past this has not been done. The answer is, well, <strong>the intent is not to do finger-profiling of you, but to ensure that the systems are not breached</strong> because of something you did somewhere else."</p>

<p>"In reality, if you call data collection as a privacy breach, you're doing almost everything, right? But in reality, we can do a lot of prevention in terms of purpose limitation, differential encryption, and property-preserving encryption to ensure that user data, even if it's compromised and put it outside, you can't make anything out except IP addresses."</p>

<h2>Defying sectoral codes</h2>

<p><strong>Srinivas P, head of Data Security at Infosys</strong>, pointed to an example of impermissible algorithms: "Often what kind of algorithms are permitted or not is also outside the purview of data privacy domain. Take for instance insurance. There's a company in Canada which is being prosecuted now, what they've done is the people who bought cars, they have chosen to avail the service about the maintenance using IoT basically, to see when to change the wheel, when the warranty of the wheel is going to end, and timely maintenance steps, things like that. So that data, which included the speed, acceleration, the time at which you're going, driving in Canada, I think in Toronto, which area, territory, are there lots of pubs there, <strong>all kinds of data it looked at and felt that certain kinds of users are highly prone to accidents, and therefore increase their premium. So is this something we can allow?</strong></p>

<p>"So these kinds of things, it's difficult to put into data privacy law, and say what's permitted or not. The provincial insurance regulators have to step in and determine that. Because insurance is based on a concept of statistical likelihood of anybody who is taking insurance are equally likely to cause an accident or become a victim of an accident unless you're racing or rallying. <strong>These algorithms sometimes defy the traditional logic built into the sectoral codes</strong>. Therefore I think there is a need for other laws to pitch in and what can be done or not, but innovators will continue to do because their focus is to use technology to make money."</p>

<h2>Unintended consequences</h2>

<p>Most algorithmic harms come from <em>unintended</em> consequences, not from nefarious and deliberate processes.</p>

<p><strong>Akash Mahajan from Appsecco</strong> pointed to an example: "Unintended consequences from the point of view of IT security, one really large phone manufacturer did this project where they figured out that whenever it's time for a new version of their operating system to be released, their servers tend to get slow because obviously everyone wants to download and get the latest update as soon as it's out. So <strong>they decided that this is definitely a machine learning problem, let's figure out where to send more server provision</strong>. Which geographic region in the world. Based on where more people are downloading and bandwidth consumption is more. They're provisioning and spending money for the servers where it's most.</p>

<p><strong>"But what happens when they have to release an immediate security patch</strong>, because anyone who is running a rogue wireless access point can attack their phone. So if there was any security assumption made by a company or individual or government that this phone is secure, and it'll stay secure, and suddenly the patch doesn't reach them fast enough, because their ML decides that this region doesn't usually require this download so early. Those are some unintended consequences we'll never think of. The same applies to OTP notifications — when we used another outer-manned (?) pipeline to be able to authenticate against something."</p>

<p>Sunil Abraham pointed out, "Unintended consequences is the age-old problem in regulation. There's nothing we can do in any domain around unintended consequences."</p>

<h2>Ambient or proxy data</h2>

<p>Let's say you prevent collection of certain data. But what happens when that data is extrapolated from other pointers anyway?</p>

<p>Beni Chugh from the IFMR Finance Foundation said, "When I come to algorithms in particular, we as a society may need to have some kind of fencing off that there may be certain kinds of variables that we're definitely not going to touch — even if I say touch, what about the proxies, the other variables pick up off those fenced off variables?"</p>

<p>Sunil Abraham suggested a way around this: "You could do the blind which means you delete the column of that database and then you think that the outcome will not be discriminatory, or <strong>you could also do it by having the column in the database, and checking if the outcome correlates to the column</strong>."</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This discussion formed part of a broader series examining artificial intelligence and privacy implications shortly after India's Supreme Court recognised privacy as a fundamental right in August 2017. The conference participants confronted practical challenges that theoretical legal frameworks often overlooked—algorithmic opacity, sectoral regulatory gaps, and the difficulty of anticipating downstream consequences of machine learning systems.

The recommendation systems debate reflected growing awareness of filter bubbles and echo chambers, concepts popularised by Eli Pariser's work and increasingly relevant as social media platforms deployed algorithmic curation at scale. Jain's emphasis on harm-based evaluation rather than algorithmic fairness per se anticipated approaches later adopted in jurisdictions examining algorithmic impact assessments, focusing regulatory attention on measurable outcomes rather than theoretical constructs.

Venkatanarayanan's corporate surveillance example highlighted tensions between security imperatives and employee privacy expectations. Comprehensive endpoint monitoring had become technically feasible through advanced threat detection systems, yet raised questions about proportionality and purpose limitation that existing frameworks struggled to address. His reference to property-preserving encryption and differential privacy techniques pointed toward technical solutions that might reconcile security objectives with privacy protection.

The Canadian insurance case Srinivas described exemplified how algorithmic risk assessment could conflict with actuarial principles and anti-discrimination norms. Traditional insurance regulation assumed pooled risk amongst broad categories, whereas granular behavioural data enabled individualised pricing that potentially penalised protected characteristics or proxies thereof. This tension between statistical sophistication and fairness principles remained unresolved across multiple jurisdictions.

Mahajan's security patch distribution scenario illustrated how machine learning optimisation for one objective—server efficiency—could inadvertently compromise another—timely security updates. Such cases demonstrated that algorithmic harms often emerged not from malicious intent but from narrow optimisation functions that failed to account for edge cases or competing priorities.

Abraham and Chugh's discussion of proxy variables addressed a fundamental challenge in anti-discrimination regulation. Even when sensitive attributes were excluded from datasets, algorithms could infer protected characteristics through correlated variables, rendering simple data deletion insufficient. Abraham's proposal to retain sensitive columns for correlation testing represented a technical approach to detecting disparate impact, though implementation challenges remained substantial.

## External Link

- <a href="https://www.medianama.com/2017/10/223-ai-privacy-challenges-understanding-regulating/">Read on MediaNama</a>

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
