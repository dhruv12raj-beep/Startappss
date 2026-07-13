#Create a metaclass that automatically adds a class variable named created_by = "Admin".



class MyMeta(type):
    def __new__(cls, name, bases, namespace):

        namespace["created_by"]  ="Admin"

        return super().__new__(cls, name, bases, namespace)
    


class Student(metaclass = MyMeta):
    name = "Dhruv"


std = Student()
print(std.name)
print(std.created_by)
    