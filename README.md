# 🦠 Immune Cell Clustering in Rheumatoid Arthritis
### *Leveraging Density-Based Clustering (OPTICS) to decode immune landscapes in RA Flare & Remission.*

<div align="center">
  <img src="Rishika-Madhanagopal/assets/reachability_plot_label_3.png" width="100%" style="border-radius: 10px;" alt="Reachability Plot" />
</div>

## 🔬 OVERVIEW
This repository houses the research and computational framework for the project: **"Density-Based Clustering in Immune Cell Cytometry Data."** By utilizing flow cytometry data from the **BioFlare project**, this study applies advanced density-based algorithms to identify discrete immune cell populations. The goal is to isolate high-dimensional cellular signatures associated with **Rheumatoid Arthritis (RA)** disease states, distinguishing between active flare and clinical remission.

## 🧬 METHODOLOGY
Unlike traditional K-Means, this pipeline utilizes **OPTICS (Ordering Points To Identify the Clustering Structure)** to handle the varying densities and noise inherent in biological cytometry data.

* **Dimensionality Reduction:** Implementation of **t-SNE** and **UMAP** to project 20+ parameter cytometry data into interpretable 2D manifolds.
* **Clustering:** Application of **OPTICS** to detect clusters of arbitrary shape and identify outlier "noise" cells.
* **Visualization:** Generation of **Reachability Plots** to visualize the hierarchical density structure of the immune landscape.

## 🚀 KEY FEATURES
- ✅ **OPTICS Implementation:** Robust density-based clustering for noisy biological datasets.
- ✅ **Multi-Manifold Visualization:** Comparative analysis using both **UMAP** and **t-SNE**.
- ✅ **Noise Detection:** Automated identification of non-clustered "outlier" cell populations.
- ✅ **Clinical Context:** Analysis focused specifically on RA flare/remission biomarkers.

## 📁 PROJECT STRUCTURE
```bash
Rheumatoid-Arthritis/
├── clustering.py           # Core implementation of OPTICS algorithm
├── reachability_plot.py    # Visualization of clustering hierarchy & density
├── umap.py                 # UMAP manifold projection scripts
├── tsne.py                 # t-SNE visualization scripts
├── Dissertation_final.pdf  # Comprehensive theoretical and clinical results
└── individual_presentation_RA.pdf # Summary of key findings and visualizations
```






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

# Requirements
Make sure to install the necessary Python libraries before running the scripts. You can use the following command to install the required packages:

pip install numpy scipy matplotlib scikit-learn umap-learn



