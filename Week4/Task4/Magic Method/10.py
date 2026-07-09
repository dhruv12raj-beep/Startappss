#   20.	Make an object callable using __call__().

class Multiplier:

    def __init__(self,n):
        self.n = n

    def __call__(self, value):
        return  value * self.n
    

double = Multiplier(2)
triple = Multiplier(3)

print(double(10))
print(triple(10))