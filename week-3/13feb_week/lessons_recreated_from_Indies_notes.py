# you can not just call the function you created
# you need to import
# import function_definitions

# you then call the module and the function within it
# function_definitions.say_hello()


# when you import a file, the file gets run by the interpreter
# you need ensure that the file doesn't call the function itself

# create a function that opens a file for reading
# loops through the file
# prints the file contents


# defining the function
def print_file(filename):
    file_handle = open(filename, 'r')

    for line in file_handle:
        print(line, end='')


# testing
if __name__ == '__main__':
    print_file('../../week-2/Exercise13/pelican.txt')

# calling the function you just created
import my_functions

my_functions.greet('Indie', 'Stephanie')

import simple_calculator

x = 10
y = 2

add = simple_calculator.add(x, y)
print(add)
minus = simple_calculator.subtract(x, y)
print(minus)
multiply = simple_calculator.multiply(x, y)
print(multiply)
divide = simple_calculator.divide(x, y)
print(divide)

# unpack
number = [25, 3]
# add_result = simple_calculator.add(number[1], number[0])
# rather than unpacking manually, use a * to unpack
add_result = simple_calculator.add(*number)
print(add_result)

lots_answer = simple_calculator.add_lots(1, 2, 3, 4, 5)
print(lots_answer)


def print_stuff(name, *, age, fave_col, fave_food):
    print(f'Your name is {name}')
    print(f'Your age is {age} years old')
    print(f'Your fave colour is {fave_col}')
    print(f'Your favourite food is {fave_food}')


# calling the parameters
print_stuff(name='Bart', age=8, fave_col='Yellow', fave_food='Dogs')


# add lots using *
def add_lots_w_message(*numbers, message):
    answer = 0
    for n in numbers:
        answer += n
    # make sure return is indented
    return message + ' ' + str(answer)


# calling add lots
result3 = add_lots_w_message(5, 2, 4, message='answer is:')
print(result3)


# Double **
# These are used for dictionaries.
# **
def print_stuff_keywords(**info):
    print(f'Your name is {name}')
    print(f'Your age is {age} years old')
    print(f'Your fave colour is {fave_col}')
    print(f'Your favourite food is {fave_food}')


# lambda function
compare = lambda a, b: -1 if a > b else (+1 if a > b else 0)

x = 42
y = 3

print('a>b', compare(x, y))

# lambda exercise
source_list = [3, 4, 5, 6]
new_list = list(map(lambda a: a + 1, source_list))
print(new_list)
