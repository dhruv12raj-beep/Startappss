# 33.	Flatten a nested list and store only unique values using set comprehension.

nested = [[1, 2], [3, 4], [5, 6]]

unique = {num for sublist in nested for num in sublist}
print(unique)

