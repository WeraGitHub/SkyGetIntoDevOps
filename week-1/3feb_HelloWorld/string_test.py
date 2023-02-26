text = 'hello world ?'

print(text.count('e'))  # count how many letters e is in the string

if text.startswith('hell'):  # if the string begins with the argument given('hell') it returns true
    print("It's hell in there")
else:  # otherwise, run this code
    print("It's heaven in here :)")

if text.isalpha():  # if the string is an alphabetic string it returns true
    print('string is all alpha')
else:  # otherwise, run this code
    print('string is not purely alpha')

text = ' \t\r\n'  # \t  tab      \r  carriage return      \n  new line
if text.isspace():  # if the string is a whitespace string it returns true
    print('string is whitespace')
else:  # otherwise, run this code
    print('string is not whitespace')
