"""Define a class and create objects"""

class Cake:
    def __init__(self, kind, price, slices):
        self.kind = kind
        self.price = price
        self.slices = slices
        self.remaining_slices = slices

    def describe(self):
        return f"The {self.kind} cake costs ${self.price} and is divided into {self.slices} slices."

    def sell(self, count):
        if(count <= 0):
            return f"Cannot sell zero or negative slices!"
        elif(self.remaining_slices - count < 0):
            return f"Cannot sell more slices than we have {self.remaining_slices}!" 
        else:
            self.remaining_slices -= count
            return f"This cake has {self.remaining_slices} slices remaining"
        
spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24,6)

print(spice_cake.describe())
print(chocolate_cake.describe())
print(spice_cake.sell(5))
print(spice_cake.sell(4))
print(spice_cake.sell(-1))
print(spice_cake.sell(0))