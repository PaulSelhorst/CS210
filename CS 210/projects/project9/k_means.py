import random
import math
import csv
import matplotlib.pyplot as plt

def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.

    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load.

    Returns:
        A dictionary where each element corresponds to a data point, with keys 
        corresponding to the row number and values as a tuple of floats.

    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
            31.4,  0.5, 12.3
        Then the return dictionary will be:
            {0: (2.4, 7.8), 1: (10, -3.2), 2: (31.4, 12.3)}
    """
    data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        i = 0
        for row in reader:
            if row[column_titles[0]] == '' or row[column_titles[1]] == '':
                continue
            else:
                data[i] = tuple(float(row[col]) for col in column_titles)
                i += 1
    return data

def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Eucledian distance between two points represented as tuples.
    Listing 7.1 in PPC, with modifications for compliance to PEP8

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.

    Example:
        euclid_dist((1, 2.5), (2.1, 4)) should return 1.86 (approximately).
    """
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff
    return math.sqrt(total)

def create_centroids(k: int, data: dict) -> list:
    """Create k centroids by picking random points from the data until 
    you have k unique centroids.

    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as tuples of floats.

    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    centroids = []
    while len(centroids) < k:
        rand_key = random.randint(1,len(data))
        if data[rand_key] not in centroids:
            centroids.append(data[rand_key])
    return centroids

def create_clusters(k: int, centroids: list, data: dict) -> tuple:
    """Create clusters using the k-means algorithm
    From Listing 7.8, modified to comply with PEP8
    Args:
        k: how many clusters to create
        centroids: the list of centroids, one per cluster
        values: list of tuples
        repeats: how many iterations to run

    Returns:
        list, list: two lists are returned -- one is a list of clusters and the 
            second one is the list of centroids
    """
    old_clusters = []
    while True:
        clusters = []
        for i in range(k):
            clusters.append([])

        for aKey in data:
            distances = []
            for clusterIndex in range(k):
                dToC = euclid_dist(data[aKey], centroids[clusterIndex])
                distances.append(dToC)
            minDist = min(distances)
            index = distances.index(minDist)
            clusters[index].append(aKey)
        dimensions = len(data[1])
        for clusterIndex in range(k):
            sums = [0] * dimensions
            for aKey in clusters[clusterIndex]:
                dataPoints = data[aKey]
                for ind in range(len(dataPoints)):
                    sums[ind] = sums[ind] + dataPoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind] / clusterLen
            centroids[clusterIndex] = sums
        for clusterIndex in range(k):
            for aKey in range(len(clusters[clusterIndex])):
                clusters[clusterIndex][aKey] = data[clusters[clusterIndex][aKey]]
        if clusters == old_clusters:
            break
        old_clusters = clusters
    return clusters, centroids

def visualize_clusters(dataset_name: str, titles: list, clusters: list,centroids: list) -> plt.Figure:
    """OPTIONAL - Extra credit (up to 50xp)
    Visualize the clusters and centroids. Use a different color for each cluster. 
    Args: 
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """
    fig, ax = plt.subplots()
    ax.set_title(f'K-means clustering for {dataset_name}')
    ax.set_xlabel(titles[0])
    ax.set_ylabel(titles[1])
    for cluster in clusters:
        x = [point[0] for point in cluster]
        y = [point[1] for point in cluster]
        ax.scatter(x, y)
    x = [point[0] for point in centroids]
    y = [point[1] for point in centroids]
    ax.scatter(x, y, marker='x', color='black')
    plt.savefig(f"clusters_{dataset_name}_{'_' .join(titles)}.png")
    return fig

def main():
    random.seed(5)
    """ Main driver for the program."""

    # Specifies the files and columns to analyze in the keys, and the number
    # of clusters in the values.
    datasets = {('earthquakes', ('latitude', 'longitude')): 5,
                ('earthquakes', ('depth', 'mag')): 5,
                ('cis210_scores', ('Projects', 'Exams')): 5}
    # Feel free to add more datasets or column pairs and experiment with different values of k

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f'\nDataset: {dataset} {titles}')
        # Part 8.1
        data = load_numerical_data(dataset + '.csv', column_titles=titles)

        # Part 8.3
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")

        # Parts 8.2 and 8.4 (create_clusters calls euclid_dist)
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")
    
        # Optional extra-credit 8.5
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")

if __name__ == '__main__':
    main()