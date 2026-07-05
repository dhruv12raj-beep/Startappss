#21. Create a dictionary where keys are numbers from 1 to 10 and values are their squares.

# key_expression: value_expression for item in iterable

nums = {i:i**2 for i in range(1,11)}
print(nums)