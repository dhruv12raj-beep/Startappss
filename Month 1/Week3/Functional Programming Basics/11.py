# 19.	Write a function that prints employee details using **kwargs.


def employee(**detail):
    return f"Employee details: {detail}"

print(employee(name= "dhruv", salary =50000 ))