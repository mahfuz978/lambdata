"""
acme products
"""
from random import randint
class Product:
    def __init__(self, price=10, weight=20, flammability=0.5):
        self.name = "Brush"
        self.price = price
        self.weight = weight
        self.flammability = flammability
        

    def identifier(self):
        return randint(low=1000000, high=9999999)



# exit()pdrod