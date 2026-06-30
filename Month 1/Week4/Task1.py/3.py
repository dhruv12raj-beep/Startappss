

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

    def withdrawl(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawl successfuly ")

    def check_balance(self):
        print(self.balance)

    def transfer_money(self):
        pass

    def print_statement(self):
        pass

    
