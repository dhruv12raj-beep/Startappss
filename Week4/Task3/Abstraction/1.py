'''19.	Create an abstract class Vehicle with an abstract method start(). Implement it in Car and Bike.'''


from abc import abstractmethod, ABC

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        print("vehicle starts")

class Car(Vehicle):
    def startd(self):
        return "car starts"

class Bike(Vehicle):
    def startd(self):
        return "bike starts"


mycar = Car()
print(mycar.start())