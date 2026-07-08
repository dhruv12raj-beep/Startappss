#7.	Create a list of cubes of odd numbers from 1 to 30.

nums = [i**3 for i in range(1,31) if i % 2!=0 ]
print(nums)