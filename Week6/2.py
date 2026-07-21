# Find the most common word in a paragraph using Counter.

from collections import Counter

paragraph = "python is awesome"

count = Counter(paragraph)
print(count.most_common(5))