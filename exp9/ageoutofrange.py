class AgeOutOfRangeError(Exception):
    pass

def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            raise AgeOutOfRangeError("Age must be between 0 and 120")

        return age
    except ValueError:
        print("Invalid input. Enter a valid integer.")
    except AgeOutOfRangeError as e:
        print(f"Error: {e}")
    return None

age = get_age()
print("Registration done!!")
