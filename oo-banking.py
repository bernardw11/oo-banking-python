
# 1. Build a new class called `BankAccount`...
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 1000
        self.status = "open"
        self.debt = 0
        self.interest_rate = 2
        self.credit_cards = 1
    
    def deposit(self, quantity):
        self.balance += quantity
    
    def check_balance(self):
        print(f"You, {self.name}, have a balance of: ${self.balance}")

    def is_valid(self):
        if self.status == "open":
            return True
        else:
            return False
    
    def close_account(self):
        self.status = "closed"

#  ... and instantiate a new account for a user named "Kiran".
kiran_account = BankAccount("Kiran")
# i. Confirm that Kiran's new account is of the type `BankAccount`.
print(type(kiran_account))
# ii. Confirm that the name on Kiran's account is "Kiran".
print(kiran_account.name)
# iii. Confirm that Kiran's account has a balance of $1000.
print(kiran_account.balance)
# iv. Confirm that Kiran's account is `open`.
print(kiran_account.status)
# v. Set Kiran's balance to $2000. Confirm his new account balance.
kiran_account.balance = 2000
print(kiran_account.balance)
# Now you're on your own to write tests for the rest...


kiran_account.deposit(500)
kiran_account.check_balance()
kiran_account.balance = 1000


new_account = BankAccount("Bob")
new_account.balance = 0
new_account.status = "zero"
print(new_account.is_valid())
new_account.balance = 1000000
new_account.status = "closed"
print(new_account.is_valid())



amanda_account = BankAccount("Amanda")

class Transfer:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.status = "pending" # status: pending, complete, rejected, reversed
    
    def both_valid(self):
        return self.sender.is_valid() and self.recipient.is_valid()

    def execute_transaction(self):
        if self.amount < self.sender.balance:
            self.sender.balance -= self.amount
            self.recipient.balance += self.amount
            print(f"{self.sender.name} has transferred ${self.amount} to {self.recipient.name}!!!")
            self.status = "complete"
        else:
            self.status = "rejected"

new_transfer = Transfer(amanda_account, kiran_account, 50)
print(new_transfer.sender.name)
print(new_transfer.recipient.name)
print(new_transfer.amount)

new_transfer.execute_transaction()
new_transfer.sender.check_balance()
new_transfer.recipient.check_balance()