

class Car:
    def __init__(self, speed):
        if speed < 0:
            self.__speed = 0
        else:
            self.__speed = speed
        


    def accelerate(self):
        pass

    def brake(self):
        pass

    def get_speed(self):
        pass