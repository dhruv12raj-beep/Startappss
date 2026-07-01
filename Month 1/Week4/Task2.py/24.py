

class UniversityStudent:

    def __init__(self, cgpa):
        if 0.0 <= cgpa <=10.0:
            self.__cgpa = float(cgpa)
            
    @property
    def cgpa(self):
        return f"CGPA: {self.__cgpa}"
    
    @cgpa.setter
    def cgpa(self,value):
        if 0.0 <= value <=10.0:
            self.__cgpa = float(value)
            print(f"CGPA set Successfully: {self.__cgpa}")
        else:
            print("CGPA should be between 0.0 and 10.0")

student = UniversityStudent(8)
print(student.cgpa)
student.cgpa= 9

        



    

