'''20.	Create an abstract class Employee with an abstract method calculate_salary(). Implement it for FullTimeEmployee and Freelancer.'''


from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        print("calculating salary")

class FullTimeEmployee(Employee):

    def calculate_salary(self):
        print("Calculating FulltimeEmployee salary")


class Freelancer(Employee):
    
    def calculate_salary(self):
        print("Calculating Freelancer salary")


full = FullTimeEmployee()
free= Freelancer()

full.calculate_salary()
free.calculate_salary()

    