'''Given
sales=[
("Rahul","Laptop"),
("Rahul","Laptop"),
("Aman","Mouse"),
("Rahul","Mouse")
]
Output
Rahul
Laptop :2
Mouse :1
Aman
Mouse :1
Use
defaultdict
Counter
'''

from collections import defaultdict, Counter

sales = [
("Rahul","Laptop"),
("Rahul","Laptop"),
("Aman","Mouse"),
("Rahul","Mouse")
]

dd = defaultdict(Counter)

for key , value in sales:
    dd[key][value] +=1

print(dd)