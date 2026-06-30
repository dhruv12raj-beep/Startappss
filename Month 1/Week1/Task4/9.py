# Take a string and check whether it starts with a given character.


string = input("Enter String: ")

target_char = "c"

for char in string:
    if char == target_char:
        print("Matched")
    else:
        print()