# Lencer

# Define minimum input length for task titles/descriptions
MIN_INPUT_LENGTH = 3

# File path and name for storing tasks
TASKS_FILE = 'tasks.json'

# ANSI Escape Codes for formatting
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
RESET_FORMATTING = '\033[0m'

# Define Menu Options
PRIORITY_OPTIONS = [
    {
        'key': '1',
        'label': 'High Priority',
        'level': 'High',
        'aliases': ['h', 'high']
    },
    {
        'key': '2',
        'label': 'Medium Priority',
        'level': 'Medium',
        'aliases': ['m', 'medium']
    },
    {
        'key': '3',
        'label': 'Low Priority',
        'level': 'Low',
        'aliases': ['l', 'low']
    },
]

# Define Menu Options
MENU_OPTIONS = [
    {
        'key': '1',
        'label': 'Add Task',
        'function': 'add_task',
        'aliases': ['a', 'add']
    },
    {
        'key': '2',
        'label': 'View Tasks',
        'function': 'view_tasks',
        'aliases': ['v', 'view']
    },
    {
        'key': '3',
        'label': 'Mark Task Complete',
        'function': 'mark_complete',
        'aliases': ['m', 'mark']
    },
    {
        'key': '4',
        'label': 'Delete Task',
        'function': 'delete_task',
        'aliases': ['d', 'delete', 'del']
    },
    {
        'key': '5',
        'label': 'Exit',
        'function': 'exit_app',
        'aliases': ['e', 'exit']
    },
]

