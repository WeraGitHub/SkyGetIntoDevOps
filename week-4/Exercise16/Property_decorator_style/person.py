import datetime


class Person:
    number_of_Person_instances = 0

    def __init__(self, firstname, lastname, dob, gender, address):
        self._firstname = firstname
        self._lastname = lastname
        self.__dob = dob
        self._gender = gender
        self._address = address
        self.__person = True
        Person.number_of_Person_instances += 1

    def __str__(self):
        return f"{self.firstname} {self.lastname} is an instance of a class Person."

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, new_firstname):
        self._firstname = new_firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self._lastname = new_lastname

    @property
    def dob(self):
        return self.__dob

    # no setter for date of birth - it's semi private - as we decided we don't want users to change it

    def calculate_age(self):
        age = datetime.date.today().year - self.dob.year - ((datetime.date.today().month, datetime.date.today().day) <
                                                            (self.dob.month, self.dob.day))
        return age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    def is_person(self):
        return self.__person

    def walk(self):
        print(f"{self.firstname} is walking")

    def walk_to(self, location):
        print(f"{self.firstname} is walking to {location}")

    def talk(self):
        print(f"{self.firstname} is talking")

    def laugh(self):
        print(f"{self.firstname} is laughing")

    def sleep(self):
        print(f"{self.firstname} is sleeping")

    def eat(self):
        print(f"{self.firstname} is eating")

    @classmethod
    def get_number_of_person_instances(cls) -> int:
        return cls.number_of_Person_instances
