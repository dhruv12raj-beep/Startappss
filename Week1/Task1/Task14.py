'''Check admission eligibility:
Marks ≥ 60 OR Sports Certificate = Yes'''

marks = int(input("enter marks: "))
certificate = input("do you have certificate?, enter yes or no: ")


if marks >= 60 and certificate == "yes":
    print("eligible for admission")
else:
    print("not eligible")