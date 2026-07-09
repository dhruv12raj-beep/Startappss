#28.	Create a Calculator class with a static method to calculate the square of a number


class Calculator:

    @staticmethod
    def square(num):
        return num **2
    

calci = Calculator()
print(calci.square(4))