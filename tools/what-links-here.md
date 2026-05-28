{% include under-construction.html %}

{% assign all_content = site.pages | concat: site.documents %}

{% assign requested_page = "/sunil/" %}
{% assign backlinks = site.data.backlinks[requested_page] %}

{% assign target_page = all_content | where: "url", requested_page | first %}

<div class="backlinks-tool">

  <div class="backlinks-header">

    <h2>What Links Here</h2>

    <div class="backlinks-controls">

      <label for="backlinkSearch">
        Search backlinks
      </label>

      <input
        type="search"
        id="backlinkSearch"
        placeholder="Type to filter results..."
        aria-label="Search backlinks">

      <label for="backlinkSort">
        Sort
      </label>

      <select id="backlinkSort">
        <option value="az">A–Z</option>
        <option value="za">Z–A</option>
      </select>

    </div>

    <p class="backlinks-target">

      <strong>Page:</strong>

      {% if target_page %}
        {{ target_page.title }}
      {% else %}
        {{ requested_page }}
      {% endif %}

    </p>

    {% if backlinks %}
      <p class="backlinks-count">
        Total backlinks: {{ backlinks.size }}
      </p>
    {% endif %}

  </div>

  {% if backlinks %}

    <ul class="backlinks-list" id="backlinksList">

      {% for source in backlinks %}

        {% assign source_page = all_content | where: "url", source | first %}

        <li class="backlink-item">

          {% if source_page %}

            <a href="{{ source }}">
              {{ source_page.title }}
            </a>

          {% else %}

            <a href="{{ source }}" class="unresolved-link">
              {{ source }}
            </a>

          {% endif %}

        </li>

      {% endfor %}

    </ul>

  {% else %}

    <p>No backlinks found.</p>

  {% endif %}

</div>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const searchBox = document.getElementById("backlinkSearch");
  const sortSelect = document.getElementById("backlinkSort");
  const list = document.getElementById("backlinksList");

  if (!list) return;

  function sortItems() {

    const items = Array.from(list.querySelectorAll(".backlink-item"));

    items.sort((a, b) => {

      const textA = a.innerText.trim().toLowerCase();
      const textB = b.innerText.trim().toLowerCase();

      if (sortSelect.value === "za") {
        return textB.localeCompare(textA);
      }

      return textA.localeCompare(textB);

    });

    items.forEach(item => list.appendChild(item));

  }

  function filterItems() {

    const query = searchBox.value.toLowerCase();

    list.querySelectorAll(".backlink-item").forEach(item => {

      const text = item.innerText.toLowerCase();

      item.style.display = text.includes(query) ? "" : "none";

    });

  }

  sortSelect.addEventListener("change", sortItems);
  searchBox.addEventListener("input", filterItems);

});
</script>

<style>
.backlinks-tool {
  margin-top: 2rem;
}

.backlinks-header {
  margin-bottom: 1.5rem;
}

.backlinks-header h2 {
  margin-bottom: 1rem;
}

.backlinks-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: center;
  margin-bottom: 1rem;
}

.backlinks-controls label {
  font-weight: 600;
}

.backlinks-controls input,
.backlinks-controls select {
  padding: 0.55rem 0.7rem;
  border: 1px solid #666;
  border-radius: 6px;
  font-size: 1rem;
}

.backlinks-controls input {
  min-width: 260px;
  max-width: 100%;
}

.backlinks-target,
.backlinks-count {
  color: #444;
}

.backlinks-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.backlink-item {
  margin-bottom: 0.75rem;
  padding: 0.85rem 1rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #fafafa;
}

.backlink-item a {
  text-decoration: none;
}

.backlink-item a:hover {
  text-decoration: underline;
}

.unresolved-link {
  font-family: monospace;
}

.backlinks-controls input:focus,
.backlinks-controls select:focus {
  outline: 3px solid #1f5fbf;
  outline-offset: 2px;
}

@media (prefers-color-scheme: dark) {

  .backlinks-target,
  .backlinks-count {
    color: #d0d0d0;
  }

  .backlinks-controls input,
  .backlinks-controls select {
    background: #222;
    color: #eee;
    border-color: #666;
  }

  .backlink-item {
    background: #1e1e1e;
    border-color: #444;
  }

}

@media (max-width: 700px) {

  .backlinks-controls {
    flex-direction: column;
    align-items: stretch;
  }

  .backlinks-controls input {
    min-width: auto;
    width: 100%;
  }

}
</style>
