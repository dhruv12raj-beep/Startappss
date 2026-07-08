# 13.	Sort names by their length.
names = ["John","Alexander","Bob","David"]



sorted_by_length = sorted(names , key=lambda x:len(x))
print(sorted_by_length)