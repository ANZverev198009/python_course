# todo:
# Реализовать декоратор который подсчитывает время выполнения функции.
import time


def time_of_function(function):
    def wrapper(*args):
        start = time.perf_counter_ns()
        res = function(*args)
        print(f'time of function', time.perf_counter_ns() - start)
        return res

    return wrapper


@time_of_function
def fun(x, y):
    return x * y


print(fun(10, 5))
