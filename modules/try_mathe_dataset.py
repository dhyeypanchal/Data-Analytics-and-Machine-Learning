from pathlib import Path
import csv

file_path = Path("modules")/"MathE_dataset_comma_separated.csv"

with open(file_path, "r", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
# print(rows)  # Print the first row of the CSV file as a dictionary
# print(rows[0])  # Print the first row of the CSV file as a dictionary
print(rows[1]['Keywords'])  # Print the first row of the CSV file as a dictionary