# Find duplicate words in a text using Counter.

from collections import Counter


words = "how are you from ? im from very nice !"
splitted = words.split()
word_count = Counter(splitted)
duplicate = {word : count for word, count in word_count.items()  if count > 1}
print(duplicate)