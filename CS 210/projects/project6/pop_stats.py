import json
import statistics as stat

def read_data(file_name: str, keys: list) -> list:
    data_arrays = [[] for _ in keys]
    with open(file_name, 'r') as file:
        data = json.load(file)
        for item in data:
            for i, key in enumerate(keys):
                data_arrays[i].append(item[key])
    return data_arrays

def stats(an_array: list) -> dict:
    arr_stats = {
        'min': round(min(an_array),2),
        'max': round(max(an_array),2),
        'range': round(max(an_array) - min(an_array),2),
        'mean': round(sum(an_array) / len(an_array),2),
        'mode': round(stat.mode(an_array),2),
        'var': round(stat.variance(an_array),2),
        'stdev': round(stat.stdev(an_array),2)
        }
    
    return arr_stats

def print_stats(file_name: str):
    data_groups = ['pop2023', 'growth', 'density']
    data = read_data(file_name, data_groups)
    stats_list = [stats(filter_array(data[0],10000)), stats(data[1]), stats(data[2])]
    print(f"            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+")
    print(f"            |min          |max          |range        |mean         |mode         |variance     |st.dev.      |")
    print(f"            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+")

    for i in range(len(stats_list)):
        if data_groups[i] == 'pop2023':
            data_groups[i] = 'population'

        print(data_groups[i].ljust(12," "),end="")
        for k, v in stats_list[i].items():
            print(f"|{round(v,2)}".ljust(14," "),end="")
        print(f"|",end="")
        print(f"\n            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+")

def filter_array(an_array, num):
    return [x for x in an_array if x > num]
print_stats('population.json')
#print(stats(read_data('population.json', ['pop2023', 'growth', 'density'])))