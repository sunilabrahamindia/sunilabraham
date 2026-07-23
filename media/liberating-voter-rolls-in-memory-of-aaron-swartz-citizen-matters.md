---
layout: default
title: "Liberating Voter Rolls in Memory of Aaron Swartz"
description: "A Citizen Matters report on a Bangalore hacknight commemorating Aaron Swartz, featuring Sunil Abraham's presentation on copyright law and India's IT Act."
categories: [Media mentions]
date: 2013-02-10
source: "Citizen Matters"
authors: ["Zainab Bawa"]
permalink: /media/liberating-voter-rolls-in-memory-of-aaron-swartz-citizen-matters/
created: 2026-07-23
---

**"Liberating Voter Rolls in Memory of Aaron Swartz"** is a *Citizen Matters* article published on 10 February 2013, written by Zainab Bawa. It reports on a Bangalore hacknight organised by HasGeek on 19 and 20 January 2013 to commemorate the life and work of hacktivist [Aaron Swartz](/sunil/aaron-swartz/), where over 40 participants worked on data liberation projects. [Sunil Abraham](/sunil/) of the [Centre for Internet and Society](/cis/) joined the hacknight and presented on copyright law, India's IT Act, and Swartz's work, anchoring a subsequent discussion on the scope of copyright exemptions and infringement in India.

## Contents

1. [Article Details](#article-details)
2. [Full Text](#full-text)
3. [Context and Background](#context-and-background)
4. [External Link](#external-link)

## Article Details

<dl class="media-details">
  <dt>📰 Published in:</dt>
  <dd><em>Citizen Matters</em></dd>

  <dt>📅 Date:</dt>
  <dd>10 February 2013</dd>

  <dt>✍️ Author:</dt>
  <dd>Zainab Bawa</dd>

  <dt>📄 Type:</dt>
  <dd>Event report</dd>

  <dt>📰 Article Link:</dt>
  <dd>
    <a class="btn" href="https://citizenmatters.in/4897-aaron-swartz-memorial-hacknight-in-bangalore/" rel="noopener noreferrer">
      Read Online
    </a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>Over 40 geeks get together for a night of understanding Aaron Swartz's work and contributing to keep his memory and projects alive.</p>

<p>Arun Raghavan, an open source software enthusiast, and four friends worked all night on January 19th on a very unique problem. They were scraping electoral data from ceokarnataka's website. They wanted to create a user-friendly frontend for citizens to search their names and polling booth information. They did this as part of a hacknight to commemorate the life and works of Aaron Swartz, on January 19th and 20th organised by HasGeek, an event organiser for geeks.</p>

<p>Aaron Swartz was a hacktivist, who died in early January. He had helped create RSS 1.0; contributed to Creative Commons; was an early builder of Reddit, where he's often acknowledged as a co-founder; and more recently, became a data liberator, which got him into trouble with the law.</p>

<p>Aaron Swartz is gone, but his work on making the world a better place should not die with him, was the idea behind the hacknight. The idea was to understand his work, issues such as IT laws, copyright rules and access to information and contribute to keep Swartz's memory and projects alive.</p>

<p>Swartz had initiated several coding projects during his lifetime. Anand Chitipothu, Bangalore-based developer who collaborated with Swartz at the Internet Archive and maintains his web.py framework, suggested that the hacknight could also be an opportunity where people get familiar with Aaron's coding projects and work on some of them.</p>

<p>Around 40 people participated. Some participants proposed projects to liberate different kinds of public data such as electoral data, weather data, information about train timetables and crawling data from government and NIC websites. Developers worked on these projects to make the data searchable and usable.</p>

<h4>Discussions during the hacknight</h4>

<p>The hacknight started at 3 PM with a discussion about the life of Aaron Swartz and the political and legal implications of his coding projects and activism. This discussion was led by Chitipothu and Kiran Jonnalagadda of HasGeek.</p>

<p>Swartz had started freeing data funded by public money which constitutionally belonged in the public domain. He published data from the catalogue of the Library of Congress and the US case law archives on the Internet Archive. Later, Aaron downloaded articles from JSTOR to release academic papers whose research was funded with public money. Before he could sift through the downloads, Aaron was caught by the police. He returned the hard disk containing the downloads. JSTOR and MIT did not pursue cases against him, but the United States government charged Aaron for breaking into the MIT campus and faking identity by changing the MAC address of his computer.</p>

<p>At the end of Jonnalagadda's presentation, participants asked several questions about activism, what constitutes offensive speech, framework of IT laws in India, and the process of law-making.</p>

<p>Sunil Abraham of the Centre for Internet and Society (CIS) also joined the hacknight. He made a presentation about copyright laws, the Indian IT Act and Swartz's work. After Sunil's presentation, there was a half hour discussion about the scope of copyright laws in India, copyright exemptions and what constitutes copyright infringement. Participants agreed that the trouble lies with the broad interpretations of copyright and IT laws. This enables the state and private parties to target and harass a person, often on frivolous grounds.</p>

<h4>Hacknight projects</h4>

<p>At 6 PM, participants with project ideas and those who wanted to join projects formed groups. A complete list of projects that participants worked on during the hacknight are available on the hacknight website. We talked with some of the teams and individual participants to understand their projects, the process they followed for solving the problems, and outcomes at the end of the hacknight.</p>

<p><strong>Liberating electoral data:</strong> Arun Raghavan, an open source enthusiast, and four other participants (Arun K, Praveen, Mikul and Sumant) worked on scraping electoral data from ceokarnataka.kar.nic.in. They planned to build a frontend which will make it easy for users to search their names and polling booth information. Currently, the electoral roll is published as a PDF document for each polling station along with a search form (which is unreliable and fails often) for individuals to find their names on the roll and the location of their polling station.</p>

<p>It was difficult to parse the data because the PDFs were not designed for machine readability. Hence, the team had to spend time understanding how to extract the text. The other problem was that the person's name was written above the father's name, but if the person's name was very long, it overlapped the father's name. This made it difficult to determine where the person's name ended and where the father's name began. The team managed to come up with a heuristic to distinguish between the person's name and father's name based on slight differences in the way the text was printed on each sheet.</p>

<p>At the end of the hacknight, the group almost managed to get a dump of an entire electoral roll. The project repositories: ceoscraper and ceo-kar-roll-scraper.</p>

<p><strong>Other data liberation projects:</strong></p>

<p>1. Indexing Government websites by category of information: Elvis D'souza worked on crawling government websites and indexing them by category, for e.g., education, import-export trade, science and technology, etc. According to him, government websites contain lots of information including documents and spreadsheets. At the hacknight, Elvis completed the indexing process and ran some statistics about information contained in these websites. He eventually wants to build a portal where people can access this index and the documents.</p>

<p>2. Railway timetable data: Anand scraped data from the IRCTC website. Supreeth Srinivasmurthy worked with this data to plot a map. Bibhas Debnath also worked on the timetable data to build an API. A demo of this API is yet to be released.</p>

<p>3. Parsing weather data: Asok Padda converted weather data from HTML format to Excel sheets. Hourly weather data for all weather stations in India during 2012 is parsed and uploaded to Internet Archive: archive.org.</p>

<p>Other projects: Kashyap Kondamundi started building an app which will help people to calculate the current values of their mutual funds. He built 70% of this app at the hacknight.</p>

</div>

<button class="copy-btn-full" data-copytarget="#fulltext">Copy Full Text</button>

{% include back-to-top.html %}

## Context and Background

The hacknight was organised by HasGeek in Bangalore on 19 and 20 January 2013, weeks after Aaron Swartz's death in early January that year, to honour his legacy as a hacktivist and data liberation advocate. The event combined a discussion of Swartz's legal troubles, arising from his downloading of academic papers from JSTOR, with hands-on coding projects aimed at freeing public data, including Karnataka's electoral rolls, government website indexes, railway timetables, and weather data.

Sunil Abraham's presentation added a legal and policy dimension to the technical hacknight, connecting Swartz's case to India's own copyright law and IT Act framework. His session catalysed a discussion among participants on how broad interpretations of these laws could be used by the state and private parties to target individuals, directly linking the event's international inspiration to domestic policy concerns that CIS has long worked on.

## External Link

- [Read on Citizen Matters](https://citizenmatters.in/4897-aaron-swartz-memorial-hacknight-in-bangalore/)

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
