import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "Computer"]
marks = [80, 75, 90, 85]
plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Bar Graph")
plt.show()
