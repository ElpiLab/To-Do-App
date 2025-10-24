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
            print("Delete Task ")
        elif choice == "5":
            # Person 3 will implement this
            print("Exit the application")
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
        for index, task in enumerate (tasks_list, 1):
            is_complete = task.get("complete", False)
            status = "✅ COMPLETE" if is_complete else "❌ Pending"
            print(f"[{index}] - {status}")
            print(f"Title: {task['title']}")
            print(f"Priority: {task['priority']}")
            print(f"Description: {task['description']}")
            print("-" * 25)

#Requirement 3 Lencer
def mark_task_complete(tasks_list):
    print("\n==MARK TASK COMPLETE==")
    view_task(tasks_list)

    if not tasks_list:
        return tasks_list

    try:
        task_num = int(input("Enter the task number to mark complete: "))
        index = task_num -1

        if 0 <= index < len(tasks_list):
            tasks_list[index]["complete"] = True
            print(f"\nTask '{tasks_list[index]['title']}' marked as COMPLETE!")
        else:
            print(f"\n Invalid task number. Please enter a number between 1 and {len(tasks_list)}.")
    except ValueError:
        print("\n Invalid input. Please enter a valid whole number")
    
    return tasks_list 

if __name__ == "__main__":
    main()
