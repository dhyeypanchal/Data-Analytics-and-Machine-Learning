# Exploring data analysis and manipulation using pandas
# EDA means exploring and understanding your data before deciding which model to use.

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


directory = Path(__file__).resolve().parent  # Get the directory of the current script

file_path = directory / "study_hours.csv"

df = pd.read_csv(file_path)

# Inspect dimensions, types, and missing values
print(df.shape)
print(df.dtypes)
print(df.isna().sum())

# Check duplicate records
print("Duplicates:", df.duplicated().sum())

# Review distributions and unusual values
print(df.describe(include="all"))

# Inspect relationships between numeric variables
print(df.select_dtypes(include="number").corr())

# Plot the distribution of study hours
df["hours"].dropna().hist(bins=10)

plt.xlabel("Study hours")
plt.ylabel("Number of observations")
plt.title("Distribution of Study Hours")
plt.tight_layout()
plt.show()