import os

CONTACTS_FILE = "contacts.txt"


def add_contact(name, phone, email):
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!")


def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found.")
        return
    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts List:")
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")


def search_contact(name):
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found.")
        return
    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()
        found = False
        for contact in contacts:
            contact_name, phone, email = contact.strip().split(",")
            if contact_name.lower() == name.lower():
                print(f"\nContact Found:\nName: {contact_name}, Phone: {phone}, Email: {email}")
                found = True
                break
        if not found:
            print("Contact not found.")

# Main menu
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter Name to Search: ")
        search_contact(name)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
