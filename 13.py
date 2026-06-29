#bank account 
# attributes = self,name, acccount_no, balance, ifsc, address, branch
# deposit , withdrwal , total_balance


class BankAccount:

    def __init__(self,name, acccount_no, balance, ifsc, address, branch):
        self.name = name 
        self.acccount_no = acccount_no
        self.balance = balance
        self.ifsc = ifsc
        self.address = address
        self.branch = branch 

    def deposit(self,amount):
        self.balance += amount
        print(f"updated balance is {self.balance}")

    def withdrawl(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawl successfuly ")

    def total_balance(self):
        print(self.balance)


obj1 = BankAccount("SBI", 42002402, 10000, 'SBIN0001', "Indore", 'Indore')
obj1.deposit(5000)
obj1.withdrawl(5000)
obj1.total_balance()