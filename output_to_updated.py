import json

with open('output_mapped.json', 'r') as f:
    output_mapped = json.load(f)

mapped_updated = {}

for i in output_mapped.keys():
    if output_mapped[i] == "":
        pass
    else:
        mapped_updated[i] = output_mapped[i]

with open('mapped-updated.json', 'w', encoding='utf-8') as f:
    json.dump(mapped_updated, f, ensure_ascii=False, indent=4)