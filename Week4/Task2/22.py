

class EmployeeAge:

    def __init__(self,age):
        if 18 <= age <=60:
            self.__age= age
        else:
            print(f"Age must be in between 18 to 60")

    @property
    def get_age(self):
        return f"Age: {self.__age}"
    


obj = EmployeeAge(19)
print(obj.get_age)