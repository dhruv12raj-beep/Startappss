'''Create a tuple of employee names and check whether a given employee name exists in the tuple.
Example:
Input: demo
Output:
Employee Found
'''

names = ("ayush", "akash", "dhruv", "harshal", "shreya")
target = "harshal"
for name in names:
    if target in names:
        print("found")
        break
    else:
        print("not found")    