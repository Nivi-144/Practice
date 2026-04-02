import numpy as np
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self, lr=0.01, epochs=100):
        self.lr = lr; self.epochs = epochs
    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0
        self.errors_ = []
        for _ in range(self.epochs):
            err = 0
            for xi, yi in zip(X, y):
                pred = self.predict_single(xi)
                update = self.lr * (yi - pred)
                self.w += update * xi
                self.b += update
                err += int(update != 0)
            self.errors_.append(err)
    def predict_single(self, x):
        return 1 if np.dot(x, self.w) + self.b >= 0 else 0
    def predict(self, X):
        return np.array([self.predict_single(x) for x in X])
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 0, 0, 1])
p = Perceptron(lr=0.1, epochs=20)
p.fit(X, y)
print("Predictions:", p.predict(X))
plt.plot(p.errors_); plt.xlabel('Epoch'); plt.ylabel('Errors')
plt.title('Perceptron Training'); plt.tight_layout(); plt.show()
