# Create your own implementation of Python's range(start, stop) using an iterator class


class MyRange:
    def __init__(self,start,stop):
        self.current=start
        self.stop=stop
    
    def __iter__(self):
        return self
 
    def __next__(self):
        
       if self.current<self.stop:
           value=self.current
           self.current+=1
           return value
       raise StopIteration


obj = MyRange(5, 10)
for i in obj:
    print(i)