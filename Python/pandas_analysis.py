import pandas as pd
import numpy as np
from pathlib import Path

# Get the project folder path
project_folder = Path(__file__).resolve().parent.parent

# Load dataset from folder
file_path = project_folder / "data" / "ev-charging-stations-india.csv"
ev_data = pd.read_csv(file_path)

# Remove extra spaces
ev_data["state"] = ev_data["state"].str.strip()

# Convert to title case
ev_data["state"] = ev_data["state"].str.title()

# Correct spelling variations
state_corrections = {
    "Harayana": "Haryana",
    "Andhrapradesh": "Andhra Pradesh",
    "Andra Pradesh": "Andhra Pradesh",
    "Karala": "Kerala",
    "Maharashra": "Maharashtra",
    "Taminadu": "Tamil Nadu",
    "Tamilnadu": "Tamil Nadu",
    "Tamilnadu ": "Tamil Nadu",
    "Telengana": "Telangana",
    "Westbengal": "West Bengal",
    "Chattisgarh": "Chhattisgarh",
    "Uttarkhand": "Uttarakhand",
    "Uttrakhand": "Uttarakhand",
    "Delhi Ncr": "Delhi",
    "Pondicherry": "Puducherry",
    "Hyderabadu00A0": "Hyderabad",
    "Andaman": "Andaman And Nicobar Islands",
    "Jammu & Kashmir": "Jammu And Kashmir"
}

ev_data["state"] = ev_data["state"].replace(state_corrections)

# Cities mistakenly stored in state column
city_to_state = {
    "Bhubhaneswar": "Odisha",
    "Chikhali": "Maharashtra",
    "Ernakulam": "Kerala",
    "Hisar": "Haryana",
    "Hyderabad": "Telangana",
    "Jajpur": "Odisha",
    "Kochi": "Kerala",
    "Limbdi": "Gujarat",
    "Rajahmundry": "Andhra Pradesh"
}

ev_data["state"] = ev_data["state"].replace(city_to_state)

# Count the number of charging stations in each state
state_counts = ev_data["state"].value_counts()

print("=" * 70)
print("1. CHARGING STATIONS BY STATE")
print("=" * 70)

print(state_counts ,"\n" )


# Find the top 10 cities with the highest number of charging stations
top_cities = ev_data["city"].value_counts().head(10)

print("=" * 70)
print("2. TOP 10 CITIES WITH THE HIGHEST EV CHARGING STATIONS ")
print("=" * 70)

print(top_cities, "\n")


#  Count the number of charging stations by charging type
charging_type_counts = ev_data["type"].value_counts()

print("=" * 70)
print("3. NO. OF CHARGING STATIONS BY CHARGING TYPE")
print("=" * 70)

print(charging_type_counts, "\n")


# Find the top 10 states with the highest number of charging stations
top_states = ev_data["state"].value_counts().head(10)

print("=" * 70)
print("4. TOP 10 STATES WITH THE HIGHEST EV CHARGING STATIONS")
print("=" * 70)

print(top_states, "\n")


# Count the number of unique states
unique_states = ev_data["state"].nunique()

print("=" * 70)
print("5. NUMBER OF UNIQUE STATES")
print("=" * 70)

print(f"Unique States : {unique_states} \n")


# Count the number of unique cities
unique_cities = ev_data["city"].nunique()

print("=" * 70)
print("6. NUMBER OF UNIQUE CITIES")
print("=" * 70)

print(f"Unique Cities : {unique_cities} \n")


# Count the number of unique charging types
unique_types = ev_data["type"].nunique()

print("=" * 70)
print("7. NUMBER OF UNIQUE CHARGING TYPES")
print("=" * 70)

print(f"Unique Charging Types : {unique_types} \n")


# Find the cities that have more than one charging station
multiple_station_cities = ev_data["city"].value_counts()
multiple_station_cities = multiple_station_cities[multiple_station_cities > 1]

print("=" * 70)
print("8. CITIES WITH MORE THAN ONE CHARGING STATION")
print("=" * 70)

print(multiple_station_cities)