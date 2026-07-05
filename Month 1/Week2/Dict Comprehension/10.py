# 30.	Create a dictionary from two lists:
keys = ["name", "age", "city"]
values = ["Monika", 18, "Ratlam"]


dict = {k:v for k,v in zip(keys,values)}
print(dict)