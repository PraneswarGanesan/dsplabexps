def sum_list(l):
    total = 0
    for i in range(len(l)):
        total += l[i]
    return total

l = []
n = int(input("enter the number of elements: "))

for i in range(n):
    x = int(input("enter the element: "))
    l.append(x)

result = sum_list(l)
print("sum of the list:", result)
