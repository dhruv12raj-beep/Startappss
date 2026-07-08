# 26.	Filter names having length greater than 4.

names=['Ram','Shyam',
       'John','Bob',
       'Alexander']


by_length = list(filter(lambda x : len(x) >4, names))
print(by_length)