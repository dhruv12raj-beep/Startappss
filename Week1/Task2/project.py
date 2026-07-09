#ATM menu using loops.


balance = 1000

while True:
    print("-- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Money deposited successfully")
        print(f"New Balance is{balance}")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice!")