# 23.	Convert temperatures from Celsius to Fahrenheit.
# Formula
# F = (C*9/5)+32

celsius = [78,91,65,67,85]

fahrenheit = list(map(lambda x:(x*9/5)+32, celsius))
print(fahrenheit)