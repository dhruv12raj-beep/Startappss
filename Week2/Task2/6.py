#calculate average marks

marks = {"maths": 80,
         "english": 80,
         "hindi": 80,
         "social": 80,
         "science": 80}

total = sum(marks.values())
average = total/len(marks.keys())
print(average)