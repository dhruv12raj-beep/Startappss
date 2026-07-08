# 29.	Find the sum of all numbers.

from functools import reduce

nums=[1,2,3,4,5]


new = reduce(lambda x ,y:x + y , nums)

print(new)

