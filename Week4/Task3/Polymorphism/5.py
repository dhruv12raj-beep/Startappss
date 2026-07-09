'''15.	Demonstrate operator polymorphism by showing how the + operator behaves differently for integers, strings, and lists.'''



class Abc:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    def add(self,a,b):
        print(f"Result: {a + b}")


ai = Abc()
ai.add(5,6)
ai.add("hello ", "world")
ai.add([1,2,3],[4,5,6])
