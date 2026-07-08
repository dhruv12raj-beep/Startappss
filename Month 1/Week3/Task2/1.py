# 1. What methods must a class implement to become an iterator in Python?



class Iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
        
    def __next__(self):
        
        if self.num<=10:
            value = self.num
            self.num+=1
            return value
        raise StopIteration
    

obj = Iterator()

for i in obj:
    print(i)
    
