import csv, json

input_file = "whc-sites-2025.csv"
output_file = "whc-sites-2025.json"

rows = []

with open(input_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        row = {
            "id_no": r["id_no"],
            "name_en": r["name_en"],
            "name_zh": r["name_zh"],
            "longitude": float(r["longitude"]) if r["longitude"] else None,
            "latitude": float(r["latitude"]) if r["latitude"] else None,
            "category": r["category"]
        }
        rows.append(row)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print("Done! JSON saved to", output_file)
