# 27.	Create a dictionary where keys are words and values are word lengths:words = ["python", "java", "sql"]

words = ["python", "java", "sql"]

dict = {i:len(i) for i in words}
print(dict)

