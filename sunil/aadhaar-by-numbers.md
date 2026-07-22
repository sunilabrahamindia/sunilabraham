---
layout: default
title: 'Aadhaar by Numbers'
description: "Transcript of Sunil Abraham's presentation on Aadhaar, examining biometrics, identification, authentication, surveillance and alternative approaches to digital identity."
categories: [Resources, Sunil Abraham, Transcripts]
permalink: /sunil/aadhaar-by-numbers/
created: 2026-07-22
---

**Aadhaar by Numbers** is a presentation delivered by [Sunil Abraham](/sunil/) at a public seminar organised by the National Institute of Public Finance and Policy (NIPFP) in New Delhi on 29 April 2016. In the presentation, Abraham examines Aadhaar from a technical perspective, discussing biometrics, identification and authentication, surveillance, and the risks of centralised identity systems. He argues for alternative approaches using smart cards, cryptography and decentralised systems, while examining broader questions of security, accountability, corruption and the appropriate use of technology.

## Contents

1. [Key points from the presentation](#key-points)
2. [Video](#video)
3. [Full transcript](#transcript)
4. [On social media](#social-media)

## Key points from the presentation {#key-points}

1. **Aadhaar should be evaluated as a technological system, not only as a legal or privacy issue.** Abraham argues that many criticisms of Aadhaar focus on law and policy, while fundamental problems also arise from the technological architecture itself.
2. **Centralising biometric data creates significant security risks.** A central biometric database becomes a valuable target, while operational requirements such as de-duplication and authentication make it difficult to keep the underlying data permanently encrypted.
3. **Consent mechanisms cannot solve the inherent characteristics of biometric identification.** Because biometrics can potentially be captured and used remotely, covertly and without consent, Abraham distinguishes between a person identifying themselves to the state and the state identifying a person without their active participation.
4. **Biometrics are unsuitable as authentication credentials.** Unlike passwords, PINs or cryptographic keys, biometric characteristics cannot easily be revoked or changed when compromised. People also leave biometric information, such as fingerprints, in their everyday environment.
5. **Biometrics could instead be used to connect a person to a decentralised identity credential.** Abraham proposes storing cryptographic credentials and relevant information on smart cards, with biometrics used only when necessary to establish that the person presenting a card is its legitimate holder.
6. **Large-scale biometric identification inevitably produces errors that require accountable human decision-making.** He challenges the interpretation of Aadhaar's false-positive identification rates and criticises systems in which consequential decisions are made through automated or opaque manual adjudication without adequate notice, hearing, appeal or individual accountability.
7. **Identity systems need "human skin in the game".** Abraham argues that someone must be identifiable and accountable when fraudulent or "ghost" identities enter a system. Technology should not become an explanation that leaves nobody responsible when failures occur.
8. **Surveillance should be limited and directed towards power.** He compares [surveillance to salt in cooking](/articles/surveillance-is-like-salt-in-cooking/), useful in small quantities but counterproductive in excess, and argues that transparency requirements should be directly proportionate to power, while privacy protection should be inversely proportionate to power. Public resources should therefore be used to create greater accountability throughout the chain of government and welfare delivery.
9. **Newer and more complex technology is not automatically better technology.** Using biometrics and DNA profiling as examples, Abraham argues against "technoutopianism": every technology should instead be assessed according to its fitness for purpose, vulnerabilities and the safeguards needed to address human and technical failures.
10. **A decentralised and competitive identity ecosystem could be more resilient than a state monopoly.** Rather than relying on a single authority and technological approach for identification and authentication, Abraham suggests that multiple providers and technologies could create greater choice, accountability and resilience, with poorly performing actors subject to meaningful consequences.

## Video {#video}

<div class="aadhaar-video">
  <div class="aadhaar-video__embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/Y9uOBAqjIMg"
      title="Aadhaar by Numbers - Sunil Abraham"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>

  <div class="aadhaar-video__details">
    <p><strong>Aadhaar by Numbers</strong></p>
    <p>Uploaded: 7 September 2016</p>
    <p>Speaker: Sunil Abraham</p>
    <p>
  In this presentation, Sunil Abraham examines Aadhaar from a technical perspective, discussing biometrics, identification and authentication, surveillance, and alternative approaches to digital identity architecture.
  </p>
  </div>
</div>

## Full Transcript {#transcript}

<div class="transcript-text" markdown="1">

**Sunil Abraham:** I'll get started by talking a little bit about my research organisation, and then the work we have done as far as privacy research is concerned, then a little bit about what we've done on the UID, and also give you a personal life story to help you understand why I take such a perspective. And then I have seven numbers that I will take you through and explain why those numbers are important and how those numbers connect to the UID project.

So, very briefly, we are an eight-year-old research organisation with offices in Bangalore and Delhi. It's a 25-member team. We are mostly lawyers, but we also have some computer engineers and mathematicians. And we work in five areas of policy research. The first is accessibility for the disabled. The second we call access to knowledge; it's mostly copyright law and patent law. The next is openness, where we focus on free software, open standards, open access, open content. We work on Wikipedia, trying to grow five Indic-language Wikipedias. And then internet governance, where we do free speech, privacy, cybersecurity, and the international internet governance bodies such as ICANN and the ITU and WSIS process. And then finally, a little bit of work on telecom; we have a single distinguished fellow trying to push for a shared spectrum paradigm in the Indian telecom industry.

As far as privacy research goes, in particular, we did two important things. One is we served on the Justice A. P. Shah Committee that produced a report on the right to privacy. Hopefully, that report will shape the Privacy Bill when it is introduced in Parliament. And the second thing we did is we developed a citizens' draft of what the Privacy Bill in India should look like. And along with the Data Security Council of India, we held about 17 multi-stakeholder meetings across two years discussing the Privacy Bill. And very strangely, because the government refused to discuss their bill, we started getting calls from private sector players saying, "Hey, how come this language is in the Privacy Bill? Can you explain it?" And then we had to say, "Oh, relax, that's not the real bill, that's just a fraudulent bill that a non-profit organisation has put together. The real bill will leak, as it did," and there were three leaks and we've analysed that, and we've seen the sixth version of the Privacy Bill from DoPT slowly move towards Justice A. P. Shah Committee report recommendations.

And finally, on the UID, we have been researching the project from its inception. We have about six years of research on the UID project at least. And we've written seven open letters to the Standing Committee on Finance that examined the project and also had - this is known as the Jaswant - no, sorry, Yashwant Sinha Committee. So we've written seven letters. So often people say, "Oh, you have something against this particular government, that's why you are criticising the UID." No, that's not true at all. We've always criticised the UID; it's not a new criticism. And those seven open letters have been unanswered; so far, we've never gotten any response from the authority or anybody else on our seven open letters.

So finally, the small personal story so that you can understand why I'm sceptical of projects such as this. So, I was in second year of engineering. Unlike other distinguished people in this room who most probably had good educational credentials from respectable institutions, I'm only a Bachelor in Industrial and Production Engineering, and my degree is from a local college in Bangalore. And as most of you know, engineers like to consume large quantities of beer. This, I heard, is an international phenomenon, not just restricted to Bangalore. And in order to earn money to drink beer, my father had bought me a 286, 386 computer. So, the only thing that we managed to get at that point in time was some data entry work.

And we didn't realise what kind of data entry we were doing. And the first two days we did the data entry very seriously and very diligently. On the third day, we were always very surprised that the complete data entry batch was accepted without any criticism or any feedback. So we thought we must introduce two errors in it to check whether they're doing any kind of verification. So we put the two errors in, and that day also there was 100% acceptance; we got paid. And from the next day, we were typing absolute nonsense. And it turns out later that that was the data entry for the EPIC cards, the election cards. And even on my card, there are errors, and that's the reason why those errors exist, which is the subcontracting of the subcontracting.

It happened in the UID project also. When the UID authority says, "We have enrollers, enrolment agencies," those agencies didn't really go to the rural parts of India and do the enrolment themselves. They in turn worked with other subcontractors, and sometimes the subcontractors had further subcontractors. So that's the reason why the database state is not so easy to produce. I mean, it's easy to sit in Bangalore and design a project, but then when you take it to the field, there are all sorts of complications which you have to deal with.

Anyhow, in terms of simplicity, and also to set the record straight, many people think that CIS is some kind of Luddite institution, that we're against technology. So I have to articulate or state my articles of faith, some kind of creed, so that it's very clear where I stand on certain issues. Number one, I support the use of biometrics. Number two, I support the use of identification and authentication technology by the government. Number three, I support the use of ID numbers in government databases. Number four, I am pro-targeted surveillance in order to address corruption and also to protect national security. So those are my four articles of faith. I just thought to make it very clear, because as I go through my presentation, people will think that maybe he is against all these things. No, no, I am for all of these things.

And the next thing to say is, if you're having trouble following my argument, a way to simplify it is to say that I'm comparing two types of technologies: biometrics versus smart cards. And this comparison has been done before, after the Kargil conflict, when L. K. Advani, the then Home Minister, decided to launch the Multipurpose National Identity Card, MNIC. At that point, IIT Kharagpur was given the job of deciding what technology should be used. They took an existing ISO standard for smart cards that only supported symmetric keys, and they upgraded that standard to support asymmetric keys. That standard was called SCOSTA: Smart Card Operating System for Transport Applications. And it was already tested for both drivers' licences and vehicle registration documents. In two states, in Maharashtra and in Gujarat, there were already projects running with this technology in place. So that was the technology that the NDA government proposed when they were last in power.

And then the UPA government comes into power, and then they decide to make a technological choice, and they move to biometrics. And we have been constantly advocating that we go back to the old choice, which is go back to smart cards and digital signatures, the use of cryptography in order to design the project. And one of the key letters that we wrote to the Standing Committee on Finance is the comparison between SCOSTA and biometrics. And that's an easy letter to read and you will get the core of my argument. But through my presentation today, I'm going to present the same argument but in a slightly different fashion.

So, seven numbers, as I said, right? When you go to the UID - if you go to a UIDAI presentation, their numbers are all very big numbers about the millions of Indians that are enrolled and so on. My numbers are all very small. So hopefully, you won't have trouble following.

The first number is zero. Number one is zero. And this is the probability of somebody breaking the central store of passwords on the internet. Why is that probability zero? Because that central store does not exist. There is no central database on the internet where everybody's passwords have been stored.

Now, the second question is: what is the probability that somebody will break into the CIDR?

**Audience member:** Central ID repository?

**Sunil Abraham:** Central ID repository...

**Audience member:** Central Identities Data Repository. That's what CIDR is. It's also the term which has been used in the legislation.

**Sunil Abraham:** In the legislation, and from the beginning. So, what's the probability that somebody will break into that database? Has to be greater than zero. Why? Because such a database exists. So, you use Sherlock Holmes' analysis: if you enter a crime scene and you eliminate everything that is impossible, then whatever remains, however improbable, must be true, you know? So, that is the argument to say I don't need to empirically prove to you, using experimentation, that central databases will leak or will be compromised. I just have to do that theoretically, because that exists.

And the second reason why I believe this is true — and since you are from Livemint, you will find this anecdote a little bit interesting — is that during the birth of the UID project, Cordelia Jenkins was an intern at Livemint, and she called me and said, "So what do you have to say about the first draft of the bill?" And I hadn't seen the first draft of the bill at all, and I said, "Since I haven't seen it, what I can offer to do for you is play the role of a prophet, which is I will predict to you what is going to be in the bill without even reading the bill."

And I said that one of the provisions in the bill will be, "You cannot break into the CIDR," or another provision in the bill will be, "You cannot fool the technology, you cannot try and register a ghost," etc. So, those are all technological possibilities. Because they are technological possibilities, we need language in the law to make that illegal. If they were technological impossibilities — like spitting on the moon is a technological impossibility — then you don't need a provision in the law saying that it is illegal to spit on the moon, right?

So, that's the second data point that I use to demonstrate to you that the UID database will be compromised. If not in my lifetime, at some point it will be compromised. And thankfully, after the bill was enacted into law, several databases leaked. Turkey leaked, Mexico leaked, the Philippines leaked, etc., etc.

So what's the consequence? What happens when the CIDR leaks? What is the price we pay as a nation? People constantly think that biometrics is some kind of state-of-the-art authentication factor to authenticate transactions. They keep comparing biometrics to cryptography. They must be equivalent things. But that's completely untrue. What I would like to say is biometrics is just a fancy word for remote, covert and non-consensual identification technology. So, I'll say that again: remote, covert and non-consensual identification technology.

So, what happened most recently at the Chaos Computer Club is they go to a press conference where the German Chancellor is speaking, they use a high-res camera, and they lift her iris template straight from her eyes, yeah? It was done remotely, so she didn't have to be close to the technology that was harvesting the biometric. It was done covertly; she didn't know that her biometrics was lifted. And most importantly, it was done non-consensually.

So, once this database is in the hands of some international criminal gang, or once this database is in the hands of a foreign state, then that is the purpose that they're going to use the database for. People keep saying, "Oh, this is the universe of what the UIDAI can do, so that is the universe of the harms." No, that's a very silly way of understanding the universe of the harms. The universe of harms is what is technologically possible once you have that data.

So, that is what will happen, and the people that we need to be most concerned about are those that work in the military, and those that work in law enforcement, and those that work in intelligence agencies, because all their covers will be completely blown, because the reverse transaction is as easy to do. As easy as it is to match somebody with an existing biometric, you can match somebody's biometric against the whole database. That is exactly what is happening during the de-duplication process.

So, that is the first number I wanted you to meditate on: zero. And slightly greater than zero, the possibility that somebody can break into this database. And you can see straight away that this technological risk emerges because of the technological choice. If they had gone with smart cards instead, there would be no centralised repository of private keys, you know? And then it would be impossible to do those things — to remotely, covertly and non-consensually identify somebody who is carrying a smart card.

**Audience member:** Just one question.

**Sunil Abraham:** Yes.

**Audience member:** The question of what happens if the database leaks. What precisely is stored in the record? Is the biometric salted and hashed and then stored, or is it just stored as raw data?

**Sunil Abraham:** Yeah, so this was a recent discussion by somebody from the UIDAI on my Facebook page, and he said, "We use cryptography to encrypt all the data," and then he said, "The data is also anonymised and stored," yeah? If those two statements are true, then you won't be able to do the de-duplication operation. So, I asked him straight back on my Facebook page that, "If you claim that is true, then how exactly does it..."

**Audience member:** Anonymised, what?

**Sunil Abraham:** Yeah, but that's what they claimed. Yeah, that's what they claimed.

**Audience member:** But the question is, how is it stored? Is the raw data stored or is it...

**Sunil Abraham:** Both are stored. The high-resolution image is stored, and the biometric template generated from the high-resolution biometric is also stored. Both may be stored in an encrypted fashion, and both may be stored...

**Audience member:** We don't know what is...

**Sunil Abraham:** We know these two things are definitely stored. It's in their official documentation. But what is encrypted, how many keys are used to encrypt it — all of this is not in the public domain.

**Audience member:** It doesn't matter if the raw data is anyway stored.

**Sunil Abraham:** Yeah. So, the next thing is: what is the probability that you can design a poor technology, a broken technological project, and then fix it using the law? And here, I claim that that probability is zero. You cannot fix through the law what you have broken using the technology.

So, a great example of this is Digital Rights Management. Digital Rights Management is trying to protect the rights of a copyright holder using technology. But since the technology is broken, all of us are able to access pirated music and books and movies. Then, in the Digital Millennium Copyright Act, what the government of the US tries to do, they criminalise circumventing the broken technology. So, first of all, the technology is broken. Now you have another law which criminalises the circumvention. But that doesn't stop anything. Both DRM technology and the DMCA have not managed to stop violations of copyright in the US. So, you cannot try to do this patchwork. So, why is...

**Audience member:** Yeah, how easy is it to know that someone has hacked into the database? As in, how would they even come to know unless, you know, certain action is taken pursuant to, like, misuse of someone's biometric information? I mean, can there be a possibility that people are anyway tapping into the database without them coming to know?

**Sunil Abraham:** No, so, the Twitter discourse on this is when people were compromising databases during the time of the first Mission Impossible film, then you needed helicopters and people strung from ceilings with sophisticated gear. Today, most of the database leaks are interns walking out of the office with a drive, right? So, if they couldn't tell at the CIA that Snowden has — or the NSA — that Snowden has disappeared, then you can't tell here also. There are, of course, using cryptographic chains, you could engineer systems, but there is no evidence in the public documentation of the UIDAI that such things exist. What you could do is this number of keys. So, in order to access the encrypted database, like for the root zone key-signing ceremony at ICANN, you have a split-key system. There are six people who have the keys. Only when those six people come together and join their keys will you be able to decrypt. But then you also have to do the other operations, right?

You have to do the de-duplication every day, you have to do the authentication every day, so you can't do that if you are also encrypting the data. To do those things, the data has to be unencrypted, or the six people have to be constantly around. So, the use case interferes with putting secure systems in place.

So, the problem with this second area that we are discussing - so, the first area was just about the security of the central store. The second area is what the UIDAI keeps saying, is that consent is taken care of. Only if you consent will the technology work, and it's baked into the law. And the second thing they say increasingly, especially ever since iSPIRT also got involved with the project, is there's something called the India Stack, and in the India Stack we have a consent layer. And that's a very complex way of mapping what each data subject has consented to and when, and so on.

So, that is what they say. But what I'm saying, thanks to biometrics being remote, covert and non-consensual identification technology, nothing fixes that, no matter what you do with the technology and no matter what you do with the law. Because there's a big difference, in my view, between the government identifying you and you identifying yourself to the government. Who is in control of the process when it happens? So, that is the important thing for us to remember. And then the question is, so what about law enforcement?

So, it is still a standard that is being developed, and it's not fully out there. There's a slideshow available on the iSPIRT website and a couple of other places where you can get it. So, the question of consent in a project such as this has to be asked at several points.

What we know the most about is consent at the point of collection, and at that point what you are ticking on the form is the general consent that the authority can share data with certain key agencies in order to process it, because it's not the authority which is collecting the data; it is an enrolment agency, and then it goes through various steps, etc. So, that is the consent that everybody knows about.

What they are talking about in the next layer of the consent layer is where you can decide who can use your KYC information and for how long. And so they have a very detailed XML schema which says which are all the agencies that you know about, and for each of those agencies, what have you consented to share with them and for how long have you consented to share that with them, and whether, for each occasion when that information is shared with them, you should be notified, and things like that.

So, it's a very comprehensive XML protocol, but what I'm saying is that's almost irrelevant if the technology can authenticate you, if the technology can identify you remotely, covertly and non-consensually.

So, should this technology be prohibited? Should law enforcement and intelligence agencies be prohibited from using all of this? No, no, no. I'm all for — if there are troublemaking students at some university, then for sure, why don't you take your high-resolution cameras and capture all their iris information? That is fine. That is the business of law enforcement and law and order and so on.

But everyday interactions between the citizen and the state — that's a bit repugnant, to have exactly that technology, right? So, for everyday interactions between the citizen and state — the law-abiding nationalistic citizens — then why do we need to have the surveillance technology being used?

Let's have a technology where I'm completely in control, and you cannot authenticate me and you cannot identify me unless I reach into my pocket and pull out my documentation. So then, how do we marry the best of both worlds? Because biometrics also obviously is giving some value.

This is very easy to do. All you have to do is ensure that the enrolment officer collects the biometric, and the enrolment officer then writes the biometric onto the smart card and digitally signs it with his or her private key. So then, that's a very clear way of tying the body to the smart card. And if ever there is a question whether the individual has stolen the smart card, you can always take them to a machine and check whether the biometric on the individual matches the smart card. That's a much smaller match, and it's also a completely decentralised storage of the biometrics.

So, you can still marry various components of the technology. You don't have to give up on biometrics completely.

Number three. The number three is zero again, and this time it is for the utility of biometrics as a password or authentication factor. And this is very simple: whenever you have an authentication factor or password, whether it is digital signatures or PINs, revocability is the key criterion.

**Audience member:** [Unclear question]

**Sunil Abraham:** No, this is a technological critique. There are many other problems with the UID project. I am not the lawyer; you are. So, I am not discussing those questions. This is purely from the perspective of fixing the technology. Once we fix this, then there are several things to do with the law as well. But you can't fix it in the law and leave all the technology like this, is what I am saying. Most other people who are criticising the project are people that are only critiquing the law, yeah? So, I am not in that business at all. I am in the business of criticising the technology, yeah?

**Audience member:** [Unclear question]

**Sunil Abraham:** So, it is just the difference between putting your money into your account and getting stolen from your account, and putting your money into one account with everybody else in Delhi and you losing your money from that account. No, no — decentralisation. The issue is centralisation versus decentralisation.

**Audience member:** [Unclear question]

**Sunil Abraham:** No, no, no. And that is why I don't want biometrics to be used either for identification or authentication. I want digital signatures to be used. I want the state-of-the-art internet technology to be used for both those transactions. Only to tie the card to the human being, biometrics is fine.

**Audience member:** And you are saying this not just in the interaction between the state and individuals, but in any sort of interaction, even between, say, private organisations and individuals, where biometrics is being used?

**Sunil Abraham:** No, I mean, if a private organisation wants to use biometrics, it is their problem, right? I don't think CIS is in the business — or I'm personally in the business — of asking for prohibitions on things. So, we are looking at it as a choice between two competing technologies, and one technology is clearly better than the other. Sorry.

**Audience member:** No, no, I'm just saying, like, for example, when you go — if you want to apply for a visa — when you apply for a visa, even there they take your biometrics. I'm just adding to that point.

**Sunil Abraham:** Yes. So, it is a foreign state that wants to know exactly who you are. It is a surveillance question, and as I said, I am for surveillance, and that is an appropriate use of biometrics because it is a security question. And I will come to that, about the use of biometrics in the visa process.

So, very quickly, why don't we want biometrics as authentication factors? Number one, because biometrics cannot be revoked, cannot be changed. And number two, because biometrics is left everywhere. I am leaving my biometrics everywhere in this room. And number four — number three — very easy to do plausible deniability.

So, one of the texts that I am writing — I still haven't managed to finish it — is a Gandhian critique of the UID project. So, the question is, if you are a right-wing Christian in the US, most probably you will walk around with a T-shirt which says, "What would Jesus do?" But for me, being in India, the more important question is: what would Gandhi do, right?

And when Gandhi was forced under the Asiatic Law in Transvaal, along with other people of Indian origin, to get ID cards, the way Gandhi decided to destroy or resist that project was to burn the ID card. Here, of course, you can't burn your body to resist the UID project, but you can do something equally interesting. I can scan my biometrics — both my iris information and my fingerprint information — put it on the internet, and then I can claim plausible deniability that somebody else took my biometrics, authenticated with the UID database; it wasn't me, you see?

So, therefore, biometrics does not lock us in as tightly as you'd like to think. And therefore, at the border, things happen very differently. So, at the border, it's not just a machine with no supervision. There is an immigration officer. You and the immigration officer are under CCTV surveillance.

So, anyhow, if that is going to be the thing that you need — if you're going to have another layer of surveillance through CCTV required — then you might as well use the smart card. What is the advantage that the biometrics is giving to you? If there is no surveillance objective, if the objective is purely service delivery, then you might as well shift to smart cards. So then you're on a global standard, like all of the —

**Audience member:** Can you explain the smart card a little bit more? I'm a little unsure.

**Sunil Abraham:** So, it is just like cryptography on the internet. On both sides of the transaction are a key pair — private key and public key — and all that smart cards do is they allow you to store your key pair on your card. And the other advantage of smart cards is they allow you a writable partition. So, the Thai smart card, for example, allows you to store your hospital records and things like that. Your vehicle details all get stored onto your smart card. So, it's also useful in another way, which I shall come to.

**Audience member:** So, sorry, just to clarify, you're essentially saying that every citizen will have his or her — just trying to understand this — every citizen will have his or her smart card, and then that will be used for authentication whenever the citizen is interfacing with some state?

**Sunil Abraham:** I'll come to the complexity of my vision, because again, if we have only one smart card, it feels like a single point of failure. And I will give you a market reason why we don't want that, and why it would be much more resilient for a society — especially a society where we want markets to work — for us to have a much more complex mechanism here.

So, yeah, I'll move on.

The next thing to talk about is the use of biometrics as an identification technology. Yes. So, I finished discussing biometrics as authentication. Now I move to biometrics as identification.

And according to the UIDAI, the false positive identification rate is 0.057, which according to them means only 570 resident enrolments will be falsely identified as duplicates when one million people are enrolled. Okay, that's a completely wrong way of understanding probability, because the way to work that figure is using conditional probability, because the database is constantly getting bigger and bigger and bigger, right?

So, a colleague of mine, a distinguished fellow at our centre, Dr Hans Varghese Mathews, developed a model for this conditional probability, and we have an article which has been accepted after peer review in the EPW. And in this article, we make the claim that one out of 146 people will be falsely rejected when they try to enrol once the enrolment figure reaches one billion.

And in the counter-affidavit that was filed by the UIDAI in the court case, their figures for falsely rejected data are roughly the same. It's within the same ballpark.

So, what they did in their rebuttal, which was also published in the EPW, the UIDAI claimed that we were assuming that the curve would be linear. But if you read Dr Mathews' paper carefully, there is no such assumption in the paper. And what is very strange is, in their biometrics report, they have made the assumption that the curve will be linear.

So, we have done the conditional probability modelling without using the assumption of a linear curve. But what is more interesting for me is the second part of their explanation. They say, "Let's assume he's right, and let's avoid getting far too deep into the mathematics. Let us instead explain to you how we deal with it once this problem shows up."

So, we have a manual adjudication process, they claim, to rectify biometric errors. This manual adjudication process basically determines whether you exist. What is the question that is being answered in the manual adjudication process? Do you exist uniquely as a resident or not?

And this process happens completely without any of the elements of natural justice, which is: you're the affected party, but there will be no notice. You will never be told that we're going to decide this, and you will never be given an opportunity to be heard. You will never know who participated in this adjudication process, and if you are unhappy with it, there is no way for you to appeal that decision also. So, this is the problem, which I shall connect to the next thing that I'd like to say, which is —

**Audience member:** Just on the paper, I think you're making two claims.

**Sunil Abraham:** Yeah.

**Audience member:** One is that, you know, one by 146 is too huge a number, given the magnitude of the population —

**Sunil Abraham:** Yes.

**Audience member:** And the other is that there is no natural justice involved in —

**Sunil Abraham:** Not just natural justice. More importantly, there is no skin in the game, right? There's nobody to punish if something goes wrong. So, an ideal identity management system should have human skin in the game.

That is, if there are ghosts, there should be somebody to go after for those ghosts. If all answers are going to be, "Oh, there was some problem with the technology," or, "The technology is to blame," then there are no incentives or punitive measures in place to prevent ghosts from being introduced into the system.

Because this manual adjudication is very easy to beat. All the UID enrolment technology — the connectivity between the laptop and the biometric devices — is all through USB cables. USB is an unauthenticated protocol. It's very easy to buy a USB interceptor for 5,000 rupees on Alibaba. Once you do that, you can download software which is called Synthetic Fingerprint Generator, and you can generate any amount of biometric information and pass it down the pipe into the enrolment software.

And that data will be encrypted and sent to the UIDAI, and once it reaches them, there is nothing which they have on the database, either in the manual mode or in the automatic mode, that will help them determine that this is a ghost. Yeah. So, when we leave these important questions for machines to answer, unless there is a human being also willing to put their name against that decision, it is a very fragile — I'm channelling Nassim Nicholas Taleb here — we're building a very fragile ecosystem, because there's nobody to blame when things go wrong.

**Audience member:** I think their response to that paper focused on — like you said — did not really focus on the second part.

**Sunil Abraham:** Yeah.

**Audience member:** About what is the process that a human being —

**Sunil Abraham:** We only focused on the first part.

**Audience member:** Challenging the mathematics?

**Sunil Abraham:** Yes. No, very little, very little challenge to the mathematics. They finally say, "Let's assume that his numbers are correct." If they were really challenging our mathematics, they should have offered the numbers. What is it in their model that this number would be? Because that first number is completely wrong — saying if you have an FPIR of 0.057, that only 570 residents will be rejected. That's completely wrong, because that's not taking the second million into consideration.

**Audience member:** Because you are saying about one by 145?

**Sunil Abraham:** Yeah, yeah.

**Audience member:** Right. So, if you do that number, what they are saying is they have about one million registrations a day, let's say.

**Sunil Abraham:** Yeah.

**Audience member:** Then that will come to some 7,000 duplicates.

**Sunil Abraham:** Seven thousand —

**Audience member:** By 145.

**Sunil Abraham:** Okay. Oh, yeah, yeah, yeah, yeah.

**Audience member:** Then what they are saying is that it's not entirely manual. About 90% is automated. You consider factors like gender, age, etc., and use that to eliminate 90%. The remaining 10%, they are saying, is manual, and there is a process.

**Sunil Abraham:** But what I'm saying is that if I use technological sophistication to introduce a ghost, both those processes cannot catch it. If I have a technically competent — so, where is the market for this? People have benami accounts, and all the bank managers and the people that have the benami accounts are not going to roll over and say, "Okay, thanks to this new technology, we're going to let ourselves be identified and all our benami accounts are going to get connected." There's going to be an actor who will enter the market and say, "I will create ghost IDs for you."

Yeah, there are some high-value transactions that need to be protected. At that point, once that technology is available, there's no way the UID can catch that if you have a compromised enrolment agent. At the moment, to become an enrolment agent in Rajasthan, all you have to do is go to a website and answer a questionnaire as an e-Mitra, then you're an enrolment agent. The UID has never even seen you.

**Audience member:** No, the question of creating false, non-existent people and enrolling them is different from the issue of whether a person who is trying to enrol himself is —

**Sunil Abraham:** Yeah, yeah. No, those are two distinct — yeah, those are — you're right, you're right.

**Audience member:** So, the issue that you pointed out in that paper —

**Sunil Abraham:** Yeah.

**Audience member:** — is only about whether a person who is trying to enrol himself —

**Sunil Abraham:** Yes. True, true, true. That's what I'm — true. And we have now — yeah, we have a counter-rebuttal to the rebuttal, but unfortunately EPW has not published it yet. But if anybody in this room would like to see our response to their response, we can share that. Again, mathematically, we try and answer the question completely.

Okay. Now we'll move on to the next number, which is near zero again, and this is the number for surveillance.

So, many people think that people who research privacy, such as myself, are anti-surveillance. No, we are pro-surveillance, as I said in the beginning. We believe that surveillance, at least gastronomically understood, should be treated like salt in cooking: essential in tiny quantities, but counterproductive even if slightly in excess.

So, let me try and explain to you how it'll look on a chart. Suppose we had the horizontal axis for the percentage of the population under surveillance, and then the vertical axis is the amount of security in the nation-state, and we'll draw two lines: one for Canada and one for India.

So, even before we start doing any surveillance, security in India is already at some level. And then, as you bring a small percentage of the population under surveillance — say we bring 5% of the population under surveillance — because of that surveillance, you will get a security benefit, so security will increase.

And after that, because you're doing unnecessary surveillance and you're creating a big database of all the surveillance data, you're creating a honeypot. You're actually creating a security threat, and therefore, as you reach 100% of the population, the security threat also increases dramatically. So, it's an inverse hockey stick on the chart that I've just drawn for you.

And the Canadian head of the hockey stick is going to be smaller than the Indian head of the hockey stick, because Canada's terrorists, the last time they managed to bomb Canada, managed to kill two or three people. In India, we are the third most bombed country on the planet, and therefore we might need a much larger percentage of the population under surveillance.

Gastronomically speaking, you could understand that we are a bit in a pickle, yeah? So, the question then is, if the government is going to spend tax money on surveillance, then as a citizen I want a high return on my surveillance rupee, yeah? And therefore, I want surveillance to have a connection to power.

As Julian Assange has said, transparency requirements should be directly proportionate to power. And I have added an addendum, which is: privacy protection must be inversely proportionate to power. So, that is the ideal way in which the public interest question is handled in both transparency law and in privacy law.

In transparency law, under one of the 12 exceptions to the RTI, privacy is one such exception. But to the privacy exception, there is another exception, which is the public interest exception. That is the state of the transparency law. And then, in most privacy law, there will be a public interest exception. If violating your right will result in serving the public interest, then that is acceptable.

And where is there greatest public interest? Always when you try to tackle power. So, that is why we have this very easy equation for you to remember.

So, therefore, I would want all the netas and babus — all the bureaucrats and politicians — to be given UID numbers first, and smart cards. And then, as the subsidy travels from New Delhi to the village, what I want is a non-repudiable audit trail as subsidy moves from table to table.

And then, at the lowest level, we still need surveillance, but why use expensive biometric surveillance at the lowest level? Let's just have Excel spreadsheets with the names of all the beneficiaries, and let's put that on data.gov.in and also post it on the village notice boards. And whenever anybody would like to verify whether there are ghosts, whether ghosts have been eliminated, whether deserving recipients of welfare have not been removed from the database, all of that can be independently confirmed, because you will have public databases of who is getting what kind of subsidy.

And then the rest of the supply chain from Delhi to the village will be sealed, because there is a very high degree of accountability. This, in my view, tackles wholesale fraud at the top of the pyramid. But the design assumption at the UIDAI is somehow that the bottom of the pyramid is responsible for all the fraud, and that's where all the focus is at the moment. And even if we tackle small-ticket fraud, or retail fraud, at the bottom of the pyramid, I don't think that is good value for my surveillance rupee. So, that is my next point — point number five.

**Audience member:** No. So, what you're suggesting is not unlike the present system followed for LPG — their transparency portals, at least at the bottom level.

**Sunil Abraham:** At the bottom level, yes.

**Audience member:** Where everybody's sort of transactions are up there. You're proposing increasing or broadening the pyramid level of —

**Sunil Abraham:** Yes. Again, using cryptography. You don't have to use blockchain; just a standard, publicly signed audit trail would be sufficient.

**Audience member:** Where is the privacy here?

**Sunil Abraham:** Sorry?

**Audience member:** Where is the privacy here? You're putting everything open. I mean, all the data is —

**Sunil Abraham:** I didn't say that I was going to advocate for privacy, right? I said I was going to offer a better technological solution to handle the primary goal, which was corruption. The Supreme Court itself has said, "People are hungry and you're thinking of privacy," right? So, when the Supreme Court, in its wisdom, has made that statement, I have to assume that anybody getting services from the welfare state, subsidy from the welfare state, has to sacrifice some degree of privacy.

So, I'm sorry if my presentation is a bit of a surprise. You invited me thinking I was a privacy advocate, but I'm actually mounting a technological critique of the project.

**Audience member:** [Unclear question]

**Sunil Abraham:** Okay, so the job there will be completely manual. I will have to go database by database and build the profile of the individual. The database at the CIDR that the UIDAI does not talk about a lot, and has a single mention in the Act, is the transaction database. The transaction database will finally hold your transactions against 22 databases. And from a single point, I will get a 360-degree view of you.

If I get a CSV, I can only audit that particular programme. From that CSV, it is very difficult for me to build a 360-degree view of you. So, I'm breaking the data into its constituent bits where it is useful. So, it still is better than what you're getting with the UIDAI.

With smart cards, the complete authentication infrastructure is decentralised. There will be no centralised record of the authentication. So, at the transaction level, you won't know who took what, when, and all of these things. You'll just know whether this person, in the disclosure, is eligible or not. Surely, eligibility lists can be cleaned up with that amount of infringement of your privacy.

So, there is going to be infringement of privacy as we move into greater state databases. My solution offers slightly less infringement than the main solution, but still there will be infringement. That is impossible to eliminate, or we have to say that subsidy has to be given anonymously. I don't want to say that. Many of my colleagues from civil society say that, but we don't believe that would be a good solution.

**Sunil Abraham:** Sir, you had a question, sir?

**Audience member:** No, most of the money is being proposed to be routed to the bottom of the pyramid.

**Sunil Abraham:** Yes.

**Audience member:** So, that's a reason for larger requirements.

**Sunil Abraham:** Yes. What I heard from Vijay Aditya from Ekgaon Technologies is some banks in the areas that he's visited are collecting UID numbers from certain sources, creating bank accounts and collecting the direct cash transfer, and those UID holders don't even know that they have an account in that bank, etc.

So, if you don't watch the whole chain, there's a very high chance that things can be easily... So, I don't want to be naive. What I want to say is, with every generation of corruption, we will need another generation of corruption-busting technology. Once we have that corruption-busting technology, corruption will evolve. Then we'll also have to evolve. So, it's not a single victory.

**Audience member:** Just one thing. I mean, even let's say somebody could gather smart cards of 100 people —

**Sunil Abraham:** Yes.

**Audience member:** — and use those smart cards also in the same fashion. I mean, in terms of, let's say —

**Sunil Abraham:** But once it is detected and blocked, then it's difficult to do it again. With this, once you do it, you can always do it. There's no point of saying that that smart card is no longer valid.

**Audience member:** Yeah, smart cards can be blocked, that I understand. But I'm just saying that you mentioned about this particular banking — 100 people's IDs and creating these ghost, not people, but ghost accounts in —

**Sunil Abraham:** Okay. Now, same way —

**Audience member:** Yeah.

**Sunil Abraham:** So, again, Deepak, my emphasis is the chain from Delhi —

**Audience member:** Okay.

**Sunil Abraham:** — the chain from Delhi to the bank manager. If I had a cryptographic record of that publicly, then later we get people into trouble. At the moment, your only control is at the last level. That's insufficient.

Then there's nobody to blame. There's nobody to sack. There's nobody to arrest, and so on. Anyway, I'll quickly go through — I'm already fully out of time. The next one is the market argument.

Sorry, no. The next one is technoutopianism, and the number is both one and zero, to represent the modern binary age. What I basically say is, in India we've lost faith in the old gods, and therefore science and technology are the new gods. And Shekhar Gupta on Twitter said, "Left libertarians detest science and technology, and that is why they are protesting against the UID project." That was Shekhar Gupta's argument.

So, in my view, people like Shekhar Gupta are technoutopians, and they have certain articles of faith. And the articles of faith are a little bit like this. Number one, new technology is better than old technology. Number two, expensive technology is better than cheap technology. Number three, complex technology is better than simple technology. And number four, all technology is empowering, or at the very least neutral. Those are their articles of faith — people who believe in technology as ideology.

And in order to help you understand this, I'll use a very simple example. I was also a member, fortunately, of the Human DNA Profiling Bill Committee in 2015. The Department of Biotechnology invited me onto that committee. When I first read the draft version of the Bill, the introduction of the Bill said, "DNA technology is powerful technology which makes it possible to determine whether the source of origin of one body substance is identical to another without any doubt." That's what the preface of the Bill said, and this is what many other scientists have said in the media as well.

So, let's compare two technologies: photography and DNA — both biometric technologies. During one of the committee meetings, one of the scientists was explaining to me the protocol for generating a DNA profile. He said that immediately after the lab technician has generated the profile, the first step of standard hygiene is to compare the profile that has been generated by the machine to the lab technician's profile. Why? Because in the process of loading the machine, some of the lab technician's DNA could have contaminated the sample.

So, therefore, it's more fragile, more complex, more sophisticated technology — but more fragile technology. The same mistake is very unlikely to happen in the darkroom of photography. If you have taken a photograph of a person, by the time you get to your darkroom, it's highly unlikely that your image will be equally exposed as the first image that you took. Much more primitive technology, less expensive and so on, but also quite robust in its own way.

And therefore, we can also use another example. To make a fake smart card, which is the older technology, you need a lot of equipment. To make a fake gummy finger, you just need Fevicol and wax — a candle. If you have access to a candle and you have access to Fevicol, you can make a gummy finger which can be used to defeat a biometric reader.

So, just because you're using modern technology doesn't mean the attempt to defeat it is going to be that much more complicated. Each technology has to be evaluated for its fitness of purpose. So, I'm not saying that DNA technology should not be used, but when we use it, we have to design provisions in the law so we can handle these types of human fallibility. What if one of the labs had been bribed, and so on?

So, you take multiple versions of the sample and you send them to multiple labs, like a double-blind review in the scientific process. If both labs confirm exactly the same thing, then you know you've got it right. You could even have a dud sample in it to check whether the labs are actually doing their job, and so on. So, there are scientific ways of making the law work for you and making the technology work for you.

Number seven — again, riffing off what Shekhar Gupta said about left libertarians — I would have thought that what is being proposed is completely a communist plot, right? There's going to be a monopoly by the UIDAI on providing identification and authentication services. This body is going to charge for it. There is going to be a consumer-service provider relationship between the citizen and the state.

Shouldn't it have been like the IT Act? In the IT Act, we have a certificate authority — there is a whole ecosystem of — sorry, we have the regulator of certificate authorities, the Controller of Certifying Authorities. Then we have an ecosystem of certificate authorities, and multiple people can vouch for a particular domain name and provide a certificate for a domain name.

Similarly, if the Bill had actually opened out a competitive marketplace for identity providers and authentication providers, then each company could have chosen its own technology. If some persons were really convinced that biometrics is the best thing, their identification could be based on biometrics, and some other people could provide some other technology. That would have been a much more robust system, and then various actors in the marketplace could be punished and incentivised for ghosts, etc.

Today, if we find out that there are a crore ghosts in the system, we still have to live with the UIDAI. How are we going to have a punitive measure? How are we going to ensure that the market punishes the UIDAI for what it does, and so on?

So, those are my broad arguments. The full paper is available online. It's an article that I wrote for Frontline, which nobody reads, I think, these days. So, it's called "The Surveillance Project". That was not what I called it. I called it "The Numbers of Security: The UID Case File". That was my original name, but the Frontline team decided to call it "The Surveillance Project".

And the other thing that I can offer is our rebuttal from Dr Matthews, and then our open letters are also available on the website. So, thank you, and I'm really sorry for exhausting all the time in my presentation.

</div>

## On Social Media {#social-media}

Sunil posted this video on 𝕏 (then known as Twitter) on 17 October 2016 with the note: "Dear #FriendWithoutAadhaar — If you have an hour to waste. Please watch this:" The post has remained pinned to his profile since then, as the debate around Aadhaar continues to be relevant and important.

<div class="aadhaar-social-card">
  <div class="aadhaar-social-date">17 October 2016</div>
  <div class="aadhaar-tweet-center">
    <blockquote class="twitter-tweet" data-theme="light">
      <p lang="en" dir="ltr">
        Dear <a href="https://twitter.com/hashtag/FriendWithoutAadhaar?src=hash&amp;ref_src=twsrc%5Etfw">#FriendWithoutAadhaar</a> - If you have an hour to waste. Please watch this:
      </p>
      &mdash; Sunil Abraham (@sunil_abraham)
      <a href="https://twitter.com/sunil_abraham/status/788018356209197058?ref_src=twsrc%5Etfw">October 17, 2016</a>
    </blockquote>
  </div>
</div>

{% include sunilspeaks.html %}

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<style>
  /* Aadhaar Video */
.aadhaar-video {
  max-width: 700px;
  margin: 2rem auto;
  background: #f8fafc;
  border: 1px solid #d7dee8;
  border-radius: 10px;
  overflow: hidden;
}

.aadhaar-video__embed {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  background: #000;
}

.aadhaar-video__embed iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.aadhaar-video__details {
  padding: 1.25rem 1.5rem;
  color: #222;
}

.aadhaar-video__details p {
  margin: 0 0 0.75rem;
}

.aadhaar-video__details p:last-child {
  margin-bottom: 0;
}

body.tsap-dark-mode .aadhaar-video {
  background: #1e293b !important;
  border-color: #475569 !important;
}

body.tsap-dark-mode .aadhaar-video__details {
  color: #e2e8f0 !important;
}

body.tsap-dark-mode .aadhaar-video__details strong {
  color: #f8fafc !important;
}


  /* Aadhaar - Social Media */
.aadhaar-social-card {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  background: #f8fafc;
  border: 1px solid #d7dee8;
  border-radius: 10px;
}

.aadhaar-social-date {
  margin-bottom: 1rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid #d7dee8;
  color: #334155;
  font-size: 0.85rem;
  font-weight: 600;
}

.aadhaar-tweet-center {
  display: flex;
  justify-content: center;
}

.aadhaar-tweet-center .twitter-tweet {
  width: 100% !important;
  max-width: 550px !important;
  margin: 0 !important;
}

@media (max-width: 768px) {
  .aadhaar-social-card {
    margin: 1.5rem 0;
    padding: 1rem;
  }
}

body.tsap-dark-mode .aadhaar-social-card {
  background: #1e293b !important;
  border-color: #475569 !important;
}

body.tsap-dark-mode .aadhaar-social-date {
  color: #e2e8f0 !important;
  border-bottom-color: #475569 !important;
}

body.tsap-dark-mode .aadhaar-social-card blockquote.twitter-tweet {
  color: #e2e8f0 !important;
  background: transparent !important;
}

body.tsap-dark-mode .aadhaar-social-card blockquote.twitter-tweet a {
  color: #7dd3fc !important;
}

  .transcript-text {
  margin: 1.5rem 0;
  padding: 1.25rem;
  border: 1px solid var(--border-color, #d0d7de);
  border-left: 4px solid #1f5fbf;
  border-radius: 0.5rem;
  background: transparent;
}

body.tsap-dark-mode .transcript-text {
  border-color: #475569;
  border-left-color: #60a5fa;
}
</style>
