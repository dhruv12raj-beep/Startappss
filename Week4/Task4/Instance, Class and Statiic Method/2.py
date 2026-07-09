#27.	Create an Employee class with a class variable company and a class method to update it.


class Employee:
    company = "IBM"

    @classmethod
    def show_company(cls,name):
        cls.company = name
        return f"company name = {cls.company}"
    
emp = Employee()
emp.show_company("Startappss")
print(emp.company)
