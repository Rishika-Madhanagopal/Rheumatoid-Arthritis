# Rheumatoid Arthritis - Immune Cell Clustering

## Overview
This repository contains the dissertation project titled **"Density-Based Clustering in Immune Cell Cytometry Data"**. The research leverages flow cytometry data from the BioFlare project, applying the OPTICS clustering algorithm to identify immune cell populations associated with rheumatoid arthritis (RA) flares and remission.

## Contents:
- `Dissertation_final.pdf`: Full dissertation document.
- `clustering.py`: Python script implementing the OPTICS clustering algorithm to group immune cells based on density.
- `reachability_plot.py`: Script to generate reachability plots that visualize cluster structures and noise points.
- `tsne.py`: Script for generating t-SNE visualizations, reducing high-dimensional data for better interpretation.
- `umap.py`: Script for creating UMAP visualizations, another dimensionality reduction method useful for data exploration.

## Visualizations:
- **Reachability Plot**:  A graph representing the clustering hierarchy, highlighting noise points (in grey) and clusters formed at different density thresholds.
- **UMAP/t-SNE**:Visualize high-dimensional immune cell data in 2D, allowing for easier interpretation of immune cell populations.
## Usage:
To explore the clustering or generate visualizations, use the following commands:

```bash
# Run the OPTICS clustering algorithm
python clustering.py   

# Generate the reachability plot
python reachability_plot.py   

# Produce the t-SNE scatter plot
python tsne.py   

# Create the UMAP scatter plot
python umap.py

Requirements:
Make sure to install the necessary Python libraries before running the scripts. You can use the following command to install the required packages:

```bash
pip install numpy scipy matplotlib scikit-learn umap-learn





