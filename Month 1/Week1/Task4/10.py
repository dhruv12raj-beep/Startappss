#Take a string and print the frequency of each character.
'''Example:
Input: banana

Output:
b = 1
a = 3
n = 2
'''
string = input("Enter String: ")
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char]= 1

    
for ch , count in freq.items():
    print(f"{ch} = {count}")
