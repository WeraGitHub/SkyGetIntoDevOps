# Enumeration and it's benefits :)


#############################################
print('Example number one - using list')
names_list = ['Deanne', 'Weronika', 'Rafaella', 'Winston']

index = 0  # create a new variable called index and assign value of 0
for name in names_list:  # create a for loop to iterate through names list
    print(index, name)
    index += 1  # increase the value of index by 1

# Let's do the same thing using enumerate
for index, name in enumerate(names_list):
    print(index, name)


#############################################
print('Example number one - using set')
names_set = {'Deanne', 'Weronika', 'Rafaella', 'Winston'}

for index, name in enumerate(names_set):
    print(index, name)
# remember: sets are inconsequential


#############################################
print('Example number one - using dictionary')
# use enumerate with dictionary
names_dictionary = {'one': 'Deanne', 'two': 'Weronika', 'three': 'Rafaella', 'four': 'Winston'}

for key, name in enumerate(names_dictionary.items()):
    print(key, name)

concatenated_names = "  ".join(names_dictionary)
print('try concatenated dictionaries')
print(concatonated_names)
