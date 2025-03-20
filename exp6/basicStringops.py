# ============================
#  STRING OPERATIONS
# ============================

print("\n🔷 STRING OPERATIONS 🔷")

# Taking string input
user_string = input("Enter a string: ")  # Example input: "Hello World"

# 1️⃣ String Length
print("\n1️⃣ String Length:")
print("Length of the string:", len(user_string))  # Output: 11

# 2️⃣ Accessing Characters
print("\n2️⃣ Accessing Characters:")
for i in range(len(user_string)):
    print(f"Character at index {i}: {user_string[i]}")
# Output:
# Character at index 0: H
# Character at index 1: e
# ...

# 3️⃣ String Slicing
print("\n3️⃣ String Slicing:")
print("First 5 characters:", user_string[:5])  # Output: Hello
print("Last 5 characters:", user_string[-5:])  # Output: World

# 4️⃣ String Reversal
print("\n4️⃣ Reversing String:")
print("Reversed String:", user_string[::-1])  # Output: dlroW olleH

# 5️⃣ Converting Case
print("\n5️⃣ Case Conversion:")
print("Uppercase:", user_string.upper())  # Output: HELLO WORLD
print("Lowercase:", user_string.lower())  # Output: hello world
print("Title Case:", user_string.title())  # Output: Hello World
print("Swap Case:", user_string.swapcase())  # Output: hELLO wORLD

# 6️⃣ Checking Substring Presence
print("\n6️⃣ Checking Substring Presence:")
sub_string = input("Enter a substring to check: ")  # Example input: "Hello"
if sub_string in user_string:
    print(f"'{sub_string}' is present in the string.")
else:
    print(f"'{sub_string}' is not present.")

# 7️⃣ String Replacement
print("\n7️⃣ String Replacement:")
old_word = input("Enter word to replace: ")  # Example input: "World"
new_word = input("Enter new word: ")  # Example input: "Python"
print("Updated String:", user_string.replace(old_word, new_word))
# Output: Hello Python

# 8️⃣ String Splitting
print("\n8️⃣ Splitting String:")
split_words = user_string.split()  # Default split by space
print("Words:", split_words)
# Output: ['Hello', 'World']

# 9️⃣ String Joining
print("\n9️⃣ Joining Strings:")
joined_string = "-".join(split_words)
print("Joined with '-':", joined_string)  # Output: Hello-World

# 🔟 Counting Characters
print("\n🔟 Counting Occurrences:")
char_to_count = input("Enter a character to count: ")  # Example input: "o"
print(f"Occurrences of '{char_to_count}':", user_string.count(char_to_count))

# 1️⃣1️⃣ Removing Spaces
print("\n1️⃣1️⃣ Removing Spaces:")
print("Without Leading & Trailing Spaces:", user_string.strip())
print("Without Leading Spaces:", user_string.lstrip())
print("Without Trailing Spaces:", user_string.rstrip())

# 1️⃣2️⃣ Checking Start and End of String
print("\n1️⃣2️⃣ Checking Start and End:")
start_check = input("Enter starting word to check: ")  # Example: "Hello"
print("Starts with", start_check, "?", user_string.startswith(start_check))

end_check = input("Enter ending word to check: ")  # Example: "World"
print("Ends with", end_check, "?", user_string.endswith(end_check))

# 1️⃣3️⃣ Checking if String is Numeric or Alphabetic
print("\n1️⃣3️⃣ Checking String Type:")
print("Is Alphabetic?", user_string.isalpha())  # False (due to spaces)
print("Is Numeric?", user_string.isnumeric())  # False
print("Is Alphanumeric?", user_string.isalnum())  # False (due to spaces)

print("\n🔷 END OF STRING OPERATIONS 🔷")
