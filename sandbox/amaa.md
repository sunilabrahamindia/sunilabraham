---
layout: default
title: "Athanasius Mathen Abraham Ayrookuzhiel Works Mapping"
sitemap: false
robots: noindex
---

This sandbox is a workspace to map and track the progress of the literary works of [Athanasius Mathen Abraham Ayrookuzhiel](/amaa/). The main portal may be seen [here](/amaa/portal/). This space lists works completed, articles created, and holds room for works yet to be undertaken. You may also see the collected works [Essays on Dalits, Religion and Liberation](/amaa/edrl/).

## Essays

<style>
.amaa-table { width:100%; border-collapse:collapse; font-size:0.92rem; line-height:1.5; }
.amaa-table th { padding:0.5rem 0.75rem; background:#f3f0ec; border-bottom:2px solid #dcd9d5; text-align:left; font-weight:600; }
.amaa-table td { padding:0.5rem 0.75rem; border-bottom:1px solid #dcd9d5; vertical-align:top; }
.amaa-table td.title { word-wrap:break-word; white-space:normal; max-width:340px; }
.amaa-table td.edrl { text-align:center; white-space:nowrap; width:3rem; }
.amaa-table td.edrl.y { background:#d4efdc; color:#276039; font-weight:600; }
.amaa-table td.edrl.n { background:#fadadd; color:#922b21; font-weight:600; }
.amaa-table td.tsap { white-space:nowrap; width:6rem; }
.amaa-table tr:nth-child(even) { background:#f9f8f5; }
@media (min-width:768px) {
  .amaa-table td.title { max-width:none; width:75%; }
}
.amaa-tally { display:flex; flex-wrap:wrap; gap:0.6rem; margin-bottom:1rem; font-size:0.88rem; }
.amaa-tally-item { padding:0.35rem 0.75rem; border-radius:999px; background:#f3f0ec; border:1px solid #dcd9d5; color:#28251d; white-space:nowrap; }
.amaa-tally-item span { font-weight:700; margin-left:0.25rem; }
</style>

<div class="amaa-tally" id="amaa-tally"></div>

<table class="amaa-table" id="amaa-essays">
  <thead>
    <tr>
      <th class="title">Title</th>
      <th class="edrl">EDRL</th>
      <th class="tsap">TSAP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="title">Indian Religious Heritage and Social Transformation: Change of Perspective within the CISRS</td>
      <td class="edrl y">Y</td>
      <td class="tsap">Rafika OCR</td>
    </tr>
    <tr>
      <td class="title">A Proposal for the Study of Religious Heritage of the Dalits: Some Methodological Considerations</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">Religious Legitimation and Delegitimation of Social Relations of Power (of Caste): The Case of the Dalits in Historical Perspective</td>
      <td class="edrl y">Y</td>
      <td class="tsap">Rafika OCR</td>
    </tr>
    <tr>
      <td class="title">Religions and Culture in Dalits' Struggle for Liberation</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">The Religious Factor in Dalit Liberation: Some Reflections</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">Chinna Pulayan: The Dalit Teacher of Sankaracharya</td>
      <td class="edrl y">Y</td>
      <td class="tsap"><a href="/amaa/chinnapulayan-the-dalit-teacher-of-sankaracharya/">Page</a></td>
    </tr>
    <tr>
      <td class="title">The Dalits, Religions and Inter-Faith Dialogue</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">The Role of Religions in Dalit Liberation: Some Reflections</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">Dalits' Challenges and Religious Systems: A People Ignored by Church History</td>
      <td class="edrl y">Y</td>
      <td class="tsap">Rafika OCR</td>
    </tr>
    <tr>
      <td class="title">The Dalit Church's Mission: A Dalit Response</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">Christian Dalits in Revolt</td>
      <td class="edrl y">Y</td>
      <td class="tsap">—</td>
    </tr>
    <tr>
      <td class="title">Swami Anand Thirth – "Untouchability": Gandhian Solutions on Trial</td>
      <td class="edrl y">Y</td>
      <td class="tsap"><a href="/amaa/swami-anand-thirth-untouchability-gandhian-solution-on-trial/">Page</a></td>
    </tr>
    <tr>
      <td class="title">The Motives of Mar Ivanios for the Reunion with the Catholic Church</td>
      <td class="edrl n">N</td>
      <td class="tsap"><a href="/amaa/mar-ivanios-reunion-motives/">Page</a></td>
    </tr>
    <tr>
      <td class="title">The Sacred in Popular Hinduism: An Empirical Study in Chirakkal, North Malabar</td>
      <td class="edrl n">N</td>
      <td class="tsap"><a href="/amaa/the-sacred-in-popular-hinduism-chirakkal-north-malabar/">Page</a></td>
    </tr>
    <tr>
      <td class="title">Religion: A Way of Salvation or an Ideology of Oppression</td>
      <td class="edrl n">N</td>
      <td class="tsap">Rafika OCR</td>
    </tr>
    <tr>
      <td class="title">The Living Hindu Popular Religious Consciousness and Some Reflections on it in the Context of Hindu-Christian Dialogue</td>
      <td class="edrl n">N</td>
      <td class="tsap">Rafika OCR</td>
    </tr>
  </tbody>
</table>

<script>
(function(){
  var rows = document.querySelectorAll('#amaa-essays tbody tr');
  var total = rows.length, onTsap = 0, onEdrl = 0, notEdrl = 0;
  rows.forEach(function(row){
    var edrlCell = row.querySelector('td.edrl');
    var tsapCell = row.querySelector('td.tsap');
    if(edrlCell && edrlCell.textContent.trim() === 'Y') onEdrl++;
    if(edrlCell && edrlCell.textContent.trim() === 'N') notEdrl++;
    if(tsapCell && tsapCell.querySelector('a')) onTsap++;
  });
  var tally = document.getElementById('amaa-tally');
  tally.innerHTML =
    '<div class="amaa-tally-item">Total entries <span>' + total + '</span></div>' +
    '<div class="amaa-tally-item">On TSAP <span>' + onTsap + '</span></div>' +
    '<div class="amaa-tally-item">In EDRL <span>' + onEdrl + '</span></div>' +
    '<div class="amaa-tally-item">Not in EDRL <span>' + notEdrl + '</span></div>';
})();
</script>
