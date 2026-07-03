"""10.	Create a Shape class with common properties.
 Inherit Rectangle, Circle, and Triangle classes and implement their own methods."""


class Shape:
    def __init__(self,colour):
        self.colour = colour

    def info(self):
        print(f"Name: {self.colour}")

class Rectangle(Shape):
    def __init__(self, colour, lenght, width):
        super().__init__(colour)
        self.length = lenght
        self.width = width

    def area(self):
        print(f"Area of Rectangle: {self.length * self.width}")

class Circle(Shape):
    def __init__(self, colour,radius):
        super().__init__(colour)
        self.radius = radius


    def area(self):
        print(f"Area of circle: {3.14 * (self.radius**2)}")


class Triangle(Shape):
    def __init__(self, colour,base,height):
        super().__init__(colour)
        self.base = base
        self.height = height

    def area(self):
        print(f"Area of Triangle: {0.5* self.base*self.height}")




r = Rectangle("GReen Rectangle", 5,6)
c = Circle("Pink Circle", 5.5)
t = Triangle("Blue Triangle",3,5)

r.info()
r.area()

c.info()
c.area()

t.info()
t.area()
