#Ask user for a password and stop when correct password is entered.

password = "admin@123"

while True:
    user = input("Enter Your Password: ")

    if user == password:
        print("Correct Password")
        break
    else:
        print("Incorrect password, Try again")