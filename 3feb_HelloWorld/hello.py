# this is a comment

# PEP 8 - python enhancement proposal - style guide, how to format our code

print("hello")
print('hello everyone       !')

# there are three types of streams, standard output, standard input and standard error stream
# variable is a box in memory
house_number = 84
print(type(house_number))
print(house_number)
print('Your house number is', house_number)
print('Your house number is' + str(house_number))
print('one', 'two', 'three')
print('one' + ' ' + 'two ' + 'three')

answer = 1 + 2
print('Type of answer', type(answer))
print(answer)
answer = answer + 10
answer += 10
print(answer)
# python is a dynamic language, more specifically: python is dynamically-typed language
favourite_colour = 'purple'
print('Type of my favourite_color is', type(favourite_colour))

like_broccoli = True
print(like_broccoli, "is a type of: ", type(like_broccoli))

fraction = 0.75
print(fraction, "type of", type(fraction))
