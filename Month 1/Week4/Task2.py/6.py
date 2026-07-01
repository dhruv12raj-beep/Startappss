

class Car:
    def __init__(self, speed):
        if speed < 0:
            self.__speed = 0
        else:
            self.__speed = speed
        

    def accelerate(self,rev):
        self.__speed += rev
        print(f"Speed increased to {self.__speed}")

    def brake(self,brk):
        self.__speed -= brk
        if self.__speed < 0:
            self.__speed = 0
        print(f"You're at {self.__speed} now.")

    def get_speed(self):
        return f"Speed:{self.__speed}"

mahindra = Car(100)
mahindra.accelerate(20)
mahindra.brake(90)
print(mahindra.get_speed())