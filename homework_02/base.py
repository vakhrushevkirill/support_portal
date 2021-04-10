from abc import ABC
from homework_02.exceptions import *


class Vehicle(ABC):
    # для чего мы определяем абстарктный класс в данном случае?
    # чисто условность? Тест пройдет как с ABC, так и без него
    weight = 0
    fuel = 0
    fuel_consumption = 1
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError()
    
    def move(self, distantion):
        if not self.fuel:
            raise NotEnoughFuel()
        else:
            if (self.fuel - self.fuel_consumption * distantion) >= 0:
                self.fuel -= self.fuel_consumption * distantion
            else:
                raise NotEnoughFuel()