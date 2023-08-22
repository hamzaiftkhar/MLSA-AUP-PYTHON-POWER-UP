class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_price(self):
        return self.price * self.quantity


class ElectronicsItem(CartItem):
    def calculate_item_price(self):
        # Apply any specific logic for electronics item pricing if needed
        return self.price * self.quantity


class ClothingItem(CartItem):
    def calculate_item_price(self):
        # Apply any specific logic for clothing item pricing if needed
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_cart(self):
        for item in self.items:
            print(f"{item.name} - Quantity: {item.quantity}, Price per item: ${item.price}, Total Price: ${item.calculate_item_price()}")

    def calculate_total_price(self):
        total = sum(item.calculate_item_price() for item in self.items)
        return total


# Instantiate items
laptop = ElectronicsItem("Laptop", 1000, 1)
shirt = ClothingItem("Shirt", 25, 3)

# Instantiate shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item(laptop)
cart.add_item(shirt)

# Display cart contents
cart.show_cart()

# Calculate and display the total cart price
total_price = cart.calculate_total_price()
print(f"Total Cart Price: ${total_price}")