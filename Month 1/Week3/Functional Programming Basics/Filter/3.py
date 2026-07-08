# 27.	Filter numbers divisible by 3.
nums=range(1,31)


new_nums = list(filter(lambda x: x%3==0, nums))
print(new_nums)
