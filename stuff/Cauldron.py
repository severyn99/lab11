from stuff.Stuff import *
from enums.StuffType import *


class Cauldron(Stuff):
    stuff_type = StuffType.CAULDRON

    def __init__(self, name, price, producer, material, weight, capacity):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.capacity = capacity

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.stuff_type.value) + " material " + str(self.material) + " capacity " \
               + str(self.capacity)
