names = ['Iman', 'Saynab', 'Indie']
print(names)

# for item_placeholder in some_collection:
#     code goes here

for name in names:
    print('I am in the loop')
    print('Hello', name)

for number, name in enumerate(names, 99):
    # print('I am in the loop')
    print('Hello number', number, name)

print('The end')


