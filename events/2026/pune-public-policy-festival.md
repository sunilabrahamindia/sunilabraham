{% assign props = site.data.properties %}

<section class="tsapdata" vocab="https://schema.org/" typeof="Event">

  <table class="tsapdata-table">
    <tbody>

      {% if page.event_type %}
      <tr>
        <th class="tsapdata-prop" scope="row">{{ props.event_type.label }}</th>
        <td class="tsapdata-val" property="additionalType">{{ page.event_type }}</td>
      </tr>
      {% endif %}

      {% if page.date %}
      <tr>
        <th class="tsapdata-prop" scope="row">{{ props.date.label }}</th>
        <td class="tsapdata-val" property="startDate">{{ page.date | date: "%-d %B %Y" }}</td>
      </tr>
      {% endif %}

      {% if page.location %}
      <tr>
        <th class="tsapdata-prop" scope="row">{{ props.location.label }}</th>
        <td class="tsapdata-val" property="location">{{ page.location }}</td>
      </tr>
      {% endif %}

      {% if page.sunils_role %}
      <tr>
        <th class="tsapdata-prop" scope="row">{{ props.sunils_role.label }}</th>
        <td class="tsapdata-val">
          {% for role in page.sunils_role %}
          <div class="tsapdata-multival">{{ role }}</div>
          {% endfor %}
        </td>
      </tr>
      {% endif %}

      {% if page.organisers %}
      <tr>
        <th class="tsapdata-prop" scope="row">{{ props.organisers.label }}</th>
        <td class="tsapdata-val" property="organizer">
          {% for org in page.organisers %}
          <div class="tsapdata-multival">{{ org }}</div>
          {% endfor %}
        </td>
      </tr>
      {% endif %}

      {% if page.website %}
      <tr>
        <th class="tsapdata-prop" scope="row">{{ props.website.label }}</th>
        <td class="tsapdata-val" property="url">
          {% for url in page.website %}
          <div class="tsapdata-multival">
            <a href="{{ url }}" rel="noopener noreferrer">{{ url }}</a>
          </div>
          {% endfor %}
        </td>
      </tr>
      {% endif %}

    </tbody>
  </table>

</section>

<style>
.tsapdata {
  width: 100%;
  box-sizing: border-box;
  margin: 1.5rem 0;
  font-family: inherit;
}

.tsapdata-table {
  width: 100%;
  border-collapse: collapse;
  border-top: 1px solid #c8ccd1;
  border-bottom: 1px solid #c8ccd1;
  border-left: none;
  border-right: none;
  background: #ffffff;
  table-layout: auto;
}

.tsapdata-prop {
  width: 30%;
  background: #f8f9fa;
  color: #3a3a3a;
  font-weight: normal;
  font-size: inherit;
  vertical-align: top;
  padding: 0.4rem 0.6rem;
  border-top: 1px solid #c8ccd1;
  border-bottom: 1px solid #c8ccd1;
  border-left: none;
  border-right: none;
}

.tsapdata-val {
  background: #ffffff;
  color: #202122;
  font-weight: 500;
  vertical-align: top;
  padding: 0.4rem 0.6rem;
  border-top: 1px solid #c8ccd1;
  border-bottom: 1px solid #c8ccd1;
  border-left: 1px solid #c8ccd1;
  border-right: none;
  word-break: break-word;
  line-height: 1.5;
}

.tsapdata-multival {
  padding: 0.15rem 0;
  border-bottom: 1px solid #eaecf0;
}

.tsapdata-multival:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.tsapdata-multival:first-child {
  padding-top: 0;
}

.tsapdata-val a {
  color: #3366cc;
  text-decoration: none;
}

.tsapdata-val a:hover {
  text-decoration: underline;
}

@media (max-width: 500px) {
  .tsapdata-prop {
    width: 110px;
    white-space: normal;
  }
}
</style>
