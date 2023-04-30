#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def upper_case_args(func):
    def wrapper(*args, **kwargs):
        upper_args = []
        for arg in args:
            if isinstance(arg, str):
                upper_args.append(arg.upper())
            else:
                upper_args.append(arg)
        return func(*upper_args, **kwargs)
    return wrapper


@upper_case_args
def say_hello(name, greeting='Hello'):
    print(f"{greeting}, {name}!")



say_hello('Alice', greeting='Hi')