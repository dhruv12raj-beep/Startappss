#Bank Account 


class BankAccount:

    def __init__(self, account_number, account_holder, bank_name,branch , balance , account_type , ifsc , mobile_number):
        self.account_number = account_number
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.branch = branch
        self.balance = balance 
        self.account_type = account_type
        self.ifsc = ifsc 
        self.mobile_number = mobile_number

    def deposit(self,amount):
        self.balance += amount
        print(f"updated balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"Remmaining Balance : Rs{self.balance} ")
        else:
            print("Insufficient Funds")

    def check_balance(self):
        print(f"Current Balance is: {self.balance}")

    def transfer_money(self,other_account,amount):
        if amount <= self.balance:
            self.balance -= amount 
            other_account.balance += amount 
            print(f"Rs {amount} transferred successfully")
        else:
            print("Insufficient Funds")

    def print_statement(self):
        print("---Account details---")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Bank Name:",self.bank_name)
        print("Branch:",self.branch)
        print("Account Type:",self.account_type)
        print("IFSC:",self.ifsc)
        print("Mobile Number:",self.mobile_number)
        print("Account Balance:",self.balance)

obj1 = BankAccount(122121212,"Vijay", "HDFC", "Indore", 120000, "Current", "HDFC000123", 123456789)
obj2 = BankAccount(567899999,"Hitesh", "SBI", "Indore", 6500, "Savings", "SBIN000123", 987654321)
obj1.check_balance()
obj1.deposit(5000)
obj1.transfer_money(obj2,10000)
obj1.print_statement()