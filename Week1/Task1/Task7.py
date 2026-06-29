#Check whether a number is divisible by 10 or 5

num = int(input("enter number: "))

if num % 5 or num % 10==0 :
    print(f"{num} is divisible by 5 and 10 ")
else:
    print("not divisible")