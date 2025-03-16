def studentrange(min,max):
    try:
        while (True):
            n = int(input(f"Enter the number between the range of your choice between{min} and {max}: "))
            if min <= n < max:
                print("Yes correct mark !. ATB")
                break
            else:
                print("Please enter the mark in the range")
    except ValueError:
        print("Error : Please enter a number.!")

studentrange(1,100)
