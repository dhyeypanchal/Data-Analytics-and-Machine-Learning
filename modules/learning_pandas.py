# Lesson 5 — Pandas: cleaning, analyzing, and preparing real datasets

import pandas as pd

# Create a Series (one column of data)
hours = pd.Series([2.0, 1.5, 3.0], name="hours")
print(hours)

# Create a DataFrame (a table with multiple columns)
df = pd.DataFrame({
    "day": ["Monday", "Tuesday", "Wednesday"],
    "hours": [2.0, 1.5, 3.0],
    "sleep_hours": [7.5, 6.5, 8.0]
})

print(df)  # Display the complete table