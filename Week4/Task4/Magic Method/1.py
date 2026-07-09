# Create a class that overrides __str__() to display employee information.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}"


e1 = Employee(89, "Dhruv", 97000)

print(e1)    