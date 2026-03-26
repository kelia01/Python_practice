# Create a BankAccount class that has:

# Attributes: owner, balance (starts at 0)
# Method: deposit(amount) adds money to balance
# Method: withdraw(amount) subtracts money if enough balance (print error if not)
# Method: check_balance() prints current balance
#Create an account, deposit money, withdraw money, and check balance.

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            print("U entered invalid amount")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        print("Error: Your balance is less than the amount")

    def check_balance(self):
        print(f"ur balance: {self.balance}")

kel = BankAccount("Kelia")
kel.deposit(3000)
kel.check_balance()
