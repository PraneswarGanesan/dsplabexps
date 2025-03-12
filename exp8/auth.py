import os

USER_FILE = "users.txt"

def signup(username, password):
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    print("Signup successful!")

def login(username, password):
    if not os.path.exists(USER_FILE):
        print("No users found.")
        return
    with open(USER_FILE, "r") as file:
        users = file.readlines()
        for user in users:
            stored_user, stored_pass = user.strip().split(",")
            if stored_user == username and stored_pass == password:
                print("Login successful!")
                return
    print("Invalid credentials.")

while True:
    print("\nUser Authentication System")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        signup(username, password)
    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        login(username, password)
    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
