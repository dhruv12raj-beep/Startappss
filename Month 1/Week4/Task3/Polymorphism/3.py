''''13.	Create Developer, Tester, and Manager classes with a work() method.
 Store all objects in a list and execute their methods using polymorphism.'''


class Developer:
    def work(self):
        print("Developer works")

class Tester:
    def work(self):
        print("Tester works")

class Manager:
    def work(self):
        print("Manager works")


d= Developer()
t = Tester()
m = Manager()


emp = [d,t,m]
for i in emp:
    i.work()

