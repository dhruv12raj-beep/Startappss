'''1.	Create a Vehicle class with a start() method. Create Car, Bike, 
and Truck classes that inherit from Vehicle and add their own methods.'''


class Vehicle:
    def start(self):
        print("Vehicle Starts")

class Car(Vehicle):
    def open_sunroof(self):
        print("Opens sunroof")

class Bike(Vehicle):
    def wheele(self):
        print("doing a wheele")

class Truck(Vehicle):
    def blow_horn(self):
        print("blows horn!")


car = Car()
bike = Bike()
truck = Truck()

car.start()
bike.start()
truck.start()

car.open_sunroof()
bike.wheele()
truck.blow_horn()