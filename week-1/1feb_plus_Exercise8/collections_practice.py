# list is a collection
# tuple is a collection
# dictionary is  a collection
# set is a collection


person0_name = 'Victoria'
person1_name = 'Asha'
person2_name = 'Anum'
person3_name = 'Deanne'

# tuple
names_tuple = ('Victoria', 'Aisha', 'Anum', 'Deanne')
names_tuple_type = type(names_tuple)
print(names_tuple_type)

print(names_tuple)
print(names_tuple[2])

# not allowed because tuples are immutable
# they can not be changed
# names_tuple[0] = 'Dominique'


# list
# lists are mutable
names_list = ['Victoria', 'Aisha', 'Anum', 'Deanne']
names_list_type = type(names_list)
print(names_list_type)
print(names_list)
names_list[0] = 'Dominique'
print(names_list)

print(names_list[-1])
print(names_list[-2])
print(names_list[2])
