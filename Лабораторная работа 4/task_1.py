import json

def task() -> float:
    with open("input.json", 'r') as file:
        data = json.load(file)

    summa = 0

    for i in data:
        if "score" and "weight" in i:
            summa += i["score"] * i["weight"]

    return round(summa, 3)

print(task())
