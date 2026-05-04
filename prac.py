import numpy as np

# Calculate Gini Impurity
def gini(y):
    classes = np.unique(y)
    impurity = 1
    for c in classes:
        p = np.sum(y == c) / len(y)
        impurity -= p ** 2
    return impurity

# Split dataset
def split(X, y, feature, threshold):
    left_mask = X[:, feature] <= threshold
    right_mask = X[:, feature] > threshold
    return X[left_mask], X[right_mask], y[left_mask], y[right_mask]

# Find best split
def best_split(X, y):
    best_feature, best_thresh, best_gain = None, None, -1
    parent_gini = gini(y)

    n_features = X.shape[1]

    for feature in range(n_features):
        thresholds = np.unique(X[:, feature])

        for t in thresholds:
            X_l, X_r, y_l, y_r = split(X, y, feature, t)

            if len(y_l) == 0 or len(y_r) == 0:
                continue

            n = len(y)
            g = (len(y_l)/n) * gini(y_l) + (len(y_r)/n) * gini(y_r)
            gain = parent_gini - g

            if gain > best_gain:
                best_feature = feature
                best_thresh = t
                best_gain = gain

    return best_feature, best_thresh

# Node class
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

# Build tree
def build_tree(X, y, depth=0, max_depth=3):
    if len(np.unique(y)) == 1 or depth >= max_depth:
        return Node(value=np.bincount(y).argmax())

    feature, threshold = best_split(X, y)

    if feature is None:
        return Node(value=np.bincount(y).argmax())

    X_l, X_r, y_l, y_r = split(X, y, feature, threshold)

    left = build_tree(X_l, y_l, depth+1, max_depth)
    right = build_tree(X_r, y_r, depth+1, max_depth)

    return Node(feature, threshold, left, right)

# Predict one sample
def predict_one(node, x):
    if node.value is not None:
        return node.value

    if x[node.feature] <= node.threshold:
        return predict_one(node.left, x)
    else:
        return predict_one(node.right, x)

# Predict multiple
def predict(tree, X):
    return np.array([predict_one(tree, x) for x in X])
