

class Book:

    def __init__(self,book_id , title, author , publisher  ,genre  , price , total_pages, available_copies):
        self.book_id = book_id
        self.title = title 
        self.author = author
        self.publisher = publisher 
        self.genre = genre 
        self.price = price 
        self.total_pages = total_pages
        self.available_copies = available_copies

    def issue_book(self):
        print(f"{self.book_id} issued.")

    def return_book(self):
        print(f"{self.book_id} returned")

    def show_details(self):
        print(self.book_id,self.title, self.author, self.publisher, self.genre, self.price, self.total_pages, self.available_copies)

    def update_price(self, price):
        self.price = price 
        print(f"price updated now available for {self.price}")

    def check_availability(self):
        if self.available_copies > 1:
            print("available")
        else:
            print("unavailable")
        

obj = Book(123,"bhagwat gita", "ved vyas" , "gorakhpur", "sacred scripture", 1000,1100, 50)
obj.check_availability()
obj.show_details()
obj.return_book()
obj.issue_book()
obj.update_price(2000)