import os

TODO_FILE = "todo_list.txt"

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(f"{task},pending\n")
    print("Task added successfully!")


def view_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(tasks, start=1):
                task_name, status = task.strip().split(",")
                print(f"{index}. {task_name} [{status}]")


def complete_task(task_number):
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_number <= len(tasks):
        task_name, _ = tasks[task_number - 1].strip().split(",")
        tasks[task_number - 1] = f"{task_name},completed\n"
        
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)
        
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task(task_number):
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)
        
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")


while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter Task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_num = int(input("Enter Task Number to Mark as Completed: "))
        complete_task(task_num)
    elif choice == "4":
        view_tasks()
        task_num = int(input("Enter Task Number to Delete: "))
        delete_task(task_num)
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
