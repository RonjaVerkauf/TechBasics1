import csv
import random
import heapq
from collections import defaultdict

# Dateipfade
input_file = "grades.csv"
output_file = "grades_updated.csv"

# Wochen (ohne Woche 6)
weeks = [f"Week {i}" for i in range(1, 14) if i != 6]

# Zufallsnote
def random_grade():
    return random.choice([0, 1, 2, 3])

# Datenstrukturen für Bonusausgabe
stream_totals = defaultdict(list)
week_totals = defaultdict(list)

try:
    with open(input_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ["Total Points", "Average Points"]
        students = []

        for row in reader:
            grades = []
            for week in weeks:
                value = row.get(week, "").strip()
                if value == "":
                    value = str(random_grade())
                    row[week] = value
                try:
                    grade = int(value)
                except ValueError:
                    grade = 0
                grades.append(grade)
                week_totals[week].append(grade)

            total = sum(heapq.nlargest(10, grades))
            avg = round(sum(grades) / len(grades), 2)

            row["Total Points"] = total
            row["Average Points"] = avg

            stream = row.get("Stream", "Unknown")
            stream_totals[stream].append(avg)
            students.append(row)

    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    # Bonusausgabe
    print("\n🎓 Durchschnittliche Punkte nach Stream:")
    for stream, values in stream_totals.items():
        avg = round(sum(values) / len(values), 2)
        print(f"  ➤ Stream {stream}: {avg} Punkte")

    print("\n Durchschnittliche Punkte pro Woche:")
    for week in sorted(week_totals.keys(), key=lambda w: int(w.split()[1])):
        avg = round(sum(week_totals[week]) / len(week_totals[week]), 2)
        print(f"   {week}: {avg} Punkte")

except FileNotFoundError:
    print("❌ Fehler: Die Datei 'grades.csv' wurde nicht gefunden.")
