import datetime

from person import Person
from customer import Customer
from employee import Employee

weronika = Person('Weronika', 'L', datetime.date(1991, 1, 10), 'f', 'address 111')

print(str(weronika))
weronika.walk()
weronika.walk_to('home')
print('Calculate age: ', weronika.calculate_age())
print('Number of people instances', Person.get_number_of_person_instances())
print('Number of customer instances', Customer.get_number_of_customers())
print('Number of employee instances', Employee.get_number_of_employees())
print('\n')

weronika_customer = Customer('Weronika', 'L', datetime.date(1991, 1, 10), 'f', 'address', 2)
weronika_customer_2 = Customer('Weronika2', 'L2', datetime.date(1991, 1, 10), 'f', 'address', 3)

weronika_customer.walk()
print(str(weronika_customer))
print(f"{weronika_customer.firstname} is a customer: {weronika_customer.is_customer()}, is also a person: "
      f"{weronika_customer.is_person()}")
print(weronika_customer.get_customer_info())
weronika_customer.purchase("lamp")
weronika_customer.add_loyalty_points(500)
print('Loyalty points:', weronika_customer.loyalty_points)
print('Number of people instances', Person.get_number_of_person_instances())
print('Number of customer instances', Customer.get_number_of_customers())
print('Number of employee instances', Employee.get_number_of_employees())
print('\n')

weronika_employee = Employee('Weronika', 'L', datetime.date(1991, 1, 10), 'f', 'address', 'sky', 'DevOps', 'expert', 2,
                             datetime.date(2020, 5, 10), 50000, 35)

print(str(weronika_employee))
weronika_employee.laugh()
weronika_employee.walk_to("work")
weronika_employee.work()
weronika_employee.lunch_break()
weronika_employee.work()
print('Holiday days available: ', weronika_employee.holidays)
weronika_employee.take_holidays(5)
print('Holiday days available: ', weronika_employee.holidays)
print('Years with company:', weronika_employee.calculate_how_many_years_with_company())
print('Number of people instances', Person.get_number_of_person_instances())
print('Number of customer instances', Customer.get_number_of_customers())
print('Number of employee instances', Employee.get_number_of_employees())
