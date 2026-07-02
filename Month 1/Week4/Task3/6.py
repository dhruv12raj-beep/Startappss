'''6.	Create a hierarchical inheritance example where Employee 
is the parent class and Developer, Tester, and HR are child classes.'''


class Employee:
    def greet(self):
        print("Welcome")

class Developer(Employee):
    def works(self):
        print("Developer Codes")


class Tester(Employee):
    def test(self):
        print("Tester tests the code")

class HR(Employee):
    def manage(self):
        print("HR manages Employees")

employee = Employee()
employee.greet()

developer = Developer()
tester = Tester()
hr = HR()

developer.greet()
developer.works()

tester.greet()
tester.test()

hr.greet()
hr.manage()