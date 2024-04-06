import matplotlib.pyplot as plt
import numpy as np

def read_data(file_name:str) -> list:
    with open(file_name, 'r') as in_file:
        ls = [line.strip().split(",") for line in in_file]
        return ls

def list_to_dict(ls:list) -> dict:
    for id, rain in ls:
        d = {id:rain for id, rain in ls}
    return d

def mean_rainfall(values:list) -> float:
    acc = 0
    for id, rain in values:
        acc += float(rain)
    return acc / len(values)
    
def plot_avg_monthly_rain_vs_year(ls:list) -> None:
    avg_monthly_rain = [float(rain) for date, rain in ls]
    years = [int(date[:4]) for date, rain in ls]
    plt.plot(years, avg_monthly_rain)
    plt.xlabel("Year")
    plt.ylabel("Average Monthly Rainfall")
    plt.axhline(y=mean_rainfall(ls), color='r', linestyle=':')
    plt.show()

#print(list_to_dict(read_data("november_rain.txt")))
print(mean_rainfall(read_data("november_rain.txt")))
plot_avg_monthly_rain_vs_year((read_data("november_rain.txt")))