#25.	Reverse the following dictionary:d = {"a":1, "b":2, "c":3}
d = {"a":1, "b":2, "c":3}

reversed = {value : key for key , value in d.items()}
print(reversed)