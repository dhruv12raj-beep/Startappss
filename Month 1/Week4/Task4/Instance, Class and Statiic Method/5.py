#30.Create a class method that creates an object from a comma-separated string like "Rahul,22".



class Class:

    def __init__(self,name ,age):
        self.name = name
        self.age = age 

    @classmethod
    def create(cls,string):
        name , age = string.split(",")
        return cls(name, int(age))
    

c= Class.create("Rahul,22")
print(c.name)
print(c.age)