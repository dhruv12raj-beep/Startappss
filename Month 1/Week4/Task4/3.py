#13.	Create a custom class that overrides __len__() to return the number of products in a cart.


class Flipkart:

    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)

    def __len__(self):
        return len(self.products)
    


cart = Flipkart()
cart.add_product("Laptop")
cart.add_product("Cover")
cart.add_product("Keyboard")
print(len(cart))