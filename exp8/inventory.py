import os

INVENTORY_FILE = "inventory.txt"

def add_product(name, quantity, price):
    with open(INVENTORY_FILE, "a") as file:
        file.write(f"{name},{quantity},{price}\n")
    print("Product added successfully!")

def view_inventory():
    if not os.path.exists(INVENTORY_FILE):
        print("No products found.")
        return
    with open(INVENTORY_FILE, "r") as file:
        products = file.readlines()
        if not products:
            print("No products found.")
        else:
            print("\nInventory List:")
            for index, product in enumerate(products, start=1):
                name, quantity, price = product.strip().split(",")
                print(f"{index}. {name} - {quantity} units - ${price}")

def update_product(name, new_quantity, new_price):
    if not os.path.exists(INVENTORY_FILE):
        print("No products found.")
        return
    with open(INVENTORY_FILE, "r") as file:
        products = file.readlines()
    
    updated = False
    with open(INVENTORY_FILE, "w") as file:
        for product in products:
            pname, quantity, price = product.strip().split(",")
            if pname.lower() == name.lower():
                file.write(f"{pname},{new_quantity},{new_price}\n")
                updated = True
            else:
                file.write(product)
    
    print("Product updated successfully!" if updated else "Product not found.")

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Product")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter Product Name: ")
        quantity = input("Enter Quantity: ")
        price = input("Enter Price: ")
        add_product(name, quantity, price)
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        name = input("Enter Product Name to Update: ")
        new_quantity = input("Enter New Quantity: ")
        new_price = input("Enter New Price: ")
        update_product(name, new_quantity, new_price)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
