'''Take a string from the user and print:
First character
Last character
Length of the string'''

user = input("Enter Aything you want, i'll return you first and last char only: ")
print("first character:", user[0])
print("last character:", user[-1])
print("length of string:" , len(user))