'''Create a list with duplicate values and remove duplicates without using set().
Example:
Input: [1,2,2,3,4,4,5]

Output: [1,2,3,4,5]
'''

nums = [1,2,2,3,4,4,5]
result = []
for num in nums:
    if num not in result:
        result.append(num)

print(result)