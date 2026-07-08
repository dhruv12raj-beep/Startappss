# 32.	Create a dictionary of prime numbers from 1 to 100 and their squares.

dict = {n:n**2 for n in range(2,101) if all(n%i!=0 for i in range(2,int(n**0.5)+1))}

print(dict) 