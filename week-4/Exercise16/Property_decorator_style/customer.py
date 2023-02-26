from person import Person


class Customer(Person):

    number_of_customers = 0

    def __init__(self, firstname, lastname, dob, gender, address, customer_id,
                 loyalty_points=0):
        super().__init__(firstname, lastname, dob, gender, address)
        self.__customer_id = customer_id
        self.__customer = True
        self._loyalty_points = loyalty_points
        Customer.number_of_customers += 1

    def __str__(self):
        return f"{self.firstname} {self.lastname} is an instance of a class Customer (Person)."

    @property
    def customer_id(self):
        return self.__customer_id

    def is_customer(self):
        return self.__customer

    @property
    def loyalty_points(self):
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, new_loyalty_points):
        self._loyalty_points = new_loyalty_points

    def add_loyalty_points(self, points):
        self.loyalty_points += points

    def get_customer_info(self):
        return f"Customer name: {self.firstname} {self.lastname}, id: {self.customer_id}, loyalty points accumulated:" \
               f" {self.loyalty_points}"

    def purchase(self, item):
        self.add_loyalty_points(20)
        print(f"{self.firstname} bought {item} and earned extra 20 loyalty points")
        print("Total loyalty points: " + str(self.loyalty_points))

    @classmethod
    def get_number_of_customers(cls):
        return cls.number_of_customers
