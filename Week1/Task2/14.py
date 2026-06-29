#Find the sum of digits of a number.


num = int(input("enter number: "))
result = 0
while num:
    digit = num % 10 
    result += digit 
    num //=10 

print(result)