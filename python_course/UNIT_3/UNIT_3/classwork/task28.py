#todo:
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda
lst = [123, 234, 345, 456]
second = lambda x:sum(map(int, str(x)))

print([second(elem) for elem in lst])