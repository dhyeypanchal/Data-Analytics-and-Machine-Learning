from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler

# X contains input features; y contains the target we want to predict

# Create a small example dataset
df = pd.DataFrame({
    "study_hours": [2, 4, 6, 8, 10, 3, 7, 5, 9, 4],
    "sleep_hours": [5, 6, 7, 8, 7, 5, 8, 6, 7, 7],
    "exam_score":  [45, 55, 65, 80, 90, 48, 78, 62, 85, 58]
})
X = df[["study_hours", "sleep_hours"]]
y = df["exam_score"]

# Reserve 20% of observations for final evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# print("Training rows:", len(X_train))
# print("Testing rows:", len(X_test))

scaler = StandardScaler()

# Learn the mean and standard deviation from training data only
X_train_scaled = scaler.fit_transform(X_train)

# Reuse the same parameters for the test data
X_test_scaled = scaler.transform(X_test)