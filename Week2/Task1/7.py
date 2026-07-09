'''Create a tuple of subject names and a list of marks. Print:
Maths : 90
English : 85
Science : 80
using a loop.
'''

tuple = ("Maths", "English", "Science")
list = [90,85,80]

for i in range(len(tuple)):
    print(f"{tuple[i]}:{list[i]}")