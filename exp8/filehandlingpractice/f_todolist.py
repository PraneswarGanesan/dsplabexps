import os

todo_file = "todolist.txt"

def add_task(task):
    with open(todo_file, "a") as file:
        file.write(f"{task.strip()},Pending\n")
        print("Task added successfully.")

def view_tasks():
    if not os.path.exists(todo_file):
        print("No tasks found.")
        return
    with open(todo_file, "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nTo-Do List:\n")
            for i, task in enumerate(tasks, 1):
                task_details = task.strip().split(",")
                print(f"{i}. Task: {task_details[0]}, Status: {task_details[1]}")

def remove_task(task_number):
    if not os.path.exists(todo_file):
        print("No tasks found.")
        return
    with open(todo_file, "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        with open(todo_file, "w") as file:
            file.writelines(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

def update_status(task_number, new_status):
    if not os.path.exists(todo_file):
        print("No tasks found.")
        return
    with open(todo_file, "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        task_details = tasks[task_number - 1].strip().split(",")
        task_details[1] = new_status
        tasks[task_number - 1] = ",".join(task_details) + "\n"
        with open(todo_file, "w") as file:
            file.writelines(tasks)
        print("Task status updated successfully.")
    else:
        print("Invalid task number.")

while True:
    print('''
        1. Add Task
        2. View Tasks
        3. Remove Task
        4. Update Task Status
        5. Exit
    ''')
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        task = input("Enter the task: ")
        add_task(task)

    elif ch == 2:
        view_tasks()
    
    elif ch == 3:
        view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)

    elif ch == 4:
        view_tasks()
        task_number = int(input("Enter the task number to update: "))
        new_status = input("Enter new status (Pending/Completed): ")
        update_status(task_number, new_status)

    elif ch == 5:
        print("Exiting the To-Do List App.")
        break
    
    else:
        print("Invalid choice! Choose again.")
