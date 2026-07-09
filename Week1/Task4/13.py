''' Take 5 marks from the user and store them in a list. Calculate:
Total
Average
Highest Marks
Lowest Marks
'''

nums = []
for i in range(5):
    item = int(input(f"Enter Marks {i+1}: "))
    nums.append(item)
print(f"Total= {sum(nums)}")
print(f"Average= {sum(nums)/len(nums)}")
print(f"highest= {max(nums)}")
print(f"lowest= {min(nums)}")
