# Using filter() and lambda, find all prime numbers between 1 and 50.

nums = range(1,51)

new = list(filter(lambda x: x>1 and all(x% i !=0 for i in range(2, int(x**0.5)+1)),nums))
print(new)