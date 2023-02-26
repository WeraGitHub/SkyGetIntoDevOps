import datetime
from person import Person


class Employee(Person):

    number_of_employees = 0

    def __init__(self, firstname, lastname, dob, gender, address, company, department, position, employee_id,
                 start_date, salary, holidays=25):
        super().__init__(firstname, lastname, dob, gender, address)
        self.__company = company
        self._department = department
        self._position = position
        self.__employee_id = employee_id
        self.__employee = True
        self.__start_date = start_date
        self._salary = salary
        self._holidays = holidays
        Employee.number_of_employees += 1

    def __str__(self):
        return f"{self.firstname} {self.lastname} is an instance of a class Employee (Person)."

    @property
    def company(self):
        return self.__company

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        self._department = new_department

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    @property
    def employee_id(self):
        return self.__employee_id

    def is_employee(self):
        return self.__employee

    @property
    def start_date(self):
        return self.__start_date

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    @property
    def holidays(self):
        return self._holidays

    @holidays.setter
    def holidays(self, new_holidays):
        self._holidays = new_holidays

    def work(self):
        print(f"Employee {self.firstname} is working.")

    def lunch_break(self):
        print(f"Employee {self.firstname} is taking a lunch break")

    def take_holidays(self, number_of_days_taken):
        holidays_left = self.holidays - number_of_days_taken
        self._holidays = holidays_left
        print(f"Employee {self.firstname} is taking {number_of_days_taken} days of annual leave.")

    def calculate_how_many_years_with_company(self):
        today = datetime.date.today()
        start_date = self.start_date
        years = today.year - start_date.year - ((today.month, today.day) < (start_date.month, start_date.day))
        return years

    @classmethod
    def get_number_of_employees(cls):
        return cls.number_of_employees
