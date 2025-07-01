from services import TaskManager
from utils import save_tasks_to_file, load_tasks_from_file

def main():
    manager = TaskManager()
    filename = "tasks.json"

    # Load tasks from file
    manager.tasks = load_tasks_from_file(filename)

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = manager.add_task(title, description)
            print("Task added:", task)

        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to skip): ") or None
            description = input("Enter new description (leave blank to skip): ") or None
            completed = input("Mark as completed? (yes/no/leave blank to skip): ")
            completed = True if completed.lower() == "yes" else False if completed.lower() == "no" else None
            task = manager.update_task(task_id, title, description, completed)
            if task:
                print("Task updated:", task)
            else:
                print("Task not found.")

        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            task = manager.delete_task(task_id)
            if task:
                print("Task deleted:", task)
            else:
                print("Task not found.")

        elif choice == "4":
            tasks = manager.list_tasks()
            print("\nTasks:")
            for task in tasks:
                print(task)

        elif choice == "5":
            save_tasks_to_file(manager.tasks, filename)
            print("Tasks saved. Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()