import matplotlib.pyplot as plt
marks = [45, 56, 67, 78, 89, 90, 67, 56, 78, 88, 90, 76]
plt.hist(marks, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
