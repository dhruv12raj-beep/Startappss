# Create a Student data class with the fields:
# •	id
# •	name
# •	age
# •	course

from dataclasses import dataclass

@dataclass
class Student:
    id:int
    name :str
    age :  int
    course : str


    def show_details(self):
        print(f"Name: {self.name} , id : {self.id} , age : {self.age}, course: {self.course}")

std = Student(11,"dhruv", 23,"Python")
std.show_details()
print(type(std.id))