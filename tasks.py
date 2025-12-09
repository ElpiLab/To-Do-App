from file import save_tasks_to_file
import config

# Requirement 1 - Add tasks - Elpidio + Lencer
def add_task(tasks_list):
    """
    Prompts user for task details and adds a new task to the list.
    Enforces minimum length for title and description.
    """
    print("\n=== ADD NEW TASK ===")
    
    # Input validation loop for Title
    while True:
        title = input(f"Enter task title (min {config.MIN_INPUT_LENGTH} chars): ").strip()
        if len(title) >= config.MIN_INPUT_LENGTH:
            # title = title.replace("|", "-")  # For non-JSON version: Sanitize input to prevent user from entering the delimiter
            break
        print(f"Title must be at least {config.MIN_INPUT_LENGTH} characters long.")

    # Input validation loop for Description
    while True:
        description = input(f"Enter task description (min {config.MIN_INPUT_LENGTH} chars): ").strip()
        if len(description) >= config.MIN_INPUT_LENGTH:
            # description = description.replace("|", "-")  # For non-JSON version: Sanitize input to prevent user from entering the delimiter
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
            # Check if input matches key, alias, or first word of label
            # e.g. '1', 'h', 'high' for High Priority
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
    Displays all tasks in the list with their status and details.
    """
    print("\n=== YOUR TASKS ===")
    
    if len(tasks_list) == 0:
        print("No tasks found. Add some tasks first!")
        return
    
    # Enumerate starting from 1 for user-friendly numbering
    for i, task in enumerate(tasks_list, 1):
        status = "DONE" if task["completed"] else "TODO"
        print(f"{i}. [{status}] {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Priority: {task['priority']}")
        print()

# Requirement 3 - Mark Complete - Lencer
def mark_complete(tasks_list):
    """
    Marks a selected task as complete based on user input.
    """
    print("\n=== MARK TASK COMPLETE ===")
    
    if len(tasks_list) == 0:
        print("No tasks to mark complete!")
        return
    
    # Show tasks so user knows which number to pick
    view_tasks(tasks_list)
    
    while True:
        try:
            user_input = input("Enter task number to mark complete (or 'c' to cancel): ").strip()
            
            if user_input.lower() == 'c':
                print("Operation cancelled.")
                return

            task_num = int(user_input)
            
            # Validate task number range
            if 1 <= task_num <= len(tasks_list):
                # Adjust for 0-based indexing
                tasks_list[task_num-1]["completed"] = True
                print(f"Done! Task '{tasks_list[task_num-1]['title']}' marked as complete!")
                
                # Auto-save after marking complete
                save_tasks_to_file(tasks_list)
                break
            else:
                print(f"{config.BOLD}Invalid task number!{config.RESET_FORMATTING} Please enter a number between 1 and {len(tasks_list)}.")
                
        except ValueError:
            print(f"{config.BOLD}Invalid input!{config.RESET_FORMATTING} Please enter a valid number.")

# Requirement 4 - Delete Task - Valentina
def delete_task(tasks_list):
    """
    Removes a selected task from the list.
    """
    print("\n=== DELETE TASK ===")
    
    if len(tasks_list) == 0:
        print("No tasks to delete!")
        return
    
    # Show tasks so user knows which number to pick
    view_tasks(tasks_list)
    
    while True:
        try:
            user_input = input("Enter task number to delete (or 'c' to cancel): ").strip()
            
            if user_input.lower() == 'c':
                print("Operation cancelled.")
                return

            task_num = int(user_input)
            
            # Validate task number range
            if 1 <= task_num <= len(tasks_list):
                # Remove task using pop() which returns the removed item
                deleted_task = tasks_list.pop(task_num-1)
                print(f" The task '{deleted_task['title']}' is deleted!")
                
                # Auto-save after deletion
                save_tasks_to_file(tasks_list)
                break
            else:
                print(f"{config.BOLD}Invalid task number!{config.RESET_FORMATTING} Please enter a number between 1 and {len(tasks_list)}.")
                
        except ValueError:
            print(f"{config.BOLD}Invalid input!{config.RESET_FORMATTING} Please enter a valid number.")
