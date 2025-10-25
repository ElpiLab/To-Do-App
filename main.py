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
            # Person 2 will implement this  
            print("View Tasks")
        elif choice == "3":
            # Person 2 will implement this
            print("Mark Tasks as Complete")
        elif choice == "4":
            # Person 3 will implement this
            print("Delete Task ")
        elif choice == "5":
            # Person 3 will implement this
            print("Exit the application")
            break
        else:
            print("Invalid choice! Please a valid number between 1-5")

# Requirement 1 - Add Task - Elpidio
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
    print(f"Here is the overview of your task {task}")

    return tasks_list


# Requirement 5 - Exit - Valentina
def exit_app(tasks_list):
    print("\n=== EXIT ===")
    print("Thank you for using Student Task Manager!")
    print(f"You have {len(tasks_list)} task(s) in your list.")
    print("Goodbye!")

    # Note: File saving would be added here later

if __name__ == "__main__":
    main()

# Requirement 4 Valentina 
 
def delete_task(tasks_list):
    print("\n== DELETE TASK ==")

    if not tasks_list:
        print("There are no tasks to delete.")
        return tasks_list

    for i, task in enumerate(tasks_list, start=1):
        print(f"{i}. {task['title']}")

    try:
        task_num = int(input("Enter the task number you want to delete: ")) - 1
        if 0 <= task_num < len(tasks_list):
            deleted = tasks_list.pop(task_num)
            print(f"Task '{deleted['title']}' deleted successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

    return tasks_list
    
# Requirement 5 Valentina
def exit_app(tasks_list):
    print("\n== EXIT APPLICATION ==")
    save = input("Do you want to save your tasks before exiting? (y/n): ").lower()

    if save == "y":
        with open("tasks.txt", "w") as file:
            for task in tasks_list:
                status = "Complete" if task.get("complete", False) else "Pending"
                file.write(f"{task['title']} | {task['description']} | {task['priority']} | {status}\n")
        print("\n Tasks saved successfully in 'tasks.txt'.")

    print("\n Thank you for using Student Task Manager. Goodbye!")
    
