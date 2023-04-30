# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.

class Pet:
    def __init__(self, name, weight, satiety):
        self.name = name
        self.weight = weight
        self.satiety: int = satiety

    def info(self):
        return print(f'{self.__dict__}')

    def hungry(self):
        if self.satiety < 5:
            return print(f'{self.satiety} , голоден')
        elif self.satiety > 10:
            return print(f'{self.satiety} , сыт')
        else:
            return print(f'{self.satiety}')

    def feed(self,eat):
        self.eat = eat
        self.satiety +=eat
        self.info()


p = Pet('cat',20,4)
p.info()
p.hungry()
p.feed(7)
