import copy

original_list = [1, 2, [3, 4], 5]
shallow_copy = copy.copy(original_list)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
