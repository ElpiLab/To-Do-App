from file import save_tasks_to_file
from tasks_add_view import view_tasks
import config

# Requirement 3 - Mark Complete
def mark_complete(tasks_list):
    """
    Mark a selected task as complete.
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
            
            if 1 <= task_num <= len(tasks_list):
                tasks_list[task_num-1]["completed"] = True
                print(f"Done! Task '{tasks_list[task_num-1]['title']}' marked as complete!")
                
                save_tasks_to_file(tasks_list)
                break
            else:
                print(f"{config.BOLD}Invalid task number!{config.RESET_FORMATTING} Please enter a number between 1 and {len(tasks_list)}.")
                
        except ValueError:
            print(f"{config.BOLD}Invalid input!{config.RESET_FORMATTING} Please enter a valid number.")

# Requirement 4 - Delete Task 
def delete_task(tasks_list):
    """
    Removes a selected task from the list.
    """
    print("\n=== DELETE TASK ===")
    
    if len(tasks_list) == 0:
        print("No tasks to delete!")
        return
    
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
                deleted_task = tasks_list.pop(task_num-1)
                print(f" The task '{deleted_task['title']}' is deleted!")
                
                # Auto-save after deletion
                save_tasks_to_file(tasks_list)
                break
            else:
                print(f"{config.BOLD}Invalid task number!{config.RESET_FORMATTING} Please enter a number between 1 and {len(tasks_list)}.")
                
        except ValueError:
            print(f"{config.BOLD}Invalid input!{config.RESET_FORMATTING} Please enter a valid number.")



