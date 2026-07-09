#Take a string and remove all spaces from it.
'''Example:
Input: Python Programming Language
Output: PythonProgrammingLanguage'''


string = input("Enter a string: ")

result = ""

for char in string:
    if char != " ":
        result += char 
    
print("without spaces: ", result)