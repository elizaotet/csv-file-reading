import csv
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "logs.csv"

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)

    d = {}
    for row in reader:
        if row["status"] == "OK":
            model = row["model"]
            run = row["run_id"]
            if model not in d:
                d[model] = []
            d[model].append(int(row["duration_seconds"]))
    for key in d:
        total = 0
        for i in range(len(d[key])):
            total += d[key][i]
        count = len(d[key])
        average = total / count
        print(f"{key}: {average} seconds average ({count} successful runs)")
