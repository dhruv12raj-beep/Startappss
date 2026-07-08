# Create an infinite iterator that generates consecutive integers starting from 1.

class InfiniteIntegers:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.num
        self.num += 1  
        return value

infinite_nums = InfiniteIntegers()

for i in infinite_nums:
    print(i)