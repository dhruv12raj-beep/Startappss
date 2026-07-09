# group students by grade using dictionary 


students = {"dhruv": "A",
            "aryan": "C",
            "ankita":"B",
            "nitin":"A"}

grades = {}
for name , grade in students.items():
    if grade not in grades:
        grades[grade] = []
    
    grades[grade].append(name)

print(grades)

