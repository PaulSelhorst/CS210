import csv
import statistics
import matplotlib.pyplot as plt

# ------ You shouldn't have to modify main --------


def load_data(file_name: str, types: dict) -> dict:
    """
    Load the Titanic data from a CSV file to a dictionary.

    Parameters:
    - file_name (str): Name of the CSV file.
    - types (dict): Dictionary specifying column names and their data types.

    Returns:
    - dict: Dictionary containing the data from the CSV file.
    """
    data_dict = {}
    with open(file_name, 'r') as file:
        monkey = csv.reader(file)
        for key in zip(types, types.values()):
            data_dict[key] = []
        next(monkey)
        for line in monkey:
            fields = line
            for key, fields in zip(data_dict.keys(), fields):
                data_dict[key].append(fields)
    return data_dict


    # with open(file_name, 'r', encoding='utf8') as csv_file:
    #     csv_reader = csv.DictReader(csv_file)
    #     for row in csv_reader:
    #         for key, data_type in types.items():
    #             try:
    #                 data_dict[key].append(data_type(row[key]))
    #             except ValueError:
    #                 # Handle potential conversion errors
    #                 data_dict[key].append(None)

    return data_dict

def summarize(data:dict):
    """Print summary statistics for each column in the data."""
    try:
        for key in data:
            if key[1] in (float,int):
                dict_list = [float(values) for values in data[key]]
                print(f'Statistics for {key[0]}:')
                print(f'min:'.rjust(8) , f'{float(round(min(dict_list),1))}'.rjust(6))
                print(f'max:'.rjust(8) , f'{float(round(max(dict_list),1))}'.rjust(6))
                print(f'mean:'.rjust(8) , f'{float(round(statistics.mean(dict_list),1))}'.rjust(6))
                print(f'stdev:'.rjust(8) , f'{float(round(statistics.stdev(dict_list),1))}'.rjust(6))
                print(f'mode:'.rjust(8) , f'{float(round(statistics.mode(dict_list),1))}'.rjust(6))
            else:
                print(f'Statistics for {key[0]}:')
                print(f'Number of unique values: {len(set(data[key]))}')
                print(f'Most common value: {max(set(data[key]), key = data[key].count)}'.rjust(len(f'Most common value: {max(set(data[key]), key = data[key].count)}')+6))
    except:
        print('Error: Invalid data type')

def pearson_corr(x: list, y: list) -> float:
    """
    Compute the Pearson correlation coefficient between two lists of numerical values.

    Parameters:
    - x (list): List of numerical values.
    - y (list): List of numerical values.

    Returns:
    - float: Pearson correlation coefficient.

    Raises:
    - ValueError: If the input lists have uneven lengths or contain non-int and non-float values.
    """
    if len(x) != len(y):
        raise ValueError('The list parameters must have the same number of elements.')

    if not all(isinstance(value, (int, float)) for value in x) or not all(isinstance(value, (int, float)) for value in y):
        raise ValueError('pearson_corr only works with int or float lists.')

    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_y_squared = sum(yi ** 2 for yi in y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5
    
    if denominator == 0:
        return 0  # Return 0 if denominator is zero to avoid division by zero
    
    correlation = numerator / denominator
    return round(correlation, 2)

def survivor_vis(data:dict, col_1:tuple, col_2:tuple):
    survived = [int(x) for x in data[('Survived', int)]]
    data_col_1 = [float(x) for x in data[col_1]]
    data_col_2 = [float(x) for x in data[col_2]]
    print(survived)
    survivedx = []
    survivedy = []
    deadx = []
    deady = []

    for i in range(len(survived)):
        if survived[i] == 1:
            survivedx.append(data_col_1[i])
            survivedy.append(data_col_2[i])
        else:
            deadx.append(data_col_1[i])
            deady.append(data_col_2[i])

    print(survivedx)
    print(survivedy)
    print(deadx)
    print(deady)
    #error checking
    if col_1[1] not in (float,int):
        raise ValueError('survivor_vis only works with int or float columns.')
    if col_2[1] not in (float,int):
        raise ValueError('survivor_vis only works with int or float columns.')
    if col_1 not in data.keys():
        raise ValueError('The first column is not in the data dictionary.')
    if col_2 not in data.keys():
        raise ValueError('The second column is not in the data dictionary.')
    if len(data[col_1]) != len(data[col_2]):
        raise ValueError('The columns must have the same number of elements.')
    
    #scatter plot
    figure = plt.figure(figsize = (8,4))

    plt.scatter(survivedx, survivedy, color = 'green', marker = 'o', label = 'Survived')
    plt.scatter(deadx, deady, color = 'red', marker = 'x', label = 'Died')
    plt.xlabel(col_1[0])
    plt.ylabel(col_2[0])
    plt.title('Survival of Titanic Passengers')
    print(int(max(data[col_1])))
    plt.savefig(f'scatter_{col_1[0]}_vs_{col_2[0]}.png')
    plt.show(block = False)


def main():
    """Main program driver for Project 3."""

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)
    # 3.2 Print informative summaries
    print("\nPart 3.2")
    summarize(data)

    print("\nPart 3.3")
    # # 3.3 Compute correlations between age and survival
    # corr_age_survived = pearson_corr(data[('Age', float)],
    #                                  data[('Survived', int)])
    # print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # # 3.3 Correlation between fare and survival
    # corr_fare_survived = pearson_corr(data[('Fare', float)],
    #                                   data[('Survived', int)])
    # print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # # 3.3 Correlation between family size and survival
    # corr_fare_survived = pearson_corr(data[('FamilySize', int)],
    #                                   data[('Survived', int)])
    # print(f'Correlation between family size and survival is'
    #       f' {corr_fare_survived:3.2f}')

    # 3.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    #fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    #fig = survivor_vis(data, ('Age', float), ('Parch', int))

main()