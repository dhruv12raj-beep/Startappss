# Create a Company class and an Employee class. A company has multiple employees. Show employee details after deleting the company object.


class Company:
    def __init__(self, name):
        self.name = name 
        self.employees  = []


class Employee:
    def __init__(self,name):
        self.name = name 


c = Company("Accenture")
e1 = Employee("Akash")
e2 = Employee("Mayaank")

c.employees.append(e1)
c.employees.append(e2)

for s in c.employees:
    print(f"Company : {c.name} -> Employee {s.name}")

del c
print(e1.name)
print(e2.name)