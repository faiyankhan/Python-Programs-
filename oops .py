# Object Oriented Programming in Python
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        return self.salary
   
abhishek = Employee("Abhishek","44000")
print(abhishek.salary)
print(abhishek.name)
abhishek.getsalary()

lavkush = Employee("lavkush","42000")
print(lavkush.salary)
print(lavkush.name)
lavkush.getsalary()
