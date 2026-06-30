#Print numbers from 1 to 20 except 5.

for i in range(1,20+1):
    if i == 5:
        continue
    else:
        print(i , end= " ")