# Create a Car class and an Engine class. The engine should be created inside the car object.

class Car:
    def __init__(self,model):
        self.model = model
        self.engine = Engine(228)        

class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power


c= Car("Be6")
print(f"Car Model:{c.model}, Horse_Power : {c.engine.horse_power}")