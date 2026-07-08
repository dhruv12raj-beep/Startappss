#6.	Flatten the following nested list:

nested = [[1, 2], [3, 4], [5, 6]]

flatten  = [num for sublist in nested for num in sublist]
print(flatten)