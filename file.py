import config
import json


def tasks_from_file():
    """Load all tasks from the JSON data file."""
    with open(config.TASKS_FILE, 'r') as file_object:
        return json.load(file_object)


def save_tasks_to_file(tasks_list):
    """Persist tasks to the JSON data file."""
    with open(config.TASKS_FILE, 'w') as file_object:
        json.dump(tasks_list, file_object, indent=4)
