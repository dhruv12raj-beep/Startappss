# Take a string and count how many vowels (a, e, i, o, u) are present.

vowels = "aeiou"
string = input("Enter Anything: ").lower() 
count = 0

for ch in string:
    if ch in vowels:
        count += 1
    
print(f"{count} vowels are present.")