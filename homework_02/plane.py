"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)
    
    def load_cargo(self, add_cargo):
        if self.cargo + add_cargo <= self.max_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload()
    
    def remove_all_cargo(self):
        # объявите метод `remove_all_cargo`, который принимает число
        # зачем в условии задания написанно что нужно передавать числовой аргумент?
        # если в тестах функция вызывается без аргумента?
        tmp_cargo = self.cargo
        self.cargo = 0
        return tmp_cargo