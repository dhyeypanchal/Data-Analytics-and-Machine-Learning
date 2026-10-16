import pandas as pd

df = pd.DataFrame({
    "study_hours": [2, 4, None, 5, 6],
    "exam_score": [45, 60, 55, 70, 75]
})

# Count missing values in each column
print(df.isnull().sum())

# Fill missing study hours with the median
df["study_hours"] = df["study_hours"].fillna(
    df["study_hours"].median()
)

# print(df)

df = pd.DataFrame({
    "student": ["A", "B", "B", "C"],
    "study_hours": [2, 4, 4, -3],
    "score": [50, 65, 65, 70]
})

# Count duplicate rows
print(df.duplicated().sum())

# Remove exact duplicate rows
df = df.drop_duplicates()

# Find potentially invalid study hours
# print(df[df["study_hours"] < 0])


df = pd.DataFrame({
    "city": ["London", "Toronto", "London"]
})

# One-hot encoding
df = pd.get_dummies(df, columns=["city"], dtype=int)
print(df)