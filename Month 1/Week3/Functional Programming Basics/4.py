# 12.	Sort the list according to the second element.

data = [(1,4),(2,1),(3,2),(4,5)]

sorted = sorted(data, key = lambda x:x[1])
print(sorted)