# if statement
i_like_broccoli = False

print("The start")

if i_like_broccoli:
    print('You like broccoli')
    print('I am eating broccoli')
else:
    print('You dont like broccoli')

print('The end')


fruits = ['apple', 'banana', 'cherry']

if 'cherry' in fruits:
    print("Yummy, I like cherries")

last_fruit = fruits.pop()
print(last_fruit)

print(fruits)

if fruits:
    print("there's still fruit in the fruit bowl")

last_fruit = fruits.pop()
print(last_fruit)

print(fruits)

if fruits:
    print("there's still fruit in the fruit bowl")


last_fruit = fruits.pop()
print(last_fruit)

print(fruits)

if fruits:
    print("there's still fruit in the fruit bowl")
else:
    print("fruit bowl is empty")

word = 'hi'
if word:
    print('the string is not empty')
else:
    print('the string is empty')

if word == 'hi':
    print('Hello you')
elif word == 'bye':
    print('goodbye you')
else:
    print('are you ok?')


x = 2
y = 4

if x == y:
    print('x and y are the same')
else:
    print('x and y are different')

if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')


word = '2'
number = 3
if int(word) < number:
    print('word is less than number')
