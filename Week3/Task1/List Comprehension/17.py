#17.	Create a set of first letters from:["Monika", "Riya", "Anjali", "Siya"]

names = ["Monika", "Riya", "Anjali", "Siya"]

first_letter = {char[0] for char in names}
print(first_letter)