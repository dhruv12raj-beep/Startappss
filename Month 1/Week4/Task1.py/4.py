#Employee Management System


class Employee:
    def __init__(self,employee,name, department, designation , salary , email, joining_date, experience):
        self.employee = employee
        self.name = name
        self.department= department
        self.designation = designation
        self.salary = salary
        self.email = email
        self.joining_date = joining_date
        self.experience = experience

    def login(self):
        print(f"welcome{self.name}")

    def apply_leave(self):
        print(f"{self.name} employee id {self.employee} applied for leave")

    def calculate_salary(self):
        print(f"{self.name} salary is: {self.salary}")

    def show_details(self):
        print("---Employee Details---")
        print(f"Employee id: {self.employee}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Employee Designation: {self.designation}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee Email: {self.email}")
        print(f"Joining Date: {self.joining_date}")
        print(f"Experience: {self.experience}")


obj = Employee("123","Reshmi","IT","Senior Software Engineer" ,120000, "reshmi9876@gmail.com","29-06-2026", "7 years" )
obj.login()
obj.apply_leave()
obj.calculate_salary()
obj.show_details()
