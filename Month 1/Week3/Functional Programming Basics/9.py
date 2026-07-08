# 17.	Write a function that accepts any number of integers and returns their sum.

# total(1,2,3,4,5)


def total(*args):
    return sum(args)

print(total(1,2,3,4,5))
