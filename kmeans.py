from sklearn.cluster import KMeans
import numpy as np
X = np.array([[3,5],[7,8],[12,5],[16,9]])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
print("Labels:", kmeans.labels_)
print("Centroids:")
print(kmeans.cluster_centers_)
