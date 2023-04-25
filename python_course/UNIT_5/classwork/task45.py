# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a >0 and self.b >0 and 0 < self.c < (self.a + self.b) and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
            print('треугольник существует')
        else:
            print("треугольник не существует")




triangle = Triangle(2,3,5)
triangle.check_triangle()


