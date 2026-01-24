---
layout: default
title: "Aadhaar: On a Sticky Wicket"
description: "Investigation into technical vulnerabilities of Aadhaar's biometric authentication system, examining replay attacks, hardware security failures, and insider threats documented in 2017."
categories: [Media mentions]
date: 2017-06-16
authors: ["Pratap Vikram Singh"]
source: "Governance Now"
permalink: /media/aadhaar-sticky-wicket-governance-now/
created: 2026-01-24
---

**Aadhaar: On a Sticky Wicket** is an investigative feature published in *Governance Now* on 16 June 2017. Written by Pratap Vikram Singh, the article examines technology-related criticisms of Aadhaar's biometric authentication system. It opens with an account of Institute of Chemical Technology students who successfully spoofed fingerprint devices using wax and glue, before analysing systemic vulnerabilities including replay attacks, hardware security deficiencies, insider threats to the Central Identities Data Repository, and connectivity-dependent authentication failures.

## Contents

1. [Article Details](#article-details)  
2. [Full Text](#full-text)  
3. [Context and Background](#context-and-background)  
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Governance Now</em></dd>

  <dt>📅 Date:</dt>
  <dd>16 June 2017</dd>

  <dt>👤 Authors:</dt>
  <dd>Pratap Vikram Singh</dd>

  <dt>📄 Type:</dt>
  <dd>Feature Article</dd>

  <dt>📰 Publication Link:</dt>
  <dd>
    <a class="btn" href="https://www.governancenow.com/gov-next/egov/aadhaar-on-a-sticky-wicket">
      Read Online
    </a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>As arguments continue for and against the biometric authentication system, a look at the technology-related criticism of Aadhaar.</p>

<hr class="article-separator">

<p>In April, the Institute of Chemical Technology (ICT), Mumbai was making news. Its ranking in the National Institutional Ranking Framework (NIRF) 2017 dropped from the second position to 25th. In the same month, the institute was again trending, for another reason. A mischief by a group of third and fourth year undergraduate students not only surprised the top management of the institute but also the political heads in the government.</p>

<p>Let's start at the very beginning. Like most colleges and universities, the ICT mandates that students must have 75 percent attendance to appear in the final exams. To ensure this, the institute two years ago installed biometric devices in every classroom. Soon some students figured out a way to tweak this rule. They found that they could mark their attendance by using any biometric device kept in any classroom. A student need not go to his/her specific class to mark the attendance. As a result, in the past two years, over 350 students, including 'hostelers' and day scholars, marked their attendance without actually attending their classes.</p>

<p>The students took this prank to another level last year. Some of them researched several videos on YouTube to learn the process of making duplicate fingerprints. After browsing through several such videos and educating themselves in the hacking tools, it was time to experiment. Their method was simple: they took a matchbox, removed its cover, filled it with liquid wax and pressed their index finger against it. Once dry, a reverse image of the fingerprint gets imprinted on the wax. To bring it to its original form, the students spread sticky Fevicol glue over it, and left it for 12–16 hours until it solidified – the climate in Mumbai anyway remains humid during summers. And, voila, a duplicate fingerprint impression was made. However, this was just one part of the experiment. The real test lay in actually checking the fingerprint against the biometric device in the institute.</p>

<p>High on their invention, the students immediately went to test it. Their first attempt was in September. They did not succeed. They tried again for two or three days, but failed. Not losing their hope, they tried their luck with silicon polymer this time. They heated it a little – 60–70 degrees maybe. They hammered it to make a plane surface and pressed their fingers on it. "That didn't work out," says a member of the institute aware of the incident. Then they again tried the wax-glue technique in December. And it worked!</p>

<p>From January to April, the students exploited this new vulnerability in the attendance system to its full potential. But all good things must come to an end. One day a student went to the college dean's office with a request to mark his attendance for a particular day. During his cross-questioning, one thing led to another, and before he realised, the student had spilled the beans.</p>

<p>The students were reprimanded. The college decided to decrease the semester grade point average (SGPA) score by two points for the students involved. Musab Qazi in his report in the Hindustan Times quoted vice-chancellor GD Yadav as saying, "Even though the attendance records showed otherwise, we suspected that the students were not attending classes because they performed poorly in their exams. Then we came to know that they used polymer films to mark their attendance." The VC, in other words, admitted the biometric attendance system was hacked. However, the students didn't use polymer film; but wax and glue.</p>

<p>When Governance Now spoke to Yadav, he said he was misquoted by the newspaper. He denied any hacking of the biometric device. The students, he said, had not duplicated the fingerprint, but rather went to the adjacent classroom to mark their attendance.</p>

<p>Notwithstanding the scale or even veracity of the attendance rigging controversy, the ICT students seem to have exposed the most fundamental flaw with the fingerprint-based authentication systems used across the world – they can be easily copied and spoofed. Of late, there have been incidents wherein researchers and journalists have revealed technical and systemic glitches in the Aadhaar ecosystem only to be chased away by the government. Aadhaar has otherwise been criticised for infringement on an individual's right to privacy and the possibility of profiling. Let's take a look at the technology-related criticism of Aadhaar.</p>

<h3>Hardware security</h3>

<p>Thanks to a few incidents which came to light this year, the UIDAI has decided to build a secured hardware ecosystem. A series of 'replay' attacks showed that the fingerprint devices in use are leaky and prone to hacks. In a replay attack, the biometric data of a user is saved on the device during authentication and used afterwards for future authentication. One such incident surfaced when a UIDAI communication sent to one of the authentication user agencies (AUA) was leaked. In its letter, the authority had sought explanation from the AUA about how they could do multiple and simultaneous authentications using the same biometrics on 11 January. The leak was followed by a police complaint against Axis Bank, Suvidha Infoserve (business correspondent service provider) and eMudhra (e-sign provider) for doing 'unauthorised transactions'.</p>

<p>"Within a bank someone was demonstrating that this was possible. Someone was doing research: can the biometrics be restored and can it be used again in future. The banks were preparing for large scale attacks," says Sunil Abraham, executive director, Centre for Internet and Society. Once every single taxpayer's bank account is connected using the Aadhaar enabled payment system (AEPS), it will become a low-hanging fruit for hackers, says Abraham. "The serious attacks would start, then," he says.</p>

<p>To cope with the security lacunas, the authority wrote to all AUAs and other agencies, to comply with the hardware specifications it had issued in November. The authority asked the agencies to use 'registered devices', complying mandatorily with L0 standard (which provides for encryption at the application level). Off the record, researchers, however, claim that even L0 devices can be hacked. A software programme, intended to manipulate a computing device, could display the biometrics of the person during an authentication, which could then be stored and reused. To make the system foolproof, say researchers, the authority must mandate L1 compliance too.</p>

<p>It is interesting to note that even the L0 and L1 compliant devices can be easily gamed using duplicate fingerprints on a polymer film or glue. The detection of duplicate fingerprints can only be done through high-end fingerprint devices, says a government official overseeing the security specifications of biometric devices. "Those are called fake finger immune devices. They can detect the impression. They won't authenticate if the fingerprint is not original," the official says.</p>

<p>"These devices are expensive. They are the future generation devices. They will be immune to fake fingerprints. They detect the blood circulation; any insulation between the finger and the device will be detected," the official says. There are a very few companies which make such devices. There are 23 different parameters, mostly about image quality. The fake finger immunity functionality will be added whenever we chose to mandate it, the official says.</p>

<h3>Insider threat</h3>

<p>A paper titled 'Privacy and security of Aadhaar: a computer science perspective', co-authored by IIT Madras professor Shweta Agrawal and IIT Delhi professors Subhashis Banerjee and Subodh Sharma, notes that biometric and demographic data are public and hence "can be used without consent". It also points out the vulnerability to correlation of identity across domains.</p>

<p>Computer science experts believe that there are inadequate protections against insider attacks on central identities data repository (CIDR) data. "The CIDR data is encrypted but the decryption keys reside in CIDR. The [UIDAI] managers can have access to the decryption keys," they say.</p>

<p>"You need to have process to have control over the access. Data should only be accessed through a fixed computer programme, and not by a human, designed for some fixed functionalities considered sanitised," says Shweta Agrawal of IIT Madras. The combination of cards can be codified as a computer programme. So it can't be used for bad purposes, says Agrawal.</p>

<p>The authority must have a separate administrative control for online audit and key management. It should prohibit manual inspection of CIDR data, the IIT professors recommend, adding that only 'pre-approved and audited' computer programmes with tamper-proof guarantees should access CIDR data.</p>

<h3>Biometrics for authentication or identification?</h3>

<p>Biometric is an essential identifier. It might not be inappropriate to capture the biometrics at the time of enrollment for creating the Aadhaar database. Experts believe biometric data is unfit for being used for authentication. Reason: biometric data, like the demographic data, is publicly available.</p>

<p>Fingerprint can be duplicated or faked easily (as seen in the ICT incident). The application of biometrics for authentication runs the risk of its usage without consent.</p>

<p>"Identification is inherently public. Even if I pick up a paper my fingerprint goes on it. One has to be careful using biometrics. So biometric in general has to be considered as identification information not authentication.</p>

<p>"Authentication should be a secret, like my ATM PIN number which only I should know. So there is no question of someone using it without my consent unless I give it to them," says Agrawal.</p>

<p>Or you can tie-up identification and authentication, as in you can use biometric for authentication with a password, she adds. Functionality and security are two conflicting goals. You can always achieve one without the other. Ideally a system or a project like Aadhaar has to be best of both, she says.</p>

<p>Does the Aadhaar project provide the said balance? "It is a very ambitious project. It's too premature to say it has best of both," opines Agrawal.</p>

<p>"The technology is available, but more should happen on this front. Also, the information about the design should be made available. How things function should be known," she says.</p>

<p>A former state IT secretary, who is now on a central deputation in Delhi, says that biometric authentication should only be used in a limited set of cases, in proportion to the requirement. It is an excellent tool for de-duplication and eliminating the bogus and ghost beneficiaries from several databases, leading to windfall gain for the public exchequer. This view is shared by many senior government officials.</p>

<h3>Untested, dependent on connectivity</h3>

<p>"It fails. It can be faked. The person who controls the device decides whether the person is present or not," says Usha Ramanathan, independent legal researcher. The biometrics change with age, and so an individual will have to re-enroll. "What we do know is that when 80 crore numbers were issued, 8 crore enrolments were rejected, and we know that people have been declared duplicates even when they never have been enrolled earlier," says Ramanathan. In Delhi, the enrolment has far exceeded expectations – the rate is 129 percent. The database has not been put through an independent audit, so no one knows what it's worth.</p>

<p>"The UIDAI had a UBCC [UIDAI Biometric Centre of Competence] in it – which does research because the nature and diversity of India's working population made biometrics a challenge," says Ramanathan.</p>

<p>The authority says that the centre [UBCC] no longer exists. Check when they admitted to having the centre, and you will find that it was only during the time it thought that the database might get scrutinised by someone from outside the UIDAI.</p>

<p>Moreover, there are many areas where connectivity is extremely poor. If there is no connectivity, there is buffering; the biometric is retained and the authentication is done at a later point. In other circumstances, says Ramanathan, there is no means for us to know whether we are giving our fingerprints to a registered device or not, why the device accepts or rejects the biometric. The person controlling the device also controls the transaction.</p>

<p>"What do you think it means when they say in the Ratan Watal committee on Digital Economy that they do not want to use biometrics? They mention only two reasons: connectivity problems and indifferent quality of the PoS devices. Why then are these aspects not relevant for PDS or NREGA?," questions Ramanathan.</p>

<p><em>(The article appears in 30 June 2017 edition)</em></p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

This article appeared during a period of heightened scrutiny of Aadhaar's technical architecture, following revelation of multiple security vulnerabilities in early 2017. The Institute of Chemical Technology incident received significant media attention when students successfully spoofed biometric attendance devices using homemade fake fingerprints created from wax and Fevicol glue, enabling large-scale fraudulent attendance over an extended period. Vice-Chancellor G.D. Yadav initially acknowledged to Hindustan Times that the biometric system had been compromised before later denying any hacking occurred, claiming students merely used adjacent classrooms.

The ICT episode exemplified fundamental weaknesses in fingerprint-based authentication systems that UIDAI was simultaneously confronting. Around the same period, replay attacks demonstrated how stored biometric data could be reused for unauthorised authentication. UIDAI subsequently filed criminal complaints against Axis Bank, Suvidha Infoserve, and eMudhra following the discovery of unauthorised transactions enabled by replayed biometric data.

These replay attacks exposed critical hardware vulnerabilities in existing biometric devices. UIDAI responded by issuing specifications mandating the use of 'registered devices' compliant with L0 encryption standards, which provided application-level encryption. However, security researchers interviewed off-record maintained even L0-compliant devices remained vulnerable to software manipulation that could capture and store biometric data during authentication. L1 compliance, requiring secure hardware elements, remained unimplemented. Neither L0 nor L1 standards addressed spoofing through fake fingerprints; only expensive 'fake finger immune devices' capable of detecting blood circulation could prevent such attacks, but UIDAI had not mandated their deployment.

Academic criticism intensified through a research paper by IIT Madras professor Shweta Agrawal and IIT Delhi professors Subhashis Banerjee and Subodh Sharma titled 'Privacy and Security of Aadhaar: A Computer Science Perspective'. The paper identified inadequate protections against insider threats to the Central Identities Data Repository, noting that whilst CIDR data remained encrypted, decryption keys resided within CIDR itself, accessible to managers. The authors recommended prohibiting manual inspection of CIDR data, permitting access only through pre-approved, audited, tamper-proof computer programmes, and establishing separate administrative controls for online audit and key management.

The paper fundamentally challenged biometric authentication's appropriateness, arguing that biometric data constituted publicly available identification information rather than secret authentication credentials comparable to ATM PINs. The authors contended fingerprints left on surfaces could be captured without consent, making biometrics suitable for deduplication during enrolment but problematic for ongoing authentication. They proposed hybrid systems combining biometric identification with password-based authentication.

Independent legal researcher Usha Ramanathan documented systemic failures including large-scale enrolment rejections, over-enrolment in certain regions, and false duplicate declarations. She noted the UIDAI Biometric Centre of Competence, established to address challenges posed by India's diverse working population, had been disbanded and was only acknowledged when external scrutiny seemed imminent. Ramanathan highlighted the Ratan Watal Committee on Digital Economy's recommendation against biometric authentication due to connectivity problems and indifferent point-of-sale device quality, questioning why these concerns didn't apply equally to PDS and MGNREGA implementations.

## External Link

- <a href="https://www.governancenow.com/gov-next/egov/aadhaar-on-a-sticky-wicket">Read on Governance Now</a>

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
  color: #1b2a49;
  font-size: 1.1rem;
  margin-top: 1.5rem;
  margin-bottom: 0.8rem;
  font-weight: 600;
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
.article-separator {
  border: none;
  border-top: 1px solid rgba(0,0,0,0.08);
  margin: 0.75rem 0 1rem 0;
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
