#12.	Create a class that overrides __repr__() for debugging.


class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"emp id = {self.emp_id}, name = {self.name}, salary ={self.salary}"


e1 = Employee(89, "Dhruv", 97000)

print(repr(e1))