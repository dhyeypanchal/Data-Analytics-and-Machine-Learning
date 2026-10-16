score = 82

if score >= 90:
    result = "Excellent"
elif score >= 75:
    result = "Good"
else:
    result = "Needs improvement"

print(result)

# An empty list is falsey. So are 0, 0.0, "", None, and empty dictionaries and sets.
if []:
    print("This will not print because the list is empty.")
else:
    print("This will print because the list is empty, which is considered falsey.")