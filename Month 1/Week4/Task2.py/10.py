

class ATM:

    def __init__(self, pin):
        if len(str(pin)) == 4:
            self.__pin = pin
        else:
            print("PIN must contains 4 digit")

    def verify_pin(self, pin):
        if self.__pin == pin:
            print("Access Granted")
        else:
            print("Incorrect PIN")

    def change_pin(self,pin):
        if len(str(pin)) ==4:
            self.__pin = pin
            print(f"PIN changed Successfully: {self.__pin}")
        else:
            print(f"Pin must be 4 digits")

sbi = ATM(4333)
sbi.verify_pin(4333)
sbi.change_pin(1211)

        

        