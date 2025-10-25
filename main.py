"""
Student Task Manager - Main Application
Team: Elpidio, Lencer, Valentina
"""

def main(): #Elpidio
    tasks = []  # This will store our tasks
    
    print("STUDENT TASK MANAGER")
    print("======================")
    
    while True:
        print("\n MAIN MENU")
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
            view_task(tasks)
        elif choice == "3":
            # Person 2 will implement this
           tasks = mark_task_complete(tasks)
        elif choice == "4":
            # Person 3 will implement this
            tasks = delete_task(tasks)

        elif choice == "5":
           # Person 3 will implement this
         exit_app(tasks)
         break
        else:
            print("❌ Invalid choice! Please enter 1-5")


# Requirement 1 Elpidio
def add_task(tasks_list):
    title = input("Please enter the title of your task: ")
    description = input("Please describe this task: ")
    priority = input("Enter the level of priority of the task: ")

    task = {"title" : title,
            "description": description,
            "priority": priority
            }

    tasks_list.append(task)
    print(f"Here is the overview of your task {task}")

    return tasks_list

# Requirement 2 Lencer
def view_task(tasks_list):
    if not tasks_list:
        print("\n Your To Do List is empty. Add a task to get started!")
    else:
        print("\n---YOUR CURRENT TASKS---")
        for index, task in enumerate (tasks_list, 1): # Start enumeration at 1 so users see [1], [2], [3] instead of [0], [1], [2]
            is_complete = task.get("complete", False)
            status = "✅ COMPLETE" if is_complete else "❌ Pending"
            print(f"[{index}] - {status}")
            print(f"Title: {task['title']}")
            print(f"Priority: {task['priority']}")
            print(f"Description: {task['description']}")
            print("-" * 25)

#Requirement 3 Lencer
def mark_task_complete(tasks_list):
    #prompts user to mark a task as complete
    print("\n==MARK TASK COMPLETE==")
    view_task(tasks_list)

    if not tasks_list:
        return tasks_list

    try:
        task_num = int(input("Enter the task number from your CURRENT TASKS to mark complete: "))
        index = task_num -1

        #Check if the calculated index is valid (within the list's bounds)
        if 0 <= index < len(tasks_list):
            tasks_list[index]["complete"] = True
            print(f"\nTask '{tasks_list[index]['title']}' marked as COMPLETE!")
            print("To confirm the status change, select Option 2 (View Tasks) from the menu.")
        else:
            print(f"\n Invalid task number. Please enter a number between 1 and {len(tasks_list)}.")
    except ValueError:
        #Handle case where user enters text/non-integer input
        print("\n Invalid input. Please enter a valid whole number")
    
    return tasks_list 

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
    
