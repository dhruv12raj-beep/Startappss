#15.	Override __eq__() to compare two students using their roll numbers.

class Students:
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def __eq__(self, value):
        return f"{self.roll_no == value.roll_no}"


std1 = Students(101)
std2 = Students(102)


print(std1 == std2)