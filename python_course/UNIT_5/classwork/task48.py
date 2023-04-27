# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    def __init__(self):
        self.Colour = 'Красный'
        self.Square = 5

    def set_colour(self,Colour):
        self.Colour = Colour

    def set_square(self,Square):
        self.Square = Square

    def print_colour(self):
        print(self.Colour)

    def print_square(self):
        print(self.Square)


square = Shape()

square.print_square()
square.set_square(4)
square.print_square()
square.print_colour()
square.set_colour('Зеленый')
square.print_colour()