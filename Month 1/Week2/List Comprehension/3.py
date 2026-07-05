#3.	Create a list containing the length of each word in: = ["python", "java", "c++", "javascript"]


words = ["python", "java", "c++", "javascript"]

length = [len(i) for i in words ]
print(length)