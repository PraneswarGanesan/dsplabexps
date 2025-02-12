def find_max(lst):
    maximum = lst[0]
    for a in lst:
        if a > maximum:
            maximum = a
    return maximum

num = int(input("how many numbers: "))
lst = []

for n in range(num):
    number = int(input("enter number: "))
    lst.append(number)

print("maximum element in the list is:", find_max(lst))
