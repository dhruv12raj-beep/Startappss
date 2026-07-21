from collections import *

'''Count how many employees belong to each department using defaultdict.'''


names = [("rahul","IT"),("Aman","HR"),("Rohit", "IT")]

count = defaultdict(int)

for emp , dep in names:
    count[dep] +=1

print(count)