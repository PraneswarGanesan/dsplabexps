# ============================
#  LIST AND TUPLE OPERATIONS
# ============================

# ======== LIST OPERATIONS =========
print("\n1️⃣ Creating and Accessing Lists")
# Creating a list
my_list = [10, 20, 30, 40, 50]
print(my_list)  

# Accessing elements
print(my_list[0])  
print(my_list[-1])  

# Output:
# [10, 20, 30, 40, 50]
# 10
# 50


print("\n2️⃣ List Slicing")
# List slicing
print(my_list[1:4])  
print(my_list[:3])  
print(my_list[2:])  
print(my_list[::-1])  

# Output:
# [20, 30, 40]
# [10, 20, 30]
# [30, 40, 50]
# [50, 40, 30, 20, 10]


print("\n3️⃣ Adding Elements to a List")
# Using append()
my_list.append(60)  
print(my_list)  

# Using insert()
my_list.insert(2, 25)  
print(my_list)  

# Using extend()
my_list.extend([70, 80])  
print(my_list)  

# Output:
# [10, 20, 30, 40, 50, 60]
# [10, 20, 25, 30, 40, 50, 60]
# [10, 20, 25, 30, 40, 50, 60, 70, 80]


print("\n4️⃣ Removing Elements from a List")
# Using remove()
my_list.remove(25)  
print(my_list)  

# Using pop()
popped_value = my_list.pop()  
print(my_list, "| Popped:", popped_value)  

# Using del
del my_list[1]  
print(my_list)  

# Output:
# [10, 20, 30, 40, 50, 60, 70, 80]
# [10, 20, 30, 40, 50, 60, 70] | Popped: 80
# [10, 30, 40, 50, 60, 70]


print("\n5️⃣ Sorting and Reversing a List")
numbers = [4, 1, 8, 3, 6]
numbers.sort()  
print(numbers)  

numbers.sort(reverse=True)  
print(numbers)  

numbers.reverse()  
print(numbers)  

# Output:
# [1, 3, 4, 6, 8]
# [8, 6, 4, 3, 1]
# [1, 3, 4, 6, 8]


print("\n6️⃣ List Comprehensions")
squares = [x**2 for x in range(1, 6)]  
print(squares)  

even_numbers = [x for x in range(1, 11) if x % 2 == 0]  
print(even_numbers)  

# Output:
# [1, 4, 9, 16, 25]
# [2, 4, 6, 8, 10]


print("\n7️⃣ Converting List to String and Vice Versa")
word_list = ["Python", "is", "awesome"]
sentence = " ".join(word_list)  
print(sentence)  

new_list = sentence.split(" ")  
print(new_list)  

# Output:
# Python is awesome
# ['Python', 'is', 'awesome']


print("\n8️⃣ Copying a List")
list1 = [1, 2, 3]
list2 = list1.copy()  
print(list2)  

# Output:
# [1, 2, 3]


print("\n9️⃣ Finding Min, Max, Sum, and Length")
num_list = [10, 20, 5, 40, 15]
print(min(num_list))  
print(max(num_list))  
print(sum(num_list))  
print(len(num_list))  

# Output:
# 5
# 40
# 90
# 5


# ======== TUPLE OPERATIONS =========
print("\n🔷 TUPLE OPERATIONS 🔷")

print("\n1️⃣ Creating and Accessing Tuples")
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  

print(my_tuple[0])  
print(my_tuple[-1])  

# Output:
# (1, 2, 3, 4, 5)
# 1
# 5


print("\n2️⃣ Tuple Slicing")
print(my_tuple[1:4])  
print(my_tuple[:3])  
print(my_tuple[2:])  
print(my_tuple[::-1])  

# Output:
# (2, 3, 4)
# (1, 2, 3)
# (3, 4, 5)
# (5, 4, 3, 2, 1)


print("\n3️⃣ Tuple Concatenation & Repetition")
tuple1 = (10, 20)
tuple2 = (30, 40)
new_tuple = tuple1 + tuple2  
print(new_tuple)  

repeat_tuple = tuple1 * 3  
print(repeat_tuple)  

# Output:
# (10, 20, 30, 40)
# (10, 20, 10, 20, 10, 20)


print("\n4️⃣ Tuple Unpacking")
a, b, c, d, e = my_tuple  
print(a, b, c, d, e)  

# Output:
# 1 2 3 4 5


print("\n5️⃣ Tuple to List and Vice Versa")
tuple_to_list = list(my_tuple)  
print(tuple_to_list)  

list_to_tuple = tuple(tuple_to_list)  
print(list_to_tuple)  

# Output:
# [1, 2, 3, 4, 5]
# (1, 2, 3, 4, 5)


print("\n6️⃣ Finding Min, Max, and Length in Tuples")
num_tuple = (5, 10, 15, 20)
print(min(num_tuple))  
print(max(num_tuple))  
print(len(num_tuple))  

# Output:
# 5
# 20
# 4


print("\n7️⃣ Checking Membership in Tuples")
print(10 in num_tuple)  
print(50 in num_tuple)  

# Output:
# True
# False


print("\n8️⃣ Nested Tuples")
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])  
print(nested_tuple[2][1])  

# Output:
# (2, 3)
# 5


print("\n9️⃣ Tuple Iteration")
for item in my_tuple:
    print(item, end=" ")  

# Output:
# 1 2 3 4 5


print("\n\n🔷 END OF PROGRAM 🔷")
