# Cluster Analysis Project

This project demonstrates hierarchical clustering and risk analysis on a dataset using Python. It incorporates data visualization techniques and statistical analysis to uncover patterns in risk-related features.

---

## Project Overview

This project performs the following tasks:
- Hierarchical clustering on binary data.
- Visualization of dendrograms to identify clusters.
- Frequency analysis of risk tags.
- Calculation of correlation (Phi coefficient) between binary variables.
- Generation of heatmaps to visualize cluster centroids and correlations.

---

## Features and Functionality

### Clustering
- Utilizes Jaccard distance for clustering binary data.
- Plots dendrograms to visualize the clustering process.
- Assigns data points to clusters based on a set distance threshold.

### Frequency Analysis
- Computes the frequency of `True` values for risk tags.
- Visualizes frequencies using color-coded bar charts.

### Correlation Analysis
- Calculates the Phi coefficient between binary variables.
- Displays correlations using annotated heatmaps.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation.
  - `numpy` for numerical computations.
  - `seaborn` and `matplotlib` for data visualization.
  - `scipy` for statistical analysis and clustering.

---

## Setup Instructions

1. **Prerequisites**:
   - Python 3.8 or higher.
   - Required libraries:
     ```bash
     pip install pandas numpy matplotlib seaborn scipy
     ```

2. **Dataset**:
   - Place the dataset `compiled_risk_data.xlsx` in the project directory.

3. **Run the Script**:
   - Execute the script in your Python environment.

4. **Output Files**:
   - Clustering and frequency visualizations will be displayed.

---

## Usage

1. **Cluster Analysis**:
   - Modify the `selected_features` variable to specify features for clustering.
   - Adjust the threshold `t` in `fcluster` to control cluster granularity.

2. **Frequency Analysis**:
   - Ensure the dataset contains binary risk tag columns.
   - View the bar chart for frequency insights.

3. **Correlation Analysis**:
   - Analyze the Phi coefficient heatmap to identify significant correlations between features.

---

## Key Outputs

1. **Dendrogram**: Displays hierarchical clustering structure.

2. **Cluster Heatmap**: Visualizes cluster centroids for features.

3. **Frequency Bar Chart**: Highlights occurrences of `True` values for risk tags.

4. **Correlation Heatmap**: Shows relationships between binary variables.

---

## References

- **Libraries**:
  - [Pandas Documentation](https://pandas.pydata.org/)
  - [Seaborn Documentation](https://seaborn.pydata.org/)
  - [Scipy Clustering](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)

- **Concepts**:
  - Hierarchical Clustering: [Wikipedia](https://en.wikipedia.org/wiki/Hierarchical_clustering)
  - Phi Coefficient: [Wikipedia](https://en.wikipedia.org/wiki/Phi_coefficient)

---

Developed by: Sujal
