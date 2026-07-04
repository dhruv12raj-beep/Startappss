#29.	Create an Employee class with a static method to validate age (minimum 18 years).


class Employee:

    @staticmethod
    def validate(age):
        if age >=18:
            print("Requirement Satisfied")
        else:
            print("Not Allowed")

emp = Employee()
emp.validate(19)