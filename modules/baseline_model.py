
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset beside this script
csv_path = Path(__file__).resolve().parent / "study_hours.csv"
df = pd.read_csv(csv_path)

# Select the input feature and prediction target
X = df[["sleep_hours"]]
y = df["hours"]

# Reserve 20% of the rows for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a baseline that always predicts the training mean
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)
baseline_predictions = baseline.predict(X_test)

# Train a model that learns a linear relationship
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Calculate evaluation metrics
for name, pred in [
    ("Baseline", baseline_predictions),
    ("Linear Regression", predictions),
]:
    mae = mean_absolute_error(y_test, pred)
    mse = mean_squared_error(y_test, pred)
    r2 = r2_score(y_test, pred)

    print(f"\n{name}")
    print(f"MAE:  {mae:.3f}")
    print(f"MSE:  {mse:.3f}")
    print(f"R²:   {r2:.3f}")

# Display actual and predicted values
print("\nActual:", y_test.to_list())
print("Predicted:", predictions.round(2).tolist())
