# Create a Laptop class that creates a Keyboard object internally. Display keyboard details using the laptop object.



class Laptop:
    def __init__(self,name):
        self.name = name
        self.keyboard = Keyboard('In build Keyboard')

class Keyboard:
    def __init__(self, name):
        self.name = name 

l = Laptop("Asus")
print(f"Laptop name : {l.name} , keyboard : {l.keyboard.name}")