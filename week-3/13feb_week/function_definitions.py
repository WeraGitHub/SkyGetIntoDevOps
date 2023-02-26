# we use define to create our functions
# use def
# use brackets for the parameters
# use the colon at the end to start defining what the function is
def say_hello():
    print('Hello')


# call (invoke) the function to check how it works
say_hello()

# define variation on the function
# say hello to a name


def say_hello_to_name(firstname):
    print('Hello', firstname, '!')
    print('Your first name is', firstname)


# call the function to check it
say_hello_to_name('Indie')


# magic built in
print('This file FUNCTION DEFINITIONS is called', __name__)


if __name__ == '__main__':
    say_hello()
    say_hello()
    say_hello_to_name('Indie')
else:
    print('definitions is NOT the entry point')
