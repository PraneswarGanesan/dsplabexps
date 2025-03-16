def dividenumber():
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        q = a/(b-c)
        print (f"the quotient is : {q}")
    except ZeroDivisionError:
        print("error: division by zero occured")
    except ValueError:
        print("Error: please enter a correct number")
    except Exception as e:
        print(f"unexcepted error {e} occured")


dividenumber()