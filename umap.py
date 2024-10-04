import matplotlib.pyplot as plt
import seaborn as sns
import umap
import numpy as np

# UMAP dimensionality reduction
embedding = umap.UMAP(n_components=2, random_state=42)
reduced = embedding.fit_transform(data)
a, b = reduced.T

# Loop through all keys in the results_dict
for key in results_dict:
    # Extract labels and parameters
    labels = results_dict[key]['labels']
    parameters = results_dict[key]['parameters']

    # Define a color palette
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)  # Number of clusters excluding noise
    palette = sns.color_palette("bright", n_colors=n_clusters)  # Bright colors for clusters
    palette = [(0.8, 0.8, 0.8)] + palette  # Light grey for noise (-1), followed by bright colors

    # Map labels to colors
    colors = np.array([palette[label + 1] if label >= 0 else palette[0] for label in labels])

    # Plotting the scatter plot with different size and alpha for noise and clusters
    fig, ax = plt.subplots()
    ax.scatter(x=a[labels == -1], y=b[labels == -1], c=colors[labels == -1], s=0.5, alpha=0.2, label='Noise')  # Noise: small and transparent
    ax.scatter(x=a[labels != -1], y=b[labels != -1], c=colors[labels != -1], s=1.5, alpha=0.9, label='Clusters')  # Clusters: larger and more opaque

    # Add title to each plot with the parameters
    ax.set_title(f"OPTICS Clustering\nxi={parameters['xi']}, min_samples={parameters['min_samples']}, max_eps={parameters['max_eps']}, min_cluster_size={parameters['min_cluster_size']}")

    # Save each plot as an image file (optional)
    # plt.savefig(f"results/cluster_{key}.png", dpi=250, bbox_inches="tight")

    # Display the plot
    plt.show()

    plt.close()
