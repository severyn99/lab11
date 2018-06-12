from stuff.Stuff import *
from enums.StuffType import *


class Tent(Stuff):
    stuff_type = StuffType.TENT

    def __init__(self, name, price, producer, material, weight, capacity, doors_number):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.capacity = capacity
        self.doors_number = doors_number

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Type: " + str(self.stuff_type.value) + " material " + str(self.material) + " capacity " \
               + str(self.capacity)
