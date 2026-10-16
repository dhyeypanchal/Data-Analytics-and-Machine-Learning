import pandas as pd
from pathlib import Path

# Load a CSV file into a DataFrame
script_dir = Path(__file__).resolve().parent  # Get the directory of the current script
csv_file_path = script_dir / "study_hours.csv"  # Build
df = pd.read_csv(csv_file_path)

study_hour = df[['day','hours']]
# print(study_hour,'print study_hour')

# print(df.head())       # Preview the first 5 rows
# print(df.shape)        # Number of rows and columns
# print(df.columns)      # Column names
# print(df.dtypes)       # Data type of each column
# print(df.info())       # Non-null counts and data types
# print(df.describe())   # Summary statistics for numeric columns


# # Select rows by index labels
# print(df.loc[0])  # Row labeled 0

# # Select rows by integer position
# print(df.iloc[0])  # First row by position

# # Select rows 0 and 1, and columns
# print(df.loc[0:1, ["hours", "day"]])  # Rows 0 and 1, specific columns

# # Select first two rows and first two columns by position
# print(df.iloc[0:2, 0:2])


# for text matching, use str.contains() with regex
# Find days whose names contain "day"
matching = df[df["day"].str.contains("mon", case=False, na=False)]
# print(matching)

# Keep rows with at least 2 study hours
productive = df[df["hours"] >= 2]

# Keep rows meeting two conditions
filtered = df[(df["hours"] >= 2) & (df["sleep_hours"] >= 7)]

# Keep rows meeting either condition
either = df[(df["hours"] >= 3) | (df["sleep_hours"] >= 8)]

# Keep records from selected days
selected = df[df["day"].isin(["Monday", "Wednesday"])]

# print(productive)
# print(filtered)
# print(either)
# print(selected)

# Create a new column using an existing column
df["hours_minutes"] = df["hours"] * 60

# Create a category based on a condition
df["productive"] = df["hours"] >= 2

# Create a ratio between two columns
df["study_sleep_ratio"] = df["hours"] / df["sleep_hours"]

# Build an example with a missing value
df = pd.DataFrame({
    "hours": [2.0, None, 3.0, 1.5,2.0],
    "sleep_hours": [7.5, 6.0, None, 8.0,7.5]
})

# print(df.isna())          # True where values are missing
# print(df.isna().sum())    # Missing count per column
# print(df.isna().mean())   # Fraction missing per column


# Remove rows containing at least one missing value
complete_rows = df.dropna() # it will do shallow copy of the dataframe and remove rows with missing values, and not change existing dataframe
# print(complete_rows.head())

# Fill missing values in one column with its median
df["hours_filled"] = df["hours"].fillna(df["hours"].median())

# print(df.duplicated().sum(),df.head())  # Count duplicate rows and preview the first 5 rows
df.drop_duplicates(inplace=True)  # Remove duplicate rows in place
# print(df.duplicated().sum(),df.head())

# Sort from highest to lowest study hours
ranked = df.sort_values("hours", ascending=False)

# Show the 3 highest records
top_three = ranked.head(3)
# print(top_three)

df = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E"],
    "program": ["SE", "CS", "SE", "CS", "SE"],
    "hours": [2, 3, 4, 1, 5]
})

# Calculate average study hours for each program
summary = df.groupby("program")["hours"].mean()
# print(summary)

# Summarize each program with multiple statistics
summary = df.groupby("program")["hours"].agg(
    ["count", "mean", "median", "min", "max"]
)


# print(summary)


# now let we see how to merge two dataframes (it is similar to SQL join operation)

students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

results = pd.DataFrame({
    "student_id": [1, 2, 3],
    "score": [80, 90, 75]
})

# Join the tables using their shared key
combined = pd.merge(students, results, on="student_id", how="inner")

print(combined)


import pandas as pd

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6],
    "sleep_hours": [6, 7, 7, 8, 8, 9],
    "exam_score": [50, 60, 65, 75, 82, 90]
})

# X contains the input features
X = df[["study_hours", "sleep_hours"]]

# y contains the value the model must predict
y = df["exam_score"]