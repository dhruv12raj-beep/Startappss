# find topper subject

marks = {"maths": 97,
         "english": 98,
         "hindi": 80,
         "social": 77,
         "science": 95}


for key in marks:
    if marks[key] == max(marks.values()):
        print(f"{key}: {marks[key]}")