import json

with open("whc-sites-2025.json", encoding="utf-8") as f:
    data = json.load(f)

with open("whc-sites-2025.js", "w", encoding="utf-8") as f:
    f.write("const heritageData = ")
    json.dump(data, f, ensure_ascii=False)
    f.write(";")
