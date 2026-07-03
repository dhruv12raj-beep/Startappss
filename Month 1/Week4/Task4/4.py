# 14.	Override __add__() to add two bank account balances.

class Bank:

    def __init__(self,balance):
        self.balance = balance

    def __add__(self, other):
        return f"{self.balance + other.balance}"


sbi = Bank(15000)
hdfc = Bank(18000)

print(sbi + hdfc)