import pandas as pd
import numpy as np
from pathlib import Path

# Get the project folder path
project_folder = Path(__file__).resolve().parent.parent

# Load dataset form folder
file_path = project_folder / "data" / "ev-charging-stations-india.csv"
ev_data = pd.read_csv(file_path)

# Convert latitude and longitude into numeric values
ev_data["lattitude"] = pd.to_numeric(ev_data["lattitude"], errors="coerce")
ev_data["longitude"] = pd.to_numeric(ev_data["longitude"], errors="coerce")

# Remove rows with missing coordinates
ev_data = ev_data.dropna(subset=["lattitude", "longitude"])

# Keep only valid coordinates within India's range
ev_data = ev_data[
    (ev_data["lattitude"] >= 6) &
    (ev_data["lattitude"] <= 38) &
    (ev_data["longitude"] >= 68) &
    (ev_data["longitude"] <= 98)
]

# Calculate the average latitude and longitude of all charging stations
average_latitude = np.mean(ev_data["lattitude"])
average_longitude = np.mean(ev_data["longitude"])

print("=" * 70)
print("1. AVERAGE LATITUDE AND LONGITUDE")
print("=" * 70)

print(f"Average Latitude  : {average_latitude:.4f}")
print(f"Average Longitude : {average_longitude:.4f}\n")


# Calculate the median  of latitude and longitude 
median_latitude = np.median(ev_data["lattitude"])
median_longitude = np.median(ev_data["longitude"])

print("\n" + "=" * 70)
print("2. MEDIAN LATITUDE AND LONGITUDE")
print("=" * 70)

print(f"Median Latitude   : {median_latitude:.4f}")
print(f"Median Longitude  : {median_longitude:.4f} \n")


# Calculate the standard deviation of latitude and longitude
latitude_std = np.std(ev_data["lattitude"])
longitude_std = np.std(ev_data["longitude"])

print("\n" + "=" * 70)
print("3. STANDARD DEVIATION")
print("=" * 70)

print(f"Latitude Standard Deviation  : {latitude_std:.4f}")
print(f"Longitude Standard Deviation : {longitude_std:.4f} \n")

# Find the minimum and maximum latitude
minimum_latitude = np.min(ev_data["lattitude"])
maximum_latitude = np.max(ev_data["lattitude"])

print("\n" + "=" * 70)
print("4. MINIMUM AND MAXIMUM LATITUDE")
print("=" * 70)

print(f"Minimum Latitude : {minimum_latitude:.4f}")
print(f"Maximum Latitude : {maximum_latitude:.4f} \n")

# Find the minimum and maximum longitude
minimum_longitude = np.min(ev_data["longitude"])
maximum_longitude = np.max(ev_data["longitude"])

print("\n" + "=" * 70)
print("5. MINIMUM AND MAXIMUM LONGITUDE")
print("=" * 70)

print(f"Minimum Longitude : {minimum_longitude:.4f}")
print(f"Maximum Longitude : {maximum_longitude:.4f}")