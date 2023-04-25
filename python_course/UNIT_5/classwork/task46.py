# todo: Задача 1 Переопределите метод __str__, чтобы в нем печатались все атрибуты объекта и их значения через запятую. Например:
# def __init__(self):
#     self.x = 0
#     self.y = 1
#
# Должно быть напечатано x:0, y:1

class Methods:
    def __init__(self):
        self.x = 0
        self.y = 1

    def __str__(self):
        return f'{self.__dict__}'


strin = Methods()
print(strin)
