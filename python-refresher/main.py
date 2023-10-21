class Item:

    # Class attributes
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} should be zero or greater than 0"
        assert quantity >=0, f"Validation failed. "

        # Assign self objects
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discont(self):
        self.price = self.price * Item.pay_rate


item1 = Item("Phone", 300, 5)
print(item1.calculate_price())

# Accessing class attribute
print("This is ", Item.pay_rate, "rate")

print(Item.__dict__)
print(item1.__dict__)
item1.apply_discont()
print(item1.price)


