import math

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def isNumber(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def deposit(self, amount=0):
        if Account.isNumber(amount) and amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Unallowed amount.")

    def withdraw(self, amount=0):
        if Account.isNumber(amount) and amount > 0:
            if amount > self.balance:
                print("Too large amount.")
                print(f"Your balance is {self.balance} and you tried to withdraw {amount}")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}")
                print(f"New balance is {self.balance}")
        else:
            print("Unallowed amount")

c1 = Account("Tobias", 500)
print(c1)
c1.deposit(300)
c1.withdraw(1000)
c1.withdraw(450)
