#!/usr/bin/python

# Example Python script

# import package called sys
import sys

# variable holding the length of the sys.argv
argument_count = len(sys.argv)

# if else statement checking if argc is greater than one
if argument_count > 1:
    # if it is True, run the next line
    print('Too many args')
else:
    # otherwise execute the below
    where = 'World'
    print("Hello", where)

# print concatenation of string and the first item of sys.argv[0]
print('Goodbye from ' + sys.argv[0])

print('Goodbye from ' + sys.argv[1])
