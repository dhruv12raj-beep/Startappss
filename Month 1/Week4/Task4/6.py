#16. Override __lt__() to compare employees based on salary.


class Employee:
    def __init__(self,salary):
        self.salary = salary

    def __lt__(self, other):
        return f"{self.salary > other.salary}"


emp1 = Employee(10)
emp2 = Employee(20)

print(emp1 > emp2)