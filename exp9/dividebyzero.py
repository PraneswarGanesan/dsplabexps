try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    q = a/(b-c)
    print("the quotient is: ", q)
except ZeroDivisionError:
    print("Division by zero error occured")
except ValueError: 
    print("please enter a valid integer")
