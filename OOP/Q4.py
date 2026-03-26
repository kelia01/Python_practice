# #Create a CoffeeShop class that has:
# Attributes: name, menu (dictionary of drink: price), orders (empty list)
# Method: add_order(drink) adds drink to orders if on menu
# Method: fulfill_order() removes first order and prints "Ready!"
# Method: total() returns sum of all order prices
# Method: cheapest() returns cheapest drink on menu
# Create a coffee shop with at least 3 drinks, add orders, fulfill them, and calculate total.

class CoffeeShop:
    def __init__(self, name):
        self.menu = { "drink": 0.00 }
        self.orders = []

    def add_order(self, drink):
        if drink in self.menu:
            self.orders.append(drink)


    def fulfill_order(self):
        self.orders.pop(0)
        print("Ready!")


    def total(self):
        for drink in self.orders:
            self.total += self.menu[drink]

    def cheapest(self):
        for drink in self.menu:
            min()