# create a blueprint (a class) for a bank account

class Account:
    numCreated = 0

    def __init__(self, opening_amount):
        self._balance = opening_amount
        Account.numCreated += 1

    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        if amount >= 0:
            self._balance -= amount
        return

    def get_balance(self):
        return self._balance
