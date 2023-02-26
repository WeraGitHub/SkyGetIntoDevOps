# create a blueprint (a class) for a bank account

class Account:
    number_of_accounts = 0

    def __init__(self, opening_amount):
        self._balance = opening_amount
        Account.number_of_accounts += 1

    # ########### DATA #############
    # getter
    def get_balance(self):
        return self._balance

    # getter
    def get_firstname(self):
        return self._firstname

    # setter
    def set_firstname(self, firstname):
        self._firstname = firstname

    # properties style
    # getter
    @property
    def lastname(self):
        return self._lastname

    # setter
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    # ####### Functionality ######
    # behaviour / functionality
    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        if amount >= 0:
            self._balance -= amount
        return

    # overloading of __str__ special method
    def __str__(self):
        return "Bank account has a balance of £" + str(self._balance)
