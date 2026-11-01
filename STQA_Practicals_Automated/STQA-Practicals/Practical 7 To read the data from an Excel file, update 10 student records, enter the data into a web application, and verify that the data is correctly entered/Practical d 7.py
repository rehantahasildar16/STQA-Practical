import csv
from pathlib import Path

base = Path(__file__).resolve().parent
csv_file = base / "Students_data.csv"

with csv_file.open("r", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print("Roll No\tName\tCourse")
for row in rows[:10]:
    print(row["Roll No"], row["Name"], row["Course"], sep="\t")
print("\nTotal student records:", len(rows))
