from stuff.Stuff import *
from enums.StuffType import *


class SleepingBag(Stuff):
    stuff_type = StuffType.SLEEPING_BAG

    def __init__(self, name, price, producer, material, weight, size, temperature_rate):
        self.name = name
        self.price = price
        self.producer = producer
        self.material = material
        self.weight = weight
        self.size = size
        self.temperature_rate = temperature_rate

    def __str__(self):
        return "Name: " + self.name + "  Weight: " + str(
            self.weight) + " Temperature rate: " + str(self.temperature_rate) + " material " + str(self.material)\
               + " size " + str(self.size)
