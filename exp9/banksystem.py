class InsufficentError(Exception):
    pass

def withdraw(amount, balance):
    try:
        if amount > balance:
            raise InsufficentError("No funds equal to your amount in balance is not present")
        if amount <= 0:
            raise ValueError("Please enter the correct amount and it must be greater than zero")
        balance -= amount
        print(f"{amount} is withdrawn from your account")
        print(f"Current balance: {balance}")
        return balance
    except InsufficentError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    return balance

balance = 45000
balance = withdraw(-100, balance)
balance = withdraw(200000, balance)
balance = withdraw(3500, balance)
