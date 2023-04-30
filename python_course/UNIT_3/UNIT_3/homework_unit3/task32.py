#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
#Ввод: GGCTAA
#Вывод: CCGATT

string_inp = input('Ввод: ')
to_remov = {"G":"C", "C":"G", "T":"A", "A":"T"}

for i,j in to_remov.items():
    string_inp = string_inp.replace(i,j)
    print(i,j)
    print(string_inp)
print("Вывод: " + string_inp)


