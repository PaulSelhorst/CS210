import csv
import matplotlib.pyplot as plt

def load_data(file_name:str, types:dict)->dict:
    data = {}
    with open(file_name, 'r') as file:
        monkey = csv.reader(file)
        for key in zip(types, types.values()):
            data[key] = []
        next(monkey)
        for line in monkey:
            fields = line
            for key, fields in zip(data.keys(), fields):
                data[key].append(fields)
    return data

def bar_chart(data:dict, col_1:tuple, col_2:tuple):
    """Create a bar chart comparing the survival rates of two groups."""
    try:
        alive_m = []
        alive_f = []
        dead_m = []
        dead_f = []
        col_2 = [int(x) for x in data[col_2]]
        for i in range(len(col_2)):
            if col_2[i] == 1:
                if data[col_1][i] == 'male':
                    alive_m.append(i)
                elif data[col_1][i] == 'female':
                    alive_f.append(i)
            else:
                if data[col_1][i] == 'male':
                    dead_m.append(i)
                elif data[col_1][i] == 'female':
                    dead_f.append(i)
        sex = ("Male", "Female")
        status = {
            "Alive": [len(alive_m), len(alive_f)],
            "Dead": [len(dead_m), len(dead_f)]
        }
        width = 0.5
        bottom = [0, 0]
        fig, ax = plt.subplots()
        for boolean, status in status.items():
            p = ax.bar(sex, status, width, label=boolean, bottom = bottom)
            bottom = [sum(x) for x in zip(bottom, status)]
        plt.ylim(0, 600)
        ax.set_ylabel('Count')
        ax.set_title('Count of survivors by gender')
        ax.legend(loc = "upper right")
        plt.show()
        #print(alive_f)
        #print(alive_m)
        #print(dead_m)
        #print(dead_f)
    except:
        print('Error: Invalid data type')

def bar_chart2(data:dict, col_1:tuple, col_2:tuple):
    """Create a bar chart comparing the survival rates of two groups."""
    try:
        alive_m = []
        alive_f = []
        dead_m = []
        dead_f = []
        col_2 = [int(x) for x in data[col_2]]
        for i in range(len(col_2)):
            if col_2[i] == 1:
                if data[col_1][i] == 'male':
                    alive_m.append(i)
                elif data[col_1][i] == 'female':
                    alive_f.append(i)
            else:
                if data[col_1][i] == 'male':
                    dead_m.append(i)
                elif data[col_1][i] == 'female':
                    dead_f.append(i)
        sex = ("Male", "Female")
        status = {
            "Alive": [len(alive_m) / (len(alive_m) + len(dead_m)) * 100, len(alive_f) / (len(alive_f) + len(dead_f)) * 100],
            "Dead": [len(dead_m) / (len(alive_m) + len(dead_m)) * 100, len(dead_f) / (len(alive_f) + len(dead_f)) * 100]
        }
        width = 0.5
        bottom = [0, 0]
        fig, ax = plt.subplots()
        for boolean, status in status.items():
            p = ax.bar(sex, status, width, label=boolean, bottom = bottom)
            bottom = [sum(x) for x in zip(bottom, status)]
        plt.ylim(0, 100)
        ax.set_ylabel('Count')
        ax.set_title('Count of survivors by gender')
        ax.legend(loc = "upper right")
        plt.show()
    except:
        print('Error: Invalid data type')

def main():
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                    'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                    'Fare': float, 'Embarked': str, 'FamilySize': int,
                    'age_group': str}

    data = load_data('titanic_clean.csv', titanic_types)
    bar_chart(data, ('Sex', str), ('Survived', int))
    #bar_chart2(data, ('Sex', str), ('Survived', int))
main()
