import numpy as np
from collections import Counter

# Decision Tree (simple version reused)
class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def gini(self, y):
        classes = np.unique(y)
        impurity = 1
        for c in classes:
            p = np.sum(y == c) / len(y)
            impurity -= p**2
        return impurity

    def split(self, X, y, feature, threshold):
        left_mask = X[:, feature] <= threshold
        right_mask = X[:, feature] > threshold
        return X[left_mask], X[right_mask], y[left_mask], y[right_mask]

    def best_split(self, X, y):
        best_feature, best_thresh, best_gain = None, None, -1
        parent_gini = self.gini(y)

        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for t in thresholds:
                X_l, X_r, y_l, y_r = self.split(X, y, feature, t)
                if len(y_l) == 0 or len(y_r) == 0:
                    continue
                g = (len(y_l)/len(y))*self.gini(y_l) + (len(y_r)/len(y))*self.gini(y_r)
                gain = parent_gini - g
                if gain > best_gain:
                    best_feature, best_thresh = feature, t
                    best_gain = gain
        return best_feature, best_thresh

    def build_tree(self, X, y, depth=0):
        if len(np.unique(y)) == 1 or depth >= self.max_depth:
            return Counter(y).most_common(1)[0][0]

        feature, threshold = self.best_split(X, y)
        if feature is None:
            return Counter(y).most_common(1)[0][0]

        X_l, X_r, y_l, y_r = self.split(X, y, feature, threshold)

        return {
            "feature": feature,
            "threshold": threshold,
            "left": self.build_tree(X_l, y_l, depth+1),
            "right": self.build_tree(X_r, y_r, depth+1)
        }

    def predict_one(self, tree, x):
        if not isinstance(tree, dict):
            return tree
        if x[tree["feature"]] <= tree["threshold"]:
            return self.predict_one(tree["left"], x)
        return self.predict_one(tree["right"], x)

    def predict(self, X):
        return np.array([self.predict_one(self.tree, x) for x in X])


# Random Forest
class RandomForest:
    def __init__(self, n_trees=5, max_depth=3):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []

    def bootstrap_sample(self, X, y):
        n_samples = X.shape[0]
        idxs = np.random.choice(n_samples, n_samples, replace=True)
        return X[idxs], y[idxs]

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(max_depth=self.max_depth)
            X_sample, y_sample = self.bootstrap_sample(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        return np.array([Counter(row).most_common(1)[0][0] for row in tree_preds])
