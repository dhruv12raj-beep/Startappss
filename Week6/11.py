'''Group employees according to salary range.
0-20000

20001-50000

50001+
Use defaultdict.
'''

from collections import defaultdict


employees = [
    ("Rahul", 18000),
    ("Aman", 35000),
    ("Dhruv", 90000),
    ("Kriya", 15000),
    ("Aizen", 80000),
    ("Pow", 75000),
]
salary_group= defaultdict(list)

for emp, salary in employees:
    if 0 < salary <= 20000:
        salary_group["0-20000"].append(emp)
    elif 20001 <= salary <= 50000:
        salary_group["20001-50000"].append(emp)
    else:
        salary_group["50001 +"].append(emp)


print(salary_group)






