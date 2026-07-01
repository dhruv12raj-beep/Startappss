

class BankAccount:

    def __init__(self,account_number, balance):
        self.__account_number= account_number
        self.__balance = balance


    def deposit(self, amount):
        if amount < 0:
            print("Amount Must be greater than 0")
        self.__balance += amount
        print(f"{amount} deposited successfuly , updated balance {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
                print("Insufficient Funds-- Gareeb")
        else:
            self.__balance -= amount
            print(f"Withdraw Successful, updated balance {self.__balance}")

    def get_balance(self):
        return self.__balance

object = BankAccount(123456,19000)
object.deposit(5000)
object.withdraw(12000)
print(object.get_balance())
