'''Find the first unique character.
apple

↓

Output

a
'''
from collections import Counter

chars = 'apple'

count = Counter(chars)


for ch in chars:
    if count[ch]==1:
        print(ch)
        break

