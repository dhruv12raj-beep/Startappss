'''Implement Browser History.
Functions
visit()

back()

forward()

current_page()
'''

from collections import deque

class History:

    def __init__(self,homepage):
        self.back_deque = deque()
        self.front_deque = deque()
        self.current = homepage

    def visit(self,url):
        self.back_deque.append(self.current)
        self.current = url 
        self.front_deque.clear()

    def back(self):
        if not self.back_deque:
            return "No previous page exists"
        self.front_deque.append(self.current)
        self.current = self.back_deque.pop()
        return self.current
    

    def forward(self):
        if not self.front_deque:
            return "No forward page available"
        self.back_deque.append(self.current)
        self.current = self.front_deque.pop()
        return self.current 
    
    def current_page(self):
        return self.current
    

h = History("google.com")
h.visit("chatgpt.com")
print(h.back())
print(h.forward())
print(h.current_page())
