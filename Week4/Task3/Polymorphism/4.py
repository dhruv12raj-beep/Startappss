'''14.	Demonstrate method overriding using an Animal class and Dog and Cat subclasses'''

class Animal:
    def sound(self):
        print("Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

class Cat(Animal):
    def sound(self):
        print("Meows")


d = Dog()
d.sound()

c= Cat()
c.sound()