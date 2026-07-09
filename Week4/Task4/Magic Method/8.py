#18.	Create a class using __getitem__() so elements can be accessed using indexing.

class Inventory:
    def __init__(self, items):
        self.items = items
    

    def __getitem__(self, key):
        return self.items[key]
    

inv = Inventory([1,2,3,4,5])

print(inv[0])
print(inv[1])
print(inv[2])