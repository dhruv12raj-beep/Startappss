#Search a number in a list and stop when found.

nums = [10 ,20 ,30 ,40 ,50 ]

target = int(input("Enter Number: "))

found = False

for num in nums:
    if num == target:
        print("Found")
        found = True 
        break 
    

if not found:
    print("Number not found")