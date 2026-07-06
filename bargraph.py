import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C", "C++"]
marks = [85, 78, 90, 88]

plt.bar(subjects, marks)
plt.title("Bar Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
