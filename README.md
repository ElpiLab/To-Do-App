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

- As a user, I want to add a new task with a title, description, and priority so that I have all my To-Do tasks centralized and easily organized.
- As a user, I want to see my tasks in the console so that I can immediately get an overview of my workload.
- As a user, I want to delete old or redundant tasks so that my task list remains clean and focused only on actionable items.

## Use Cases

- Show Menu: Display list of actions in the console: Add Task, View Tasks, Delete Task, Exit.
- Create Tasks: Allow entry of tasks with details such as title, description, and priority level.
- Show Current Tasks: Display all tasks with clear priority and status.
- Delete Tasks: Allow the user to permanently remove unwanted or completed tasks from the list.

## Technical Features

### 1. Interactive App (Console Input)
The application interacts with the user through the console, accepting input and displaying responses in real time.  
It provides clear prompts, menus, and feedback to create an engaging and easy-to-use experience.

### 2. Data Validation (Input Checking)
The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `task_add_view.py` and `task_complete_delete.py` as follows:

- **Menu selection:** When adding a task, the program enforces a minimum length to prevent empty or meaningless entries:
	```python
	 while True:
        title = input(f"Enter task title (min {config.MIN_INPUT_LENGTH} chars): ").strip()
        if len(title) >= config.MIN_INPUT_LENGTH:
            break
        print(f"Title must be at least {config.MIN_INPUT_LENGTH} characters long.")
	```
	This ensures only valid menu items can be ordered.

- **Menu file validation:** When reading the menu file, the program checks for valid price values and skips invalid lines:
- **Task Integrity:** When adding a task, the program enforces a minimum length to prevent empty or meaningless entries:


- **Operational Safety:** When deleting or completing tasks, the system uses try-except blocks to catch non-numeric inputs and range checks to prevent "IndexError" crashes
 

This ensures that every task stored in the JSON file has valid content.

### 3. File Processing (Read / Write)
The application can read data from and write data to files, allowing users to save and retrieve information.  
This ensures that data is stored securely and can be accessed or updated when needed.

## Future Roadmap (Missing Features)

- Pomodoro
- Task editing
- Time tracking
- Due dates & calendar

- ## Team

- Elpidio – Development & Documentation  
- Lencer – Development, Refactoring & Documentation  
- Valentina – Development, Refactoring, Branding, Presentation & Documentation  
