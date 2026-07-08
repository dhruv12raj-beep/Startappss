#23.	Create a dictionary from:names = ["Monika", "Riya", "Anjali"]where values are lengths of names.
names = ["Monika", "Riya", "Anjali"]

names = {i:len(i) for i in names}
print(names)