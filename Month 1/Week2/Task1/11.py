'''Take a string and check whether it contains only digits.
Example:
Input: 12345
Output: Valid Number
'''

s = input("enter string:")

for char in s:
    if char.isdigit()== False:
        print("Invaild Number")
        break
else:
    print("Valid Number")
        
