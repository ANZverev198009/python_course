# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.
class Person:
    def __init__(self, last_name, age):
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    def __setattr__(self, name, value):
        if name == '_age':
            if hasattr(self, '_age'):
                raise AttributeError("Age cannot be changed")
        super().__setattr__(name, value)