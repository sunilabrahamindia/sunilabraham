---
layout: default
title: Portal:A. M. A. Ayrookuzhiel
permalink: /amaa/portal/
categories: [A. M. A. Ayrookuzhiel, Portals, Project pages]
description: Portal page for the life, work, and legacy of Rev. A. M. A. Ayrookuzhiel, bringing together his biography, writings, research contributions, and related materials.
---
{% include under-construction.html %}

<div class="amaa-banner">
  <img 
    src="/amaa/images/amaa-portal-banner.png" 
    alt="Portal banner for A. M. A. Ayrookuzhiel">
  <div class="amaa-banner-text">
    Portal: A. M. A. Ayrookuzhiel
  </div>
</div>

The **A. M. A. Ayrookuzhiel Portal** brings together all material related to the life and work of Rev. A. M. A. Ayrookuzhiel. It serves as a single place to explore his biography, writings, research contributions, and the wider conversations his work shaped. This page links to primary texts, related articles, family archives, and other resources that help readers understand his ideas and the world he engaged with.

<div class="collapse-box">
  <div class="collapse-header" role="button" tabindex="0" aria-expanded="false">
    <span class="collapse-text">Show Biography Details</span>
    <span class="arrow" aria-hidden="true">▾</span>
  </div>

  <div class="collapse-content" aria-hidden="true">
    <dl class="bio-details">
      <dt>🧍 Full Name:</dt>
      <dd>Athanasius Mathen Abraham Ayrookuzhiel</dd>

      <dt>📆 Born:</dt>
      <dd>1933, Chengannur, Kerala, India</dd>

      <dt>✝️ Died:</dt>
      <dd>Friday, 29 November 1996</dd>

      <dt>🌍 Nationality:</dt>
      <dd>Indian</dd>

      <dt>🎓 Roles:</dt>
      <dd>Theologian, Priest, Scholar</dd>

      <dt>🏛️ Institutions:</dt>
      <dd>
        <ul>
          <li>CISRS, Bangalore</li>
          <li>St Paul High Anglican Church, Wokingham</li>
          <li>Order of Ordine Imitationis Christi</li>
        </ul>
      </dd>

      <dt>📚 Areas of Work:</dt>
      <dd>
        <ul>
          <li>Dalit Theology</li>
          <li>Contextual Theology</li>
          <li>Sociology of Religion</li>
          <li>Cultural Studies</li>
        </ul>
      </dd>

      <dt>📘 Major Publications:</dt>
      <dd>
        <ul>
          <li><em>The Sacred in Popular Hinduism</em> (1983)</li>
          <li><em>Swami Anand Thirth</em> (1987)</li>
          <li><em>The Dalit Desiyata</em> (1990)</li>
          <li><em>Dalit Kavithakal</em> (1992)</li>
          <li><em>Dalit Sahityam</em> (1995)</li>
          <li><em>Essays on Dalits, Religion and Liberation</em> (2006)</li>
        </ul>
      </dd>

      <dt>👰‍♀️ Spouse:</dt>
      <dd>Ponnamma Thekedath</dd>

      <dt>👥 Children:</dt>
      <dd>
        <ul>
          <li>Sunil Abraham (born Sunday, 17 June 1973)</li>
          <li>Matthew Abraham</li>
          <li>Jacob Abraham</li>
        </ul>
      </dd>
    </dl>
  </div>
</div>

## Biography
Rev. A. M. A. Ayrookuzhiel (1933–1996) was an Indian theologian who linked faith with the social realities of marginalised communities. Born in Kerala and trained in seminaries in India and Europe, he developed an interest in how belief, justice, and everyday life come together. His years in the United Kingdom, where he served as a curate in Wokingham and married Ponnamma Thekedath, broadened his understanding of the church’s role in a changing world. The couple returned to India in 1973, where he began shaping a theology rooted in local experience.

At the Christian Institute for the Study of Religion and Society (CISRS) in Bangalore, Ayrookuzhiel helped shift attention towards the struggles of Dalits and other oppressed groups. He argued that theology should grow from people’s lived realities rather than abstract debate. His research drew on field studies and cultural traditions, showing how stories, songs, and rituals expressed both suffering and resistance. These insights contributed to the early formation of Dalit Theology in India.

Across books, essays, and edited volumes, he explored caste, culture, and religion with clarity and empathy. Many writings were later collected in *Essays on Dalits, Religion and Liberation* (2006). At the time of his death in 1996, he was working on a major study of Dalit religious identity. His work continues to influence discussions on justice, culture, and the role of faith in public life.  
[Read more](/amaa/){: .btn }

## Major works
*Essays on Dalits, Religion and Liberation* (2006) brings together Rev. A. M. A. Ayrookuzhiel’s most important writings on caste, culture, and the role of religion in shaping social life. The essays show how he approached theology from the viewpoint of Dalit experience rather than formal doctrine. Drawing on fieldwork, oral traditions, and community practices, he examined how rituals, stories, and symbols carried both memories of oppression and sources of strength. A recurring theme in the book is his idea of religious colonisation, where dominant groups absorbed Dalit traditions into a system that denied their independent identity. At the same time, he highlighted the creative ways Dalit communities preserved their own cultural expressions. The collection traces his effort to make theology a tool for dignity and liberation. Published a decade after his death, the volume remains a key resource for understanding Indian contextual and Dalit theology.  
[Read more](/amaa/essays-on-dalits-religion-and-liberation/){: .btn }

<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".collapse-header").forEach(header => {
    const content = header.nextElementSibling;
    const textSpan = header.querySelector(".collapse-text");
    const arrow = header.querySelector(".arrow");

    function toggle() {
      const isOpen = content.classList.toggle("open");
      header.classList.toggle("open");

      // accessibility attributes
      header.setAttribute("aria-expanded", String(isOpen));
      content.setAttribute("aria-hidden", String(!isOpen));

      // update text + arrow
      if (isOpen) {
        textSpan.textContent = "Hide Biography Details";
        arrow.textContent = "▴";
      } else {
        textSpan.textContent = "Show Biography Details";
        arrow.textContent = "▾";
      }
    }

    header.addEventListener("click", toggle);

    // keyboard support: Enter and Space
    header.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
        e.preventDefault();
        toggle();
      }
    });
  });
});
</script>


<style>
/* ===== Local CSS: A. M. A. Ayrookuzhiel Portal Banner ===== */

.amaa-banner {
  position: relative;
  width: 100%;
  max-width: 100%;
  margin: 0 auto 1.5rem auto;
}

/* Mobile-first image styles */
.amaa-banner img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 6px;
  object-fit: cover;
  border: 2px solid rgba(0,0,0,0.35);
}

.amaa-banner-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #ffffff;
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  padding: 0.5rem 1rem;
  width: 100%;
  max-width: 90%;
  line-height: 1.3;
  background: rgba(0,0,0,0.35);
  border-radius: 6px;
  text-shadow: 0 0 10px rgba(0,0,0,0.7);
}

/* Mobile text adjustments */
@media (max-width: 600px) {
  .amaa-banner-text {
    font-size: 1.4rem;
    padding: 0.4rem 0.8rem;
  }
}

/* Desktop: limit banner height */
@media (min-width: 900px) {
  .amaa-banner {
    max-height: 150px; /* Adjust height here */
  }

  .amaa-banner img {
    height: 150px; /* Same value as max-height */
    width: 100%;
    object-fit: cover;
  }
}

  /* ===== Biography Details Box (same styling as media-details) ===== */

.bio-details {
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

.bio-details dt {
  font-weight: 600;
  color: #1b2a49;
  margin-top: 0.7rem;
}

.bio-details dd {
  margin: 0 0 0.3rem 0.3rem;
  color: #555;
}

/* Bullet list support inside dd */
.bio-details ul {
  margin: 0.2rem 0 0.6rem 0.6rem;
  padding-left: 0;
}

.bio-details ul li {
  margin-bottom: 0.2rem;
}

  /* ===== Collapsible Box Wrapper ===== */
/* Collapse container */
.collapse-box {
  max-width: 700px;
  margin: 1.2rem auto;
}

/* Header */
.collapse-header {
  background: #eef3fa;
  border: 1px solid #d8e2f0;
  padding: 0.7rem 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 10px;
  color: #1b2a49;
  box-shadow: 0 2px 4px rgba(0,0,0,0.03);
  user-select: none;
}

.collapse-header:hover {
  background: #e7edf7;
}

/* Arrow */
.collapse-header .arrow {
  transition: transform 0.25s ease;
}

/* Content panel */
.collapse-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s ease;
}

.collapse-content.open {
  max-height: 2000px;
}
.collapse-header:focus {
  outline: 3px solid rgba(50,120,214,0.18);
  outline-offset: 2px;
}
</style>

