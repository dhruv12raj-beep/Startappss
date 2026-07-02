

class Employee:
    def __init__(self,employee_id , salary):
        self.__employee_id = employee_id
        if salary < 0:
            print("salary can't be negative")
        else:
            self.__salary = salary

    def get_salary(self):
        return f"salary: {self.__salary}"

    def set_salary(self,amount):
        if amount > 0:
            self.__salary = amount
        print(f"salary updated: {self.__salary}")

    
object = Employee(567, 99900)
print(object.get_salary())
object.set_salary(80000)

        