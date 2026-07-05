# 31.	Find the frequency of each element in a list using dictionary comprehension.

l = [1,2,2,3,4,5,6]

d = {i:l.count(i) for i in l }
print(d)