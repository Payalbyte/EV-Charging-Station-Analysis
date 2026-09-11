import pandas as pd
import numpy as np
from pathlib import Path

# Get the project folder path
project_folder = Path(__file__).resolve().parent.parent

# Load dataset
file_path = project_folder / "data" / "ev-charging-stations-india.csv"

ev_data = pd.read_csv(file_path)

# Display the first 5 rows
print("=" * 70)
print("1. FIRST 5 ROWS OF THE DATASET")
print("=" * 70)

print(ev_data.head(), "\n")


# Display the last 5 rows
print("=" * 70)
print("2. LAST 5 ROWS OF THE DATASET")
print("=" * 70)

print(ev_data.tail(), "\n")

# Check the number of rows and columns
print("=" * 70)
print("3. DATASET SHAPE")
print("=" * 70)

print(f"Rows    : {ev_data.shape[0]}")
print(f"Columns : {ev_data.shape[1]}\n")

# Display all column names
print("=" * 70)
print("4. COLUMN NAMES")
print("=" * 70)

for i, column in enumerate(ev_data.columns, start=1):
    print(f"{i}. {column}")

print()

# Check dataset information and data types
print("=" * 70)
print("5. DATASET INFORMATION")
print("=" * 70)

ev_data.info()

print()

# Generate a statistical summary of numerical columns
print("=" * 70)
print("6. STATISTICAL SUMMARY")
print("=" * 70)

print(ev_data.describe(), "\n")

# Check the number of missing values in each column
print("=" * 70)
print("7. MISSING VALUES")
print("=" * 70)

print(ev_data.isnull().sum(), "\n")

# Check the number of duplicate records
print("=" * 70)
print("8. DUPLICATE RECORDS")
print("=" * 70)

print(f"Duplicate Records : {ev_data.duplicated().sum()}\n")