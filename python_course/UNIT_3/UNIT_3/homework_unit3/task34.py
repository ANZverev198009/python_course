# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n):
    k = 0
    if n == 0:
        k = 0
    elif n == 1:
        k = 1

    return k = (n + sumn(n - 1))


sumn(4)
