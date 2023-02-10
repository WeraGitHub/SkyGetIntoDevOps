# euro_as_unicode = "\u20ac"
#
# print(euro_as_unicode)
#
# euro_as_symbol_name = "\N{euro sign}"
#
# print(euro_as_symbol_name)
#
# pizza = "\N{Slice of pizza}"
#
# print(pizza)
#
# # print function is variadic
# # it accepts a flexible (variable) number of arguments
# print('one', 'two', 'three')
# print('one', 'two', 'three', sep='-', end='...')
# print('one', 'two', 'three', end='\n\n\n')

# concatenation

address_parts = ['Bart Simpson', '742 Evergreen Terrace', 'Springfield', 'MA', 'USA']

address = ''

for part in address_parts:
    address += part + '\n'

print(address)
address2 = "\n".join(address_parts)

print(address2)

sentence = 'Victoria shouted "BOO" to the group'
print(sentence)

sentence = """Victoria's favourite drink is gin. 

It makes her say "YUM YUM"!"""
print(sentence)

bart = address_parts[0].upper()
print(bart)

line = "I will not punch my sister.\n"
repeated_lines = line * 20
print(repeated_lines)

