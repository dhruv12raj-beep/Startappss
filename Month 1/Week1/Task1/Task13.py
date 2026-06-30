'''Check scholarship eligibility:
Marks ≥ 80 AND Attendance ≥ 75'''

marks = int(input("enter marks: "))
attendance = int(input("enter attendance: "))

if marks  >= 80  and attendance >= 75:
    print("eligible for scholarship")
else:
    print("not eligible ")