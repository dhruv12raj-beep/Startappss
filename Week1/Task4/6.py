#Take a sentence and count the total number of words.

sentence = input("enter sentence: ").split()
count = 0
for i in sentence:
    count +=1

print(count)