'''5.	Create a BankAccount parent class and derive SavingsAccount and CurrentAccount.
 Add account-specific features while reusing common methods.'''


class BankAccount:
    def __init__(self,bank_name,account_no,holder_name,ifsc,mobile_no,balance):
        self.bank_name = bank_name
        self.account_no = account_no
        self.holder_name = holder_name
        self.ifsc = ifsc
        self.mobile_no = mobile_no
        self.balance = balance


    def show_details(self):
        print("---Bank Details---")
        print(f"Bank Name: {self.bank_name}")
        print(f"IFSC: {self.ifsc}")
        print(f"Account_no: {self.account_no}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Mobile_NO: {self.mobile_no}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def daily_limit(self):
        print("Dailt Transaction Limit: 100000")
    
class CurrentAccount(BankAccount):
    def daily_limit(self):
        print("Daily Transaction Limit: 500000")
    

hdfc = BankAccount("HDFC", 510020004846, "Dhruv Verma", "HDFC210045", 7041234567, 780000)

sbi = SavingsAccount("State Bank Of India",12345672345,"Neil Nitin Mukesh","SBIN000123", 7123456789, 12000)

bob = CurrentAccount("Bank of Baroda", 9876543223,"Salman Khan", "BARBPITHAM", 7000400200, 90808)


sbi.show_details()
sbi.daily_limit()

bob.show_details()
bob.daily_limit()