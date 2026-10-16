
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error

# Load the CSV beside this Python script
csv_path = Path(__file__).resolve().parent / "study_hours.csv"
df = pd.read_csv(csv_path)

# Select input features and the value to predict
X = df[["hours", "sleep_hours"]]
y = df["hours"]  # Example target: predict study hours

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a baseline that always predicts the training mean
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)

# Predict values for the test set
predictions = baseline.predict(X_test)

# Calculate average absolute prediction error
mae = mean_absolute_error(y_test, predictions)
print("Actual values:", y_test.to_list())
print("Predictions:", predictions)
print("Baseline MAE:", mae)
