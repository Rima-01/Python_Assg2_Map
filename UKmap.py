import pandas as pd # To read the dataset into a dataframe
import matplotlib.pyplot as plt # matplotlib to plot map as a background and plot sensors on it.
from PIL import Image # Python Imaging Library to load the map image.

# Define the bounding box for the map
LONG_MIN = -10.592
LONG_MAX = 1.6848
LAT_MIN = 50.681
LAT_MAX = 57.985

# File paths
data_path = 'GrowLocations.csv'
map_path = 'map7.png'

# Read the GrowLocations dataset into a DataFrame
def read_and_clean_data(data_path):
    # Read the CSV file
    try:
        df = pd.read_csv(data_path)
        print("Data loaded successfully!")
    except Exception as e:
        print("Error reading file:", e)
        return None

    # Swap Latitude and Longitude columns
    df = df.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})
    print("Swapped Latitude and Longitude columns.")

    # Remove invalid latitude and longitude values
    df = df.dropna(subset=['Latitude', 'Longitude'])  # Drop rows with NaN values
    df = df[(df['Longitude'] >= LONG_MIN) & (df['Longitude'] <= LONG_MAX)]
    df = df[(df['Latitude'] >= LAT_MIN) & (df['Latitude'] <= LAT_MAX)]

    print(f"Cleaned dataset contains {len(df)} rows.")
    return df

# Plot the valid sensor locations on the provided map
def plot_sensor_locations(df, map_path):
    try:
        # Load the map image
        map_image = Image.open(map_path)
        
        # Plot the map
        plt.figure(figsize=(11, 15))
        plt.imshow(map_image, extent=[LONG_MIN, LONG_MAX, LAT_MIN, LAT_MAX])
        
        # Plot the sensor locations with enhanced accuracy
        plt.scatter(df['Longitude'], df['Latitude'], c='blue', s=150, alpha=0.5, edgecolor='black', linewidth=0.5, label='Sensor Locations')
        plt.title("Grow Sensor Locations on UK Map", fontsize=16)
        plt.xlabel("Longitude", fontsize=14)
        plt.ylabel("Latitude", fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.show()
    except Exception as e:
        print("Error plotting map:", e)

# Main execution block
def main():
    # Read and clean the data
    grow_data = read_and_clean_data(data_path)
    if grow_data is not None:
        # Plot the data on the map
        plot_sensor_locations(grow_data, map_path)

# Run the script
if __name__ == "__main__":
    main()
