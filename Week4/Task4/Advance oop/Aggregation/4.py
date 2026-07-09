# Create a School class and a Teacher class. A school contains multiple teachers. Delete the school object and verify that teacher objects still exist.


class School:
    def __init__(self, name):
        self.name = name 
        self.techers = []


class Teacher:
    def __init__(self,name):
        self.name = name 

s= School("Bhawans")

t1 = Teacher("Dhruv")
t2 = Teacher("Karan")
t3 = Teacher("Maithili")


s.techers.append(t1)
s.techers.append(t2)
s.techers.append(t3)

for o in s.techers:
    print(f"School: {s.name} -> Techers:  {o.name} ")

del s

print(t1.name)
print(t2.name)
print(t3.name)