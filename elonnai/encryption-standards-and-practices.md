---
layout: default
title: "Encryption Standards and Practices"
description: "A 2011 CIS blog post by Elonnai Hickok examining encryption practices in India, regulatory inconsistencies, and the relationship between encryption, data security, privacy, and national security."
authors: ["Elonnai Hickok"]
categories: [Elonnai Hickok]
date: 2011-04-05
source: "Centre for Internet and Society"
permalink: /elonnai/encryption-standards-and-practices/
created: 2026-08-09
---

**"Encryption Standards and Practices"** is a blog post by [Elonnai Hickok](/elonnai/) published by the [Centre for Internet and Society](/cis/) on 5 April 2011. It surveys fundamental cryptographic techniques—including symmetric, asymmetric, hash functions, and message authentication codes—and contrasts them with India's outdated official encryption limits. The article examines how conflicting sectoral guidelines in banking, trade, and e-governance create market uncertainty and security vulnerabilities, while outlining the complex triadic relationship between citizens, market actors, and the state regarding surveillance and data protection.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published by:</dt>
  <dd><em>Centre for Internet and Society</em></dd>

  <dt>📅 Date:</dt>
  <dd>5 April 2011</dd>

  <dt>✍️ Author:</dt>
  <dd>Elonnai Hickok</dd>

  <dt>📄 Type:</dt>
  <dd>Blog post</dd>

  <dt>🔗 Original Link:</dt>
  <dd>
    <a href="https://cis-india.org/internet-governance/blog/privacy/privacy_encryption">Read the original post</a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>The below note looks at different types of encryption, varying practices of encryption in India, and the relationship between encryption, data security, and national security.</p>

<hr class="article-separator">

<h3>Introduction: Different Types of Encryption</h3>

<p>When looking at the informational side of privacy, encryption is an important component to understand. Encryption in itself is a useful tool for protecting data that is highly personal in nature and is being stored, used in a transaction, or shared across multiple databases. The quality of encryption is judged by the ability to prevent an outside party from determining the original content of an encrypted message. There are many different types of encryption including:</p>

<ul>
<li><strong>Symmetric Key Encryption:</strong> Communicating parties share the same private key that is used to encrypt and decrypt the data. This form of encryption is the most basic, and is fast and effective, but there have been problems in the secure exchange of the unique keys between communicating parties over networks<sup id="ref-1"><a href="#note-1">1</a></sup>.</li>
<li><strong>Asymmetric Key Encryption:</strong> This system relies on the use of two keys – one public, and one private. In this system only the user knows the private key. In order to ensure security in the system a mathematical algorithm that is easy to calculate in one direction, but nearly impossible to reverse calculate is often used. Use of a public and a private key asymmetric avoids the problem of secure exchange that is experienced by symmetric key encryption. The basis of the two keys should be so different, that it is possible to publicize one without the danger of being able to derive the original data. Decoding of data takes place in a two step process. The first step is to decrypt the symmetric key using the private key. The second step is to decode the data using the symmetric key and interpret the actual data<sup id="ref-2"><a href="#note-2">2</a></sup>.</li>
<li><strong>One-way Hash Functions:</strong> One-way hash functions are mathematical algorithms that transform an input message into a message of fixed length. The key to the security of hash functions is that the inverse of the hash function must be impossible to prove<sup id="ref-3"><a href="#note-3">3</a></sup>.</li>
<li><strong>Message Authentication Codes:</strong> MACs are data blocks appended to messages to protect the authentication and integrity of messages. MACs typically depend on the use of one-way hash functions<sup id="ref-4"><a href="#note-4">4</a></sup>.</li>
<li><strong>Random Number Generators:</strong> An unpredictable sequence of numbers that is produced by a mathematical algorithm<sup id="ref-5"><a href="#note-5">5</a></sup>.</li>
</ul>

<h3>Encryption in India</h3>

<p>Encryption in India is a hotly debated and very confusing subject. The government has issued one standard, but individuals and organizations follow completely different standards. According to a note issued by the Department of Telecommunications ("DOT") in 2007, the use of bulk encryption is not permitted by Licensees, but nevertheless Licensees are still responsible for the privacy of consumers' data (section 32.1). The same note pointed out that encryption up to 40 bit key length in the symmetric key algorithms is permitted, but any encryption higher than this may be used only with the written permission of the Licensor. Furthermore, if higher encryption is used, the decryption key must be split into two parts and deposited with the Licensor. The 40 bit key standard was previously established in 2002 in a note submitted by the DOT:"License Agreement for Provision of Internet Service (including Internet Telephony)' issued by Department of Telecommunications"<sup id="ref-6"><a href="#note-6">6</a></sup> Though a 40 bit standard has been established, there are many sectors that do not adhere to this rule. Below are a few sectoral examples:</p>

<ul>
<li><strong>A) Banking:</strong> 'Report on Internet Banking' by the Reserve Bank of India 22 June 2001:<br>
"All transactions must be authenticated using a user ID and password. SSL/128 bit encryption must be used as the minimum level of security. As and when the regulatory framework is in place, all such transactions should be digitally certified by one of the licensed Certification Authorities."<sup id="ref-7"><a href="#note-7">7</a></sup></li>
<li><strong>B) Trade:</strong> The following advanced security products are advisable:<br>
"Microprocessor based SMART cards, Dynamic Password (Secure ID Tokens), 64 bit/128 bit encryption"<sup id="ref-8"><a href="#note-8">8</a></sup></li>
<li><strong>C) Trains:</strong> 'Terms & Conditions' for online Railway Booking 2010:<br>
"Credit card details will travel on the Internet in a fully encrypted (128 bit, browser independent encryption) form. To ensure security, your card details are NOT stored in our Website."<sup id="ref-9"><a href="#note-9">9</a></sup></li>
</ul>

<p>The varying level of standards poses a serious obstacle to Indian business, as foreign countries do not trust that their data will be secure in India. Also, the differing standards will pose a compliance problem for Indian businesses attempting to launch their services on the cloud.</p>

<h3>Data Security, Encryption, and Privacy:</h3>

<p>To understand how encryption relates to privacy, it is important to begin by looking at data security vs. privacy. Security and privacy have an interesting relationship, because they go hand in hand, and yet at the same time they are opposed to each other. First, data security and privacy are not the same. Breaches in data security occur when information is accessed without authorization. There is no loss of privacy, however, until that information is misused. Though data security is critical for protecting privacy, the principles of data security call for practices that threaten privacy principles. For example, data security focuses on data retention, logging, etc, while privacy focuses on the consent, restricted access to data, limited data retention, and anonymity<sup id="ref-10"><a href="#note-10">10</a></sup>. If security measures are carried out without privacy interests in mind, surveillance can easily result in severe privacy violations. Thus, data security should influence and support a privacy regime but not drive it. In this context, encryption and data security will create an expectation of privacy, rather than undermine or overshadow privacy. By the same token encryption cannot be seen as the cure for privacy challenges. Encryption cannot adequately protect data, but when supported by a strong privacy and security regime - it can be very effective. It is also a good measuring rod for determining how committed a company has been to protecting a person's privacy and ensuring the security of his or her data. In light of the symbiotic yet complicated relationship that privacy and data security have with each other, it would make sense for legislation and domestic encryption standards to be merged and addressed together. This would ensure that a) the standard is not archaic (as the current 40 bit one is); b) would take into account the threat to privacy that surveillance can impose and would address decryption when addressing encryption; and c) would anticipate the collection and cataloging of data and ensure security of the data and person as well as national security.</p>

<h3>National Security and Encryption</h3>

<p>Encryption is a subject that causes governments a great deal of concern. For example in order to preserve foreign policy and in national security interests, the US maintains export controls on encryption items<sup id="ref-11"><a href="#note-11">11</a></sup>. This means that a license is required to export or re-export identified items. Though the Indian government currently does not have an analogous system, it would be prudent to consider one. Though the government is aware of the connection between encryption and national security, it seems to be addressing it by setting a low standard for the public which enables it to monitor communications etc. easily. It is important to remember though that today we live in a digital age where there are no boundaries. One cannot encrypt data at 40 bits in India and think it is safe, because that encryption can be broken everywhere else in the world. Despite the fact that there are no boundaries in the digital age, users of the internet and communication technologies are subject to different and potentially inconsistent regulatory and self-regulatory data security frameworks and consequently different encryption standards. One way to overcome this problem could be to set in fact a global standard for encryption that would be maximal for the prevention of data leaks. For instance, there are existing algorithms that are royalty free and available to the global public such as the Advanced Encryption Standard algorithm, which is available worldwide. The public disclosure and analysis of the algorithm bolsters the likelihood that it is genuinely secure, and its widespread use will lead to the expedited discovery of vulnerabilities and accelerated efforts to resolve potential weaknesses. Another concern that standardized encryption levels would resolve is the problem of differing export standards and export controls. As seen by the example of the US, industrialized nations often restrict the export of encryption algorithms that are of such strength that they are considered "dual use" - in other words, algorithms that are strong enough to be used for military as well as commercial purposes. Some countries require that the keys be shared, while others take a hands-off approach. In India joining a global standard or creating a national standard of maximum strength would work to address the current issue of inconsistencies among the required encryption levels.</p>

<h3>The Relationship between the Market, the Individual, the State, and Encryption</h3>

<p>Moving away from the technical language it is useful to break down encryption from a social science point of view. Who are the actors involved - what is their relationship with each other, and how does encryption come into the picture. When one looks at encryption it is possible to conceive of many different scenarios, each with different players. In the first scenario there is an individual and another individual. They are sending information back and forth. The third individual could be an entity, a business, or just another individual. The first two individuals want to keep their information away from this third, unknown person or entity. For that reason, the first two encrypt their communications. Encryption is a tool that has the ability to re-draw the lines between the public and private sphere by giving individuals the ability to form a very private line of communication, and thus a very private relationship in a space that is very non-private - such as the internet. In another scenario between the individuals and the markets - the market wants information about an individual to enhance its effectiveness and profits. To create trust, the market promises that information given is encrypted. Thus, the market is attempting to initiate a trusting relationship with individuals. This relationship though, is forced and false, because individuals must compromise how much information they disclose for a product or service in return.</p>

<p>In the second scenario, there is an individual, another individual, and a Government. In this situation the two individuals again say that they want to have a private conversation in a public space, and so it is encrypted, but the Government - which is worried about national security decides that it wants to listen in on the conversation. This places a new dynamic on the relationship. No longer are the two individuals private. Not only can the government hear their conversation, but they have no choice over whether their conversation is heard or not. This is a relationship based off of the premises of distrust between the government and individuals. It presupposes, and is biased in assuming, that if you have done nothing wrong - you have nothing to hide. Using the same set of actors, perhaps a government requires the collection of information about its citizenry that is sensitive. To ensure the privacy of its people, the government encrypts the information, but the individual has essentially lost control over his/her information. He/she is forced to trust that the Government will not misuse the information given.</p>

<p>In the third scenario there is a market, an individual, and the government. The market gathers information about an individual on transactional levels, but encrypts it - because in the wrong hands this information could be misused. The government still wants access to the information and so they demand the information. What does the market say? Does it side with the individual or the Government? If governments sanction the market, they can make it bend to their will. Thus, the government is in a position to control the market and the individual, but to what ends and for what means. In all of these situations the understood role of the market, the government, and the individual has been shifted by the ability to encrypt information. The idea of using encryption as a means to keep information safe speaks to a new relationship that has formed between the government, the market, and the individual.</p>

<h3>Bibliography</h3>

<ol class="references-list">
<li id="note-1">
Burke, Jerome; McDonald, John. <em>Architectural Support for Fast Symmetric-Key Cryptography</em>.
<a href="#ref-1" aria-label="Return to reference 1">↩</a>
</li>

<li id="note-2">
Munro, Paul. <em>Public Key Encryption</em>. University of Pittsburgh, 2004.
<a href="#ref-2" aria-label="Return to reference 2">↩</a>
</li>

<li id="note-3">
Merkle, Ralph. <em>One Way Hash Functions and DES</em>.
<a href="#ref-3" aria-label="Return to reference 3">↩</a>
</li>

<li id="note-4">
Department of Commerce. <a href="http://csrc.nist.gov/publications/fips/fips198/fips-198a.pdf">Federal Information Processing Standards Publication: The Keyed-Hash Message Authentication Code</a>.
<a href="#ref-4" aria-label="Return to reference 4">↩</a>
</li>

<li id="note-5">
<a href="http://www.ruskwig.com/random_encryption.htm">Ruskwig: Random Encryption Techniques</a>.
<a href="#ref-5" aria-label="Return to reference 5">↩</a>
</li>

<li id="note-6">
Department of Telecommunications. <a href="http://www.indentvoice.com/other/ISPLicense.pdf">License Agreement for Provision of Internet Service (including Internet Telephony)</a>.
<a href="#ref-6" aria-label="Return to reference 6">↩</a>
</li>

<li id="note-7">
Reserve Bank of India. <em>Report on Internet Banking</em>, 22 June 2001.
<a href="#ref-7" aria-label="Return to reference 7">↩</a>
</li>

<li id="note-8">
Securities & Exchange Board of India. <em>Internet Trading Guidelines</em>, 31 January 2000.
<a href="#ref-8" aria-label="Return to reference 8">↩</a>
</li>

<li id="note-9">
Indian Railway Catering and Tourism Corporation (IRCTC). <em>Terms & Conditions for Online Railway Booking</em>, 2010.
<a href="#ref-9" aria-label="Return to reference 9">↩</a>
</li>

<li id="note-10">
American Bar Association. <em>International Guide to Privacy</em>.
<a href="#ref-10" aria-label="Return to reference 10">↩</a>
</li>

<li id="note-11">
Department of Commerce: Bureau of Industry and Security. <em>Encryption Export Controls</em>, 25 June 2010.
<a href="#ref-11" aria-label="Return to reference 11">↩</a>
</li>
</ol>

</div>

{% include back-to-top.html %}

## Context and Background

In early 2011, the legal framework governing cryptographic practices in India was characterized by deep regulatory fragmentation. While official Department of Telecommunications (DoT) telecom licence conditions permitted symmetric encryption up to 40-bit key lengths without written permission and required higher encryption keys to be deposited with the Licensor in split form, sectoral standards and practices called for stronger security. The Reserve Bank of India (RBI) specified 128-bit SSL encryption as the minimum level for internet banking, while Securities and Exchange Board of India (SEBI) guidelines described smart cards, dynamic password tokens, and 64-bit/128-bit encryption as advisable. IRCTC's 2010 online railway booking terms stated that credit card details would travel in 128-bit encrypted form. This disconnect created administrative friction for domestic firms, exposed digital infrastructure to international cybersecurity vulnerabilities, and raised compliance hurdles for emerging cloud services.

The post emphasizes the structural distinction between data security and privacy. While data security focuses on technical safeguards like access logging and retention to prevent unauthorized intrusions, privacy centres on consent, purpose limitation, and user autonomy. Relying purely on security measures without privacy-by-design principles risks facilitating pervasive state monitoring, as security tools can easily turn into surveillance mechanisms. Consequently, the essay argues for a unified regulatory policy that updates cryptographic limits while also addressing the privacy implications of surveillance and decryption.

From an international perspective, the analysis discusses the use of standardised, royalty-free algorithms such as the Advanced Encryption Standard (AES) and the challenges created by differing national encryption and export-control regimes. Industrialized nations often impose strict export controls on dual-use cryptographic tools capable of military applications. The article argues that the low 40-bit standard left Indian users with encryption that could not be considered secure in a global digital environment, since such encryption could be broken elsewhere in the world.

Finally, the article frames encryption through a social science lens, mapping out the power dynamic between citizens, markets, and the state. Cryptography serves as a critical mechanism enabling individuals to assert private spaces within public networks. However, the article also considers situations in which governments seek access to encrypted information or require markets to provide information, raising questions about the relationship between the individual, the market, and the state. The piece concludes that establishing robust, high-grade encryption standards is essential for safeguarding civil liberties, promoting economic confidence, and balancing legitimate national security requirements against individual rights.

## External Link

- [Encryption Standards and Practices](https://cis-india.org/internet-governance/blog/privacy/privacy_encryption)

{% include navbox-elonnai.html %}

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
.highlighted-text ul,
.highlighted-text ol {
  margin: 0 0 1rem 1.5rem;
}
.article-separator {
  border: none;
  border-top: 1px solid rgba(0,0,0,0.08);
  margin: 0.75rem 0 1rem 0;
}

.references-list {
  margin: 0 0 1rem 1.5rem;
}

.references-list li {
  margin-bottom: .8rem;
}

.references-list li:last-child {
  margin-bottom: 0;
}

.references-list a[href^="#ref-"] {
  margin-left: .35rem;
  text-decoration: none;
}
</style>
