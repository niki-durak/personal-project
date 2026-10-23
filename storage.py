import json

def save_to_json(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses,file, indent=2)

def load_from_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []