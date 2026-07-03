'''9.	Create a hybrid inheritance example and print the MRO using ClassName.mro().'''

class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(A):
    def info(self):
        print("Class C")

class D(B,C):
    def open(self):
        print("Class D")



d = D()
d.show()
d.display()
d.info()
d.open()


print(D.mro())
