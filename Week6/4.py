# Group students department-wise using defaultdict.
'''Input
[
("Rahul","IT"),
("Aman","HR"),
("Rohit","IT")
]
'''

from collections import defaultdict

names = [("rahul","IT"),("Aman","HR"),("Rohit", "IT")]

grouped_data =  defaultdict(list)

for std, dept in names:
    grouped_data[dept].append(std)

print(grouped_data)