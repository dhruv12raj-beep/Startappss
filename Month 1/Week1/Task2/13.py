# Find the largest number from 5 user inputs.


largest = float("-inf")
for i in range(5):
    num = int(input("enter number: "))

    if num > largest:
        largest = num 

print("largest number is", largest )