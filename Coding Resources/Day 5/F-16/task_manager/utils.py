import json
from models import Task

def save_tasks_to_file(tasks, filename):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []