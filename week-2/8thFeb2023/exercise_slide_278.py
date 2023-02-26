# this is the exercise we did together during the lesson

# recap:
# my dict is a dictionary with keys as strings (countries in this case) and
# values as strings as well (capital cities)
mydict = {'Australia': 'Canberra', 'Eire': 'Dublin', 'France': 'Paris', 'Finland': 'Helsinki', 'UK': 'London',
          'US': 'Washington'}
# the below will look for a key string 'UK' in mydict and print the value - the capital of UK
print(mydict['UK'])

country = 'Iceland'  # we're creating a new string variable ad assign a string 'Iceland' to it
# now we will add a key-value pair to our dictionary the key is 'Iceland' (held in variable country)
# and the key is a string 'Reykjavik'
mydict[country] = 'Reykjavik'

# when we print the whole dictionary, now we can see Iceland in there as well
print(mydict)


print('\n\nThe exercise we meant to do: ')
# and this is what we supposed to do:
# here we have a dictionary where keys are stings (countries) and the values are lists of strings (cities)
my_dict = {'UK': ['London', 'Wigan', 'Macclesfield', 'Bolton'],
           'US': ['Miami', 'Springfield', 'New York', 'Boston']}

# if we print the dictionary value for the key 'UK' we will get the list of cities
print(my_dict['UK'])
# to print a specific city we can use [index number] because our value is a list!
print(my_dict['UK'][0])
print(my_dict['UK'][2])

homer = 1  # we are assigning integer 1 to a variable named homer
# now we will use homer variable instead of typying 1 manually
print(my_dict['US'][homer])  # this is the same as print(my_dict['US'][1])

# the below will add a new key-value pair to our dictionary, where key is string 'FR' and the value is a list of strings
my_dict['FR'] = ['Paris', 'Lyon', 'Bordeaux', 'Touloiuse']

# and lastly, we are using for loop to iterate (go through) the keys of our recent dictionary
for country in my_dict.keys():
    # for each item (country) it will print the country key(country) and the value (my_dict[country]),
    # which in this case is a list of cities
    print(country, ': ', my_dict[country])
