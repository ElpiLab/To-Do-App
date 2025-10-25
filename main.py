"""
Student Task Manager - Main Application
Team: Elpidio, Lencer, Valentina
"""

def main():  # Elpidio
    tasks = []  # This will store our tasks
    
    print("STUDENT TASK MANAGER")
    print("======================")
    
    while True:
        print("\nMAIN MENU")
        print("1. Add Task")
        print("2. View Tasks") 
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            tasks = add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            tasks = mark_complete(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            exit_app(tasks)
            break
        else:
            print("Invalid choice! Please a valid number between 1-5")

# Requirement 1 - Add tasks - Elpidio
def add_task(tasks_list):
    print("\n=== ADD NEW TASK ===")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = input("Choose a priority level (High/Medium/Low): ")
    
    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "completed": False
    }
    
    tasks_list.append(task)
    print(f"Your task '{title}' has been added successfully!")
    return tasks_list


# Requirement 2 - View Tasks - Lencer
def view_tasks(tasks_list):
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


# Requirement 3 - Mark Complete - Lencer
def mark_complete(tasks_list):
    print("\n=== MARK TASK COMPLETE ===")
    
    if len(tasks_list) == 0:
        print("No tasks to mark complete!")
        return tasks_list
    
    # Show tasks first
    view_tasks(tasks_list)
    
    try:
        task_num = int(input("Enter task number to mark complete: "))
        
        if 1 <= task_num <= len(tasks_list):
            tasks_list[task_num-1]["completed"] = True
            print(f"Done! Task '{tasks_list[task_num-1]['title']}' marked as complete!")
        else:
            print("Invalid task number!")
            
    except ValueError:
        print("Please enter a valid number!")
    
    return tasks_list


# Requirement 4 - Delete Task - Valentina
def delete_task(tasks_list):
    print("\n=== DELETE TASK ===")
    
    if len(tasks_list) == 0:
        print("No tasks to delete!")
        return tasks_list
    
    # Show tasks first
    view_tasks(tasks_list)
    
    try:
        task_num = int(input("Enter task number to delete: "))
        
        if 1 <= task_num <= len(tasks_list):
            deleted_task = tasks_list.pop(task_num-1)
            print(f" The task '{deleted_task['title']}' is deleted!")
        else:
            print("Invalid task number!")
            
    except ValueError:
        print("Please enter a valid number!")
    
    return tasks_list


# Requirement 5 - Exit . Valentina
def exit_app(tasks_list):
    print("\n=== EXIT ===")
    print("Thank you for using Student Task Manager!")
    print(f"You have {len(tasks_list)} task(s) in your list.")
    print("Goodbye!")

    # Note: File saving would be added here later

if __name__ == "__main__":
    main()