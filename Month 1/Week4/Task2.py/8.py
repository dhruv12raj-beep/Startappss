

class Laptop:

    def __init__(self, volume):
        if 0 <= volume <=100:
            self.__volume = volume

    def increase_volume(self,amount):
        self.__volume += amount
        if self.__volume > 100:
            self.__volume = 100
            print(f"Now at {self.__volume}")

    def decrease_volume(self,amount):
        self.__volume -= amount
        if self.__volume <0:
            self.__volume= 0
        else:
            print(f"Now at {self.__volume} volume.")

    def get_volume(self):
        return self.__volume
    
asus = Laptop(90)
asus.increase_volume(20)
asus.decrease_volume(110)
print(asus.get_volume())

