class ProductInventory:
    def __init__(self):
        self.inventory = {}
    def add_product(self, name, quantity):
        try:
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
            self.inventory[name] = self.inventory.get(name, 0) + quantity
        except ValueError as e:
            print(f"Error: {e}")
    def remove_product(self, name, quantity):
        try:
            if name not in self.inventory:
                raise KeyError("Product not found")
            if quantity > self.inventory[name]:
                raise ValueError("Not enough stock to remove")
            self.inventory[name] -= quantity
            if self.inventory[name] == 0:
                del self.inventory[name]
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")
    def show_inventory(self):
        print(self.inventory)
inventory = ProductInventory()
inventory.add_product("Laptop", 5)
inventory.remove_product("Phone", 2)
inventory.add_product("Tablet", -3)
inventory.show_inventory()
inventory = ProductInventory()
inventory.add_product("Laptop", 10)
inventory.add_product("Phone", 5)
inventory.add_product("Tablet", 7)
inventory.remove_product("Laptop", 3)
inventory.remove_product("Tablet", 2)
inventory.show_inventory()

