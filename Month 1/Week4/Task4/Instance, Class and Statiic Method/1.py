#26.	Create a Student class with an instance method to display student details.


class Student:

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def show_details(self):
        return f"Student name: {self.name} and his/her age:{self.age}"
    

std = Student("Dhruv",23)
print(std.show_details())