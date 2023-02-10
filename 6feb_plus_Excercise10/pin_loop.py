# import getpass

correct_pin = '1234'
for i in range(3):
    supplied_pin = input('Please enter your PIN: ')  # getpass.getpass(prompt='Enter your PIN: ')
    if supplied_pin == correct_pin:
        print('Correct!')
        break
    elif i < 2:
        print('Wrong PIN', i + 1, 'number of times, try again: ')
    else:
        print('Wrong 3 times. Goodbye')
