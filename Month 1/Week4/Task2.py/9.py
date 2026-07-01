

class MovieTicket:

    def __init__(self, seat_number, price):
        self.__seat_number = seat_number
        self.__price = price

    def book_ticket(self):
        print(f"ticket booked for {self.__seat_number}")

    def cancel_ticket(self):
        print(f"ticket booked for {self.__seat_number}")

    def get_ticket_details(self):
        print(f"---Ticket Details---")
        print(f"Seat Number: {self.__seat_number}")
        print(f"Ticket Price: {self.__price}")



spiderman = MovieTicket("A5",450)
spiderman.book_ticket()
spiderman.get_ticket_details()

        