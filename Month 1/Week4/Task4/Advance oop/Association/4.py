# Create a Driver and Car class where a driver drives a car, but both objects can exist independently.

class Car:
    def __init__(self, model):
        self.model = model


class Driver:
    def __init__(self, name):
        self.name = name


car1 = Car("Mahindra")
driver1 = Driver("Dhruv")

print(f"{driver1.name} drives {car1.model}")