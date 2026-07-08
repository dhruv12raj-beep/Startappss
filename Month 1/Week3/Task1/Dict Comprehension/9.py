# 29.	Create a dictionary mapping numbers from 1 to 10 to "Even" or "Odd".


dict = {i: "even" if i % 2==0 else "odd" for i in range(1,11) }
print(dict)