from stuff.Stuff import *
from enums.StuffType import *


class Boat(Stuff):
    stuff_type = StuffType.BOAT

    def __init__(self, name, price, producer, material, weight, boat_capacity):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.boat_capacity = boat_capacity

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.stuff_type.value) + " material " + str(self.material)
