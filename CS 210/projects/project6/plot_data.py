import json
import matplotlib.pyplot as plt
from pop_stats import *
import json
import plotly.graph_objects as go

def plot_pop_data(pop, lat, lon):
        file_name = "population.json"
        
        with open(file_name) as f:
            data = json.load(f)

        pop = [(entry["pop2023"])/1000 for entry in data]
        lat = [entry["lat"] for entry in data]
        lon = [entry["lng"] for entry in data]
        
        plt.scatter(lon, lat, s=pop, alpha=1)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Population in 2023")
        plt.show()



def plot_hist(data, n_bins=10):
    plt.hist(data, bins=n_bins)
    plt.xlabel("Density")
    plt.ylabel("Frequency")
    plt.title("Density Histogram")
    plt.show()

def plot_on_map(pop, lat, lon):
    fig = go.Figure(data=go.Scattergeo(
        lat = lat,
        lon = lon,
        mode = 'markers',
        marker = dict(
            size = pop,
            colorbar = dict(
                title = 'Population'
            ),
        ),
    ))
    fig.update_layout(
        title = 'Population in Oregon',
        geo_scope='usa',
    )
    fig.update_geos(fitbounds="locations")

    fig.show()


if __name__ == "__main__":
    file_name = "population.json"
    
    [pop, lat, lng, growth, dens] = read_data(file_name, \
        ["pop2023", "lat", "lng", "growth", "density"])
    
    #plot_pop_data(pop, lat, lng)
    pop = filter_array(pop, 10000)
    for i in range(len(pop)):
        pop[i] = pop[i] / 5000
    plot_on_map(pop, lat, lng)
    #plot_hist(dens)