import yaml
from pathlib import Path

output = {
    "broken_links": [
        {
            "source": "/test-page/",
            "target": "/missing-page/"
        }
    ]
}

with open("_data/broken_links.yml", "w", encoding="utf-8") as f:
    yaml.dump(output, f, allow_unicode=True, sort_keys=False)

print("Generated _data/broken_links.yml")