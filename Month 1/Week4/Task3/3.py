'''3.	Implement multiple inheritance using Father and Mother classes.
 Create a Child class that inherits from both and accesses methods from each parent.'''


class Father:
    def fixes(self):
        print("Can Fix Everthing")

class Mother:
    def cooks(self):
        print("Cooks Delicious Food")

class Child(Father,Mother):
    def play(self):
        print("Plays Football")


father = Father()
mother = Mother()

child = Child()

child.fixes()
child.cooks()
child.play()

