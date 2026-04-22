import math
data = [
    ("Sunny", "No"),
    ("Sunny", "No"),
    ("Overcast", "Yes"),
    ("Rain", "Yes"),
    ("Rain", "Yes"),
    ("Rain", "No"),
    ("Overcast", "Yes"),
    ("Sunny", "No"),
    ("Sunny", "Yes"),
    ("Rain", "Yes")
]
def train(data):
    total = len(data)
    yes = sum(1 for x in data if x[1] == "Yes")
    no = total - yes

    prob_yes = yes / total
    prob_no = no / total

    return prob_yes, prob_no

def predict(outlook, data):
    prob_yes, prob_no = train(data)

    yes_count = sum(1 for x in data if x[0] == outlook and x[1] == "Yes")
    no_count = sum(1 for x in data if x[0] == outlook and x[1] == "No")

    total_yes = sum(1 for x in data if x[1] == "Yes")
    total_no = sum(1 for x in data if x[1] == "No")

    p_outlook_yes = yes_count / total_yes if total_yes else 0
    p_outlook_no = no_count / total_no if total_no else 0

    score_yes = prob_yes * p_outlook_yes
    score_no = prob_no * p_outlook_no

    return "Yes" if score_yes > score_no else "No"

print(predict("Sunny", data))
