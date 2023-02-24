import datetime


class Person:

    number_of_Person_instances = 0

    def __init__(self, firstname, lastname, dob_day, dob_month, dob_year, gender, address):
        self.firstname = firstname
        self.lastname = lastname
        self._dob = datetime.datetime(dob_year, dob_month, dob_day)
        self.gender = gender
        self.address = address
        self.__person = True
        Person.number_of_Person_instances += 1

    def __str__(self):
        return f"{self.get_full_name()} is an instance of a class Person."

    # ######## getters and setters for the attributes ############################################################
    def get_firstname(self):
        return self.firstname

    def set_firstname(self, new_firstname):
        self.firstname = new_firstname

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, new_lastname):
        self.lastname = new_lastname

    def get_full_name(self):
        return f"{self.get_firstname} {self.get_lastname}"

    def get_dob(self):
        return self._dob

    # no setter for date of birth - it's semi private - as we decided we don't want users to change it

    def calculate_age(self):
        age = datetime.date.today().year - self.get_dob().year - \
              ((datetime.date.today().month, datetime.date.today().day) < (self.get_dob().month, self.get_dob().day))
        return age

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address

    def is_person(self):
        return self.__person

    # ######## methods for the Person class actions / behaviors ###################################################

    def walk(self):
        print(f"{self.get_firstname()} is walking")

    def walk_to(self, location):
        print(f"{self.get_firstname()} is walking to {location}")

    def talk(self):
        print(f"{self.get_firstname()} is talking")

    def laugh(self):
        print(f"{self.get_firstname()} is laughing")

    def sleep(self):
        print(f"{self.get_firstname()} is sleeping")

    def eat(self):
        print(f"{self.get_firstname()} is eating")

    @classmethod
    def get_number_of_person_instances(cls) -> int:
        return cls.number_of_Person_instances
