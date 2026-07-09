'''ATM Machine Simulation
Menu:

1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
'''

choice = int(input('''enter 1 for check balance",\
"enter 2 for withdraw,
"enter 3 for deposit money,
"enter 4 to exit '''))

balance = 0 

if choice ==1:
    print("Balance is", balance)
elif choice ==2:
    amount = int(input("enter amount: "))
    if balance >= amount:
        balance-=amount
        print(f"withdrawl successful remaining bal {balance}")
    else:
        print("insufficient funds")

elif choice ==3:
    deposit = int(input("enter deposit amount: "))
    balance += deposit 
    print(f"deposit successful balance is {balance}")

elif choice ==4:
    print("bye")