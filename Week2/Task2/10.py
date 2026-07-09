#create a inventory system using dictionary


inventory = {}

n = int(input("Enter number of contacts."))
for i in range(n):
    item = input("enter name: ")
    quantity = int(input("enter number: "))

    inventory[item] = quantity

for i,q in inventory.items():
    print(f"Item:{i} ,Quantity: {q}") 