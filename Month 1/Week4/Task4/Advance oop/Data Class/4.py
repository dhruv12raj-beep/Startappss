# Create a Book data class with:
# •	title
# •	author
# •	price
# Display the object using the automatically generated __repr__() method.


from dataclasses import dataclass


@dataclass
class Book:
    title : str
    author : str
    price : int


book = Book("Dragon Ball Super","Akira Toriyama", 1200)
print(book)