'''Implement Stack using deque.
Methods
push()

pop()

peek()

is_empty()
'''

from collections import deque


class Stack:

    def __init__(self):
        self.stacck = deque()

    def push(self, value):
        self.stacck.append(value)

    def pop(self):
        return self.stacck.pop()
    
    def peek(self):
        return self.stacck[-1]
    
    def is_empty(self):
        return len(self.stacck)==0
    

s = Stack()
s.push(10)
s.push(15)
s.push(20)
s.push(30)
s.push(50)

print(s.pop())

print(s.peek())
print(s.is_empty())
