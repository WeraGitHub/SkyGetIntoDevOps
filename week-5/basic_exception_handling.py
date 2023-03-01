# basic structure

try:
    # this is where our desired code goes
    print('This is the TRY block')
    # file_object = open('foo', 'x')
    x = 10 / 0
except FileNotFoundError as ex:
    # this will catch the specific exception
    print('This file cannot be found', ex.filename)
    print('This is the EXCEPT block')
    # in other languages this is a CATCH block

# we can have multiple except blocks
except FileExistsError as ex:
    print('This file already exists', ex.filename)
    print('This is another EXCEPT block')

except Exception as ex:
    print('This will catch anything else')
    print(type(ex))

finally:
    print('This is the FINALLY block. It will always run')
    print("It's used for tidying up\n")


# ########################################################################

def my_func(*arguments):
    if not all(arguments):
        raise ValueError('False argument in my_func')


try:
    my_func('Tom', '', 42)
except ValueError as err:
    print('Oops:', err, '\n')


class MyError(Exception):
    pass


def my_func(*arguments):
    if not all(arguments):
        raise MyError('False argument in my_func')


try:
    my_func('Tom', '', 42)
except MyError as err:
    print('Oops:', err)
