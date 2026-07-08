# 24.	Create a dictionary of even numbers from 1 to 20 and their squares

nums = {i:i**2 for i in range(1,21) if i %2==0}
print(nums)