#5.	Create a list of numbers from 1 to 50 that are divisible by both 2 and 5.


nums = [i for i in range(1,51) if i %2==0 and i %5==0]
print(nums)