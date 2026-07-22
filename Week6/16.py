# Implement Undo/Redo.
# Use only deque.

from collections import deque


class NoteBook:
    def __init__(self,current):
        self.back = deque()
        self.forward = deque()
        self.current = current

    def newstring(self,text):
        self.back.append(self.current)
        self.current = text 
        self.forward.clear()    
    
    def undo(self):
        if not self.back:
            raise ValueError("Nothing to undo")
        self.forward.append(self.current)
        self.current = self.back.pop()
        return self.current
        
    def redo(self):
        if not self.forward:
            raise ValueError("Nothing to redo")
        self.back.append(self.current)
        self.current = self.forward.pop()
        return self.current

    def return_current(self):
        return self.current

n = NoteBook("hello")
n.newstring("bhai kya kar rahe ho?")
print(n.undo())
print(n.redo())
print(n.return_current())