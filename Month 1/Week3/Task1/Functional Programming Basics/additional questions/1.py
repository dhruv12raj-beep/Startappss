# Using map() and lambda, convert
# ['1','2','3','4']
# into
# [1,2,3,4]

nums = ['1','2','3','4']


converted = map(lambda x : str(x), nums)
print(list(converted))
