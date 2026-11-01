import csv
from pathlib import Path

base = Path(__file__).resolve().parent
csv_file = base / "Students_data.csv"
output_file = base / "Students_data_updated.csv"

with csv_file.open("r", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

if not fieldnames or "Course" not in fieldnames:
    raise ValueError("CSV must contain a Course column")

for row in rows[:10]:
    row["Course"] = "MCA"

with output_file.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Updated", min(10, len(rows)), "student records.")
print("Output saved to:", output_file)
