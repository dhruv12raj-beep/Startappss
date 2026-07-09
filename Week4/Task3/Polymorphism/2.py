'''12.	Create CreditCard, UPI, and Wallet classes with a pay() method.
 Write a function that accepts any payment object and calls pay().'''


class CreditCard:
    def pay(self):
        print("Pays with CreditCard")
class Upi:
    def pay(self):
        print("Pays with Upi")
class Wallet:
    def pay(self):
        print("Pays with Wallet")


cc = CreditCard()
upi = Upi()
wallet = Wallet()

def payment(anymethod):
    anymethod.pay()

payment(cc)
payment(upi)
payment(wallet)
