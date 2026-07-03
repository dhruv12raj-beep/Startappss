'''18.	Create a Shape hierarchy with an area() method in each child class and write a function that accepts any shape object to calculate/display its area.'''


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(f"Area of circle: {3.14 * (self.radius**2)}")


class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of Rectangle: {self.length * self.width}")


def display_area(abc):
    abc.area()

c= Circle(7)
r = Rectangle(4,5)


display_area(c)
display_area(r)

