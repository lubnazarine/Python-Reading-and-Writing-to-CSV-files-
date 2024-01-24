class Item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self._price = price

    @property
    def price(self):
        return self._price   

class Cake(Item):
    def __init__(self, flavour, price, slices):
        super().__init__("cake", price)
        self.slices = slices
        self.flavour = flavour

spice_cake = Cake("spice",18,8)
chocolate_cake = Cake("chocolate",24,6)

spice_cake.slices=7
#the following line should not be allowed as price is a private attribute and it is set by a property
spice_cake.price=17
