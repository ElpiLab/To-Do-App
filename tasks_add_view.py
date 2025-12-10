from file import save_tasks_to_file
import config

def add_task(tasks_list):
    """
    Prompt for task details, validate inputs, and append the task.
    """
    print("\n=== ADD NEW TASK ===")
    
    # Input validation loop for Title
    while True:
        title = input(f"Enter task title (min {config.MIN_INPUT_LENGTH} chars): ").strip()
        if len(title) >= config.MIN_INPUT_LENGTH:
            break
        print(f"Title must be at least {config.MIN_INPUT_LENGTH} characters long.")

    # Input validation loop for Description
    while True:
        description = input(f"Enter task description (min {config.MIN_INPUT_LENGTH} chars): ").strip()
        if len(description) >= config.MIN_INPUT_LENGTH:
            break
        print(f"Description must be at least {config.MIN_INPUT_LENGTH} characters long.")

    # Display Priority Options
    print("\nSelect Priority:")
    for option in config.PRIORITY_OPTIONS:
        # Underline first letter of label for display
        label = option['label']
        first_letter = label[0]
        rest = label[1:]
        display_label = f"{config.UNDERLINE}{first_letter}{config.RESET_FORMATTING}{rest}"
        print(f"{option['key']}. {display_label}")
    
    priority = "Medium" # Default fallback
    
    # Priority Selection Loop
    while True:
        p_choice = input("Choose a priority level: ").lower().strip()
        found = False
        for option in config.PRIORITY_OPTIONS:
            if (p_choice == option['key'] or 
                p_choice in option['aliases'] or 
                p_choice == option['label'].split()[0].lower()
                ):
                priority = option['level']
                found = True
                break
        
        if found:
            break
        print("Invalid priority. Please try again. Use the number, first letter or first word.")

    # Create task dictionary
    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "completed": False
    }
    
    # Add to list and save
    tasks_list.append(task)
    print(f"Your task '{title}' has been added successfully!")
    
    # Auto-save after adding task
    save_tasks_to_file(tasks_list)

# Requirement 2 - View Tasks - Lencer
def view_tasks(tasks_list):
    """
    Display tasks with status and details.
    """
    print("\n=== YOUR TASKS ===")
    
    if len(tasks_list) == 0:
        print("No tasks found. Add some tasks first!")
        return
    
    for i, task in enumerate(tasks_list, 1):
        status = "DONE" if task["completed"] else "TODO"
        print(f"{i}. [{status}] {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Priority: {task['priority']}")
        print()