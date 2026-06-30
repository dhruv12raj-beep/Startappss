#Find the sum of even numbers from 1 to 100.
result = 0 
for i in range(1,100+1):
    if i % 2 ==0:
        result += i 
print(result)