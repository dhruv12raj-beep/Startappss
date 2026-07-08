from functools import reduce

# Using reduce(), calculate the factorial of 6.

nums = range(1,7)
kk = reduce(lambda x , y : x*y, nums)
print(kk)   