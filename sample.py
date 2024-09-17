import datetime
import unittest

class Task:
    def __init__(self, description, due_date=None, priority=0):
        self.description = description
        self.completed = False
        self.due_date = due_date
        self.priority = priority

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.description}' added successfully.")

    def view_tasks(self, filter_option=None):
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
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

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

# Making some changes to the code.

# This Python script implements a Todo List Manager application with the following features:
# 1. Add tasks with descriptions, due dates, and priorities
# 2. View all tasks or filter them by completion status
# 3. Mark tasks as complete
# 4. Set task priorities
# 5. Basic error handling for user inputs
#
# The script also includes a set of unit tests to verify the core functionality of the TodoList class.
# When run, it first executes the tests and then starts the main application loop.
# Users can interact with the application through a command-line interface, choosing options
# from a menu to manage their tasks.