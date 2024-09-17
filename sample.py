import datetime
import unittest

class Task:
    def __init__(self, description, due_date=None, priority=0):
        self.description = description
        self.completed = False
        self.due_date = due_date
        self.priority = priority
        self.created_at = datetime.datetime.now()

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.description}' added successfully.")

    def view_tasks(self, filter_option=None, sort_by=None):
        # Check if the task list is empty
        if not self.tasks:
            print("No tasks in the list.")
            return

        # Filter tasks based on the filter_option
        filtered_tasks = self.tasks
        if filter_option == "completed":
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_option == "pending":
            filtered_tasks = [task for task in self.tasks if not task.completed]

        # Sort tasks based on the sort_by option
        if sort_by == "priority":
            filtered_tasks.sort(key=lambda x: (-x.priority, x.created_at))
        elif sort_by == "due_date":
            filtered_tasks.sort(key=lambda x: (x.due_date or datetime.date.max, x.created_at))

        # Display filtered tasks
        for index, task in enumerate(filtered_tasks, 1):
            status = "✓" if task.completed else " "
            due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
            priority = "!" * task.priority
            print(f"{index}. [{status}] {task.description} (Due: {due_date}) {priority}")

    def complete_task(self, task_index):
        # Mark a task as complete if the index is valid
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Task '{self.tasks[task_index - 1].description}' marked as complete.")
        else:
            print("Invalid task index.")

    def set_priority(self, task_index, priority):
        # Set priority for a task if the index is valid
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].priority = priority
            print(f"Priority set for task '{self.tasks[task_index - 1].description}'.")
        else:
            print("Invalid task index.")

    def edit_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            print(f"Editing task: {task.description}")
            new_description = input("Enter new description (or press Enter to keep current): ")
            if new_description:
                task.description = new_description
            new_due_date = get_date_input()
            if new_due_date:
                task.due_date = new_due_date
            new_priority = input("Enter new priority (0-3, or press Enter to keep current): ")
            if new_priority:
                task.priority = int(new_priority)
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

def get_date_input():
    # Get a valid date input from the user
    while True:
        date_str = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
        if not date_str:
            return None
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-D.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- Todo List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Set Task Priority")
        print("5. Filter Tasks")
        print("6. Edit Task")
        print("7. Sort Tasks")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            description = input("Enter the task description: ")
            due_date = get_date_input()
            priority = int(input("Enter priority (0-3, 0 being lowest): "))
            todo_list.add_task(Task(description, due_date, priority))
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to mark as complete: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to set priority: "))
            priority = int(input("Enter priority (0-3, 0 being lowest): "))
            todo_list.set_priority(task_index, priority)
        elif choice == "5":
            filter_option = input("Enter filter option (all/completed/pending): ").lower()
            todo_list.view_tasks(filter_option if filter_option != "all" else None)
        elif choice == "6":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to edit: "))
            todo_list.edit_task(task_index)
        elif choice == "7":
            sort_option = input("Sort by (priority/due_date): ").lower()
            todo_list.view_tasks(sort_by=sort_option)
        elif choice == "8":
            print("Thank you for using Todo List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        task = Task("Test task")
        self.todo_list.add_task(task)
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].description, "Test task")

    def test_complete_task(self):
        task = Task("Test task")
        self.todo_list.add_task(task)
        self.todo_list.complete_task(1)
        self.assertTrue(self.todo_list.tasks[0].completed)

    def test_set_priority(self):
        task = Task("Test task")
        self.todo_list.add_task(task)
        self.todo_list.set_priority(1, 2)
        self.assertEqual(self.todo_list.tasks[0].priority, 2)

if __name__ == "__main__":
    # Run the tests
    unittest.main(exit=False)
    
    # Run the main application
    main()

# This Python script implements a Todo List Manager with the following components:

# Classes:
# 1. Task: Represents a single task with attributes for description, completion status,
#    due date, priority, and creation timestamp.
# 2. TodoList: Manages a collection of Task objects and provides methods for task operations.

# Key features:
# 1. Add tasks: Create new tasks with descriptions, optional due dates (YYYY-MM-DD format),
#    and priority levels (0-3).
# 2. View tasks: Display all tasks or filter by completion status (completed/pending).
# 3. Complete tasks: Mark individual tasks as completed.
# 4. Set priorities: Assign priority levels to tasks (0-3, with 3 being highest).
# 5. Edit tasks: Update task descriptions, due dates, and priorities.
# 6. Sort tasks: Sort tasks by priority or due date.

# User interface:
# - Command-line menu system for user interaction.
# - Input validation for date formats and menu choices.

# Testing:
# - Includes unit tests for core TodoList functionalities (add, complete, set priority).
# - Tests are automatically run before the main application starts.

# Execution flow:
# 1. Unit tests are executed.
# 2. Main application loop begins, presenting the user with a menu of options.
# 3. User can perform actions until choosing to quit the application.

# Note: This script is designed for educational purposes and basic task management.
# It does not include data persistence between sessions.