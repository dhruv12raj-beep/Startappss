# Create an iterator class that iterates through a list of employee names one by one.


class EmployeeIterator:
    def __init__(self,employee):
        self.employee=employee
        self.index=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
      if self.index<len(self.employee):
          value=self.employee[self.index]
          self.index+=1
          return value
      raise StopIteration



employee = ["John", "Mike", "Sara", "Alex"]
obj = EmployeeIterator(employee)
for emp in obj:
    print(emp) 