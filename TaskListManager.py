def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def display_tasks(tasks):
    if tasks:
        print("\nCurrent Task List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nThe task list is empty.")

def remove_task(tasks):
    try:
        display_tasks(tasks)
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def update_task(tasks):
    try:
        display_tasks(tasks)
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[index] = new_task
            print(f"Task {index + 1} updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def sort_tasks(tasks):
    tasks.sort()
    print("Tasks have been sorted alphabetically.")


def main():
    tasks = []
    while True:
        print("1. Display Task \t 2. Add Task \t 3. Remove Tasks \t 4. Update Tasks \t 5. Sort Tasks \t 6. Exit \nTask List Manager : ")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            print("Exiting Task List Manager...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
main()