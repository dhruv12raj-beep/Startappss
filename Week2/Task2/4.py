#find missing number from a set

nums = {1,2,4,5}
n = 5
missing = n *(n+1)//2 - sum(nums)
print(missing)


