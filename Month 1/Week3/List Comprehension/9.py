#9.	Create a list of common elements between two lists.

num1 = [1,2,3,4,5,6]
num2 = [4,5,6,7,8,8]


# nums = [set(num1) & set(num2)]
# print(nums)

nums = [i for i in num1 if i in num2]
print(nums)