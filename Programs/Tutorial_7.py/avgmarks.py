
friends = {
    "F001": {
        "name": "John",
        "marks": {
            "maths": 90,
            "science": 80,
            "english": 70,
            "history": 60
        }
    },
    "F002": {
        "name": "Jane",
        "marks": {
            "maths": 80,
            "science": 70,
            "english": 60,
            "history": 50
        }
    },
    "F003": {
        "name": "Jack",
        "marks": {
            "maths": 70,
            "science": 60,
            "english": 50
        }
    },
    "F004": {
        "name": "Jill",
        "marks": {
            "maths": 60,
            "science": 50,
            "english": 40
        }
    }
}
english = []
for i in friends:
    for j in friends[i]["marks"]:
        if friends[i]["marks"]["english"] not in english:
            english.append(friends[i]["marks"]["english"])
science = []
for i in friends:
    for j in friends[i]["marks"]:
        if friends[i]["marks"]["science"] not in science:
            science.append(friends[i]["marks"]["science"])
history = []
for i in friends:
    for j in friends[i]["marks"]:
        if "history" == j:
            history.append(friends[i]["marks"]["history"])


print(sum(english)/4)
print(sum(science)/4)
print(sum(history)/2)
