# mobile phone


class MobilePhone:

    def __init__(self, phone, battery_percentage):
        if  0 <= battery_percentage <=100:
            self.__battery_percentage = battery_percentage 
        else:
            self.__battery_percentage = 0 
            print("invalid battery percentage! set to 0")
        self.phone = phone 

    def charge(self,amount):
        self.__battery_percentage +=amount
        if self.__battery_percentage > 100:
            self.__battery_percentage = 100
        print(f"{self.__battery_percentage} percent charged")

    def use_phone(self,amount):
        self.__battery_percentage -=amount
        if self.__battery_percentage < 0:
            self.__battery_percentage = 0

        print(f"{self.phone} is at {self.__battery_percentage}")

    def get_battery(self):
        return self.__battery_percentage


object = MobilePhone("Iphone",80 )
object.charge(30)
object.use_phone(50)
print(object.get_battery())

