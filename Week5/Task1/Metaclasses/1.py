# Create a metaclass that converts every class attribute name to uppercase during class creation.
# Example
# class Student(metaclass=MyMeta):
#     name = "Rahul"
# Should become internally:
# NAME = "Rahul"
#name = the string name of the class being created
# bases = a tuple of base classs inherited by the new class
#namespace = a dictinary containing attributes and methods defined in the class body


class MyMeta(type):
    def __new__(cls, name, bases, namespace): 
        new_namespace = {}

        for key, value in namespace.items():
            if not key.startswith("__"):
                new_namespace[key.upper()] = value
            else:
                new_namespace[key] = value
        return super().__new__(cls,name, bases, new_namespace)
    

class Student(metaclass =MyMeta):
    name = "Dhruv"
    age = 23


std = Student()

print(std.NAME)
print(std.AGE)