# Print the top 5 most frequent numbers from a list.


from collections import Counter

nums = [1,2,3,4,5,5,4,3,56,7,21,34,55]


count_nums = Counter(nums)
print(count_nums.most_common(5))