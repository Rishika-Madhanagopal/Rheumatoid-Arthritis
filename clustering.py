import pandas
import matplotlib.pyplot as plt
import seaborn
import umap
from sklearn.cluster import OPTICS
import numpy
import pandas

# Load data
data = pandas.read_table('data/t_baseline.txt').sample(n= 50000, random_state= 42)

# OPTICS clustering parameters
xi = [0.01,0.5,0.1]
min_samples = [5,10,20]
max_eps = [1.0,2.0,5.0]
min_cluster_size = [30,50,100]

# Initialize dictionary to store labels and their corresponding parameters
results_dict = {}

total_combinations = len(xi) * len(min_samples) * len(max_eps) * len(min_cluster_size)
current_combination = 0

# Loop through all parameter combinations
for i in xi:
    for j in min_samples:
        for k in max_eps:
            for l in min_cluster_size:
                current_combination += 1
                print(f'Running combination {current_combination} of {total_combinations}: xi={i}, min_samples={j}, max_eps={k}, min_cluster_size={l}')
                
                # Perform OPTICS clustering
                optics = OPTICS(xi=i, min_samples=j, max_eps=k, min_cluster_size=l, metric="manhattan")
                optics.fit(data)
                
                # Store labels and parameters in the dictionary
                label_key = f'label_{current_combination}'
                results_dict[label_key] = {
                    'labels': optics.labels_, # Store the labels here
                    'parameters': {'xi': i, 'min_samples': j, 'max_eps': k, 'min_cluster_size': l}
                }

# Example to access and compare labels:
for key, value in results_dict.items():
    print(f'{key}: Unique labels = {set(value["labels"])}') # Access the stored labels
    print(f'Parameters: {value["parameters"]}')
