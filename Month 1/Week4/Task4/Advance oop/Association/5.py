# Create a Trainer and Course class where one trainer teaches multiple courses using association.


class Trainer:
    def __init__(self, name):
        self.name = name
        self.courses = []


class Course:
    def __init__(self, title):
        self.title = title


t1 = Trainer("Dhruv")

c1 = Course("Python")
c2 = Course("DSA")

t1.courses.append(c1)
t1.courses.append(c2)

for c in t1.courses:
    print(f"{t1.name} teaches {c.title}")