# Create a metaclass that ensures every class has a variable named id.

class MyMeta(type):

    def __new__(cls, name, bases, namespace):
        if "id" not in namespace:
            raise AttributeError(f"Class {name} must define id attribute")
        return super().__new__(cls,name, bases, namespace)
    

class Employee(metaclass =MyMeta):
    name = "dhruv"

emp = Employee()
print(emp.name)
print(emp.id)