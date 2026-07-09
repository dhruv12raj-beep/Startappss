# Create a Customer and Bank class. A customer can have an account in a bank. Display the customer's bank information


class Bank:
    def __init__(self, name):
        self.name = name


class Customer:
    def __init__(self, name, account_no, bank):
        self.name = name
        self.account_no = account_no
        self.bank = bank


b1 = Bank("SBI")

c1 = Customer("Aizen", "501003050302", b1)

print(f"Customer: {c1.name} | Account No: {c1.account_no} | Bank: {c1.bank.name}")