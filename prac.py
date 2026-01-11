class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee("Rama", 10000)
print(emp.name)

emp.show()

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Rama', 25000)

print('Name:', emp.name)

# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)

 # base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "AI Project"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Amar")
c.show()

# Direct access protected data member
print('Project:', c._project)
com = Company()
print(com._project)

class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Amar', 25)

# # retrieving age using getter
print('Name:', stud.name, stud.get_age())
stud.set_age(30)
print("name:",stud.name, stud.get_age())