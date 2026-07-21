# Write a program to count the frequency of each character in a string using Counter.

from collections import Counter

string = "banana"

count_chars = Counter(string)
print(count_chars)

print(count_chars.most_common(2))
