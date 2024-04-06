import csv
import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, 'r') as in_file:
        csv_reader = csv.reader(in_file)
        header = next(csv_reader)
    dx = {}
    for line in csv_reader:
        key = (line[0], line[1])
        value_dict = {}
        for i in range(3, len(header)):
            value_dict[header[i]] = line[i]
        dx[key] = value_dict
    return dx

def extract_column(data_dict, col_name):
    column = []
    for city_dict in data_dict.values():
        column += [float(city_dict[col_name])]
    return column

def plot_data(data_dict):
    x = extract_column(data_dict, 'Housing')
    y = extract_column(data_dict, 'Cost_of_Living')
    figure = plt.figure(figsize = (16,8))
    plt.scatter(x, y, marker = 'x', c = 'green')
    plt.title('Housing vs Cost of Living')
    plt.xlabel('Housing')
    plt.ylabel('Cost of Living')
    plt.savefig(f'scatter_H_C.png')
    plt.show()
