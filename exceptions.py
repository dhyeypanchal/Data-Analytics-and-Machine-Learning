raw_value = "d.5"

try:
    value = float(raw_value)
except ValueError:
    print("Invalid numeric input")
else:
    print(f"Value: {value}")