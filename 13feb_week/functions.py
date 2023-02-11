print(' Python functions\n', '-' * 30, '\n')


# Functions are objects, defined with the def statement, followed by the argument list


def make_list(val, times):
    res = str(val) * times
    return res


print(make_list('hello functions ', 5))

print('\n\n\n Function parameters\n', '-' * 30, '\n')


def print_list(val, times):
    print(str(val) * times)


print_list(5, 3)  # parameters are passed by assignment(copy
print_list(0, 4)


def change_list(inlist, val, times):  # they are references, changes alter the callers variables
    inlist += str(val) * times


mylist = []
change_list(mylist, 'h', 8)
print(mylist)

print('\n\n\n Assigning default values to parameters\n', '-' * 30, '\n')


def print_vat(gross, vat_pc=17.5, message='Summary:'):
    net = gross / (1 + (vat_pc / 100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))


print_vat(9.55, message='Final sum:')

print('\n\n\n Passing parameters - review\n', '-' * 30, '\n')


def my_func(file, dire, user='root'):
    print('file: {:}, dir: {:}, to: {:} '.format(file, dire, user))


my_func('one', 'two', 'three')  # passing parameters by position
my_func('one', 'two')  # by default
my_func(file='one', dire='two', user='three')  # or by name

print('\n\n\n Enforcing named parameters  *  \n', '-' * 30, '\n')


# use a bare * to force a user to supply named arguments
# all parameters defined after (to the right) of the * must be named parameters,
# but those to the left may be positional


def print_vat(*, gross=0.0, vat_pc=17.5, message='Summary:'):
    net = gross / (1 + (vat_pc / 100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))


print_vat(vat_pc=15, gross=9.55)
print_vat()

print('\n\n\n Unpacking and variadic functions\n', '-' * 30, '\n')


def my_func(a, b, c):
    print(a, b, c)


my_tup = 23, 45, 67
my_func(*my_tup)  # unpacking passes a sequence's elements as single arguments


def my_func(dire, *files):  # variadic functions have a variable number of parameters
    print('dir:', dire, 'files:', files)


my_func('c:stuff', 'f1.txt', 'f2.txt', 'f3.txt')

print('\n\n\n Keyword parameters\n', '-' * 30, '\n')


# prefix ** to indicate a dictionary


def print_vat(**kwargs):
    print(kwargs)


print_vat(vatpc=15, gross=9.55, message='Summary')

# use ** to unpack caller's parameters from a dictionary
args_dict = dict(vatpc=15, gross=9.55, message='Summary')
print_vat(**args_dict)

print('\n\n\n Returning objects from a function\n', '-' * 30, '\n')


# if return is not used - a reference to None is returned


def calc_vat(gross, vat_pc=17.5):
    net = gross / (1 + (vat_pc / 100))
    vat = gross - net
    return [f'{net:05.2f}', f'{vat:05.2f}']


result = calc_vat(42.30)
print(calc_vat(9.55))

print('\n\n\n Variables in functions\n', '-' * 30, '\n')
# By default, variables used in a function are local
# Global variables are defined using global

result = 3


def scope_test1():
    result = 42


scope_test1()
print(result)


def scope_test2():
    global result
    result = 42


scope_test2()
print(result)
# global variables are generally frowned upon


print('\n\n\n Lambda functions\n', '-' * 30, '\n')
compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)

x = 42
y = 3

print("a > b   ", compare(x, y))

# applies on operation to each item in a list like in this example
# new_list = list(map(lambda a: a + 1, source_list))


print('\n\n\n Lambda as a sort key\n', '-' * 30, '\n')

# Lambda functions are often used as parameters to build-ins. We could have defined a function that takes one argument
# and return the key field in the correct format comparison.
