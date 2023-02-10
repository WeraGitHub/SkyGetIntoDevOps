print("Generic built-in functions like len, min, max and sum\n")

myn = [45, 66, 12, 3, 99, 3.142, 42]
print("min:", min(myn), "max:", max(myn))
print("sum:", sum(myn))

myd = {'fred': 3, 'jim': 8, 'dave': 42}
print("min:", min(myd), "max:", max(myd))


print("\n\nUseful tuple operations\n")
a = 12
b = 2
print("a =", a, "and b =", b)
# swap values
a, b = b, a
print("a =", a, "and b =", b)

# set values from a numeric range
Gouda, Edam, Caithness = range(3)
print(Gouda, Edam, Caithness)

# repeat values
my_tuple = 'a', 'b', 'c'
another_tuple = my_tuple * 4
print(another_tuple)

thing = ('Hello')
print(type(thing))
thing = ('Hello',)
print(type(thing))


print("\n\nPython lists\n")
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese[1])
cheese[-1] = 'Red Leicester'
print(cheese)


print("\n\nTuple and list slicing\n")
my_tuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
print(my_tuple[2:4])
print(my_tuple[-4])
my_list = list(my_tuple)
print(my_list[1:])

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Brie']
del cheese[1:3]
print(cheese)


print("\n\nExtended iterable unpacking\n")
my_tuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
x, y, *z = my_tuple
print(x, y, z)

t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'
# for a, *b, c in t1, t2:
#     print(a, b, c)


print("\n\nAdding items to a list\n")

names = ['Steff', 'Anum', 'Saynab']
print(names)
names += ['Aisha', 'Rafaella']
print(names)
names.extend(['Rach', 'Indie'])
print(names)
names.append('Weronika')
print(names)
names.insert(1, 'Iman')
print(names)
names[:0] = ['Dominique', 'Deanne']  # don't do this one, it's ugly
print(names)
print(len(names))
names.insert(0, 'Angel')
print(names)


print("\n\nRemoving items by position\n")
popped_name = names.pop()
print(names)
print(popped_name)

names.pop(3)
print(names)

names.remove('Indie')
print(names)
names.insert(0, 'Steff')
names.insert(7, 'Steff')
print(names)
# names.remove('Steff')
print(names)
for name in names:
    if "Steff" == name: names.remove('Steff')

print(names)


print("\n\nSorting\n")
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.sort(key=len)
print(names)

sorted_names = sorted(names, reverse=True)
print(sorted_names)


print("\n\nMiscellaneous list methods\n")
where_is_steph = names.index('Rach')
print(where_is_steph)


print("\n\n\nSets\n")
names = {'Bob', 'Dave', 'Fred', 'Dave'}
print(names)

names_list = ['Aisha', 'Angel', 'Dominique']
names_as_set = set(names_list)
print(names_as_set)
names_as_set.add('Mariam')
names_as_set.remove('Angel')
print(names_as_set)
names_as_set.pop()
print(names_as_set)
names_as_set.discard('Weronika')
print(names_as_set)
names_as_set.add('Angel')

result = names_as_set - {'Aisha', 'Angel'}
print('result:', result)

second_set = {'Rach', 'Rafaella', 'Aisha'}
print(names_as_set.union(second_set))

print("\n\nSet operators\n")
s6 = {23, 42, 66, 123}
s7 = {123, 56, 27, 42}
print(s6 & s7)
print(s6.intersection(s7))
print(s6 | s7)
print(s6.union(s7))
print(s6 - s7)
print(s6.difference(s7))
print(s6 ^ s7)
print(s6.symmetric_difference(s7))



print("\n\n\nPython dictionaries\n")

mydict = {'Australia': 'Canberra', 'Eire': 'Dublin', 'France': 'Paris', 'Finland': 'Helsinki', 'UK': 'London', 'US': 'Washington'}
print(mydict['UK'])
country = 'Iceland'
mydict[country] = 'Reykjavik'
print(mydict)
print(mydict['Eire'])

