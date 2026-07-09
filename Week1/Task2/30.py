#Armstrong 

num = int(input("enter number: "))
temp = num 
length = len(str(temp))
result= 0
while temp > 0 :
    digit = temp %10 
    result += digit ** length 
    temp//=10 

if num == result:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
    
    