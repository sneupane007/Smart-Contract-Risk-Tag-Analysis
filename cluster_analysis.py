#Cluster Analysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import pointbiserialr
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import fcluster

print("Libraries imported successfully!")

# Load the dataset
df = pd.read_excel('/content/drive/MyDrive/compiled_risk_data.xlsx')

# Select the features based on frequency and correlation analyses

selected_features = df[['owner_change_balance', 'exploitation', 'buy_tax', 'sell_tax',
                        'is_airdrop_scam', 'Is_anti_whale','is_fake_token', 'anti_whale_modifiable' ]]
selected_features = selected_features.replace({True:1, False:0})
print("Features selected for clustering:")

print(selected_features.head())

from scipy.spatial.distance import pdist, squareform

# Assuming 'selected_features' is your DataFrame with binary data
distance_matrix = pdist(selected_features, 'jaccard')
distance_square_matrix = squareform(distance_matrix)  # Convert to square matrix

import scipy.cluster.hierarchy as sch

# Create linkage matrix
linkage_matrix = sch.linkage(distance_matrix, method='ward')

# Plot the dendogram

plt.figure(figsize=(12, 8))
dendrogram = sch.dendrogram(linkage_matrix)
dendrogram = sch.dendrogram(linkage_matrix, labels=selected_features.index)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data points')
plt.ylabel('Jaccard distance')
plt.show()

# Example: Set maximum distance at 1.5 for cluster formation
cluster_labels = fcluster(linkage_matrix, t=5, criterion='distance')

# Add cluster labels back to your original DataFrame
data_new['cluster'] = cluster_labels

# Summary statistics for each cluster
cluster_summary = data_new[[feature_1, feature_2, feature_3,'cluster']].groupby('cluster').agg(['mean', 'std', 'median', 'count'])
cluster_summary

# Plot histogram of cluster labels to see distribution of cluster sizes
plt.figure(figsize=(8, 6))
plt.hist(cluster_labels, bins=np.arange(1, np.max(cluster_labels)+2)-0.5, rwidth=0.8, color='blue', alpha=0.7)
plt.title('Histogram of Cluster Sizes')
plt.xlabel('Cluster')
plt.ylabel('Number of Points')
plt.xticks(np.arange(1, np.max(cluster_labels)+1))
plt.show()

# Calculate the mean for each cluster and feature
cluster_centers = data_new[['owner_change_balance', 'exploitation', 'buy_tax', 'sell_tax',
                                         'is_airdrop_scam', 'is_fake_token', 'anti_whale_modifiable', 'Is_anti_whale', 'cluster']].groupby('cluster').mean()

plt.figure(figsize=(12, 8))
sns.heatmap(cluster_centers, annot=True, cmap='coolwarm')
plt.title('Heatmap of Cluster Centroids')
plt.show()


