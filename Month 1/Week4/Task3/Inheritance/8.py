'''8.	Create a class hierarchy for University → Department → Student.
 Show how data flows through constructors using super().'''


class University:
    def __init__(self,university_name):
        self.university_name = university_name
        print("University constructor called")

class Department(University):
    def __init__(self, university_name, department_name):
        super().__init__(university_name)
        self.department_name = department_name
        print("Department constructor called")

class Student(Department):
    def __init__(self, university_name, department_name,student_name):
        super().__init__(university_name, department_name)
        self.student_name = student_name
        print("student constructor called")

    def show_details(self):
        print("---Student Details---")
        print("University:", self.university_name)
        print("Department:", self.department_name)
        print("Student:", self.student_name)


student =Student("IIT Bombay","IT","Dhruv Verma")
student.show_details()