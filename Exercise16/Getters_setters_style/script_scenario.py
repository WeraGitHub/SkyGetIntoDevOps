from person import Person
from customer import Customer
from employee import Employee

weronika = Person('Weronika', 'L', 10, 1, 1991, 'f', 'address')

print(str(weronika))

weronika.walk()
weronika.walk_to('home')
print(weronika.calculate_age())

weronika_customer = Customer('Weronika', 'L', 10, 1, 1991, 'f', 'address', 2)

weronika_employee = Employee('Weronika', 'L', 10, 1, 1991, 'f', 'address', 'sky', 'DevOps', 'expert', 2, 1, 2, 2023,
                             50000, 35)

# TODO try all the methods and play with all the getters and setters
