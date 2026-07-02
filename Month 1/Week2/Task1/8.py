'''Take a string and find the first non-repeated character.
Example:
Input: swiss
Output: w
'''

string = input("Enter string: ")
for char in string:
    if string.count(char)==1:
        print(char)
        break