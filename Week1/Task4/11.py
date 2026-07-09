'''Take a string and find the longest word.
Example:
Input: Python is very easy to learn
'''

string = input("Enter String").split()
longest = ""

for word in string:
    if len(word) > len(longest):
        longest = word

print(longest)