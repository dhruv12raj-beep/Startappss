'''Check employee bonus eligibility:
Salary > 50000 → Bonus Eligible
Otherwise Not Eligible'''



salary = int(input("enter number: "))

if salary >= 50000:
    print("eligible for bonus")
else:
    print("not eligible")
