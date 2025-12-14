# To-Do-App

A console for managing tasks for students.  
Here is the documentation of our To-Do App in the Programming Foundations class.

## Analysis

### Problem
As first-year BIT students, we face challenges juggling multiple modules, assignments, group projects, and personal study goals. This leads to constant brain overload and decision fatigue, which in turn leads to the following struggles:

- Difficulty in prioritizing the urgency of assignments, leading to effort underestimation.
- Poor time management caused by insufficient time allocation, leading to procrastination and last-minute stress.
- Low productivity and poor focus as tasks lack clear boundaries and priorities, which causes mental strain during studies.

## Impact

Lack of a centralized system to maximize productivity, especially in first-year students, often leads to:

- Procrastination
- Inefficient study time
- Last-minute stress
- Sometimes missed deadlines with projects and assignments
- Poor grades

## Solution

Our interactive To-Do-App with task organization provides an effective system and strategic ways to improve productivity by:

- Reducing stress through clear visualization of tasks and a centralized priority system

## Scenario

Based on our modules, we have different requirements, teams, and group projects.  
The idea is to put all tasks in the console application to manage and organize them in one centralized place.

## Requirements / User Stories

-As a student, I want to add a new task with a title, description, and priority so that I have all my To Do Tasks centralized and easily organized
- As a student, I want to see the "view my tasks" on the console, so that I can immediately get an overview of the workload I have
- As a student, I want to mark a task as complete

### Use cases: 
  - Show Menu: Display list of actions in the console: Add Task, View Tasks, Mark as Done, Delete, Exit
  - Create/Edit Tasks - Allow new entry or modification of tasks with details: title, description, due date, priority.
  - Show Current Tasks: Display all tasks with clear status, priority, description
  - Edit or delete Tasks- Allow the user to modify an existing task's title, description, priority, or permanently delete it from the list.

1- Interactive App (console input)
The application is fully console-based. Users can:

    . See a main menu with options (add, view, mark complete, delete, exit).

    . Enter their choice as a number, first letter, or full word (e.g. 1, a, add).

    . Follow prompts to enter task details such as title, description, and priority.

    . Receive feedback messages after each operation (task added, updated, deleted, saved).

This satisfies the requirement for an interactive console application.

2- Data validation (input checking)
The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main.py`, `tasks_add_view.py`, and `tasks_complete_delete.py` as follows:

- **Menu Input:** User input is lowercased/stripped. It must match a menu key, an alias, or the underlined first letter of the label.
  Otherwise, the app prints a targeted “Invalid choice” message.
	```python
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

  if not selected_function:
    print(f"\n{config.BOLD}Invalid choice: '{choice}'{config.RESET_FORMATTING}")
    print("Please enter one of the following:")
    print(" - The number (e.g., '1')")
    print(" - The underlined letter (e.g., 'a')")
    print(" - The full word (e.g., 'add')")
	```
	This ensures only valid menu items can be executed.

- **Function dispatch Safety:** only calls existing functions; otherwise reports a configuration error.
	```python
	def get_function(selected_function):
    for module in (tasks_add_view, tasks_complete_delete):
        if hasattr(module, selected_function):
            return getattr(module, selected_function)
    return globals().get(selected_function)
	```
 Ensures only functions that actually exist in the action modules/globals are invoked; missing/typo’d config entries are caught as configuration errors instead of crashing.
 
- **Title description and length:** Enforce minimum length from config.MIN_INPUT_LENGTH.
	```python
	while True:
    title = input(f"Enter task title (min {config.MIN_INPUT_LENGTH} chars): ").strip()
    if len(title) >= config.MIN_INPUT_LENGTH:
        break
    print(f"Title must be at least {config.MIN_INPUT_LENGTH} characters long.")

  while True:
    description = input(f"Enter task description (min {config.MIN_INPUT_LENGTH} chars): ").strip()
    if len(description) >= config.MIN_INPUT_LENGTH:
        break
    print(f"Description must be at least {config.MIN_INPUT_LENGTH} characters long.")
	```

These prevents empty/too-short task titles.

---

- **Priority Selection:** Must match a key, alias, or first word of the label; otherwise, reprompts.
	```python
	priority = "Medium"  # default
  while True:
    p_choice = input("Choose a priority level: ").lower().strip()
    found = False
    for option in config.PRIORITY_OPTIONS:
        if (p_choice == option['key']
            or p_choice in option['aliases']
            or p_choice == option['label'].split()[0].lower()):
            priority = option['level']
            found = True
            break
    if found:
        break
    print("Invalid priority. Please try again. Use the number, first letter or first word.")
	```
 This prevents invalid priority values.
 
 - **Empty List guard:** aborts when there are no tasks to act on.
	```python
   if len(tasks_list) == 0:
    print("No tasks to mark complete!")
    return
	```
This avoids invalid indexing on an empty list.

---

- **Mark Complete/Delete:** The main menu checks for valid options and handles invalid choices gracefully:
	```python
  if len(tasks_list) == 0:
    print("No tasks to mark complete/delete!")
    return

  user_input = input("Enter task number (or 'c' to cancel): ").strip()
  if user_input.lower() == 'c':
    print("Operation cancelled.")
    return

  task_num = int(user_input)  # ValueError → "Invalid input! Please enter a valid number."
  if 1 <= task_num <= len(tasks_list):
    # mark_complete: tasks_list[task_num-1]["completed"] = True; save_tasks_to_file(...)
    # delete_task: deleted_task = tasks_list.pop(task_num-1); save_tasks_to_file(...)
  else:
    print(f"{config.BOLD}Invalid task number!{config.RESET_FORMATTING} Please enter a number between 1 and {len(tasks_list)}.")
Prevents non-numeric input and out-of-range task selection before updating/deleting and saving.	```
---

3- File processing(read/write) 
The application persists tasks using a JSON file:

- Input/output file: tasks.json

    . Stores all tasks as a JSON array of task objects.
    . Each task contains fields such as title, description, priority, and completed.

- Reading data

    . On startup, the application attempts to load existing tasks from tasks.json.

    . If the file does not exist, a new empty task list is used.

    . If the file exists but cannot be decoded as valid JSON, the app falls back to an empty list to avoid crashes.

- Writing data (auto-save)

    . After each task operation (add, mark complete, delete), the current task list is written back to tasks.json.

    . Data is written using a context manager to ensure the file is properly opened and closed.

    . This guarantees that the latest state is always stored and available on the next start.


## Future Roadmap (Missing Features)
Pomodoro

Task editing

Time tracking

Due dates & calendar
 
## Team
Elpidio – Development & Documentation

Lencer – Development, Refactoring & Documentation

Valentina – Development, Refactoring, Branding, Presentation & Documentation
