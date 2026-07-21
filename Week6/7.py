'''Implement Queue using deque.
Methods
enqueue()

dequeue()

front()

rear()
'''
from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self,item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
que = Queue()

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
print(que.queue)

print(que.dequeue())

print(que.front())
print(que.rear())

