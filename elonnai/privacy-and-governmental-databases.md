---
layout: default
title: "Privacy and Governmental Databases"
description: "A 2011 CIS blog post addressing privacy risks in incrementally designed Indian government databases and recommending technical and regulatory practices for data protection, access control, and interoperability."
authors: ["Elonnai Hickok"]
categories: [Elonnai Hickok]
date: 2011-03-23
source: "Centre for Internet and Society"
permalink: /elonnai/privacy-and-governmental-databases/
created: 2026-08-05
---

**"Privacy and Governmental Databases"** is a blog post by [Elonnai Hickok](/elonnai/) published by the [Centre for Internet and Society](/cis/) on 23 March 2011. It analyses how the ad-hoc and incremental development of government databases in India leads to structural privacy risks, including data inaccuracy, unauthorized access, and security gaps. The article outlines nine specific recommendations to establish robust privacy standards, data categorization, breach notifications, and interoperability protocols across e-governance systems.

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
  <dd>23 March 2011</dd>

  <dt>✍️ Author:</dt>
  <dd>Elonnai Hickok</dd>

  <dt>📄 Type:</dt>
  <dd>Blog post</dd>

  <dt>🔗 Original Link:</dt>
  <dd>
    <a href="https://cis-india.org/internet-governance/blog/privacy/privacy-govt-databases">Read the original post</a>
  </dd>
</dl>

## Full Text

<div class="highlighted-text" id="fulltext">

<p>In our research we have found that most government databases are incrementally designed in response to developments and improvements that need to be incorporated from time to time. This method of architecting a system leads to a poorly designed database with many privacy risks such as: inaccurate data, incomplete data, inappropriate disclosure of data, inappropriate access to data, and inappropriate security over data. To address these privacy concerns it is important to analyze the problem that is being addressed from the perspective of potential and planned interoperability with other government databases. Below is a list of problems and recommendations concerning privacy, concerning government databases.</p>

<hr class="article-separator">

<h3>Government Databases and recommendations for privacy practices</h3>

<h4>1. Citizen-State relationships and privacy standards</h4>

<p>Government databases foster different types of relationships between the state and its citizenry. For instance: User databases, service-providing databases, and information-providing databases. Each one of these relationships requires a different level of privacy. Thus, it is important to identify the type of relationship that the database will foster in order to determine what type of privacy model to implement.</p>

<h4>2. Specific privacy policy</h4>

<p>Each government database should have a specific privacy policy that are tailored to the information that they hold. Each policy should cover the following areas:</p>

<ul>
<li>data collection</li>
<li>digitization</li>
<li>usage</li>
<li>storage</li>
<li>security</li>
<li>disclosure</li>
<li>retrieval</li>
<li>access (inter-departmental and public)</li>
<li>anonymization, obfuscation and deletion.</li>
</ul>

<h4>3. Personal vs. personal sensitive and public vs. non-public data categories</h4>

<p>Data in government databases requires varying degrees of privacy safeguards. The division of personal information vs. non personal information etc. creates distinct categories for security levels over data and permissibility of public disclosure. Ex of personal information: Name, address, telephone number, religion. Ex of non-personal data: gender, age. This could work to avoid situations such as the census - where a person's name, address, age, etc, were all printed for the public eye.</p>

<h4>4. Standardization of Privacy Policies and Access Control</h4>

<p>Government databases should all be designed upon interoperable standards so that the databases can "talk" to each other. The ability to coalesce databases strengthens the potential for use and reuse by different stakeholders. Furthermore, the interoperability of systems helps to avoid the creation of silos that hold multiple copies of the same data. To protect the privacy in interoperable systems - restricted and authorized access within departments and between departments is key. The Department of Information Technology has recently published a "Government Interoperability Framework" titled "Interoperability Framework for eGovernance" This policy document is the appropriate place to articulate interoperable privacy policies that could be adopted across eGovernance projects.</p>

<h4>5. Record of breach notification</h4>

<p>If data breach occurs in government database, the breach should be recorded and the appropriate individuals notified.</p>

<h4>6. Anonymization/obfuscation and deletion policies</h4>

<p>Once the purpose for which the data has been collected has been served it must be anonymized/obfuscated or deleted as appropriate. All datasets cannot be deleted as bulk aggregate data is very useful to those interested in trend analysis. Anonymizing/obfuscating the personal details of a data set ensures that privacy is protected during such trend analysis.</p>

<h4>7. Accountability for accuracy of data</h4>

<p>Frequently data that is collected and entered into government databases is not accurate, because the departments are not collecting the data themselves. Thus, they feel no responsibility for its accuracy. If a mechanism is built into each database for identification of each data source this brings accountability for data accuracy.</p>

<h4>8. Appropriate uses of government databases</h4>

<p>Businesses should feel automatically entitled to aggregate and consolidate public information from government databases because it is technically possible to do so. Their uses of government databases must be guided by policies that define "appropriate usage."</p>

<h4>9. Access, updation and control of personal information</h4>

<p>Citizens must be able to access and update their information. Furthermore, they should be able to define to a certain extent access control to their information - which would automatically make them eligible or ineligible for various government services.</p>

<h3>Bibliography</h3>

<ol class="references-list">
  <li>
    Rezhui, Abdemounaam. <em>Preserving Privacy in Web Services</em>. Department of Computer Sciences, Virginia Tech.
  </li>

  <li>
    Medjahed, Brahim. <em>Infrastructure for E-Government Web Services</em>. IEEE Internet Computing, Virginia Tech. January/February 2003.
  </li>

  <li>
    Mladen, Karen. <em>A Report of Research on Privacy for Electronic Government</em>. Privacy in Canada.
  </li>
</ol>

</div>

{% include back-to-top.html %}

## Context and Background

In early 2011, Indian state departments were rapidly digitizing administrative records under the National e-Governance Plan (NeGP) and various sectoral initiatives. However, because many government software systems and digital registries were built reactively to solve immediate administrative requirements, they lacked standardized privacy architecture and unified security protocols. This piecemeal development led to widespread data fragmentation, excessive personal data collection, and unintentional exposures of sensitive citizen data in public directories.

The article outlines fundamental structural weaknesses stemming from this lack of comprehensive design. In particular, it highlights how outsourced data collection compromised data accuracy, while the absence of explicit data lifecycle rules allowed personal details to linger indefinitely in administrative databases. Furthermore, as state agencies began emphasizing system interoperability—supported by initiatives like the Department of Information Technology's "Interoperability Framework for e-Governance"—the risk of unauthorized inter-departmental data sharing and commercial data scraping increased significantly without robust access controls and purpose-limitation guarantees.

To address these vulnerabilities, the piece advocates for integrating privacy safeguards directly into the design of public IT infrastructure. Key recommendations include establishing distinct security tiers for personal and non-personal data, enforcing mandatory breach notifications, enabling anonymization techniques for public aggregate research, and granting citizens statutory rights to inspect, update, and manage access permissions for their personal records.

By grounding its analysis in international e-government frameworks, the post serves as an early policy blueprint for privacy-by-design principles in Indian e-governance. It argues that system interoperability must not come at the expense of citizen privacy, emphasizing that trust in public electronic services depends on clear statutory boundaries, administrative accountability, and explicit data governance rules across all tiers of government.

## External Link

- [Privacy and Governmental Databases](https://cis-india.org/internet-governance/blog/privacy/privacy-govt-databases)

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

</style>
