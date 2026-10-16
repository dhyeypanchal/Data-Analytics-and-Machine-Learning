from pathlib import Path

data_dir = Path("data")  # Refer to the project's data folder
file_path = data_dir / "study_hours.csv"  # Build the file path

print(file_path)  # data/study_hours.csv
print(file_path.exists())  # Check whether the file existsfrom pathlib import Path

data_dir = Path("data")  # Refer to the project's data folder
file_path = data_dir / "study_hours.csv"  # Build the file path

print(file_path)  # data/study_hours.csv
print(file_path.exists())  # Check whether the file exists