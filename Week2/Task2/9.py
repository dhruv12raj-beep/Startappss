# create a contact book using a dictionary

contact_boook = {}

n = int(input("Enter number of contacts."))
for i in range(n):
    name = input("enter name: ")
    phone_no = int(input("enter number: "))

    contact_boook[name] = phone_no

for n , p in contact_boook.items():
    print(f"Name: {n} , Phone no: {p}")