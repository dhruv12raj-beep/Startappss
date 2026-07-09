# Create a Movie data class with:
# •	movie_name
# •	director
# •	rating
# Create two movie objects with the same values and check whether they are equal.


from dataclasses import dataclass


@dataclass
class Movie:
    movie_name : str
    director :str
    raing : int

m1= Movie("Titanic","James Cameron",8)
m2= Movie("Titanic","James Cameron",8)


print(m1==m2)