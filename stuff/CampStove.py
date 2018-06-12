from stuff.Stuff import *
from enums.StuffType import *


class CampStove(Stuff):
    stuff_type = StuffType.CAMP_STOVE

    def __init__(self, name, price, producer, material, weight, gas_volume, type_of_fuel):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.gas_volume = gas_volume
        self.type_of_fuel = type_of_fuel

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.type_of_fuel) + " material " + str(self.material) + " gas volume " \
               + str(self.gas_volume)
