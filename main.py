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

# Requirement 2 Nats
def view_task(tasks_list):
    print("Your To Do List")
    if len(tasks_list) == 0:
        print("No tasks for you! Add a new task")
    else
     for index, task in enumerate (tasks_list, 1):
        
        
if __name__ == "__main__":
    main()
