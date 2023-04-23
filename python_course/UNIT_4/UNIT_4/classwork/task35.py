#todo: Заданы два списка. Необходимо их сериализовать в один файл.

import pickle

list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]

with open('file.pkl','ba+') as f:
    pickle.dump(list_one,f)
    pickle.dump(list_two,f)
