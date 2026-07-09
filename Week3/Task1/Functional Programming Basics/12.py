# 20.	Write a function that counts how many keyword arguments were passed.

def counts(**inputs):

    return len(inputs)


print(counts(name = "dhruv", age = 23 , city = "indore"))