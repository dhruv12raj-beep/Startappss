#Create a simple calculator using choice:

n1= int(input("enter first number:"))
n2= int(input("enter second number:"))
choice = int(input('''for addition enter 1,
    for substracion 2,
    for multiplication 3 
    for division 4: '''))

if choice ==1:
    print("result :", n1+n2)
elif choice ==2:
    print("result:",n1-n2)
elif choice ==3:
    print("result:",n1*n2)
elif choice ==4:
    print("result:",n1/n2)
else:
    print("invalid choice")
    
