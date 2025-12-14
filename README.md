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
- As a student, I want to mark a task as complete, so that I can visually track my progress and maintain motivation
- As a student, I want to track time and see the time invested(in minutes/hours) for each task/project, so that I can accurately estimate time for future projects and improve my planning.
- As a student, I want to categorize based on topics, priority, due date, and color-code, so that I can constantly manage my time during stressful periods
- As a student, I want to delete old/redundant tasks, so that my task list remains clean and focused only on actionable items.
- As a student, I want to start and end a session using Pomodoro, e.g,  (25 min work/5 min break), so that I can maintain deep focus and prevent burning out during long study sessions.
- As a student, I want to see the weekly, monthly, and yearly calendars

### Use cases: 
  - Show Menu: Display list of actions in the console: Add Task, View Tasks, Mark as Done, Delete, Exit
  - Create/Edit Tasks - Allow new entry or modification of tasks with details: title, description, due date, priority.
  - Show Current Tasks: Display all tasks with clear status, priority, description, and time spent based on Pomodoro Info 
  - Edit or delete Tasks- Allow the user to modify an existing task's title, description, priority, or permanently delete it from the list.
  - Tracking Tasks: Display statistical reports on productivity, e.g, completion time, time spent on all tasks, or each task.
  - Pomodoro Session: Implement a precise timer function to start, pause, or reset structured work/break cycles (e.g, 25 minutes study, 5 minutes break) to improve focus.(long term)

 

1- Interactive App (console input)
The application is fully console-based. Users can:

    . See a main menu with options (add, view, mark complete, delete, exit).

    . Enter their choice as a number, first letter, or full word (e.g. 1, a, add).

    . Follow prompts to enter task details such as title, description, and priority.

    . Receive feedback messages after each operation (task added, updated, deleted, saved).

This satisfies the requirement for an interactive console application

2- Data validation (input checking)

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in task_add_view.py and task_complete_delete.py as follows:

Menu selection: When adding a task, the program enforces a minimum length to prevent empty or meaningless entries:

  while True:
     title = input(f"Enter task title (min {config.MIN_INPUT_LENGTH} chars): ").strip()
     if len(title) >= config.MIN_INPUT_LENGTH:
         break
     print(f"Title must be at least {config.MIN_INPUT_LENGTH} characters long.")

This ensures only valid menu items can be ordered.

Menu file validation: When reading the menu file, the program checks for valid price values and skips invalid lines:

Task Integrity: When adding a task, the program enforces a minimum length to prevent empty or meaningless entries:

Operational Safety: When deleting or completing tasks, the system uses try-except blocks to catch non-numeric inputs and range checks to prevent "IndexError" crashes

This ensures that every task stored in the JSON file has valid content.

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
