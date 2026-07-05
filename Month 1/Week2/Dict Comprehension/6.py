# 26.	Create a frequency dictionary of characters in a string using dictionary comprehension.

string = "programming"
freq = {key : string.count(key) for key in string}
print(freq)