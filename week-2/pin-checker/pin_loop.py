# create variable correct_pin and assign it a value
correct_pin = '1234'
# for loop that will run 3 times ( iteration will start with i = 0 )
for i in range(3):
    # ask user for the PIN and save it into supplied_pin variable
    supplied_pin = input('Please enter your PIN: ')
    # if it's correct, let them know
    if supplied_pin == correct_pin:
        print('Correct!')  # print the message letting them know they got it right
        break  # get out of the loop using break keyword
    # if they haven't got it right but tried only one or twice, let them know
    elif i < 2:
        print('Wrong PIN', i + 1, 'number of times, try again: ')
    # otherwise: if they have it wrong, and it's their third try, print goodbye message
    else:
        print('Wrong 3 times. Goodbye')
