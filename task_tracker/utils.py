from pathlib import Path
import json

file_path = Path("data/tasks.json")


def print_header():
    HEADER = "NKQ Task Tracker"

    print(HEADER)
    print( "-" * len(HEADER), "\n")


def get_records():
    if file_path.exists():
        with open(file_path, "r") as file:
            try:
                records = json.load(file)
            except json.JSONDecodeError:
                records = {}
    else:
        records = {}

    return records


def write_data(records):
    with open(file_path, "w") as file:
        json.dump(records, file, indent = 4)

