# todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.
from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self):
        self.speed = speed
        self.cargo = cargo
        self.cost = cost

    @abstractmethod
    def Cost(self):
        self.cost = cost

    @abstractmethod
    def Info(self):
        return f'speed={self.speed}, cargo = {self.cargo}, cost = {self.cost}'


class Marine(Transport):
    def Info(self):
        pass


class Ground(Transport):
    def Info(self):
        pass
