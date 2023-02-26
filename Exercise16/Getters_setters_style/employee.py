import datetime
from person import Person


class Employee(Person):

    number_of_employees = 0

    def __init__(self, firstname, lastname, dob, gender, address, company, department,
                 position, employee_id, start_date, salary, holidays=25):
        super().__init__(firstname, lastname, dob, gender, address)
        self.__company = company
        self.department = department
        self.position = position
        self.__employee_id = employee_id
        self.__employee = True
        self.__start_date = start_date
        self.salary = salary
        self.holidays = holidays
        Employee.number_of_employees += 1

    def __str__(self):
        return f"{self.get_firstname()} {self.get_lastname()} is an instance of a class Employee (Person)."

    def get_company(self):
        return self.__company

    def get_department(self):
        return self.department

    def set_department(self, new_department):
        self.department = new_department

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def get_employee_id(self):
        return self.__employee_id

    def is_employee(self):
        return self.__employee

    def get_start_date(self):
        return self.__start_date

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_holidays(self):
        return self.holidays

    def set_holidays(self, new_holidays):
        self.holidays = new_holidays

    def work(self):
        print(f"Employee {self.get_firstname()} is working.")

    def lunch_break(self):
        print(f"Employee {self.get_firstname()} is taking a lunch break")

    def take_holidays(self, number_of_days_taken):
        holidays_left = self.get_holidays() - number_of_days_taken
        self.set_holidays(holidays_left)
        print(f"Employee {self.get_firstname()} is taking {number_of_days_taken} days of annual leave.")

    def calculate_how_many_years_with_company(self):
        today = datetime.date.today()
        start_date = self.get_start_date()
        years = today.year - start_date.year - ((today.month, today.day) < (start_date.month, start_date.day))
        return years

    @classmethod
    def get_number_of_employees(cls):
        return cls.number_of_employees
