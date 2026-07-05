#20.	Create a set of common elements from two lists.


data1 = [1,2,3,4,5]
data2 = [2,3,4,5,6]

common = {i for i in data1 if i in data2}
print(common)