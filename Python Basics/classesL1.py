# PYTHON OOP BASICS
# Lesson 1
# Corey Schafer
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

# Classes are object categories with attributes/variables/data and methods.
# These are relevant for code reuse and providing structure to the code.

# Class is defined as follows:

class Employee():
    # Global class variables are available for all instances
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        # Every time an instance is created, there is an increment of 1.
        Employee.num_of_emps += 1

    def __repr__(self):
        return f'Employee({self.first},{self.last},{self.pay},{self.email})'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # using class variable in instance method
        self.pay = int(self.pay * self.raise_amount) 

    # Lesson 3 is about class methods. which take the class as self argument. these are configured with 
    # @classmethod decorator
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Lesson 3
    # class method being used as an alternative constructor to accept a text string to create employee instance
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        pay = int(pay)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(date):
        if date.weekday() == 4 or date.weekday() == 5:
            return False
        return True

emp_1 = Employee('kashif','khan',30000)
emp_2 = Employee('aks','fakhar',40000)

print(emp_1.fullname())

print(emp_1.email)

# Class methods can be called with Class itself but then self will have to be provided within brackets.
print(Employee.fullname(emp_1))

# Global class variable accessible from instance and class
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print(emp_1.num_of_emps)

# class variable can be over-ridden with instance variable
emp_1.raise_amount = 1.1
print(emp_1.__dict__)

# using the class variable rather than the instance variable as defined in the apply_raise function
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# updating global class variable with a class method defined above with a class decorator
Employee.set_raise_amount(1.2)
emp_1.apply_raise()

emp_3_str = 'kuta-billa-45000'

emp_3 = Employee.from_string(emp_3_str)

# Regular method => default argument is instance(self)
# Class method => default argument is class (cls)
# Regular method => default argument is neither class or instance but some logical connection with class
# Example of static method within a class. 
import datetime
somedate = datetime.date(2020,7,12)
print(Employee.is_workday(somedate))


# LESSON 4: Class inheritance
# Sub class inherits all attributes and methods from main class
# we can override specific methods, attributes and class variables in the sub class
# print(help(class)) shows method resolution order
class Developer(Employee):
    raise_amount = 1.15

    def __init__(self,first,last,pay,prog_lang):
        # Inheritance from main class
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

print(isinstance(Developer,Employee))
print(issubclass(Developer,Employee))

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('Himesh', 'Reshamya', 20000, 'python')
dev_2 = Developer('Shah', 'Rukh', 25000, 'C#')
dev_3 = Developer('Rani', 'Mukergai', 32000, 'Java')

mng_1 = Manager('kashi','bai',90000,[dev_1,dev_2])

mng_1.add_emp(dev_3)

mng_1.remove_emp(dev_1)

mng_1.print_emps()


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# For method resolution order and other details..
# print(help(Developer))

# demonstration of repr method which allows you to print class instance with attributes etc as defined above.
print(mng_1)