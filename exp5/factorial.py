def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)

num = int(input("enter a number: "))
print("the factorial of", num, "is", fact(num))


# enter a number: 5
# the factorial of 5 is 120
