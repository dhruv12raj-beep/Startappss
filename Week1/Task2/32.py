#Find count of digits in a number.

num = int(input("Enter Number: "))

count = 0 
while num > 0:
    digit= num %10 
    count += 1
    num//=10 

print(count)