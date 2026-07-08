# /32.	Concatenate all strings.
words=['Python',
       'is',
       'awesome']

from functools import reduce

new = reduce(lambda x ,y : x+y , words)
print(new)