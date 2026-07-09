'''25.	Create an abstract class Authentication with an abstract method login(). Implement it for GoogleLogin, EmailLogin, and FacebookLogin. Show that objects cannot be created from the abstract class'''


from abc import ABC, abstractmethod


class Authenticaion(ABC):

    @abstractmethod
    def login(self):
        pass

class GoogleLogin(Authenticaion):
    def login(self):
        print("Google")

class EmailLogin(Authenticaion):
    def login(self):
        print("Email")

class Facebook(Authenticaion):
    def login(self):
        print("Facebook")


object = Authenticaion()
object.login()