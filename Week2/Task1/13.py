'''Create a list of 10 numbers and create a new list containing only numbers greater than 25.
Example:
Input: [10,20,30,40]
Output: [30,40]
'''


nums = [10,20,30,40]
result =[]
for num in nums:
    if num > 25:
        result.append(num)
print(result)
