def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

num = find_gcd(a, b)
print("the gcd of", a, "and", b, "is", num)
