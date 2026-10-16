import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

# Create a small example dataset
df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "exam_score":  [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
})

# Separate input features (X) from the target (y)
X = df[["study_hours"]]
y = df["exam_score"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict scores for unseen test observations
predictions = model.predict(X_test)

# Evaluate prediction errors
print("MAE:", mean_absolute_error(y_test, predictions))
print("RMSE:", root_mean_squared_error(y_test, predictions))