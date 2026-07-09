# print factorial 

num = int(input("enter number:"))
result = 1
if num < 0:
    print(1)
else:
    for i in range(1,num+1):
        result *= i 
    print(f" factorial is {result}")