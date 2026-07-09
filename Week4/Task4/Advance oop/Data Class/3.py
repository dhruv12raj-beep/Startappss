# Create a Product data class with:
# •	product_id
# •	product_name
# •	price
# •	quantity
# Print the object and calculate the total price.



from dataclasses import dataclass


@dataclass
class Product:
    product_id : int
    product_name :str
    price : int
    quantity : int

    def total_price(self):
        print(f"Total Price : {self.price * self.quantity}")


prd = Product(89,"Rice",1230,2)
print(prd)