class Product:
    def __init__(self, product_id, name, price, initial_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.initial_quantity = initial_quantity
        
    def update_price(self, new_price):
        self.price += new_price
        print(f"New price is {self.price}")
        
    def add_stock(self, quantity):
        self.initial_quantity += quantity
        print(f"Added {quantity} units of {self.name} to stock. New stock: {self.initial_quantity} units")
        
    def remove_stock(self,quantity):
        if quantity > self.initial_quantity:
            raise ValueError("Not enough stock available.")
        else:
            self.initial_quantity -= quantity
            print(f"Removed {quantity} units of {self.name} from stock. New stock: {self.initial_quantity} units")
            
            
product1 = Product(product_id="001", name="Laptop", price=100, initial_quantity=50)
product1.update_price(10)
product1.add_stock(20)
product1.remove_stock(15) 

        