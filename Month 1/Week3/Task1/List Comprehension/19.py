#19.	Create a set containing only uppercase letters from a string.


string = input("Enter String: ")

uppercase = {i.upper() for i in string}
print(uppercase)