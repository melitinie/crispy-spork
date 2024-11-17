import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open("input.csv") as file:
        lines = [line for line in csv.DictReader(file)]

    with open("output.json", "w") as file:
        json.dump(lines, file, indent=4)


if __name__ == '__main__':
    task()

    with open("output.json") as out:
        for line in out:
            print(line, end="")