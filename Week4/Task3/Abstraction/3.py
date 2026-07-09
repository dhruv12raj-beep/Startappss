'''21.	Create an abstract class Payment with an abstract method pay(). Implement it in UPI, CreditCard, and NetBanking.'''

from abc import ABC, abstractmethod


class Payment(ABC):
    
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Paying with UPI")


class CreditCard(Payment):
    
    def pay(self):
        print("Paying with CC")

class NetBanking(Payment):

    def pay(self):
        print("Paying with NetBanking")


upi = UPI()
cc = CreditCard()
netbanking= NetBanking()

upi.pay()
cc.pay()
netbanking.pay()