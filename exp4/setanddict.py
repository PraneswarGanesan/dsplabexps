# ============================
#  SET OPERATIONS
# ============================

print("\n🔷 SET OPERATIONS 🔷")

# Creating a set with loop input
n = int(input("Enter number of elements for the set: "))  # Example input: 3
my_set = set()

for i in range(n):
    value = input(f"Enter element {i+1}: ")  # Example inputs: "apple", "banana", "cherry"
    my_set.add(value)

print("Set:", my_set)  # Output: Set: {'apple', 'banana', 'cherry'}

# Accessing elements using loop
print("\nAccessing Set Elements:")
for item in my_set:
    print(item)
# Output:
# apple
# banana
# cherry

# Adding elements to a set
for i in range(2):
    value = input("Enter element to add: ")  # Example inputs: "orange", "grape"
    my_set.add(value)
print("Updated Set:", my_set)  # Output: Set: {'apple', 'banana', 'cherry', 'orange', 'grape'}

# Removing elements from a set
for i in range(2):
    value = input("Enter element to remove: ")  # Example inputs: "banana", "grape"
    if value in my_set:
        my_set.remove(value)
    else:
        print(f"{value} not found in set.")
print("Updated Set:", my_set)  # Output: {'apple', 'cherry', 'orange'}

# Set Operations (Union, Intersection, Difference)
set2 = set(input("Enter elements for another set (comma-separated): ").split(","))  # Example input: "apple,grape"

print("Union:", my_set.union(set2))  # Output: {'apple', 'cherry', 'orange', 'grape'}
print("Intersection:", my_set.intersection(set2))  # Output: {'apple'}
print("Difference:", my_set.difference(set2))  # Output: {'cherry', 'orange'}

# Checking Membership in Set
search_value = input("Enter a value to check in set: ")  # Example input: "cherry"
if search_value in my_set:
    print(search_value, "is present in set.")  # Output: cherry is present in set.
else:
    print(search_value, "is not present in set.")

# ============================
#  DICTIONARY OPERATIONS
# ============================

print("\n🔷 DICTIONARY OPERATIONS 🔷")

# Creating a dictionary with loop input
n = int(input("Enter number of key-value pairs: "))  # Example input: 3
my_dict = {}

for i in range(n):
    key = input(f"Enter key {i+1}: ")  # Example inputs: "name", "age", "city"
    value = input(f"Enter value for {key}: ")  # Example inputs: "Alice", "25", "New York"
    my_dict[key] = value

print("Dictionary:", my_dict)  
# Output: {'name': 'Alice', 'age': '25', 'city': 'New York'}

# Accessing dictionary keys and values
print("\nAccessing Dictionary:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")
# Output:
# name: Alice
# age: 25
# city: New York

# Adding new key-value pairs
new_key = input("Enter a new key to add: ")  # Example input: "country"
new_value = input("Enter value for new key: ")  # Example input: "USA"
my_dict[new_key] = new_value

print("Updated Dictionary:", my_dict)  
# Output: {'name': 'Alice', 'age': '25', 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair
remove_key = input("Enter a key to remove: ")  # Example input: "age"
if remove_key in my_dict:
    del my_dict[remove_key]
    print(f"Removed key '{remove_key}'.")
else:
    print(f"Key '{remove_key}' not found.")

print("Updated Dictionary:", my_dict)  
# Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

# Checking if a key exists
search_key = input("Enter a key to search: ")  # Example input: "city"
if search_key in my_dict:
    print(f"{search_key} exists with value: {my_dict[search_key]}")
else:
    print(f"{search_key} does not exist.")

# Dictionary Keys and Values
print("\nDictionary Keys:", list(my_dict.keys()))  
# Output: ['name', 'city', 'country']

print("Dictionary Values:", list(my_dict.values()))  
# Output: ['Alice', 'New York', 'USA']

# Merging two dictionaries
extra_dict = {"gender": "Female", "email": "alice@example.com"}
my_dict.update(extra_dict)
print("Merged Dictionary:", my_dict)  
# Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA', 'gender': 'Female', 'email': 'alice@example.com'}

# Converting dictionary to list of tuples
tuple_list = list(my_dict.items())
print("Dictionary as List of Tuples:", tuple_list)  
# Output: [('name', 'Alice'), ('city', 'New York'), ('country', 'USA'), ('gender', 'Female'), ('email', 'alice@example.com')]

print("\n🔷 END OF PROGRAM 🔷")
