import pandas as pd
import matplotlib.pyplot as plt

# Create a small example dataset
df = pd.DataFrame({
    "study_hours": [2, 4, 6, 8, 10, 3, 7, 5, 9, 4],
    "sleep_hours": [5, 6, 7, 8, 7, 5, 8, 6, 7, 7],
    "exam_score":  [45, 55, 65, 80, 90, 48, 78, 62, 85, 58]
})

# Display the dataset
print(df)

# Count missing values in each column
print(df.isnull().sum())

# Count duplicate rows
print(df.duplicated().sum())

# Count distinct values in each column
print(df.nunique())

# Create a histogram of exam scores
# plt.hist(df["exam_score"], bins=5, edgecolor="black")

# # Add a title and axis labels
# plt.title("Distribution of Exam Scores")
# plt.xlabel("Exam Score")
# plt.ylabel("Number of Students")

# Display the plot
# plt.show()

# Plot study hours against exam scores
# plt.scatter(df["study_hours"], df["exam_score"])

# # Label the plot
# plt.title("Study Hours vs Exam Score")
# plt.xlabel("Study Hours")
# plt.ylabel("Exam Score")

# # Display the plot
# plt.show()

# Calculate correlations between numerical columns
correlations = df.corr()

# Display the correlation matrix
# print(correlations)


# Create a box plot of exam scores
# plt.boxplot(df["exam_score"])

# plt.title("Box Plot of Exam Scores")
# plt.ylabel("Exam Score")
# plt.show()


# Calculate Pearson correlations between numerical columns
correlations = df.corr(numeric_only=True)

print(correlations)

# Show the relationship between study hours and exam score
print(correlations.loc["study_hours", "exam_score"])