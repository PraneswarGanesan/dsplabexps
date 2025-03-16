def voteragecal():
    try:
        age = int(input("Enter the age of the voter: "))
        if age>= 18:
            print("Yes he/she is eligible to vote. ")
        else: 
            print("No he/she is not eligible to vote. ")
    except ValueError:
        print("Error: Please enter correct age")

voteragecal()
