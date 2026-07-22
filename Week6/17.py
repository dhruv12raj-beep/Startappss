'''Implement LRU Cache.
Capacity = 3
Operations
put()

get()
Use OrderedDict.
'''


from collections import OrderedDict


class LRUCache:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self,item):
        if item not in self.od:
            raise ValueError("key not present")

        self.od.move_to_end(item)

    def put(self,key, value):
        if key in self.od:
            self.od.move_to_end(key)

        self.od[key] = value

        if len(self.od) > self.capacity:
            self.od.popitem(last= False)


    def display(self):
        return self.od
    

lru = LRUCache(3)
lru.put(101,"pokemon")
lru.put(102,"hobo")
lru.put(103,"karna")

lru.get(101)
lru.put(202,"open")
print(lru.display())