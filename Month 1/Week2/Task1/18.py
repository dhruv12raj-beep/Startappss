'''Create a program that stores:
subjects = ("Maths", "English", "Science", "Hindi", "SS")
marks = [90, 85, 78, 88, 92]
Print:
Maths   : 90
English : 85
Science : 78
Hindi   : 88
SS      : 92
Total Marks : ?
Average     : ?
Highest     : ?
Lowest      : ?
Also print:
Result : PASS
if average is 35 or more, otherwise:
Result : FAIL
'''

subjects = ("Maths", "English", "Science", "Hindi", "SS")
marks = [90, 85, 78, 88, 92]

for name , mark in zip(subjects, marks):
    print(f"{name}:{mark}")

print(f"Total marks: {sum(marks)}")
print(f"Average : {(sum(marks)/len(marks))}")
print(f"Highest : {max(marks)}")
print(f"Lowest : {min(marks)}")
if sum(marks)/len(marks) >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
