import os

con_f = "e_contact.txt"

def add_contact(name, phone, email):
    with open(con_f, "a") as file:
        file.write(f"{name.strip()},{phone.strip()},{email.strip()}\n")
        print("Added successfully.")

def viewallcontact():
    if not os.path.exists(con_f):
        print("No contacts found.")
        return
    with open(con_f, "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:\n")
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")

def search_contact(name):
    if not os.path.exists(con_f):
        print("No contacts found.")
        return
    with open(con_f, "r") as file:
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

while True:
    print('''
        1. Add Contact
        2. View All Contacts
        3. Search a Contact
        4. Exit
    ''')
    
    c = int(input("Enter your choice: "))
    
    if c == 1:
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        email = input("Enter the email: ")
        add_contact(name, phone, email)

    elif c == 2:
        viewallcontact()
    
    elif c == 3:
        name = input("Enter the name you want to find: ")
        search_contact(name)
    
    elif c == 4:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice! Choose again.")
