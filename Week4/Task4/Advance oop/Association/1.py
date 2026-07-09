# Create a Teacher and Student class where a teacher teaches multiple students. Display which teacher teaches which student.


class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []


class Student:
    def __init__(self, name):
        self.name = name


t1 = Teacher("Mr. Aman")

s1 = Student("Dhruv")
s2 = Student("Ankit")

t1.students.append(s1)
t1.students.append(s2)

for s in t1.students:
    print(f"{t1.name} teaches {s.name}")

