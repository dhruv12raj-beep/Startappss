'''24.	Create an abstract class that contains both a normal method and an abstract method. Demonstrate how child classes inherit the normal method while implementing the abstract one.'''

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def show_details(self):
        pass

    def greet(self):
        print("hii")

class B(A):

    def show_details(self):
        print("B")


b = B()
b.greet()
b.show_details()


