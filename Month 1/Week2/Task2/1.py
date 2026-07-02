# remove duplicate from a list using set 

nums = [1,2,3,4,4,5,6,7,7]
seen = set()
for i in nums:
    seen.add(i)
print(seen)