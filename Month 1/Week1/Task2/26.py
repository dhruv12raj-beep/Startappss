#Check whether a number is prime.

num = int(input("enter number: "))

for i in range(2 ,int(num**0.5)+1):
    if num % i ==0:
        print("Not a Prime Number")
    else:
        print("Prime Number")
