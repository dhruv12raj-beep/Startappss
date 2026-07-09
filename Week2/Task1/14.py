'''Take 5 names in a list and print them in alphabetical order.
Example:
Input:
["Ram", "demo", "Mohan"]
Output:
["demo", "Mohan", "Ram"]
'''


names = ["Ram", "demo", "Mohan","genz", "list"]

names.sort(key=str.lower)
print(names)

