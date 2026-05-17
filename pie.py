import matplotlib.pyplot as plt
labels = ["Python", "Java", "C", "C++"]
sizes = [35, 25, 20, 20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
