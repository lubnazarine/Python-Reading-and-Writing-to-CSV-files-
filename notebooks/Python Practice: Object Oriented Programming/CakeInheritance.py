class Item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self.price = price

class Cake(Item):
    def __init__(self, flavour, price, slices):
        super().__init__("cake", price)
        self.slices = slices
        self.flavour = flavour

spice_cake = Cake("spice",18,8)
chocolate_cake = Cake("chocolate",24,6)

print(spice_cake.item_type)
print(spice_cake.price)
print(spice_cake.flavour)
print(spice_cake.slices)
print(chocolate_cake.item_type)
print(chocolate_cake.price)
print(chocolate_cake.flavour)
print(chocolate_cake.slices)