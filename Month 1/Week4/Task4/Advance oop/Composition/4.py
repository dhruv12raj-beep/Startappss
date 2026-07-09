# Create a Mobile class containing a Battery object created inside the mobile.


class Mobile:
    def __init__(self, model):
        self.model = model
        self.battery = Battery(5000)


class Battery:
    def __init__(self,capacity):
        self.capacity = capacity

c = Mobile("Iphone")
print(f"Phone model : {c.model}  -> Battery : {c.battery.capacity}")
