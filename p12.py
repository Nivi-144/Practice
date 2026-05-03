import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
X = np.array([
[1, 2], [1.5, 1.8], [5, 8],
[8, 8], [1, 0.6], [9, 11]])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print("Labels:", labels)
print("Centroids:\n", centroids)
plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')
plt.scatter(centroids[:,0], centroids[:,1], color='red', marker='X')
plt.title("K-Means Clustering")
plt.show()
