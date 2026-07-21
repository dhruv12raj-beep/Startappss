'''Create a namedtuple for Student.
Fields
id

name

salary
Print all students earning more than ₹50,000.
'''


from collections import namedtuple

students = namedtuple("Student",["id","name","salary"])

std1 = students(101,"dhruvv",90222)
std2 = students(103,"kriya",45000)
std3 = students(102,"pow",30000)
std4 = students(105,"aizen",78000)

updated_std3 = std3._replace(salary = 40000)
print(updated_std3)
print(updated_std3._asdict())

data = [std1,std2,std3,std4]
for i in data:
    if i.salary>50000:
        print(i)