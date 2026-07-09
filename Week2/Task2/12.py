# find the duplicate numbers using sets.


seen = set()
duplicate  = []
nums = [1,2,3,4,5,12,3,45]

for i in nums:
    if i in seen:
        duplicate.append(i)
    else:
        seen.add(i)

print(duplicate)