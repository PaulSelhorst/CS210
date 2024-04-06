import json
import matplotlib.pyplot as plt
from pop_stats import *
import plotly.express as px
import folium

def plot_pop_data(pop, lat, lon):
   # Scatter plot using matplotlib
   file_name = "population.json"
   with open(file_name) as f:
        data = json.load(f)

   pop = [(entry["pop2023"])/1000 for entry in data]
   lat = [entry["lat"] for entry in data]
   lon = [entry["lng"] for entry in data]

   plt.scatter(lon, lat, s=pop, alpha=1)
   plt.title('Population Scatter Plot')
   plt.xlabel('Longitude')
   plt.ylabel('Latitude')
   plt.show()

def plot_hist(data, n_bins=10):
    plt.hist(data, bins=n_bins)
    plt.xlabel("Density")
    plt.ylabel("Frequency")
    plt.title("Density Histogram")
    plt.show()

# def plot_hist(data, nbins=20):
#    # Histogram using matplotlib
#    plt.figure(figsize=(10, 6))
#    plt.hist(data['population_density'], bins=nbins, color='skyblue', edgecolor='black')
#    plt.title('Population Density Histogram')
#    plt.xlabel('Population Density')
#    plt.ylabel('Frequency')
#    plt.show()

def plot_on_map(data):
   # Scatter plot on map using plotly or folium
   # Example using Plotly Express
   fig = px.scatter_geo(data, lat='latitude', lon='longitude', size='population', text='city',
                        projection='natural earth', title='Population Scatter Plot on Map')
   fig.show()

   # Example using Folium
   map_osm = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=6)
   for i in range(len(data)):
       folium.CircleMarker(
           location=[data.iloc[i]['latitude'], data.iloc[i]['longitude']],
           radius=data.iloc[i]['population'] / 100000,
           popup=data.iloc[i]['city'],
           color='blue',
           fill=True,
           fill_color='blue'
       ).add_to(map_osm)
   map_osm.save('map.html')


file_name = "population.json"
    
[pop, lat, lng, growth, dens] = read_data(file_name, \
    ["pop2023", "lat", "lng", "growth", "density"])
#plot_pop_data(pop, lat, lng)
#lot_hist(dens)
plot_on_map(read_data(file_name, ["pop2023", "lat", "lng"]))