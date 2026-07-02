'''Create a tuple of 10 numbers and count how many numbers are greater than 50.
Example:
numbers = (10, 70, 20, 80, 30)
Output:
2
'''

nums = (10,70,20,80,30)
count = 0
for num in nums:
    if num > 50:
        count+=1

print(count)