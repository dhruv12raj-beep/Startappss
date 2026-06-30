'''Login System (3 Attempts)

Rules:

Correct username and password
Maximum 3 attempts
Lock account after 3 failures'''


correct_username = "admin999"
correct_password = "12345678"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("login successful")
        break
    else:
        attempts -=1
        print("invalid creadentials")
        print(f"attemps left {attempts}")

    if attempts == 0:
        print("account locked !!!")

