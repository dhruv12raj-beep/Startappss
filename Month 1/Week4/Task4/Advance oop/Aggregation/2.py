# Create a Library class and a Book class. A library has multiple books. Demonstrate that books still exist even if the library object is deleted.


class Library:
    def __init__(self,name):
        self.name = name
        self.book = []


class Book:
    def __init__(self, name, author):
        self.name = name 
        self.author = author


b1 = Book("Python Basics", "Reetu")
b2 = Book("DSA Guide", "Rahul")

lib = Library("City Library")
lib.book.append(b1)
lib.book.append(b2)

for b in lib.book:
    print(f"Library: {lib.name} -> Book: {b.name}, Author {b.author}")

del lib
print(b1.name, b1.author)
print(b2.name, b2.author)
