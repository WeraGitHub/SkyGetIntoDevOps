from account import Account
from saving_account import SavingAccount

# from the module import the Class

# bring it to life
# create an object instance from the class
# instantiation
lisa_account = Account(250)  # calling a constructor - a special method to ensure our object is ready to be used
bart_account = Account(20)


# objects dot attributes (data)
# object dot methods (behaviour, aka functions)
def get_and_display_balances():
    global lisa_balance, bart_balance
    lisa_balance = lisa_account.get_balance()
    bart_balance = bart_account.get_balance()
    print(f'Lisa has £{lisa_balance} and Bart has £{bart_balance}.')


get_and_display_balances()

lisa_account._balance = 1000
print(lisa_account._balance)

get_and_display_balances()

lisa_account.deposit(50)

get_and_display_balances()

lisa_account.withdraw(50)
bart_account.withdraw(-50)

get_and_display_balances()

if hasattr(lisa_account, '__str__'):
    print('Lisa has an __str__')
    print(lisa_account)
    print(type(lisa_account))

x = 10
y = 3

if x > y:
    print('x is larger')

# if lisa_account > bart_account:
#     print('?')

word = 'Wednesday '
print(word * 4)
print(4 * word)
print(x * y)
print(3.5 * y)

nums = [1, 2, 3, 4]
if nums:
    print("The list is NOT empty")

if bart_account:
    print("Bart's account is TRUE")

print(lisa_account)
print(bart_account)

# using Java type getters and setters for data
lisa_account.set_firstname('Lisa')
print(str(lisa_account.get_firstname()))
account_firstname = lisa_account.get_firstname()

# using .net type properties for data
lisa_account.lastname = 'Simpson'
print(lisa_account.lastname)


# instantiate some saving account objects
lisa_saving_account = SavingAccount(250, 1.5)
marge_saving_account = SavingAccount(500, 3)
marge_saving_account.set_firstname('Marge')
marge_saving_account.lastname = 'Simpson'
