import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class KMeans:
    def __init__(self, k=3, max_iter=100):
        self.k = k; self.max_iter = max_iter
    def fit(self, X):
        self.centroids = X[np.random.choice(len(X), self.k, replace=False)]
        for _ in range(self.max_iter):
            old = self.centroids.copy()
            self.labels_ = np.argmin(
                np.array([[np.linalg.norm(x - c) for c in self.centroids] for x in X]), axis=1)
            self.centroids = np.array([X[self.labels_==i].mean(0) for i in range(self.k)])
            if np.allclose(old, self.centroids): break
        return self
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
km = KMeans(k=3).fit(X)
plt.scatter(X[:,0], X[:,1], c=km.labels_, cmap='viridis')
plt.scatter(km.centroids[:,0], km.centroids[:,1], c='red', marker='X', s=200)
plt.title('K-Means Clustering'); plt.tight_layout(); plt.show()
