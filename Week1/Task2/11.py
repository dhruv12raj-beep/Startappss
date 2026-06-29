#Find the sum of first N natural numbers.
result = 0 
n = int(input("enter number: "))
for i in range (1,n+1):
    result += i 
print(result)