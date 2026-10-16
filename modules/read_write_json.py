import json

student = {"name": "D.A.", "hours": 2.5, "active": True}

# Convert a Python dictionary into a JSON file
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=2)

# Load JSON back into a Python object
with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)
    
print(loaded_student["hours"])  # 2.5