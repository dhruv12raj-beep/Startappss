#4.	Create a list of vowels present in a string entered by the user.

vowels = ["a",'e','i','o','u']
string  = input("Enter string: ")

result = [i for i in string if i in vowels]
print(result)