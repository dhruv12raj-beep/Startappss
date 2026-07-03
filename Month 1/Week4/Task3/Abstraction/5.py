'''23.	Create an abstract class Animal with two abstract methods: sound() and move(). Implement both methods in Dog and Bird.'''

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    
    def sound(self):
        print("Barks")

    def move(self):
        print("walks")


class Bird(Animal):
    def sound(self):
        print("Chirps")

    def move(self):
        print("Flys")


d= Dog()
b = Bird()

d.sound()
d.move()

b.sound()
b.move()