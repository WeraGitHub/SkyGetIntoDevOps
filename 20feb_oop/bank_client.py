from account import Account
# from the module import the Class

# bring it to life
# create an object instance from the class
# instantiation
lisa_account = Account(250)  # calling a constructor - a special method to ensure our object is ready to be used
bart_account = Account(20)


# objects dot attributes (data)
# object dot methods (behaviour, aka functions)
lisa_balance = lisa_account.get_balance()
bart_balance = bart_account.get_balance()

print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}.')

lisa_account._balance = 1000
print(lisa_account._balance)

lisa_balance = lisa_account.get_balance()
print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}.')

lisa_account.deposit(50)

lisa_balance = lisa_account.get_balance()
print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}.')

lisa_account.withdraw(50)
bart_account.withdraw(-50)
lisa_balance = lisa_account.get_balance()
bart_balance = bart_account.get_balance()
print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}.')
