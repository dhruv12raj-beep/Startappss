# Create an Employee class and a Department class. A department contains multiple employees. Print all employee details.



class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []


class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary


d1 = Department("IT")

e1 = Employee("Dhruv", 101, 55000)
e2 = Employee("Soham", 102, 60000)

d1.employees.append(e1)
d1.employees.append(e2)

for e in d1.employees:
    print(f"Department: {d1.name} | ID: {e.emp_id}, Name: {e.name}, Salary: {e.salary}")