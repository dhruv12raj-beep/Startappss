# 30.	Find the product of all numbers.

from functools import reduce

nums=[1,2,3,4]


new = reduce(lambda x ,y : x * y , nums)
print(new)