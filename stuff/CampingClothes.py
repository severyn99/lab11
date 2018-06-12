from stuff.Stuff import *
from enums.StuffType import *


class CampingClothes(Stuff):
    stuff_type = StuffType.CAMPING_CLOTHES

    def __init__(self, name, price, producer, material, weight, size):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.size = size

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.size) + " material " + str(self.material) + " size " \
               + str(self.size)
