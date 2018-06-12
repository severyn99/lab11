from stuff.Stuff import *
from enums.StuffType import *


class CampCooler(Stuff):
    stuff_type = StuffType.CAMP_COOLER

    def __init__(self, name, price, producer, material, weight, capacity, cooler_type):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.capacity = capacity
        self.cooler_type = cooler_type

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.cooler_type.value) + " material " + str(self.material)
