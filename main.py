"""
Student Task Manager - Main Application
Team: Elpidio, Lencer, Valentina
"""
from file import tasks_from_file, save_tasks_to_file
import tasks_add_view
import tasks_complete_delete
import config
import json


def get_function(selected_function):
    """Resolve the function name to a callable across action modules or globals."""
    for module in (tasks_add_view, tasks_complete_delete):
        if hasattr(module, selected_function):
            return getattr(module, selected_function)
    return globals().get(selected_function)


def main():  
    """
    Main application entry point.
    Initializes the application, loads data, and runs the main event loop.
    """
    
    print("\nSTUDENT TASK MANAGER")
    print("======================\n")
    
    # Load tasks from file at startup
    try:
        task_list = tasks_from_file()
    except FileNotFoundError:
        print("\nNo saved tasks found. Starting with an empty list.")
        task_list = []
    except json.JSONDecodeError:
        print(f"\n{config.BOLD}Error loading tasks:{config.RESET_FORMATTING} File is corrupted or empty.")
        print("Starting with an empty task list.\n")
        task_list = []
    except Exception as e:
        print(f"\n{config.BOLD}Error loading tasks from file:{config.RESET_FORMATTING} {e}")
        print("Starting with an empty task list.\n")
        task_list = []
    
    while True:
        # Display the menu dynamically based on config.MENU_OPTIONS
        print(f"\n{config.UNDERLINE}MAIN MENU{config.RESET_FORMATTING}\n")
        for option in config.MENU_OPTIONS:
            # Underline first letter of label for display to indicate it's a hotkey
            label = option['label']
            first_letter = label[0]
            rest = label[1:]
            display_label = f"{config.UNDERLINE}{first_letter}{config.RESET_FORMATTING}{rest}"
            print(f"{option['key']}. {display_label}")
        
        choice = input("\nEnter your choice: ").lower().strip()
        
        selected_function = next(
            (
                option.get('function')
                for option in config.MENU_OPTIONS
                if choice == option['key']
                or choice in option['aliases']
                or choice == option['label'][0].lower()
            ),
            None,
        )
        
        if selected_function:
            # Dynamic Function Dispatch across action modules (add/view/complete/delete) or globals (exit)
            func = get_function(selected_function)
            
            if func:
                try:
                    # Execute the retrieved function, passing the current tasks list
                    # Functions modify the list in-place, so no return value is needed.
                    func(task_list)
                    
                    # Special handling for exit to break the application loop
                    if selected_function == "exit_app":
                        return
                        
                except Exception as e:
                    print(f"\n{config.BOLD}Error executing '{selected_function}':{config.RESET_FORMATTING} {e}")
                    print("Returning to main menu...")
            else:
                print(f"\n{config.BOLD}Configuration Error:{config.RESET_FORMATTING} Function '{selected_function}' not found.")
                print("Ensure it is imported in main.py and matches the name in config.py.")
        else:
            print(f"\n{config.BOLD}Invalid choice: '{choice}'{config.RESET_FORMATTING}")
            print("Please enter one of the following:")
            print(" - The number (e.g., '1')")
            print(" - The underlined letter (e.g., 'a')")
            print(" - The full word (e.g., 'add')")


def exit_app(tasks_list):
    """
    Handle application exit. Tasks are already auto-saved on add/complete/delete.
    """
    print("\n=== EXIT ===")
    save_tasks_to_file(tasks_list)
    print("Thank you for using Student Task Manager!")
    print(f"You have {len(tasks_list)} task(s) in your list.")
    print("Goodbye!")


if __name__ == "__main__":
    main()
