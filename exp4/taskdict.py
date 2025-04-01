print("Hello, this is a Task Scheduler")

tasks = {}

while True:
    print('''
        1. Add a Task
        2. Add Status
        3. Update Status
        4. View All Tasks
        5. Exit
    ''')

    ch = int(input("Enter your choice: "))

    if ch == 1:
        task_name = input("Enter the task name: ")
        if task_name in tasks:
            print("Task already exists!")
        else:
            tasks[task_name] = "Pending"
            print("Task added successfully.")

    elif ch == 2:
        task_name = input("Enter the task name: ")
        if task_name in tasks:
            status = input("Enter the status (Pending/In Progress/Completed): ")
            tasks[task_name] = status
            print("Status updated.")
        else:
            print("Task not found!")

    elif ch == 3:
        task_name = input("Enter the task name to update status: ")
        if task_name in tasks:
            new_status = input("Enter new status (Pending/In Progress/Completed): ")
            tasks[task_name] = new_status
            print("Status updated successfully.")
        else:
            print("Task not found!")

    elif ch == 4:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nAll Tasks:")
            for task, status in tasks.items():
                print(f"Task: {task} | Status: {status}")

    elif ch == 5:
        print("Exiting the Task Scheduler.")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
