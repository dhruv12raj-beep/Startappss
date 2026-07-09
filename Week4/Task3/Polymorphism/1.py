'''11.	Create Dog, Cat, and Cow classes with a sound() method.
Use a loop to demonstrate runtime polymorphism'''


class Dog:
    def sound(self):
        print("Dog Barks")

class Cat:
    def sound(self):
        print("Cat Meows")

class Cow:
    def sound(self):
        print("Cow Mooooo!")

d=  Dog()
c = Cat()
cow = Cow()


s = [d,c,cow]
for i in s:
    i.sound()