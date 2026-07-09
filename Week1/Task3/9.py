#Print numbers from 1 to 100 except multiples of 10.



for i in range(1,101):
    if i % 10 == 0:
        continue
    print(i, end = " ")