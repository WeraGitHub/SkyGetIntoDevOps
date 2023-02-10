# Question 1
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
print(cheese)
prints: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']

cheese.append('Oke')
print(cheese)

cheese += ['Oke', 'Oke2']
print(cheese)


# Question 2
tup = 'Hello'  # this is a string with 5 characters
print(len(tup))

tup = 'Hello',  # this is a tuple collection containing one element
print(len(tup))
