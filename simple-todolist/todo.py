import os
import json

class SimpleToDo:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.task_list = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.task_list, file)

    def display_tasks(self):
        if not self.task_list:
            print("No tasks found.")
        else:
            print("Task List:")
            for index, task in enumerate(self.task_list, start=1):
                print(f"{index}. {task['desc']} {'(done)' if task['completed'] else ''}")

    def add_new_task(self, desc):
        new_task = {"desc": desc, "completed": False}
        self.task_list.append(new_task)
        self.save_tasks()
        print(f"Task '{desc}' added successfully.")

    def remove_task(self, index):
        if 1 <= index <= len(self.task_list):
            removed_task = self.task_list.pop(index - 1)
            self.save_tasks()
            print(f"Task '{removed_task['desc']}' removed successfully.")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 1 <= index <= len(self.task_list):
            self.task_list[index - 1]['completed'] = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

def start_app():
    simple_todo = SimpleToDo()

    while True:
        print("\nMenu:")
        print("1. Show tasks")
        print("2. Add new task")
        print("3. Remove task")
        print("4. Complete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            simple_todo.display_tasks()
        elif choice == '2':
            desc = input("Enter task description: ")
            simple_todo.add_new_task(desc)
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            simple_todo.remove_task(index)
        elif choice == '4':
            index = int(input("Enter task index to mark as completed: "))
            simple_todo.complete_task(index)
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    start_app()
                            