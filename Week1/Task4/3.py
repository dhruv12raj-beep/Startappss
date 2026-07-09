#Take a string and count how many uppercase letters and lowercase letters it contains.

string = input("Enter your thoughts: ")

upper_count = 0
lower_count = 0

for char in string:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1

print("Uppercase Letters are",upper_count)   
print("Lowercase Letters are",lower_count)   