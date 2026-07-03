'''7.	Write a program to demonstrate constructor inheritance using super().'''


class BankAccount:
    def __init__(self,bank_name,account_no,holder_name,ifsc,mobile_no,balance):
        self.bank_name = bank_name
        self.account_no = account_no
        self.holder_name = holder_name
        self.ifsc = ifsc
        self.mobile_no = mobile_no
        self.balance = balance
        print("parent constructor called")


    def show_details(self):
        print("---Bank Details---")
        print(f"Bank Name: {self.bank_name}")
        print(f"IFSC: {self.ifsc}")
        print(f"Account_no: {self.account_no}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Mobile_NO: {self.mobile_no}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, bank_name, account_no, holder_name, ifsc, mobile_no, balance):
        super().__init__(bank_name, account_no, holder_name, ifsc, mobile_no, balance)

    def limit(self):
        print("transaction limit: 50000")


sbi = SavingsAccount("State Bank Of India",12345672345,"Neil Nitin Mukesh","SBIN000123", 7123456789, 12000)

sbi.show_details()
sbi.limit()