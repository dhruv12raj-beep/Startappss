#Find reverse of a number.

num = int(input("Enter Number: "))
result = 0 

while num > 0:
    digit = num %10 
    result = result * 10 + digit 
    num //=10

print(result)