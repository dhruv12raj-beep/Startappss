# eligible for voting

age = int(input("enter your age:"))
if age <=0:
    print("invalid age")
elif age <= 18:
    print('not eligible for voting')
else:
    print("Great!!, you are eligible for voting")