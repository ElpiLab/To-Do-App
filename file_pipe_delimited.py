import config

def tasks_from_file():
    """Load tasks from file using context manager"""
    tasks = []
    # Open file for reading using 'with' to ensure it closes automatically
    with open(config.TASKS_FILE, 'r') as file_object:
        # Read each line from the file (Loop)
        for line in file_object:
            # Remove newline character and split fields
            line = line.rstrip('\n')
            fields = line.split('|')
            
            if len(fields) == 4:
                task = {
                    "title": fields[0],
                    "description": fields[1],
                    "priority": fields[2],
                    "completed": fields[3].strip() == 'True'
                }
                tasks.append(task)
    
    return tasks

def save_tasks_to_file(tasks_list):
    """Save tasks to file using context manager"""
    # Open file for writing using 'with'
    with open(config.TASKS_FILE, 'w') as file_object:
        # Write each task to the file
        for task in tasks_list:
            # Convert task data to string and concatenate newline
            line = f"{task['title']}|{task['description']}|{task['priority']}|{task['completed']}\n"
            file_object.write(line)
