from stuff.Stuff import *
from enums.StuffType import *


class SleepingPad(Stuff):
    stuff_type = StuffType.SLEEPING_PAD

    def __init__(self, name, price, producer, material, weight, colour, thickness):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.colour = colour
        self.thickness = thickness

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.stuff_type.value) + " material " + str(self.material) + " colour " \
               + self.colour
