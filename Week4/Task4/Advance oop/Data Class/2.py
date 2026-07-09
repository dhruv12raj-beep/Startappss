# Create an Employee data class with:
# •	employee_id
# •	name
# •	department
# •	salary




from dataclasses import dataclass


@dataclass
class Employee:
    employee_id : int
    name : str 
    department : int
    salary : int

emp1 = Employee(12,"dhruv","IT",50000)
emp2 = Employee(13,"Mayank","IT",50000)
print(emp1==emp2)