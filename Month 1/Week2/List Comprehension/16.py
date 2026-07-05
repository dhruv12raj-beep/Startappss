#16.	Create a set of numbers divisible by 3 from 1 to 100.

nums = {i for i in range(1,101) if i % 3 ==0}
print(nums)