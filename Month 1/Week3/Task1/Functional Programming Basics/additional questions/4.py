# Using map(), filter(), and reduce() together:
# Steps:
# 1.	Filter even numbers.
# 2.	Square them.
# 3.	Find their sum.

from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

new = filter(lambda x:x %2 ==0,nums )
new = map(lambda x : x**2 , new)

new = reduce(lambda x,y :x+y , new)
print(new)