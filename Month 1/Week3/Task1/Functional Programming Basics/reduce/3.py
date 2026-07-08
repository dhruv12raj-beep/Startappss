# 31.	Find the maximum element using reduce().

from functools import reduce

nums=[10,45,23,67,12]

new = reduce(lambda x,y : x if x >y else y,nums)

print(new)