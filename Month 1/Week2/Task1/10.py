'''Take a string and print it in reverse order without using slicing ([::-1]).
Example:
Input: Python
Output: nohtyP
'''

string= "Python"
result= ""
for char in string:
    result = char + result
print(result)