'''4.	Create a class hierarchy for Animal, Dog, Cat, and Lion.
Show how common methods are inherited while child classes have their own unique methods.'''


class Animal:
    def legs(self):
        print("has four legs")

class Dog(Animal):
    def sound(self):
        print("Wooff")

class Cat(Animal):
    def climbs(self):
        print("Cat climbs the tree")

class Lion(Animal):
    def hunts(self):
        print("Lion hunts the jungle")


animal = Animal()
dog = Dog()
cat = Cat()
lion = Lion()


dog.sound()
dog.legs()

cat.climbs()
cat.legs()

lion.hunts()
lion.legs()




