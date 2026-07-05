#12.	Create a set of unique vowels from a given string.


string = input("Enter String: ")
vowels = {ch for ch in string if ch in "aeiou"}
print(vowels)