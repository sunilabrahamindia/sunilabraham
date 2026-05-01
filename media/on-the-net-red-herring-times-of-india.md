---
layout: default
title: "On the Net, Red Herring"
description: "A Times of India article by Javed Anwer on the unreliability of IP addresses as evidence in cyber crime investigations, quoting Sunil Abraham of CIS."
categories: [Media mentions]
date: 2011-12-04
authors: ["Javed Anwer"]
source: "The Times of India"
permalink: /media/on-the-net-red-herring-times-of-india/
created: 2026-05-01
---

**On the Net, Red Herring** is a *The Times of India* article by Javed Anwer, published on 4 December 2011. The report examines the over-reliance of Indian law enforcement on IP addresses as evidence in cyber crime investigations, and quotes [Sunil Abraham](/sunil/), then Executive Director of the [Centre for Internet and Society](/cis/) (CIS), who warned that there is a tendency to oversimplify the process and that local police, unlike courts, are insufficiently careful when using IP address evidence.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>The Times of India</em></dd>

  <dt>📅 Date:</dt>
  <dd>4 December 2011</dd>

  <dt>👤 Author:</dt>
  <dd>Javed Anwer</dd>

  <dt>📄 Type:</dt>
  <dd>News Report</dd>

  <dt>📰 Newspaper Link:</dt>
  <dd>Not available</dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>It was one morning that changed the life of Lakshmana Kailash K forever. In the wee hours of August 31, 2007, Kailash, a techie in Bangalore, was woken up by cops from Pune. They told him he had posted images derogatory to Chhatrapati Shivaji on Orkut, and whisked him away to Maharashtra. The police had used the IP address provided by the internet service provider and information from Google, to find that the image was posted from a computer owned by Kailash.</p>

<p>The Maharashtra cops are not the only ones to get it wrong. There is a widespread belief that IP addresses are akin to a smoking gun in most cyber crime cases. Tracing the IP address is also considered one of the easiest ways to crack a case. The result: even four years after what Kailash went through, investigators, internet service providers, private companies filtering web traffic and social networking websites, continue to jump to a conclusion on the basis of IP addresses.</p>

<p>"There is a tendency to oversimplify the process," says Sunil Abraham, executive director of Centre for Internet and Society. "While I have seen that courts have been always careful in cases where IP addresses are involved as a tool of investigation, I cant say the same about the local police."</p>

<p>In theory, IP addresses can be useful since they provide a link to individual computers. The address is a numerical string — for example, 192.168.1.1 — that is assigned to any computing device connected to a network. However, given the dynamic and interlinked nature of the internet, using them as clinching evidence is fraught with dangers.</p>

<p>The second reason, according to Patnaik, is the presence of open wi-fi networks. Most people have no clue about technology. This means unsecured or poorly-configured wi-fi networks are common. The result: someone may park his car in a residential colony, scan for open wi-fi networks and use the open connection for sending a threatening or abusive email to his boss before leaving, he says. If the mail is traced, it will lead to the person who owns the wi-fi network and not the guy who used it illegally.</p>

<p>But police officers say that, to start with, the IP address is often the only clue that's there. "Investigating cyber-crime is difficult because it's all virtual," says Ranjit Narayan, special commissioner (crime). "There are no clues other than the IP address. The investigation starts with it."</p>

<p>Now, though, after their widespread abuse, there is a growing realization about the fallacy of the IP approach. A judge in the US recently said there was "a very real disconnect between an IP address and a copyright infringer." Organizations like Electronic Frontier Foundation, which deals with matters related to cyber liberty and free speech on the web, have also taken up the issue in earnest. Perhaps, there is hope for the Kailashs of the future.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

The article was published three days before the CIS undercover investigation into the IT (Intermediaries Guidelines) Rules, 2011 was reported in *Legally India*. Both pieces appeared in December 2011, a period of heightened public debate in India about internet regulation, state surveillance, and the powers of law enforcement online.

The Lakshmana Kailash K case, which the article uses as its opening example, illustrates the practical consequences of treating IP addresses as conclusive evidence: Kailash was arrested in 2007 on the basis of an IP address that pointed to his computer, despite not being the person who posted the content. Abraham's remarks reflected a concern about the due process gaps that such investigative shortcuts create.

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
