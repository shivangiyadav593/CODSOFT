import os

def display_menu():
    print("\n To Do List")
    print("1. Add New Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Tasks saved.")
            break
        else:
            print("Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
