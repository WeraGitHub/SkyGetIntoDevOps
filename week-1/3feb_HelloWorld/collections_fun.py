# dictionaries
# key-value pairs

students_dictionary = {1: 'Rachel', 2: 'Rafaella', 3: 'Weronika'}
print(students_dictionary)
print(type(students_dictionary))

print(students_dictionary[1])

students_dictionary = {'one': 'Rachel', 'two': 'Rafaella', 'three': 'Weronika'}
print(students_dictionary)
print(type(students_dictionary))

print(students_dictionary['three'])

# sets are unique and are NOT sequences
favourite_colour = {'green', 'blue', 'black', 'yellow', 'green'}
favourite_colour.add('purple')
# favourite_colour.pop()
print(favourite_colour)
print(type(favourite_colour))


address = '736 Springfield Avenue'
print(address)
address += '8'
print(address)
