# student management system 


class Student:

    def __init__(self, student_id , name , age , gender , class_name , section , roll_number, marks):
        self.student_id = student_id
        self.name = name 
        self.age = age 
        self.gender =  gender 
        self.class_name = class_name
        self.section = section
        self.roll_number = roll_number  
        self.marks = marks

    def study(self):
        print(f"{self.name} studies in:{self.class_name} section: {self.section}")

    def attend_class(self):
        print(f"{self.name} is attending the class")

    def take_exam(self):
        print(f"{self.name} is taking an exam")

    def show_result(self):
        print(f"marks obtained: {self.marks}")

    def show_profile(self):
        print(self.student_id , self.name , self.age , self.gender, self.class_name , self.section, self.roll_number)


obj = Student(11,'Shiva', 20, 'Male', "10th", "A", "1509", 88)
obj.study()
obj.attend_class()
obj.take_exam()
obj.show_result()
obj.show_profile()