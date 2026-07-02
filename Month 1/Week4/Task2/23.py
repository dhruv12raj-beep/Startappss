

class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def area(self):
        print(f"Area of Rectangle: {self.__length * self.__width}")

    @property
    def perimeter(self):
        print(f"Perimeter of Rectangle: {2*(self.__length + self.__width)}")


r = Rectangle(5,7)
r.area
r.perimeter
    

