#Check palindrome number.

num = int(input("enter number: "))
temp = num 
result= 0
while temp > 0:
    digit = temp%10 
    result = result * 10 + digit 
    temp//=10 

if num == result:
    print("palindrome number")
else:
    print("not a palindrome number")