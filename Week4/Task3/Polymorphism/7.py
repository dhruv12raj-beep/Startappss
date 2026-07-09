'''17.	Write a program that demonstrates duck typing using different classes having the same display() method'''



class Laptop:
    def display(self):
        print("Laptop")


class Mobile:
    def display(self):
        print("Mobile")


class Smartphone:
    def display(self):
        print("Smartphone")


def show(device):
    device.display()
    

l= Laptop()
m= Mobile()
s= Smartphone()

show(l)
show(m)
show(s)