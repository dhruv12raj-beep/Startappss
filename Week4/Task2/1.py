# encapsulation 


class Student:
    def __init__(self, name , marks):
        self.__name = name
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("marks should be in between 0 to 100")
        
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def show_details(self):
        print("---Student Details---")
        print(f"Student Name: {self.__name}")
        print(f"Student Marks: {self.__marks}")


student1 = Student("Santosh", 66)
print(student1.get_name())
print(student1.get_marks())
student1.show_details()
