# count frequency of words in sentence 

s = input("Express your thoughts: ")

freq = {}

for char in s:
    if char ==" ":
        continue
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] +=1

print(freq)