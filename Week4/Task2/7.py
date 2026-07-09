

class Patient:
    allowed_blood_groups = {
        "A+", "A-",
        "B+", "B-",
        "AB+", "AB-",
        "O+", "O-"
    }

    def __init__(self, blood_group):
        if blood_group in self.allowed_blood_groups:
            self.__blood_group = blood_group
        else:
            print("invalid blood group")

    def get_blood_group(self):
        print(f"Your blood group is: {self.__blood_group}")

    def set_blood_group(self,new_blood_group):
        if new_blood_group in self.allowed_blood_groups:
            self.__blood_group = new_blood_group
            print(f"Blood group set successfully to {self.__blood_group}")
        else:
            print("Not a valid Blood Group")


karan = Patient("AB+")
karan.get_blood_group()
karan.set_blood_group("O-")