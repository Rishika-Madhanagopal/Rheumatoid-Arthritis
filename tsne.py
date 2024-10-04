import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import numpy as np

# Run t-SNE dimensionality reduction once
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
reduced_tsne = tsne.fit_transform(data)
a_tsne, b_tsne = reduced_tsne.T

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
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.scatter(x=a_tsne[labels == -1], y=b_tsne[labels == -1], c=colors[labels == -1], s=0.5,
               alpha=0.2)  # Noise: small and transparent
    ax.scatter(x=a_tsne[labels != -1], y=b_tsne[labels != -1], c=colors[labels != -1], s=8,
               alpha=0.9)  # Clusters: larger and more opaque

    # Add title to each plot with the parameters
    ax.set_title(
        f"OPTICS Clustering with t-SNE\nxi={parameters['xi']}, min_samples={parameters['min_samples']}, max_eps={parameters['max_eps']}, min_cluster_size={parameters['min_cluster_size']}",
        fontsize=15)

    # Add labels
    ax.set_xlabel('t-SNE Component 1', fontsize=12)
    ax.set_ylabel('t-SNE Component 2', fontsize=12)

    # Save each plot as an image file
    # plt.savefig(f"results/tsne_cluster_{key}.png", dpi=250, bbox_inches="tight")

    # Display the plot
    plt.show()

    # Close the plot to save memory if running multiple plots
    plt.close()
