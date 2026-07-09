# check login eligibility 

username= "admin"
password = 1234

user = input("enter username: ")
pswd = int(input("enter password: "))

if user == username and pswd == password:
    print("login successful")
else:
    print("invaild credentials")