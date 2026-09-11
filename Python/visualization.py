import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

from folium.plugins import (
    Fullscreen,
    MiniMap,
    MousePosition
)
from pathlib import Path

# Get the project folder path
project_folder = Path(__file__).resolve().parent.parent

# Load dataset
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
    "Uttarkhand": "Uttarakhand",
    "Uttrakhand": "Uttarakhand",
    "Westbengal": "West Bengal",
    "Jammu And Kashmir": "Jammu And Kashmir",
    "Pondicherry": "Puducherry",
    "Hyderabadu00A0": "Hyderabad"
}

ev_data["state"] = ev_data["state"].replace(state_corrections)

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

# Correct remaining state names
state_corrections = {
    "Tamilnadu": "Tamil Nadu",
    "Telengana": "Telangana",
    "Chattisgarh": "Chhattisgarh",
    "Delhi Ncr": "Delhi",
    "Andaman": "Andaman And Nicobar Islands"
}

ev_data["state"] = ev_data["state"].replace(state_corrections)

state_count = ev_data["state"].value_counts()

# Find top 10 cities
top_cities = ev_data["city"].value_counts().head(10)

# Create bar chart
plt.figure(figsize=(10,5))

top_cities.plot(kind="bar", color="orange")

plt.title("Top 10 Cities with Highest EV Charging Stations")

plt.xlabel("City")

plt.ylabel("Number of Charging Stations")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# Clean inconsistent state names
ev_data["state"] = ev_data["state"].replace(state_corrections)

# Create a bar chart for state-wise charging stations
state_count = ev_data["state"].value_counts()

plt.figure(figsize=(12,6))
state_count.plot(kind="bar", color="skyblue")

plt.title("Number of EV Charging Stations by State")
plt.xlabel("State")
plt.ylabel("Number of Charging Stations")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

#Analyze top 5 distribution of charging station type using a pie chart
charging_type= ev_data['type'].value_counts().head(5)

plt.figure(figsize=(8,8))

plt.pie(
    charging_type,
    labels= charging_type.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Top 5 EV charging station types")

plt.tight_layout()
plt.show()

# Display the top 10 states with the highest number of EV charging stations
top_states = ev_data["state"].value_counts().head(10)

plt.figure(figsize=(10,6))

top_states.plot(kind="barh", color="green")

plt.title("Top 10 States with Highest EV Charging Stations")

plt.xlabel("Number of Charging Stations")
plt.ylabel("State")

plt.tight_layout()

plt.show()


# Convert latitude and longitude into numeric values
ev_data["lattitude"] = pd.to_numeric(ev_data["lattitude"], errors="coerce")
ev_data["longitude"] = pd.to_numeric(ev_data["longitude"], errors="coerce")

# Remove rows with missing coordinates
location_data = ev_data.dropna(subset=["lattitude", "longitude"])


## Create an interactive map to visualize EV charging station locations

# Remove rows with missing coordinates
map_data = ev_data.dropna(subset=["lattitude", "longitude"])

# Keep only valid coordinates within India's range
map_data = map_data[
    (map_data["lattitude"] >= 6) &
    (map_data["lattitude"] <= 38) &
    (map_data["longitude"] >= 68) &
    (map_data["longitude"] <= 98)
]
print(map_data.shape)
print(map_data[["lattitude", "longitude"]].head())

# Create an interactive map
india_map = folium.Map(
    location=[22.5, 78.9],
    zoom_start=5,
    tiles=None,
    control_scale= True
)
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Esri World Street Map"
).add_to(india_map)

# Full Screen Button
Fullscreen().add_to(india_map)

# Mini Map
MiniMap(toggle_display=True).add_to(india_map)

# Show Mouse Latitude & Longitude
MousePosition().add_to(india_map)

# Add EV Charging Stations
for _, row in map_data.iterrows():

    popup_html = f"""
    <div style="width:260px">
        <h4 style="color:green;">⚡ EV Charging Station</h4>
        <hr>

        <b>🏢 Station:</b> {row['name']}<br><br>

        <b>📍 City:</b> {row['city']}<br>

        <b>🗺 State:</b> {row['state']}<br>

        <b>🔌 Type:</b> {row['type']}<br>

        <b>🏠 Address:</b><br>
        {row['address']}
    </div>
    """

    folium.Marker(
        location=[row["lattitude"], row["longitude"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=f"⚡ {row['name']}",
        icon=folium.Icon(
            color="green",
            icon="bolt",
            prefix="fa"
        )
    ).add_to(india_map)

# Layer Control
folium.LayerControl().add_to(india_map)

# Save map as HTML file
india_map.save("ev_charging_station_map.html")

print("=" * 70)
print("✅ Interactive EV Charging Station Map Created Successfully.")
print("=" * 70)

