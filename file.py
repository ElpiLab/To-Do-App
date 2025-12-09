import config
import json

def tasks_from_file(): #To define who presents this part
    """Load tasks from file using context manager"""
    tasks = []
    # Open file for reading using 'with' to ensure it closes automatically
    with open(config.TASKS_FILE, 'r') as file_object:
        tasks = json.load(file_object)
    
    return tasks

def save_tasks_to_file(tasks_list):
    """Save tasks to file using context manager"""
    # Open file for writing using 'with'
    with open(config.TASKS_FILE, 'w') as file_object:
        json.dump(tasks_list, file_object, indent=4)
