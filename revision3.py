import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
arr = np.array([1, 2, 3, 4])
print(arr.mean())
print(arr.max())
df = pd.read_csv("data.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df[df["Age"] > 20])
