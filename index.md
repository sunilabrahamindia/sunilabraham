<style>
:root{
  --page-max-width: 980px;
  --content-width: 720px;
  --space: 1rem;
  --bg: #ffffff;
  --muted: #6b7280;
  --text: #111827;
  --accent: #0f4fa2;
  --accent-2: #0aa5a0;
  --warm: #f4e5a6;
  --card-bg: #ffffff;
  --card-border: rgba(11,23,44,0.06);
  --shadow: 0 6px 18px rgba(13, 26, 50, 0.06);
  --radius: 12px;
  --line: rgba(15,79,162,0.08);
}

main { padding: var(--space); display:flex; justify-content:center; }
.page-inner { width:100%; max-width:var(--page-max-width); }

/* HERO */
.hero {
  max-width: var(--content-width);
  margin: 0 auto 1.3rem;
  padding: 1.1rem;
  border-radius: var(--radius);
  background: linear-gradient(180deg, rgba(15,79,162,0.04), rgba(10,165,160,0.02));
  border: 1px solid var(--line);
  box-shadow: var(--shadow);
}
.hero-grid { display:grid; grid-template-columns:1fr; gap:1rem; }
.hero h1 { font-size:1.28rem; margin:0; color:var(--accent); }
.hero p { font-size:0.98rem; line-height:1.55; margin-top:0.6rem; }

.hero-cta { margin-top:0.8rem; display:flex; gap:0.6rem; flex-wrap:wrap; }

.stats {
  background: rgba(15,79,162,0.05);
  padding:0.28rem 0.6rem;
  border-radius:999px;
  border:1px solid rgba(15,79,162,0.10);
  font-size:0.9rem;
  color:var(--accent);
  font-weight:600;
}

.btn {
  padding:0.48rem 0.85rem;
  border-radius:10px;
  text-decoration:none;
  font-weight:600;
  font-size:0.95rem;
  background:white;
  color:var(--accent);
  border:1px solid var(--card-border);
}
.btn-primary {
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  color:white;
}

/* CARD SYSTEM */
.section-list {
  max-width:var(--content-width);
  margin:0 auto;
  display:grid;
  gap:1rem;
}
.card {
  background:var(--card-bg);
  border-radius:var(--radius);
  padding:1rem;
  border:1px solid var(--card-border);
  box-shadow:0 4px 12px rgba(6,16,32,0.04);
}

.card-head {
  display:flex;
  gap:0.55rem;
  align-items:center;
  margin-bottom:0.6rem;
}
.card-head h2 {
  margin:0;
  color:var(--accent);
  font-size:1.05rem;
  font-weight:700;
}
.card-head .icon { font-size:1.2rem; }

.card p, .card li {
  font-size:0.97rem;
  line-height:1.6;
  color:#1f2937;
}

/* Centered image */
.media-center img {
  width:90%;
  max-width:600px;
  border-radius:8px;
  margin:0.4rem auto 0.8rem;
  display:block;
  border:1px solid rgba(11,23,44,0.06);
}

/* Did you know cards */
.knowledge-card {
  background:rgba(10,165,160,0.03);
  padding:0.7rem;
  border:1px solid rgba(10,165,160,0.06);
  border-radius:10px;
  margin-bottom:0.5rem;
  font-size:0.95rem;
}

.licence { font-size:0.92rem; color:var(--muted); }

@media (min-width: 740px) {
  .hero-grid { grid-template-columns: 1fr 260px; }
  .hero h1 { font-size:1.45rem; }
}
</style>


<main class="home-main">
  <div class="page-inner">

    <!-- HERO -->
    <section class="hero">
      <div class="hero-grid">

        <!-- LEFT (Markdown text) -->
        <div>
          <h1>Welcome to the knowledge sharing and documentation portal of Sunil Abraham</h1>

          <!-- Everything below is Markdown -->
          <p><strong>Welcome</strong> to the knowledge sharing and documentation portal of <strong>Sunil Abraham</strong>. This space brings together notes, essays, research, and reflections on technology, policy, and society. It aims to make knowledge freely accessible, encourage collaborative learning, and preserve insights that might otherwise remain scattered or unpublished.</p>

          <p>The project reflects years of engagement with digital rights, open technology, and social research in India and beyond. It seeks to connect individual thought with public understanding, bridging ideas across disciplines and communities. Each page is designed for clarity, readability, and reuse, keeping the focus on substance rather than design.</p>

          <p>Whether you are a researcher, student, practitioner, or reader exploring questions of openness, equity, and digital transformation, this documentation offers a growing archive of material to study, share, and build upon.</p>

          <div class="hero-cta">
            <a href="#about" class="btn btn-primary">Explore the project →</a>
            <span class="stats">📄 100 articles · 📁 12 pages</span>
          </div>
        </div>

        <!-- RIGHT side card (Markdown inside allowed) -->
        <div class="card">
          <div class="card-head">
            <span class="icon">📚</span>
            <h2>About this project</h2>
          </div>

          <p>This space brings together long-term reflections on technology, society, equity, and digital transformation, designed for clarity, reuse and open access.</p>

          <a href="#about" class="btn">Read more</a>
        </div>

      </div>
    </section>

    <!-- CONTENT CARDS -->
    <section class="section-list">

      <!-- ABOUT -->
      <div id="about" class="card">
        <div class="card-head">
          <span class="icon">ℹ️</span>
          <h2>About</h2>
        </div>

        This project serves as a living documentation space for research, writing, and reflection.  
        This is built to create, organise, and publish documentation in a structured yet flexible manner, enabling continuous learning and open exchange of ideas.

        It aims to:

        - Create and maintain documentation — capture insights, notes, essays, and drafts across themes and disciplines.
        - Encourage knowledge sharing — make ideas accessible, referenceable, and adaptable for wider audiences.
        - Support learning and reflection — develop patterns of learning, synthesis, and critical thought through open writing.
        - Enable collaboration and contribution — allow others to engage with, remix, and build upon existing materials.
        - Host brainstorming and ideation — serve as a space for developing and refining emerging ideas and projects.

        This documentation evolves over time, not as a static archive, but as a continuous process of thinking, writing, and sharing.

        {% include back-to-top.html %}
      </div>

      <!-- FEATURED ARTICLE -->
      <div id="featured-article" class="card">
        <div class="card-head">
          <span class="icon">⭐</span>
          <h2>Featured article</h2>
        </div>

        **Rev. Athanasius Mathen Abraham Ayrookuzhiel** (1933–1996) was an Indian theologian, priest, and scholar whose work bridged faith, culture, and social justice. Educated in philosophy and theology in Pune, Rome, and Oxford, he combined pastoral life with a deep interest in the moral and social struggles of ordinary people.

        After returning to India, he joined the [Christian Institute for the Study of Religion and Society](https://cisrs.in/) in Bangalore, where he became Associate Director. Working closely with theologian M. M. Thomas, he explored how Christian thought could engage with caste and class through the lived experiences of Dalit communities.

        Among his major works are *The Sacred in Popular Hinduism*, *Swami Anand Thirth: Untouchability, Gandhian Solution on Trial*, and *Essays on Dalits, Religion, and Liberation*. Until his death in 1996, Ayrookuzhiel remained dedicated to a theology rooted in the struggles of the marginalised.

        <a href="https://sunilabraham.in/amaa/" class="btn">Read full article...</a>

        {% include back-to-top.html %}
      </div>

      <!-- SUNIL ABRAHAM -->
      <div id="sunil-abraham" class="card">
        <div class="card-head">
          <span class="icon">👤</span>
          <h2>Sunil Abraham</h2>
        </div>

        <div class="media-center">
          <img src="https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/Sunil%20Abraham%20Colour%20Nature.jpg?raw=true"
               alt="Illustration of Sunil Abraham pointing upward in a colourful cartoon landscape">
        </div>

        **Sunil Abraham** (IAST: Sunīl Ābrahām; IPA: suːˈniːl ˈɑːbrəˌhɑːm, born 17 June 1973) is an Indian internet researcher, public policy advocate, and social entrepreneur known for his work at the intersection of technology, society, and governance.

        Sunil is a co-founder and former executive director of the [Centre for Internet and Society](https://cis-india.org/) (CIS), a Bangalore-based non-profit research organisation established in 2008.

        He also co-founded [Mahiti Infotech](https://mahiti.org/), supporting civil society organisations with FOSS-based digital solutions.

        <a href="https://sunilabraham.in/sunil/" class="btn">Read full biography...</a>

        {% include back-to-top.html %}
      </div>

      <!-- DID YOU KNOW -->
      <div id="did-you-know" class="card">
        <div class="card-head">
          <span class="icon">💡</span>
          <h2>Did you know?</h2>
        </div>

        <div class="knowledge-card">
          ... that the concept of [religious colonisation](/amaa/edrl/) was used by theologian [A. M. A. Ayrookuzhiel](/amaa) to describe how Dalit gods and myths were absorbed into a Brahmanical order?
        </div>

        <div class="knowledge-card">
          ... that the movement [Students for Peace](/articles/students-for-peace/) (1993) brought together 5,000 students on Bangalore's M. G. Road for a candlelight protest after the Ayodhya and Bombay riots?
        </div>

        <div class="knowledge-card">
          ... that [Aadhaar reverses the logic of transparency](/publications/surveillance-project/) — making citizens visible to the state while keeping the state opaque?
        </div>

        <div class="knowledge-card">
          ... that [India's 2011 Intermediaries Guidelines](/publications/eavesdropping-on-the-freedom-of-expression-in-india/) require platforms to remove content within 36 hours of a complaint?
        </div>

        {% include back-to-top.html %}
      </div>

      <!-- LICENCE -->
      <div id="licence" class="card">
        <div class="card-head">
          <span class="icon">🔖</span>
          <h2>Licence</h2>
        </div>

        <p class="licence">
        All content are released under the  
        [Creative Commons Attribution–ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) licence.
        </p>

        {% include back-to-top.html %}
      </div>

    </section>

  </div>
</main>
