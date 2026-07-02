'''Take a string from the user and count:
Alphabets 
Digits 
Special Characters 
Example:
Input: Python123@
Output:
Alphabets = 6
Digits = 3
Special Characters = 1
'''

string = input("Enter string: ")
Alphabets = 0
Digits= 0
Special= 0
for char in string:
    if char.isalpha():
        Alphabets+=1
    elif char.isdigit():
        Digits+=1
    else:
        Special+=1
print("Alphabets =",Alphabets)
print("Digits =",Alphabets)
print("Special =",Special)
