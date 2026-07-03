'''2.	Create a multilevel inheritance example using Person → Employee → Manager.
 Add different methods at each level and demonstrate method access.'''


class Person:
    def works(self):
        print("Person works 9 to 5")

class Employee(Person):
    def apply_leave(self):
        print("Applies for a leave")

class Manager(Employee):
    def assign_tasks(self):
        print("Task assigned !")

person = Person()
employee = Employee()
manager = Manager()

person.works()

employee.works()
employee.apply_leave()

manager.works()
manager.apply_leave()
manager.assign_tasks()