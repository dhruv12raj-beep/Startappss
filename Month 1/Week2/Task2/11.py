#find common skills among employees

emp1 = set(input("Enter skills: ").split())
emp2 = set(input("Enter skills").split())

common = (emp1 & emp2)
print(common)