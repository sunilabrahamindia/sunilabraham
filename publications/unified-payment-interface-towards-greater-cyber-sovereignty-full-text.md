---
layout: default
title: 'Full text: Unified Payment Interface: Towards Greater Cyber Sovereignty'
description: 'Complete full-text version of Sunil Abraham’s ORF Issue Brief No. 380 (July 2020).'
permalink: /publications/unified-payment-interface-towards-greater-cyber-sovereignty-full-text/
categories: [Full text, Publications]
source: 'Observer Research Foundation (ORF), Issue Brief No. 380'
authors: ['Sunil Abraham']
date: 2020-07-01
created: 2025-11-26
---

{% include notice.html message="This is the full text of the article *Unified Payment Interface: Towards Greater Cyber Sovereignty*. To read the main article with abstract, publication details, key findings and citation formats, please visit the main page: <a class='btn' href='/publications/unified-payment-interface-towards-greater-cyber-sovereignty/'>Main Article</a>." %}

*On 1 July 2020, the Ministry of Electronics and Information Technology (MeitY) of India celebrated #5YearsOfDigitalIndia. Given the recent call by the prime minister for Atmanirbhar Bharat ('self-reliant India') the IT minister found the occasion apt for trumpeting a crowning jewel of Digital India — the Unified Payment Interface that was launched almost four years ago. This indigenous innovation has prepared India for both the restrictions on movement required by the pandemic and also more prohibitions against foreign technologies like the ban against China-made apps. This brief outlines the lessons from India’s UPI experience that can be emulated by other countries aiming to provide affordable, ubiquitous and quality digital payment services to their public. While many other countries are still waiting for the magic of the market, the interventionist approach and private-public partnerships fostered by the Indian government has paid off. Course corrections are required, however, to protect the UPI.*

## Introduction

China, Russia[^1] and Latin American countries[^2] have been vocal about their ambitions for greater digital sovereignty (or cyber sovereignty) since the early 2000s. A decade later, some policymakers in developed countries have expressed similar concerns[^3]. Today, the clash between European governments and duopolists in the mobile operating system market — Google and Apple — has made this question central for many governments, with the exception of the United States (US)[^4]. The progressive dematerialisation of currency will soon make the financial dimension of digital sovereignty a priority.

Exploiting one’s control of technical infrastructure for financial transactions to wage economic war is a state strategy that is not new. As early as 1914, Britain had developed a strategy to “derange the enemy’s entire national economy” to pre-empt a protracted conventional war. It hoped to exploit its position as the “epicentre of the global trading system” and “the hub of the global communications network” to wage an economic war against Germany. The strategic aim was to “quickly destabilise and disorganise civilian economic systems, to create chaos and panic, and ultimately to generate social upheaval and political unrest”[^5]. However, Britain failed, primarily because the plain-text mandate to enable surveillance and control could not be achieved given the character limit in cable technology[^6].

More than a century later, many countries are asking the same question about digital payments: What if the payment networks controlled by foreign companies are ordered to stop functioning under a trade embargo?

This brief outlines and analyses India’s experience in setting up the Unified Payment Interface (UPI) — the Indian network for real-time payments (or instant payments, or faster payments). In June 2020, there were more than 1.34 billion transactions amounting to almost US$35 billion[^7]. The brief begins with an exploration of the international context, and proceeds to describe the UPI and its capabilities within its technological (i.e., IndiaStack) and institutional context — the National Payment Corporation of India (NPCI). It then provides a brief analysis of governance improvements and the strategy providing NPCI’s own payment app, called Bharat Interface for Money (BHIM). Finally, the brief attempts to understand the experiences of the internet giants—Google and Facebook, the emerging competition to UPI, and the sustainability of the Indian approach in the long term. The brief argues that both developing and developed countries should emulate the Indian example if existing national payment systems are not meeting their goals of financial inclusion.

## Background

Availability, accessibility and affordability of digital payment technologies for citizens are some of the primary reasons why state provision of payment networks is important. In July 2017, the sixth recommendation of the final report of the US Faster Payments Task Force asked “the Federal Reserve Board to explore and assess the need for operational role(s) in the faster payments system to support ubiquity, competition, and equitable access to faster payments.”[^8] While the preceding recommendations reaffirm the classic American faith in the free market, the sixth one betrays the anxiety that the market may not deliver. In light of the lack of progress since this report, Google wrote[^9] to the Federal Reserve in December 2019, asking the US Federal Reserve Board to emulate India’s UPI while building FedNow.[^10] FedNow is facing steady opposition from big banks and is only expected in 2023–24.[^11]

Historically, some central banks — such as the US Federal Reserve, Bank of England, and the Reserve Bank of India — have provided or incubated clearinghouse or payment processing networks for financial institutions in the country. They still carry out certain regional and national check-clearing and automated clearing house (ACH) payments. However, as they began to focus on the regulation of the banking sector, central banks retreated from their operational role and prioritised fostering payment and settlement networks and systems. Since the late 19th century, payments have evolved from paper cheques to telegrams, X.25 networks, USSD, SMSs and, finally, the current internet-protocol based networks. While transactions between banks initially happened in bulk and batches, they later became individual electronic fund transfers or real-time gross settlement (RTGS). The global industry standard for sending payment orders, also known as the “SWIFT code,” emerged in the mid-‘70s. Foreign credit, debit and payment processing networks began to replace intermediaries.

In the Indian context, many banks could not afford the prohibitive charges of global intermediaries. To address the market failure, the Indian central bank launched the National Payment Corporation of India (NPCI) as a multiple payment system operator. One of the payment systems operated by the NPCI is the UPI. While the central bank in the US is still debating about whether to prioritise enforcing regulations that protect the safety and efficiency of payment networks or take on an operational role, India has technologically leapfrogged due to state intervention and collaborations with the private sector. This brief examines the UPI solely from a perspective of technical and digital policy, and not that of banking or finance.

## Unified Payment Interface

India’s current approach to rapid payments can be traced back to the 2012 UPI Report.[^12] At the time, Nandan Nilekani, co-founder of the Indian IT giant Infosys was the chairman of the task force as well as an adviser for the NPCI, which strengthened the NPCI’s position in the financial technologies ecosystem. Four years later, the UPI went live, on 25 August 2016. Prior to this, the only real-time payment options from bank accounts were IMPS (24×7) and RTGS (only high-value and only during a bank’s office hours). The UPI introduced instant, around-the-clock, peer-to-peer transfers, bill payments, and merchant payments through a standard platform, with support for multiple languages across all banks and many non-bank financial companies (NBFCs).

Several aspects of the UPI were unprecedented: it was mobile-first, did not require any special hardware, and provided connectivity to 155[^13] of the bigger banks. For the very first time, individuals and merchants in India were able to raise collect requests. The four-party model for the payer was also new: the **consumer** who uses an app provided by the **tech company**, which has a contract with a **bank** that has a contract NPCI and was integrated with the UPI switch, which could communicate with the **consumer’s bank account**.[^14] Using a partly open standard for transactions between these parties helped establish trust.[^15] Some standardised innovations of the UPI include the requirement of a standardised interface for the entry of the Mobile Banking Personal Identification Number (MPIN); and interoperability with the QR-code format called Bharat QR, which allows for easy and error-free payments at physical establishments. The MPIN, combined with a secret code on the device, enables two-factor authentication without complicating the user experience with the requirement of OTP (One Time Password).

Several app providers have started to compete with each other using specialised features. For example, to enable greater accessibility for those with visual impairment, those who cannot read, and the elderly, some platforms offer a “talk-back” feature. Unlike wallets, most UPI apps provide multilingual interfaces similar to BHIM’s. Soon, some of these apps will also support audio QR and voice-driven payments. If a cyber-criminal manages to harvest a person’s virtual payment address (VPA), it is possible for them to send a collect request to the victim’s phone from a legitimate e-commerce website. To address this risk, virtual VPAs have been introduced as part of the standard. So far, however, the usage is low, with many users opting to use auto-generated VPAs provided by the apps. Finally, “bottom-up innovation” by hardware manufacturers has resulted in the combination of point-of-sale (POS) hardware with the UPI app, making it possible for firms to provide paper receipts to their consumers.[^16]

## India Stack: The Platform of Platforms

The UPI does not exist in a vacuum and is often referred to as the “cashless layer” of India Stack. India Stack[^17] is the shared brand for a suite of applications and their accompanying platforms that constitute the technological ecosystem around Aadhaar, India’s centralised biometric identification system that covers 88.6 percent[^18] of the total population. The tightcoupling between the national digital identity system and the national payment systems was aimed at compounding network effects. However, since the UPI does not use biometrics, it does not need Aadhaar, which is the presenceless layer of India Stack. The Aadhaar number only helps the UPI identify consumers, but the lack of tokenisation and the availability of these numbers with many data controllers increase the risk of financial fraud.

The second layer consists of three platforms — eKYC (Electronic Know Your Customer), eSign and DigiLocker — together called the “paperless layer.” The eKYC can be used to identify oneself to banks,[^19] eSign is used to “sign documents digitally” and DigiLocker can be used as a store for machine-readable documents. Unfortunately, all three services depend on biometrics for authentication and a key escrow (wherein the authority running the service holds the private key on behalf of the user) model. This, too, increases the risk to UPI users (albeit indirectly), especially for those that use fintech applications, which use application programme interfaces (APIs) in the paperless layer and are therefore rendered vulnerable due to the lack of tokenisation in Aadhaar. The fourth layer is called the “consent layer,” which is used to manage user consent electronically across the Stack. With a better-designed presenceless and paper layer, the tightcoupling with India Stack could have benefited the UPI but is undermined by it instead.[^20] This perverse understanding of “openness,” i.e. faux open standards, is a direct attack on the country’s “free and open-source software” (FOSS) policies,[^21] which is being exported to the rest of the Indian e-governance system through policy initiatives such as the Strategy for National Open Digital Ecosystem (NODE) consultation white paper which seeks to justify proprietary software under the cover of “Open APIs”.[^22]

Even though much of India Stack is built upon FOSS and open standards, the software is not FOSS. This is perhaps understandable, since governments across the world are struggling with the open licensing of publicly funded software. However, the NPCI’s reluctance in opening the standards specification of the UPI is not easily understandable. The lack of full details in the initial standard (UPI 1.0) made it difficult for security researchers to audit payment apps as well as the UPI standard.[^23] Even after these security vulnerabilities were addressed in the next version,[^24] the updated standard is not available in the public domain.[^25] As a common carrier for the traffic of all payment service providers, it is important for the UPI to embrace transparency rather than “security by obscurity”. Yet, the openness rhetoric deployed by both local and foreign evangelists[^26] of the service has been in the form of “open washing.”[^27] The NPCI must act urgently to institute multistakeholder standard-setting processes for the UPI at the earliest, in line with global bodies such as the W3C and the IETF.

## National Payments Corporation of India

The NPCI is a joint initiative by the Reserve Bank of India (RBI) and Indian Banks Association (IBA). The IBA, however, has been accused of lack of transparency and accountability.[^28] Despite registering as a “not-for-profit” company (known as a Section 25 company in India) in 2008, the NPCI proceeded with only 10 core promoter banks as shareholders. After becoming operational in April 2009, it soon launched a whole range of client-facing and bank-facing services based on different last-mile technologies: paper (Cheque Truncation System), biometric micro-ATMs (AePS), smart cards (RuPay), feature phones (*99# USSD), SMS, Immediate Payment Service (IMPS), and smartphones (the BHIM mobile app, Unified Payments Interface and BharatQR). Moreover, the NPCI offers services that allow recurring payments to telecom operators and utility companies, under the “Bharat Bill Payment System,” and the automatic payment of road toll called FASTag.

Since the NPCI was created under the provisions of the Payment and Settlement Systems Act, 2007, as per Section 4(2), 51 percent of the equity of the payment system must be held by public-sector banks. Initially, of the 10 crore promoter banks, the public sector banks held 60 percent while the balance was shared by foreign- and private-sector banks. In 2016, the shareholding base was expanded to 56 banks, with the public sector share reduced to 57 percent. The NPCI has expressed the desire to reduce this further to the legal minimum and induct small finance banks and payment banks in the shareholder base.[^29] This broadening of accountability in governance is an improvement. However, with little public visibility into the approval processes, it is uncertain whether smaller banks can protect their own interests and those of smaller app providers against the global technology giants.

## Governance Issues

While the RBI believes that self-regulation is sufficient,[^30] some aspects of governance do require reform. The regulation of digital payments should ideally be under a co-regulatory framework. As a payment network provider, the NPCI becomes the de facto technical regulator of all the parties that are part of the UPI ecosystem and is, in turn, regulated by the RBI. If an additional payments regulator is not feasible, public transparency measures must be adopted to raise accountability and trust. Consumers can only discern if a UPI service provider is compliant with regulations if transparency obligation forces the latter to publish aggregate performance numbers on an open data portal. Further, customers can also upload their grievances on the same portal. If this emerging paradigm of “RegTech,” is adopted, aggregate numbers decide trustworthiness of a provider and automatic actions by the regulator is based on the data uploaded and analysed on the portal.

In late 2018, the facility for recurrent payment or recurring electronic mandates on the UPI was ready to be launched.[^31] However, the RBI gave regulatory clearance only in January 2020, with a maximum cap of INR 2,000 per payment.[^32] The RBI’s cautiousness indicates that it considers the mandates a mechanism for recurring transactions such as utility payments and monthly subscriptions, not for paying loan EMIs. The design of the UPI mandates protects the consumer’s rights by allowing them to cancel them at any time and provide consent every time one is modified. A fintech or bank engaging in predatory lending practices, e.g. payday loans, may not appreciate these forms of user control. They would prefer that electronic mandates are signed biometrically using eSign and are non-cancellable, which will enable legal debt recovery, as is the case with bounced checks.

The NPCI has an alternative service called e-NACH for loan repayment, with protections under The Negotiable Instrument (Amendment) Act, 2018. However, e-NACH is much more expensive than UPI for banks. The UK Sinha Committee report recommends that the “UPI e-mandate markup language to include event-triggers in addition to time triggers,”[^33] to allow for e-Lien creation. For example, when an SME receives a payment from a client, a predetermined percentage could be immediately sent to a previously identified lender. The lender’s VPA could be hardcoded into the invoice. This would allow millions of SMEs in India to access credit based on cash-flow lending. The UPI standard already supporting the invoice ID is a precursor of this emerging service. Despite industry enthusiasm, auto-debits from a consumer’s account can result in the loss of user control and agency, and sufficient friction and safeguards must be in place. Additionally, the eSign service should use cryptography instead of biometrics to ensure nonrepudiation.

## BHIM App

By the time demonetisation was announced on 8 November 2016, the UPI had already been live for 75 days. Seven weeks later, the NPCI launched the BHIM app, a decision that reveals its expansive understanding of its own mandate. According to Arundhati Ramanathan of *The Ken*, “Depending on the time and context, NPCI is a competitor. It is a platform. It is a regulator. It is an industry association. It is a profitable non-profit. It is a rule maker. It is a judge. It is a bystander.”[^34] Ideally, once a payment network is established, the payment network provider should not compete with the app providers.

Based on the argument presented by the Faster Payments Task Force Report in the US, potential market failure could be a valid reason for the NPCI to play an operational role by introducing an app that competes with the other payment service providers. However, this should have been executed differently, with BHIM being made available under a FOSS licence as reference implementation. A permissive, non-copyleft licence, e.g. the BSD licence,[^35] would have allowed firms to make proprietary derivative works in the tradition of the Apple OS. Moreover, banks and other small and medium technology firms would be incentivised to create proprietary value-added applications based on the freely available source code. Instead, the NPCI introduced a proprietary competing app and implemented several questionable approaches to raise install numbers. This, in turn, resulted in a data breach affecting millions of citizens.[^36] While the NPCI correctly claims that BHIM was not hacked,[^37] the consequences for the users are similar since there is no easy way to change the compromised personal information, such as Aadhaar numbers.

Indeed, the approach that the NPCI adopted for BHIM has not prevented market dominance by foreign firms. In 2016, BHIM accounted for 45 percent[^38] of all UPI transactions by volume; however, that number had reduced to 5.37 percent[^39] by March 2020. Today, Google Pay and Walmart’s Phone Pe are contending for the top place in the Indian payments app market and are trailed by Alibaba-backed Paytm[^40] and about 150 other Payment Service Providers (PSPs).[^41] By adopting a “public good” or FOSS model, the NPCI could have given indigenous Indian players a high-quality starter kit, levelling the playing field for them. This would have also prevented accusations against the NPCI of preferential treatment towards iSpirt associated companies.[^42] It is important that the NPCI contributes to predictability in the ecosystem by being transparent about its mandate and providing protocols for the fair and non-discriminatory treatment of all players.

## Privacy Concerns

The privacy expectations of consumers and the surveillance requirements of banks and regulators for the purposes of fraud and risk management (FRM), fighting crime and preventing terrorism are difficult to resolve to everyone’s satisfaction. Previously, the carrying capacity limitations of USSD for the #99# NUUP service meant that IMPS across all channels worked using a Mobile Money Identifier instead of the full bank account number.[^43] When transactions were routed through the NPCI, it had no visibility into which accounts were involved. Similarly, when consumers sent IMPS instructions directly to their banks (using SMS, either in plain text or encrypted), the NPCI had little personally identifiable metadata for these transactions.

However, recent advancements in technology have made surveillance easier. While the UPI system ensures end-to-end cryptography, but at each hop across the four parties, the payload is decrypted. Since the NPCI operates the switch, it has visibility into all the details of each transaction — the Aadhaar number, device fingerprint (generated from parameters such as DeviceID, App ID and IMEI number),[^44] IP address, operating system, application, bank account numbers, and GPS location of the user when conducting the transaction. In theory, this data is meant to help with the identification and prevention of fraud, but combined with all the data collected through the other services that the NPCI provides, a 360-degree financial picture of most non-elite Indians can be constructed. Unlike VPAs that can be reissued, Aadhaar numbers are permanent and are stored by various UPI stakeholders. Consequently, any data breach can have a permanent impact.[^45]

If India enacts an omnibus privacy law, it will become necessary for the NPCI to conduct a detailed privacy impact assessment and implement measures such as tokenisation, as is expected with cards,[^46] which makes it possible to fight fraud and protect privacy at the same time. However, this law has been referred to a Joint Parliamentary Committee of both Houses,[^47] making it unlikely that a comprehensive privacy impact assessment of NPCI will be conducted any time soon. Nonetheless, other developments — both technological and legal — are ongoing and may contribute to the protection of the right to privacy. From a technical perspective, the consent layer or the fourth layer of IndiaStack is an indigenous implementation of the growing international phenomenon of data-protection intermediaries. The consent layer uses a framework called Data Empowerment and Protection Architecture (DEPA),[^48] which aims to give users granular control of their personal data through the grant and revocation of electronic consent. The standard for these electronic consents has been published by the Ministry of Electronics and Information Technology (MeitY).[^49] While the technical design has been finalised,[^50] it is not yet available to most Indians because firms have just stepped in to provide these services.

From a regulatory perspective, the RBI issued a master direction in September 2016,[^51] with the aim of competitive oligopoly of account aggregators.[^52] These are data intermediaries that allow fintech companies to access the financial records[^53] of their consumers from banks and other financial institutions. Unfortunately, the lack of clear incentives and revenue streams for account aggregators prevent this vision from becoming a reality. Under the current regulations, existing financial institutions can become account aggregators[^54] and collect revenues from both data subjects and the various data controllers. This makes it possible for account aggregators to unfairly prioritise large volumes from a small number of data controllers, instead of small volumes from millions of data subjects. The RBI must revise the guidelines to ensure that aggregators can only make money from data subjects and thus align their bottom-line with protecting the privacy rights of consumers. This is an urgent requirement, especially in light of the low levels of literacy and developments such as the RBI’s plan for a new “public credit registry,” which will create another unprecedented “360-degree view of borrowers.”[^55]

## Promoting Competition

To maximise consumer welfare in any payment ecosystem, competition must be protected at all levels, i.e. between banks, payment service providers, and payment networks. By allowing access to the UPI switch only to banks, the existing level of competition was protected to some extent. On 18 September 2017, competition between payment service providers intensified when Google launched its UPI app “Tez.” Unlike other apps that have only one partner bank, Tez had partnerships with four banks at the time of the launch.[^56] WhatsApp, too, has been aiming to take its payment services nationwide since signing up with four banks in 2018.[^57] Asking large technology platforms to work with multiple banks appears to be a deliberate policy on the part of the NPCI. After the regulatory stricture of Yes Bank, this policy has been formalised with NPCI, making it mandatory for large technology platforms to adopt a “multi-bank model” for large platforms.[^58] According to the regulations, a maximum of 50 percent of volumes can go to a single bank and PSPs should nudge customers to change VPAs.

While its Payment Service Provider certification was fast-tracked, WhatsApp is still running trials of its service,[^59] since it has still not complied with all the data-localisation requirements of the NPCI to receive approval for a full rollout.[^60] Perhaps the investment in Reliance Jio will result in new opportunities for WhatsApp.

1. Facebook’s current challenges of managing hate speech and disinformation on its “dark channel,” WhatsApp Pay provides them with both the justification and the technological means to implement the social network’s “real-name” policy. All UPI apps can call an API to verify the bank-verified name of a particular VPA. In most cases, the bank-verified name is the legal name of the individual.
2. For Reliance, there is an opportunity to capitalise on the RBI’s openness to creating competition to the NPCI and the UPI. Two months before Facebook announced its investment in Jio, the RBI published a “Draft Framework” for the authorisation of a pan-India New Umbrella Entity (NUE) for Retail Payment Systems.[^61] While there are serious concerns[^62] about the regulatory design of this framework, which must be addressed, it will be good for both competition and the cybersecurity of India’s payment networks.

So far, the Indian government has taken some highly interventionist steps to protect the UPI from global giants such as VISA and MasterCard. The NPCI has always controlled the Merchant Discount Rate (MDR) and interchange rates in a rather opaque fashion.[^63] On 27 December 2019, Finance Minister Nirmala Sitharaman announced that from January 2020, all B2C businesses with INR 500 million in annual revenues “must provide” the NPCI integration in terms of RuPay and the UPI, and that the MDR charges would be waived for these businesses as an added incentive.[^64] The Payments Council of India, which represents merchant acquirers and aggregators, has opposed this zero-MDR approach, citing the lack of any incentive to provide digital payment services. Some have viewed the government’s move as an attempt to nationalise the payments industry.[^65] While zero-MDR without subsidy from the regulator may be a valid strategy in the short term, it is unsustainable in the long run, since stakeholders will need incentives to continue supporting and innovating around digital payments. Already, some banks have begun to retaliate by capping the number of free UPI transactions available to consumers per month.

Competition between payment networks can also be fostered by introducing FOSS and open standards. For example, countries that prefer multiple payment networks can follow the Mojaloop Project. Omidyar Network, the Bill and Melinda Gates Foundation, Google, Rockefeller Foundation, and two start-ups — COIL and Modus Box — are together building this open-licensed federated payment network platform. They have taken inspiration from the UK’s Faster Payments Service and Australia’s New Payments Platform.[^66] The Mojaloop Project is meant for nations and central banks to adopt. The routing system depends on a technology called Interledger, which can work across multiple payment networks, blockchains and currencies, being an open protocol suite for sending and receiving digital payments. It is not part of a formal working group at any of the global standard-setting organisations but is “loosely organized as part of a Community Group of the World Wide Web Consortium (W3C).”[^67] Compared to a proprietary solution, this has the advantage of equipping all payment service providers with technical information about the network, allowing national technical developments to be incorporated into global standards.

## Conclusion

While it is too soon to comment on the UPI’s sustainability in the long run, it is currently better than most platforms in the developed countries in terms of access, affordability and availability of instant digital payments to hundreds of millions of citizens. Based on its success, the NPCI has established a subsidiary to export the UPI as a technology to other countries.[^68]

However, while the rough contours of the Indian approach to addressing market failure are correct, there have also been several grave errors, chief amongst them the lack of a mature governance model, interoperability rules, open standards, and transparent rule-making and enforcement. These issues have resulted in an insufficiently competitive ecosystem of payment service providers. The release of the BHIM app as a competing mobile app by the NPCI further muddied the waters for local competition. After the COVID-19 disruption, a more sustainable MDR regime must be introduced, to provide sufficient incentives for all actors in the ecosystem. Other countries must study the Indian example carefully to harvest best practices for their own contexts. For telecom infrastructure, there are many examples of governments investing in national and international backbone. Similarly, in the area of digital payments, the government could play an operational role wherever private firms find insufficient market opportunity.

**Note**: The author would like to thank Srikanth Lakshmanan of Cashless Consumer[^69] for providing him with the necessary education for writing this article.

## Endnotes

[^1]: Stanislav Budnitsky and Lianrui Jia, [Branding Internet Sovereignty: Digital Media and the Chinese–Russian Cyberalliance](https://www.orfonline.org/research/unified-payment-interface/#){: rel="nofollow" }, *European Journal of Cultural Studies* 21, no. 5 (October 2018): 594–613.

[^2]: Renata Ávila Pinto, “[La Souveraineté À L’épreuve Du Colonialisme Numérique](https://www.orfonline.org/research/unified-payment-interface/#){: rel="nofollow" }”, CETRI, 27 April 2020, accessed 16 June 2020.

[^3]: Farid Gueham, [*Digital Sovereignty: Steps Towards A New System Of Internet Governance*](https://euagenda.eu/upload/publications/untitled-77045-ea.pdf){: rel="nofollow" } (Paris: The Fondation pour l’innovation politique, January 2017).

[^4]: Aditi Agrawal, “5 European digital ministers argue for digital sovereignty amidst COVID-19, call out Big Tech for ‘imposing standards’,” *Medianama* 28 May 2020, accessed 17 June 2020.

[^5]: Nicholas A. Lambert, George Perkovich and Ariel E. Levite, “Brits-Krieg: The Strategy of Economic Warfare,” 2017.

[^6]: “Brits-Krieg: The Strategy of Economic Warfare,” op. cit.

[^7]: [Official account for BHIM by NPCI](https://twitter.com/NPCI_BHIM/status/1278235392542556161/photo/1){: rel="nofollow" }, Twitter Photo, 1 June 2020.

[^8]: The Faster Payments Task Force, [*The U.S. Path to Faster Payments*](https://fasterpaymentstaskforce.org/wp-content/uploads/faster-payments-task-force-final-report-part-two.pdf){: rel="nofollow" }, July 2017.

[^9]: IANS, “[Google wants US Federal Reserve to follow India’s UPI example](https://www.orfonline.org/research/unified-payment-interface/#){: rel="nofollow" }”, *Economic Times*, 15 December 2019.

[^10]: FedNow Service, “[FedNowSM Service development is making strides](https://www.frbservices.org/news/fed360/issues/030220/030220-fednow-service-progress.html){: rel="nofollow" }”, The Federal Reserve, 2 March 2020, accessed 17 June 2020.

[^11]: Victoria Guida, “[Big banks prepare to battle the Fed on faster payments](https://www.politico.com/story/2019/07/19/big-banks-prepare-battle-fed-faster-payments-1605935){: rel="nofollow" },” *Politico*, 19 July 2019, accessed 17 June 2020.

[^12]: Task Force, “[Report of the Task Force on an Aadhaar-Enabled Unified Payment Infrastructure](https://www.finmin.nic.in/sites/default/files/Report_Task_Force_Aadhaar_PaymentInfra.pdf){: rel="nofollow" }”, Government of India.

[^13]: “[UPI Live Members](https://www.npci.org.in/upi-live-members){: rel="nofollow" }”, NPCI. Note: “[IMPS has connectivity to 540 banks](https://www.npci.org.in/links-imps-members){: rel="nofollow" }”. India has approximately 1400 banks.

[^14]: NASSCOM Product, “[NPC2018: FinTech Summit – Masterclass – UPI 2.0](https://www.youtube.com/watch?v=XTNO_jM7fFY){: rel="nofollow" }”, 19 November 2018.

[^15]: “[Unified Payment Interface: API And Technology Specifications](https://web.archive.org/web/20170828163531/http:/www.npci.org.in:80/documents/Unified-Payment-Interface-API-Technology-Specifications-v11.pdf){: rel="nofollow" }”, NPCI, February 2016.

[^16]: Mayank Jain, “[UPI Comes To Point-Of-Sale Machines As NPCI Seeks To Increase Merchant Users](https://www.bloombergquint.com/business/upi-comes-to-point-of-sale-machines-as-npci-seeks-to-increase-merchant-users){: rel="nofollow" }”, *Bloomberg Quint*, 30 March 2017, accessed 17 June 2020.

[^17]: “[What is India Stack](https://www.indiastack.org/about/){: rel="nofollow" }”, India Stack, accessed 17 June 2020.

[^18]: “[State/UT wise Aadhaar Saturation](https://uidai.gov.in/images/state-wise-aadhaar-saturation.pdf){: rel="nofollow" },” Unique Identification Authority of India, 2020.

[^19]: This is the Supreme Court judgement in 2018; it was a mandatory requirement from the RBI.

[^20]: Web Desk, “[BHIM data leak exposes 7 million Indians’ data: Report](https://www.theweek.in/news/biz-tech/2020/06/01/bhim-data-leak-exposes-7-million-users-data-report.html){: rel="nofollow" }”, *The Week*, 1 June 2020, accessed 17 June 2020.

[^21]: National Policy on Information Technology (2012), Policy on Adoption of Open Source Software (2014), Framework for Adoption of Open Source Software (2015), MeitY.

[^22]: “[Strategy for National Open Digital Ecosystem (NODE) consultation whitepaper](https://static.mygov.in/rest/s3fs-public/mygov_158219311451553221.pdf){: rel="nofollow" }”, MeitY, accessed 17 June 2020.

[^23]: Renuka Kumar, Sreesh Kishore, Hao Lu and Atul Prakash, “[Security Analysis of Unified Payments Interface and Payment Apps in India](https://www.usenix.org/system/files/sec20summer_kumar_prepub.pdf){: rel="nofollow" },” University of Michigan, n.d.

[^24]: “Unified Payment Interface: API And Technology Specifications,” op. cit.

[^25]: Srikanth Lakshmanan, “[As UPI 2.0 Is Unveiled, It Remains Very Much a Transaction in Progress](https://thewire.in/tech/upi-2-0-is-unveiled-transaction-in-progress){: rel="nofollow" }”, *The Wire*, 21 August 2018.

[^26]: William Cook and Anand Raman, “[National Payments Corporation of India and the Remaking of Payments in India](https://www.cgap.org/sites/default/files/publications/2019_05_07_NPCI_Working_Paper_0.pdf){: rel="nofollow" }”, CGAP Working Paper, May 2019.

[^27]: Jasmine N.M. Folz, “[Free and Open Source Software in India: Mobilising Technology for the National Good](https://www.research.manchester.ac.uk/portal/files/102613332/FULL_TEXT.PDF){: rel="nofollow" }”, PhD Thesis, University of Manchester, 2018.

[^28]: S. Ramachandran, “[IBA – Association Without Any Accountability & Responsibility](http://www.allbankingsolutions.com/Wage-Revision/IBA-Without-any-accountability-and-responsibility.htm){: rel="nofollow" },” All Banking Solutions, 3 September 2015.

[^29]: PTI, “[NPCI widens shareholding base to 56 banks](https://economictimes.indiatimes.com/news/economy/finance/npci-widens-shareholding-base-to-56-banks/articleshow/54293306.cms){: rel="nofollow" }”, *The Economic Times*, 12 September 2016.

[^30]: ET Online, “[RBI proposes self-regulatory body for digital payment system](https://economictimes.indiatimes.com/wealth/personal-finance-news/rbi-proposes-self-regulatory-body-for-digital-payment-system/articleshow/73978494.cms?from=mdr){: rel="nofollow" }”, *The Economic Times Wealth*, 6 February 2020.

[^31]: “[NPC2018: FinTech Summit – Masterclass – UPI 2.0](https://www.youtube.com/watch?v=XTNO_jM7fFY){: rel="nofollow" }”, NASSCOM Product, 19 November 2018.

[^32]: Pratik Bhakta, “[EXCLUSIVE: Recurring payments on UPI set to start; payment apps boost tie-ups with lending platforms for EMIs](https://www.moneycontrol.com/news/business/recurring-payments-on-upi-set-to-start-payment-apps-boost-tie-ups-with-lending-platforms-for-emis-5321741.html){: rel="nofollow" }”, *Moneycontrol*, 27 May 2020.

[^33]: Expert Committee, “[Report of the Expert Committee on Micro, Small and Medium Enterprises](https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/MSMES24062019465CF8CB30594AC29A7A010E8A2A034C.PDF){: rel="nofollow" }”, RBI, June 2019.

[^34]: Arundhati Ramanathan, “[NPCI, The God of Many Things](https://the-ken.com/story/npci-god-many-things/){: rel="nofollow" }”, *The Ken*, 26 February 2018.

[^35]: Open Source Initiative, “[The 3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause){: rel="nofollow" },” accessed 17 June 2020.

[^36]: Srikanth Lakshmanan, “[Twitter Thread](https://twitter.com/logic/status/1267432495693221888){: rel="nofollow" }”, 1 June 2020.

[^37]: Special Correspondent, “[NPCI denies breach of BHIM app data](https://www.thehindu.com/news/national/npci-denies-breach-of-bhim-app-data/article31726398.ece){: rel="nofollow" },” *The Hindu*, 1 June 2020.

[^38]: FE Bureau, “[BHIM share in UPI pie shrinks in December](https://www.financialexpress.com/market/bhim-share-in-upi-pie-shrinks-in-december/999404/){: rel="nofollow" }”, *Financial Express*, 3 January 2018.

[^39]: Ajay Kumar Shukla, “[BHIM loses sheen as market share shrinks to 5.37%](https://government.economictimes.indiatimes.com/news/digital-payments/bhim-loses-sheen-as-growth-shrinks-to-5-37-market-share/71009004){: rel="nofollow" }”, *The Economic Times*, 6 September 2019.

[^40]: Manish Singh, “[Google and Walmart establish dominance in India’s mobile payments market as WhatsApp Pay struggles to launch](https://techcrunch.com/2020/06/03/google-and-walmarts-phonepe-establish-dominance-in-indias-mobile-payments-market-as-whatsapp-pay-struggles-to-launch/){: rel="nofollow" }”, *TechCrunch*, 4 June 2020.

[^41]: Mahesh Uppal, “[Keeping India’s payments market competitive](https://www.msn.com/en-in/money/markets/keeping-indias-payments-market-competitive/ar-BB15gtQU?li=AAgfW3S){: rel="nofollow" },” *MSN*, 9 June 2020.

[^42]: Rohin Dharmakumar, “[Platform ambitions: The story of how iSpirt lost its true north](https://the-ken.com/story/platform-ambitions-story-ispirt-lost-true-north/){: rel="nofollow" },” *The Ken*, 21 September 2017.

[^43]: “[IMPS Product Overview](https://www.npci.org.in/product-overview/imps-product-overview){: rel="nofollow" }”, NPCI, n.d.

[^44]: Renuka Kumar, Sreesh Kishore, Hao Lu and Atul Prakash, op. cit.

[^45]: Sanghamitra Kar, “[Data of over 7 million BHIM users exposed in CSC website breach: Report](https://tech.economictimes.indiatimes.com/news/mobile/bhim-app-data-breach-exposes-data-of-over-7-million-users-report/76131461?redirect=1){: rel="nofollow" }”, *The Economic Times Tech*, 1 June 2020.

[^46]: Reserve Bank of India, “[Tokenisation – Card transactions](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11449&Mode=0){: rel="nofollow" }”, 8 January 2019.

[^47]: PIB, “[Joint Committee on the Personal Data Protection Bill, 2019 seeks views and suggestions](https://pib.gov.in/PressReleasePage.aspx?PRID=1601695){: rel="nofollow" }”, Government of India, 3 February 2020.

[^48]: Shubham Ruhela, “[Data Empowerment and Protection Architecture Explained – Video](https://pn.ispirt.in/data-empowerment-and-protection-architecture-explained-video/){: rel="nofollow" }”, iSpirt, 23 June 2019.

[^49]: “[Electronic Consent Framework – Technology Specifications, Version 1.1](http://dla.gov.in/sites/default/files/pdf/MeitY-Consent-Tech-Framework%20v1.1.pdf){: rel="nofollow" }”, Government of India.

[^50]: The Reserve Bank of India, “[Technical Specifications for all participants of the Account Aggregator (AA) ecosystem](https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NT9653CEFA5CC9F84316BF533DE6C3CA4616.PDF){: rel="nofollow" }“, 8 November 2019.

[^51]: The Reserve Bank of India, “[Master Direction- Non-Banking Financial Company – Account Aggregator (Reserve Bank) Directions, 2016](https://rbidocs.rbi.org.in/rdocs/notification/PDFs/MD46859213614C3046C1BF9B7CF563FF1346.PDF){: rel="nofollow" }“, 22 November 2019.

[^52]: The Reserve Bank of India, “[Master Direction- Non-Banking Financial Company – Account Aggregator (Reserve Bank) Directions, 2016](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=10598&Mode=0){: rel="nofollow" }”, 22 November 2019, accessed 17 June 2020.

[^53]: “[Summary](https://swagger-ui.rebit.org.in/?url=https://specifications.rebit.org.in/api_specifications/account_aggregator/FIU.yaml){: rel="nofollow" }”, Swagger, n.d.

[^54]: Rohan Jahagirdar and Praneeth Bodduluri, “[Digital Economy: India’s Account Aggregator System Is Plagued by Privacy and Safety Issues](https://www.epw.in/node/157005/pdf){: rel="nofollow" }“, *Economic & Political Weekly 55*, no. 22 (30 May 2020).

[^55]: Asit Ranjan Mishra, “[US raises concerns over RBI’s move to create credit registry](https://www.livemint.com/news/india/us-raises-concerns-over-rbi-s-move-to-create-credit-registry-1557338438758.html){: rel="nofollow" }”, *Livemint*, 8 May 2019.

[^56]: “[Google launches India mobile payments app Tez](https://www.bbc.com/news/technology-41306312){: rel="nofollow" },” BBC News, 18 September 2017.

[^57]: Jagmeet Singh, “[WhatsApp Pay to Launch in India by May-End With 3 Banks on Board: Report](https://gadgets.ndtv.com/apps/news/whatsapp-pay-launch-may-end-axis-hdfc-icici-bank-sbi-rollout-report-2223592){: rel="nofollow" },” NDTV *Gadgets 360*, 5 May 2020.

[^58]: “[Guidelines for Multi-bank model and migration from Single Bank to multibank PSP model](https://www.npci.org.in/sites/default/files/circular/UPI%20OC%2081%20-%20Guidelines%20for%20Multi-bank%20model%20and%20migration%20from%20Single%20Ba....pdf){: rel="nofollow" }“, NPCI, 2 March 2020.

[^59]: Sunil Abraham, “[Why NPCI and Facebook need urgent regulatory attention](https://economictimes.indiatimes.com/industry/banking/finance/banking/why-npci-and-facebook-need-urgent-regulatory-attention/articleshow/64522587.cms){: rel="nofollow" }”, *The Economic Times*, 9 June 2018.

[^60]: Surabhi Agarwal, “[WhatsApp Pay to comply with all rules in India by May](https://tech.economictimes.indiatimes.com/news/mobile/whatsapp-pay-to-comply-with-all-rules-in-india-by-may/75333654?redirect=1){: rel="nofollow" }”, *The Economic Times Tech*, 24 April 2020.

[^61]: “[Draft Framework for authorisation of a pan-India New Umbrella Entity (NUE) for Retail Payment Systems](https://rbidocs.rbi.org.in/rdocs/Content/PDFs/DANUE6F1C5983ACA84C5D9462D3DCA803FF9C.PDF){: rel="nofollow" }“, RBI, n.d.

[^62]: Beni Chugh, Srikara Prasad, Madhu Srinivas and Mallika Sen, “[Our Response to the Draft Framework for authorisation of a pan-India New Umbrella Entity (NUE) for Retail Payment Systems](https://www.dvara.com/blog/2020/03/12/our-response-to-the-draft-framework-for-authorisation-of-a-pan-india-new-umbrella-entity-nue-for-retail-payment-systems/){: rel="nofollow" }”, 12 March 2020.

[^63]: Rohan Jahagirdar, “[Peak Fintech: Breaking down the fee structure of UPI payments to find out who makes how much](https://blog.baseaccount.com/peak-fintech-breaking-down-the-fee-structure-of-upi-payments-to-find-out-who-makes-how-much-329f752efd05){: rel="nofollow" }”, *Medium*, 28 October 2019.

[^64]: PTI, “[No MDR charges applicable on payment via RuPay, UPI from Jan 1: Sitharaman](https://economictimes.indiatimes.com/industry/banking/finance/banking/no-mdr-charges-applicable-on-payment-via-rupay-upi-from-jan-1-sitharaman/articleshow/73008967.cms){: rel="nofollow" }”, 28 December 2019.

[^65]: IANS, “[Zero MDR on RuPay, UPI to kill digital payments industry](https://www.moneylife.in/article/zero-mdr-on-rupay-upi-to-kill-digital-payments-industry/59025.html){: rel="nofollow" }”, 30 December 2019.

[^66]: David Z. Morris, “[Google and Gates Foundation to help spread digital payments in developing countries](https://fortune.com/2020/05/06/google-gates-foundation-digital-payments-developing-countries/){: rel="nofollow" },” 6 May 2020.

[^67]: “[Get Involved](https://interledger.org/community.html){: rel="nofollow" }”, Interledger, accessed 7 July 2020.

[^68]: Ashwin Manikandan, “[NPCI sets up subsidiary for exporting UPI to international markets: RBI governor](https://economictimes.indiatimes.com/news/economy/policy/npci-sets-up-subsidiary-for-exporting-upi-to-international-markets-rbi-governor/articleshow/72743281.cms){: rel="nofollow" }”, 16 December 2019.

[^69]: “[About](https://www.cashlessconsumer.in/about/){: rel="nofollow" }”, Cashless Consumer, accessed 17 June 2020.

