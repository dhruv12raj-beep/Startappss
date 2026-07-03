'''22.	Create an abstract class Shape with an abstract method area(). Implement it for Circle and Rectangle'''


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"area of circle: {3.14 * (self.radius**2)}")

class Rectangle(Shape):

    def __init__(self,l,w):
        self.length = l
        self.w = w

    def area(self):
        print(f"Area of rectangle: {self.length*self.w}")

circ = Circle(7)
rec = Rectangle(5,10)


circ.area()
rec.area()