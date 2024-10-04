import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import OPTICS

# Assuming results_dict and data are already defined

for key, value in results_dict.items():
    print(f'Plotting reachability plot for combination: {key}')

    # Retrieve the stored parameters
    params = value['parameters']

    # Refit OPTICS with the same parameters to extract reachability and ordering
    optics = OPTICS(xi=params['xi'], min_samples=params['min_samples'],
                    max_eps=params['max_eps'], min_cluster_size=params['min_cluster_size'], metric="euclidean")
    optics.fit(data)

    # Extract reachability and ordering
    reachability = optics.reachability_[optics.ordering_]
    labels = optics.labels_[optics.ordering_]

    # Plot the reachability plot
    plt.figure(figsize=(12, 8))
    plt.plot(reachability, 'k-', label='Reachability Distance')

    # Define color map with better distinction
    cmap = plt.get_cmap('tab10')
    colors = cmap(np.linspace(0, 1, len(np.unique(labels))))

    # Add color-coded cluster separation
    space = np.arange(len(data))
    for i, color in zip(range(-1, len(np.unique(labels))), colors):
        Xk = space[labels == i]
        plt.plot(Xk, reachability[labels == i], color=color, alpha=0.7, label=f'Cluster {i}' if i != -1 else 'Noise')

    plt.xlabel('Points (in Cluster Order)')
    plt.ylabel('Reachability Distance')

    # Create a title that includes both label and parameters
    title = (f'Reachability Plot for {key}\n'
             f'Parameters: xi={params["xi"]}, min_samples={params["min_samples"]}, '
             f'max_eps={params["max_eps"]}, min_cluster_size={params["min_cluster_size"]}')
    plt.title(title)

    # Adjust legend settings for better clarity
    #plt.legend(loc='best', fontsize='small', ncol=2, frameon=True)
    plt.tight_layout()

    # Create filename based only on the key
    filename = f"result/reachability_plot_{key}.png"

    # Save the figure with a descriptive filename
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()  
