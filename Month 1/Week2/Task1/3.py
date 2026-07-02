'''Take 5 student names in a list and search for a specific student name.
If found print:
Student Found
otherwise:
Student Not Found
'''

names = []

for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
target = input("Who would you like to find?:")
for j in names:
    if j == target:
        print("Student Found")
        break
else:
    print("Student not found")


