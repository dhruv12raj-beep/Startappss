# Create a House class and a Room class where rooms are created inside the house.

class House:
    def __init__(self,address):
        self.address = address
        self.rooms= []
        self.rooms.append(Room("Kitchen"))    
        self.rooms.append(Room("Bedroom"))    
        self.rooms.append(Room("Garden"))    

class Room:
    def __init__(self, name):
        self.name = name     

h1 = House("xyz street")

for r in h1.rooms:
    print(f"House address: {h1.address} , rooms: {r.name}")


