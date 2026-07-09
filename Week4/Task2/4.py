#product


class product:
    def __init__(self, name , price):
        self.__name = name 
        self.__price = price 

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price <= 0:
            print("price must me greater than 0")
        else:
            self.__price = price
            print(f"updated price is: {self.__price}")

    

obj = product("Marvel","999")
print(obj.get_price())
obj.set_price(-1)

