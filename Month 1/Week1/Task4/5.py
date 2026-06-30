#Take a string and create a new string containing only the even index characters.
'''Example:
Input: Python
Output: Pto'''


string = input("Enter a string:")

result =  ""

for i in range(len(string)):
    if i % 2 ==0:
        result += string[i]

print(f"New sting is {result} ")