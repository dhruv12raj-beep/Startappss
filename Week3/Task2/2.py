# 3. Write a custom iterator that returns only odd numbers between 1 and 20.


class Iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def  __next__(self):
        if self.num <=20:
            value = self.num
            self.num+=2
            return value
        raise StopIteration
    

obj = Iterator()
for i in obj:
    print(i)