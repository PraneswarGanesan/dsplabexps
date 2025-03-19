# ============================
#  LIST AND TUPLE OPERATIONS
# ============================

print("\n🔷 LIST OPERATIONS 🔷")

# 1️⃣ Creating a list with loop input
print("\n1️⃣ Creating a List with User Input")
n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    my_list.append(value)

print("List:", my_list)

# 2️⃣ Accessing elements using loop
print("\n2️⃣ Accessing List Elements")
for i in range(len(my_list)):
    print(f"Element {i}: {my_list[i]}")

# 3️⃣ List Slicing
print("\n3️⃣ List Slicing")
print("First 3 elements:", my_list[:3])
print("Last 3 elements:", my_list[-3:])
print("Reversed list:", my_list[::-1])

# 4️⃣ Adding elements using loops
print("\n4️⃣ Adding Elements")
for i in range(2):
    value = int(input("Enter element to append: "))
    my_list.append(value)
print("Updated List:", my_list)

# 5️⃣ Removing elements using loops
print("\n5️⃣ Removing Elements")
for i in range(2):
    value = int(input("Enter element to remove: "))
    if value in my_list:
        my_list.remove(value)
print("Updated List:", my_list)

# 6️⃣ Sorting a list
print("\n6️⃣ Sorting the List")
my_list.sort()
print("Sorted List:", my_list)

# 7️⃣ Reversing a list
print("\n7️⃣ Reversed List")
my_list.reverse()
print("Reversed List:", my_list)

# 8️⃣ List Comprehension (Generating Squares)
print("\n8️⃣ List Comprehension (Generating Squares)")
squares = [x ** 2 for x in my_list]
print("Squares:", squares)

# 9️⃣ Copying a list using loop
print("\n9️⃣ Copying a List")
copy_list = []
for i in my_list:
    copy_list.append(i)
print("Copied List:", copy_list)

# 🔷 TUPLE OPERATIONS 🔷
print("\n🔷 TUPLE OPERATIONS 🔷")

# 1️⃣ Creating a tuple from user input
print("\n1️⃣ Creating a Tuple from User Input")
n = int(input("Enter number of elements for tuple: "))
tuple_values = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    tuple_values.append(value)

my_tuple = tuple(tuple_values)
print("Tuple:", my_tuple)

# 2️⃣ Accessing tuple elements using a loop
print("\n2️⃣ Accessing Tuple Elements")
for i in range(len(my_tuple)):
    print(f"Element {i}: {my_tuple[i]}")

# 3️⃣ Tuple slicing
print("\n3️⃣ Tuple Slicing")
print("First 3 elements:", my_tuple[:3])
print("Last 3 elements:", my_tuple[-3:])
print("Reversed tuple:", my_tuple[::-1])

# 4️⃣ Tuple Concatenation
print("\n4️⃣ Concatenating Tuples")
extra_tuple = (100, 200)
new_tuple = my_tuple + extra_tuple
print("Concatenated Tuple:", new_tuple)

# 5️⃣ Checking Membership in Tuple using loop
print("\n5️⃣ Checking Membership in Tuple")
search_value = int(input("Enter a value to search in tuple: "))
found = False
for item in my_tuple:
    if item == search_value:
        found = True
        break
if found:
    print(search_value, "is present in tuple.")
else:
    print(search_value, "is not present in tuple.")

# 6️⃣ Finding Min, Max, and Length using loop
print("\n6️⃣ Finding Min, Max, and Length in Tuple")
min_value = my_tuple[0]
max_value = my_tuple[0]
sum_value = 0

for i in my_tuple:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i
    sum_value += i

print("Minimum:", min_value)
print("Maximum:", max_value)
print("Sum:", sum_value)
print("Length:", len(my_tuple))

# 7️⃣ Nested Tuples and Accessing Using Loops
print("\n7️⃣ Nested Tuple Example")
nested_tuple = (1, (2, 3), (4, 5, 6))
for item in nested_tuple:
    if isinstance(item, tuple):
        print("Nested Tuple:", item)
    else:
        print("Element:", item)

# 8️⃣ Tuple to List and Vice Versa using Loops
print("\n8️⃣ Tuple to List and Vice Versa")
tuple_to_list = []
for i in my_tuple:
    tuple_to_list.append(i)
print("Converted to List:", tuple_to_list)

list_to_tuple = tuple(tuple_to_list)
print("Converted back to Tuple:", list_to_tuple)

print("\n🔷 END OF PROGRAM 🔷")
