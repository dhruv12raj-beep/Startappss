# count vowels using a set

vowels = {'a','e','i','o','u'}
count = 0
s= input("Enter string: ")

for ch in s:
    if ch in vowels:
        count+=1

print(count)