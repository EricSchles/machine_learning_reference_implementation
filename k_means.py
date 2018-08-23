import random
import functools
import math
import copy
import numpy as np

def distance_function(point_one, point_two):
    difference = [point_one[i] - point_two[i]
                  for i in range(len(point_one))]
    squared_difference = [math.pow(elem, 2)
                          for elem in difference]
    return math.sqrt(sum(squared_difference))


def abs_diff(list_one, list_two):
    return [abs(list_one[i] - list_two[i])
            for i in range(len(list_one))]


def centriod_check(prev_centriods, current_centriods, epsilon):
    return [abs_diff(prev_centriods[i], current_centriods[i]) 
            for i in range(len(current_centriods))]
           

def generate_clusters(dataset, current_centriods, k):
    distances = []
    clusters = [[] for _ in range(k)]
    for datum_index, datum in enumerate(dataset):
        for centriod_index in range(k):
            distances.append((distance_function(
                current_centriods[centriod_index], datum),
                              datum_index, centriod_index))
        for datum_index in range(len(dataset)):
            datum_distances = [distance[1]==datum_index
                               for distance in distances]
            sorted_distances = sorted(datum_distances,
                                      key=lambda t:t[0])
            cluster_index = sorted_distances[0][2]
            clusters[cluster_index].append(dataset[datum_index])
    return clusters


def transpose(array):
    num_rows = len(array)
    num_columns = len(array[0])
    new_array = [[0 for _ in range(now_rows)]
                 for _ in range(num_columns)]
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            new_array[column_index][row_index] = array[row_index][column_index]
    return new_array


def calculate_new_centriods(clusters):
    centriods = []
    for cluster in clusters:        
        transposed_cluster = transpose(cluster)
        centriod = []
        for column in tranposed_cluster:
            centriod.append(float(np.mean(column)))
        centriods.append(centriod)
    return centriods


def k_means(dataset, k, epsilon=0.001):
    centriods = []
    for _ in range(k):
        centriods.append(random.choice(dataset))
    current_centriods = centriods
    prev_centriods = [[random.randint(-100000, 100000)
                       for _ in range(len(centriods[0]))]
                      for _ in range(len(centriods))]
    while centriod_check(prev_centriods, current_centriods, epsilon):
        clusters = generate_clusters(dataset, current_centriods, k)
        prev_centriods = copy.deepcopy(current_centriods)
        current_centriods = calculate_new_centriods(clusters)
    return current_centriods


def generate_dataset():
    dataset = []
    number_rows = random.randint(5, 50)
    for row_i in range(number_rows):
        dataset.append(
            [random.randint(-50, 50) + random.random()
             for _ in range(10)]
        )
    return dataset

if __name__ == '__main__':
    dataset = generate_dataset()
    centers = []
    for k in range(2, 5):
        centers.append(k_means(dataset, k))
    import code
    code.interact(local=locals())
